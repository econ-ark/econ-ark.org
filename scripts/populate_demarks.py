"""Copy DemARK's notebook metadata into _materials while the site builds.

DemARK (https://github.com/econ-ark/DemARK) keeps one markdown file per notebook in its
markdown/ folder. DemARK used to push those files here, but that stopped working in January
2026: its token expired, and the organization's branch protection rejects direct pushes to
master. Like populate_remarks.py, this fetches them at build time instead, so nothing needs a
token. A failed clone fails the build rather than publishing stale pages silently.
"""

import shutil
from pathlib import Path
from subprocess import run
from tempfile import TemporaryDirectory

repo_root = Path(__file__).parents[1]

if __name__ == "__main__":
    with TemporaryDirectory() as d:
        tmpdir = Path(d)
        run(["git", "clone", "--depth", "1", "https://github.com/econ-ark/DemARK"], cwd=tmpdir, check=True)
        sources = sorted((tmpdir / "DemARK" / "markdown").glob("*.md"))
        if not sources:
            raise SystemExit("DemARK's markdown/ folder has no .md files")
        for src in sources:
            shutil.copyfile(src, repo_root / "_materials" / src.name)
        print(f"Copied {len(sources)} DemARK materials into _materials")
