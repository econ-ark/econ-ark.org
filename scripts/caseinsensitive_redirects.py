from pathlib import Path
from itertools import product
from io import StringIO
from re import fullmatch, split as re_split, sub

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

def generate_case_combinations(name):
    # Find all uppercase letters and their positions
    pattern = '[A-Z]+'
    parts = re_split(f'({pattern})', name)

    # Generate case variants for matched groups
    case_options = [
        [part.lower(), part.upper()] if fullmatch(pattern, part) else [part]
        for part in parts
    ]

    # Create all combinations and join them back
    yield from (''.join(combo) for combo in product(*case_options))

def slugify(name):
    # Jekyll's default slugify, which turns a material's file name into the :name in its URL
    return sub(r'[\W_]+', '-', name).strip('-').lower()

if __name__ == '__main__':
    repo_root = Path(__file__).parents[1]

    for path in repo_root.glob('_materials/*.md'):
        with open(path) as f:
            metadata, f = parse_yaml_header(f)
            if metadata is None:
                continue
            # The page itself is at /materials/<slug>/ (the permalink in _config.yml), so
            # redirect every other capitalization of the file name to it, its own included.
            # Each redirect is a folder, so it answers with or without a trailing slash; the
            # site must therefore be built on a case-sensitive file system, as the workflow's
            # Ubuntu runner is, since on a Mac /materials/LucasAssetPrice/ would overwrite
            # /materials/lucasassetprice/
            page = slugify(path.stem)
            metadata.setdefault('redirect_from', [])
            metadata['redirect_from'] += [
                f'/materials/{n}/'
                for n in generate_case_combinations(path.stem)
                if n != page
            ]
            body = f.read()

        with open(path, 'w') as f:
            f.write('---\n')
            yaml_dump(metadata, f, default_flow_style=False)
            f.write('---\n')
            f.write(body)
