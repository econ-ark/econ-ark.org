from pathlib import Path
from itertools import product
from io import StringIO
from re import fullmatch, split as re_split

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

if __name__ == '__main__':
    repo_root = Path(__file__).parents[1]

    for path in repo_root.glob('_materials/*.md'):
        with open(path) as f:
            metadata, f = parse_yaml_header(f)
            metadata.setdefault('redirect_from', [])
            metadata['redirect_from'] += [
                n for n in generate_case_combinations(path.stem)
                if n != path.stem
            ]
            body = f.read()

        with open(path, 'w') as f:
            f.write('---\n')
            yaml_dump(metadata, f, default_flow_style=False)
            f.write('---\n')
            f.write(body)
