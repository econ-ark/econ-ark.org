"""Copy DemARK's notebook metadata into _materials while the site builds.

DemARK (https://github.com/econ-ark/DemARK) keeps one markdown file per notebook in its
markdown/ folder. DemARK used to push those files here, but that stopped working in January
2026: its token expired, and the organization's branch protection rejects direct pushes to
master. Like populate_remarks.py, this fetches them at build time instead, so nothing needs a
token. A failed clone fails the build rather than publishing stale pages silently.

An entry DemARK has deleted or renamed is deleted here too. Only files whose front matter
names DemARK as their github_repo_url are candidates, so REMARKs and other materials are
never touched.
"""

import shutil
from pathlib import Path
from subprocess import run
from tempfile import TemporaryDirectory

from yaml import YAMLError, safe_load

DEMARK_URL = "https://github.com/econ-ark/DemARK"

repo_root = Path(__file__).parents[1]


def is_from_demark(path):
    """Whether a material's front matter gives DemARK as its github_repo_url."""
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        return False
    end = next((i for i, line in enumerate(lines[1:], 1) if line.strip() == "---"), None)
    if end is None:
        return False
    try:
        metadata = safe_load("\n".join(lines[1:end]))
    except YAMLError:
        return False
    if not isinstance(metadata, dict):
        return False
    url = str(metadata.get("github_repo_url") or "").strip().rstrip("/").removesuffix(".git")
    return url.lower() == DEMARK_URL.lower()


if __name__ == "__main__":
    materials = repo_root / "_materials"
    with TemporaryDirectory() as d:
        tmpdir = Path(d)
        run(["git", "clone", "--depth", "1", "https://github.com/econ-ark/DemARK"], cwd=tmpdir, check=True)
        sources = sorted((tmpdir / "DemARK" / "markdown").glob("*.md"))
        if not sources:
            raise SystemExit("DemARK's markdown/ folder has no .md files")
        for src in sources:
            shutil.copyfile(src, materials / src.name)
        print(f"Copied {len(sources)} DemARK materials into _materials")

    current = {src.name for src in sources}
    for path in sorted(materials.glob("*.md")):
        if path.name not in current and is_from_demark(path):
            path.unlink()
            print(f"Deleted {path.name}: no longer in DemARK's markdown/")
