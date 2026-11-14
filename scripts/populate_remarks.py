"""Write a page in _materials for each REMARK in the catalog, while the site builds.

The catalog is https://github.com/econ-ark/REMARK: one REMARKs/<name>.yml per REMARK, whose
`remote` is the REMARK's repository. For each entry this clones that repository and writes
_materials/<name>.md: the repository's CITATION.cff as front matter, updated by the front
matter of its REMARK.md, then REMARK.md's body. `github_repo_url`, which the page layout
needs for its launch and source buttons, is always the catalog's `remote`.

An entry marked `private: true` is not cloned and gets no page. Two entries with the same
`remote` get one page, the first entry's. The outcome for every entry is printed.

If the catalog, an entry or an entry's repository cannot be read, the pages that can be
written still are, and then this exits with an error, so that the build fails rather than
publishing a site that is silently missing pages.
"""

import os
import sys
from concurrent.futures import ThreadPoolExecutor
from io import StringIO
from pathlib import Path
from subprocess import run
from tempfile import TemporaryDirectory

from yaml import YAMLError, safe_load, dump as yaml_dump

CATALOG_URL = 'https://github.com/econ-ark/REMARK'

# Addresses at which a REMARK's page used to be, when a hand-made page with another file name
# stood in for the one this script now writes. Keyed by the catalog entry's name; each address
# becomes a redirect to that entry's page.
FORMER_ADDRESSES = {
    'DistributionofWealthMPC': ['/materials/DistributionOfWealthMPC/'],
    'EndogeneousRetirement': ['/materials/endogenousretirement/', '/materials/EndogenousRetirement/'],
    'MethodOfModeration': ['/materials/method-of-moderation/'],
}

repo_root = Path(__file__).parents[1]


def parse_yaml_header(f):
    metadata = StringIO()
    # advance to metadata section
    for line in f:
        if line.strip() == '---':
            break
    # copy metadata section
    for line in f:
        if line.strip() == '---':
            break
        metadata.write(line)
    metadata.seek(0)
    return safe_load(metadata), f


def repository_url(remote):
    """A catalog entry's `remote` in the form the page layout expects: no trailing slash, no .git."""
    return remote.strip().rstrip('/').removesuffix('.git')


def clone(url, dest, *options):
    """Shallow-clone url into dest. Return None, or git's last line of complaint if it failed."""
    result = run(
        ['git', 'clone', '--quiet', '--depth', '1', *options, '--', url, str(dest)],
        capture_output=True,
        text=True,
        # Never wait for a username: a repository that cannot be read anonymously is a failure.
        env={**os.environ, 'GIT_TERMINAL_PROMPT': '0'},
    )
    if result.returncode == 0:
        return None
    lines = result.stderr.strip().splitlines()
    return lines[-1] if lines else f'git clone exited with status {result.returncode}'


def read_catalog(catalog_dir, materials):
    """Sort the catalog's entries into those to clone and those already settled.

    Returns (to_clone, outcomes, failures): to_clone is a list of (name, url); outcomes maps an
    entry's name to what happened to it; failures lists the names whose outcome is an error.
    """
    to_clone, outcomes, failures = [], {}, []
    first_with_url = {}
    for yml_path in sorted(catalog_dir.glob('*.yml')):
        name = yml_path.stem
        try:
            entry = safe_load(yml_path.read_text(encoding='utf-8'))
        except YAMLError:
            entry = None
        if not isinstance(entry, dict):
            outcomes[name] = f'FAILED: REMARKs/{yml_path.name} is not valid YAML with named fields'
            failures.append(name)
            continue

        private = entry.get('private', False)
        if private is not False:
            # Anything but an explicit false is treated as private: when in doubt, show nothing.
            outcome = 'private: not cloned, no page'
            if private is not True:
                outcome += f' (private: {private!r} is not true or false; treated as private)'
            page = materials / f'{name}.md'
            if page.exists():
                page.unlink()
                outcome += f'; removed the existing _materials/{name}.md from this build'
            outcomes[name] = outcome
            continue

        remote = entry.get('remote')
        if not isinstance(remote, str) or not remote.strip():
            outcomes[name] = f'FAILED: REMARKs/{yml_path.name} has no remote'
            failures.append(name)
            continue
        url = repository_url(remote)

        earlier = first_with_url.setdefault(url.lower(), name)
        if earlier != name:
            outcomes[name] = f'no second page: same repository as {earlier}'
            continue
        to_clone.append((name, url))
    return to_clone, outcomes, failures


def write_page(name, url, repo_path, materials):
    """Write _materials/<name>.md from a clone of the REMARK's repository. Return the outcome."""
    cff = repo_path / 'CITATION.cff'
    if not cff.exists():
        outcome = 'no page written: the repository has no CITATION.cff'
        if (materials / f'{name}.md').exists():
            outcome += f'; _materials/{name}.md is left as committed'
        return outcome
    remark_data = safe_load(cff.read_text(encoding='utf-8'))
    if not isinstance(remark_data, dict):
        raise ValueError('CITATION.cff is not valid YAML with named fields')

    notes = []
    body = ''  # Default to empty body
    remark_md = repo_path / 'REMARK.md'
    if remark_md.exists():
        with open(remark_md, encoding='utf-8') as f:
            mdata, f = parse_yaml_header(f)
            body = f.read()
        if isinstance(mdata, dict):
            remark_data.update(mdata)
        else:
            notes.append('REMARK.md has no front matter')
    else:
        notes.append('no REMARK.md, so the page has no body')

    # The layout builds its "View on GitHub" and Binder links from github_repo_url. The catalog
    # says where the REMARK is, and this page was just read from there.
    stated = remark_data.get('github_repo_url')
    if isinstance(stated, str) and repository_url(stated).lower() != url.lower():
        notes.append(f'its own github_repo_url, {stated}, was replaced by the catalog remote')
    remark_data['github_repo_url'] = url

    former = FORMER_ADDRESSES.get(name)
    if former:
        existing = remark_data.get('redirect_from') or []
        if isinstance(existing, str):
            existing = [existing]
        remark_data['redirect_from'] = list(existing) + former

    with open(materials / f'{name}.md', 'w', encoding='utf-8') as f:
        f.write('---\n')
        yaml_dump(remark_data, f, default_flow_style=False)
        f.write('---\n')
        f.write(body)
    return '; '.join([f'wrote _materials/{name}.md'] + notes)


def main(catalog_url=CATALOG_URL, materials=repo_root / '_materials'):
    """Write the pages. Return the exit status: 0, or 1 if anything could not be read."""
    with TemporaryDirectory() as d:
        tmpdir = Path(d)
        error = clone(catalog_url, tmpdir / 'REMARK', '--filter=tree:0')
        if error:
            print(f'FAILED: could not clone the catalog {catalog_url}: {error}')
            return 1

        to_clone, outcomes, failures = read_catalog(tmpdir / 'REMARK' / 'REMARKs', materials)
        if not outcomes and not to_clone:
            print(f'FAILED: the catalog {catalog_url} has no REMARKs/*.yml')
            return 1

        # Each repository is cloned into a folder named for its catalog entry, which need not be
        # the repository's own name.
        (tmpdir / 'repos').mkdir()
        with ThreadPoolExecutor(4) as pool:
            clones = {
                name: pool.submit(clone, url, tmpdir / 'repos' / name)
                for name, url in to_clone
            }

        for name, url in to_clone:
            error = clones[name].result()
            if error:
                outcomes[name] = f'FAILED: could not clone {url}: {error}'
                failures.append(name)
                continue
            try:
                outcomes[name] = write_page(name, url, tmpdir / 'repos' / name, materials)
            except (YAMLError, ValueError) as error:
                first_line = (str(error).splitlines() or [type(error).__name__])[0]
                outcomes[name] = f'FAILED: could not read the metadata of {url}: {first_line}'
                failures.append(name)

    width = max(len(name) for name in outcomes)
    for name in sorted(outcomes):
        print(f'{name:<{width}}  {outcomes[name]}')
    written = sum(outcome.startswith('wrote ') for outcome in outcomes.values())
    print(f'{len(outcomes)} catalog entries: {written} pages written, {len(failures)} failed')
    if failures:
        print('FAILED: ' + ', '.join(sorted(failures)))
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
