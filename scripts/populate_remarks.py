from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from io import StringIO
from itertools import product
from re import finditer
from subprocess import run
from tempfile import TemporaryDirectory

from yaml import safe_load, dump as yaml_dump

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

repo_root = Path(__file__).parents[1]

if __name__ == '__main__':
    with TemporaryDirectory() as d:
        tmpdir = Path(d)
        run(['git', 'clone', '--depth', '1', '--filter=tree:0', 'https://github.com/econ-ark/REMARK'], cwd=tmpdir)

        remotes = {}
        for yml_path in tmpdir.glob('REMARK/REMARKs/*yml'):
            with open(yml_path) as f:
                metadata = safe_load(f)
            remotes[yml_path.stem] = metadata['remote']

        futures = {}
        with ThreadPoolExecutor(4) as pool:
            for name, uri in remotes.items():
                futures[name] = pool.submit(
                    lambda uri: run(['git', 'clone', '--depth', '1', uri], cwd=tmpdir),
                    uri=uri
                )

        for name, result in futures.items():
            result.result()
            repo_path = tmpdir / name
            cff = repo_path / 'CITATION.cff'
            if not cff.exists():
                continue
            with open(cff) as f:
                remark_data = safe_load(f)

            body = ''  # Default to empty body
            remark_md = repo_path / 'REMARK.md'
            if remark_md.exists():
                with open(remark_md) as f:
                    mdata, f = parse_yaml_header(f)
                    body = f.read()
                    remark_data.update(mdata)
            else:
                print(f"WARNING: {name} has CITATION.cff but no REMARK.md file")

            with open(repo_root / '_materials' / f'{name}.md', 'w') as f:
                f.write('---\n')
                yaml_dump(remark_data, f, default_flow_style=False)
                f.write('---\n')
                f.write(body)

