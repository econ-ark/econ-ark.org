"""Tests for populate_remarks.py. They use git repositories made on disk, never the network.

Run with:  python -m unittest discover -s scripts
"""

import contextlib
import io
import unittest
from pathlib import Path
from subprocess import run
from tempfile import TemporaryDirectory

from yaml import safe_load

import populate_remarks

CITATION = 'cff-version: 1.2.0\ntitle: A Title\nauthors:\n- family-names: Doe\n  given-names: Jo\n'
REMARK_MD = '---\nremark-name: thing\nnotebooks:\n- code.ipynb\n---\nThe body.\n'


def make_repo(path, files):
    """Make a git repository at path holding files, a dict of relative path to text."""
    path.mkdir(parents=True)
    for relative, text in files.items():
        target = path / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding='utf-8')
    git = ['git', '-c', 'user.name=test', '-c', 'user.email=test@example.org']
    run(['git', 'init', '--quiet', '--initial-branch=main'], cwd=path, check=True)
    run(['git', 'add', '--all'], cwd=path, check=True)
    run([*git, 'commit', '--quiet', '--message', 'test'], cwd=path, check=True)
    return path.as_uri()


def front_matter(page):
    """A page's front matter and body."""
    _, header, body = page.read_text(encoding='utf-8').split('---\n', 2)
    return safe_load(header), body


class PopulateRemarks(unittest.TestCase):
    def setUp(self):
        tmp = TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.tmp = Path(tmp.name)
        self.materials = self.tmp / '_materials'
        self.materials.mkdir()
        self.good = make_repo(self.tmp / 'A-Repo_With-Another-Name', {
            'CITATION.cff': CITATION,
            'REMARK.md': REMARK_MD,
        })

    def build(self, entries):
        """Run the script on a catalog holding entries, a dict of entry name to yml text."""
        self.catalogs = getattr(self, 'catalogs', 0) + 1
        catalog = make_repo(
            self.tmp / f'catalog{self.catalogs}',
            {f'REMARKs/{name}.yml': text for name, text in entries.items()},
        )
        printed = io.StringIO()
        with contextlib.redirect_stdout(printed):
            status = populate_remarks.main(catalog, self.materials)
        return status, printed.getvalue()

    def pages(self):
        return sorted(page.name for page in self.materials.iterdir())

    def test_page_is_named_for_the_entry_not_the_repository(self):
        status, printed = self.build({'Thing': f'name: Thing\nremote: {self.good}\n'})
        self.assertEqual(status, 0, printed)
        self.assertEqual(self.pages(), ['Thing.md'])
        metadata, body = front_matter(self.materials / 'Thing.md')
        self.assertEqual(metadata['title'], 'A Title')            # from CITATION.cff
        self.assertEqual(metadata['notebooks'], ['code.ipynb'])   # from REMARK.md
        self.assertEqual(body, 'The body.\n')

    def test_github_repo_url_is_the_catalog_remote(self):
        stale = make_repo(self.tmp / 'stale', {
            'CITATION.cff': CITATION,
            'REMARK.md': '---\ngithub_repo_url: https://github.com/someone/moved-away\n---\n',
        })
        status, printed = self.build({
            'Plain': f'remote: {self.good}.git/\n',
            'Stale': f'remote: {stale}\n',
        })
        self.assertEqual(status, 0, printed)
        self.assertEqual(front_matter(self.materials / 'Plain.md')[0]['github_repo_url'], self.good)
        self.assertEqual(front_matter(self.materials / 'Stale.md')[0]['github_repo_url'], stale)
        self.assertIn('was replaced by the catalog remote', printed)

    def test_private_entry_is_not_cloned_and_has_no_page(self):
        (self.materials / 'Secret.md').write_text('---\ntitle: old\n---\n', encoding='utf-8')
        nowhere = (self.tmp / 'nowhere').as_uri()   # cloning this would fail the build
        status, printed = self.build({
            'Secret': f'remote: {nowhere}\nprivate: true\n',
            'Unclear': f'remote: {nowhere}\nprivate: "yes"\n',
            'Open': f'remote: {self.good}\nprivate: false\n',
        })
        self.assertEqual(status, 0, printed)
        self.assertEqual(self.pages(), ['Open.md'])
        self.assertRegex(printed, r'Secret +private: not cloned, no page')
        self.assertRegex(printed, r'Unclear +private: not cloned, no page .*treated as private')

    def test_two_entries_for_one_repository_get_one_page(self):
        status, printed = self.build({
            'First': f'remote: {self.good}\n',
            'Second': f'remote: {self.good}/\n',
        })
        self.assertEqual(status, 0, printed)
        self.assertEqual(self.pages(), ['First.md'])
        self.assertRegex(printed, r'Second +no second page: same repository as First')

    def test_unreadable_repository_fails_the_build_after_writing_the_rest(self):
        nowhere = (self.tmp / 'nowhere').as_uri()
        status, printed = self.build({
            'Gone': f'remote: {nowhere}\n',
            'Here': f'remote: {self.good}\n',
        })
        self.assertEqual(status, 1, printed)
        self.assertEqual(self.pages(), ['Here.md'])
        self.assertRegex(printed, r'Gone +FAILED: could not clone')
        self.assertTrue(printed.rstrip().endswith('FAILED: Gone'), printed)

    def test_unreadable_entry_or_metadata_fails_the_build(self):
        broken = make_repo(self.tmp / 'broken', {'CITATION.cff': 'title: [unclosed\n'})
        status, printed = self.build({
            'NoRemote': 'name: NoRemote\n',
            'NotFields': '- just\n- a list\n',
            'BadCitation': f'remote: {broken}\n',
        })
        self.assertEqual(status, 1, printed)
        self.assertEqual(self.pages(), [])
        self.assertTrue(printed.rstrip().endswith('FAILED: BadCitation, NoRemote, NotFields'), printed)

    def test_unreadable_catalog_fails_the_build(self):
        printed = io.StringIO()
        with contextlib.redirect_stdout(printed):
            status = populate_remarks.main((self.tmp / 'nowhere').as_uri(), self.materials)
        self.assertEqual(status, 1)
        self.assertIn('could not clone the catalog', printed.getvalue())

    def test_repository_without_citation_gets_no_page_and_keeps_a_committed_one(self):
        bare = make_repo(self.tmp / 'bare', {'README.md': 'nothing else\n'})
        committed = '---\ntitle: written by hand\n---\n'
        (self.materials / 'Bare.md').write_text(committed, encoding='utf-8')
        status, printed = self.build({'Bare': f'remote: {bare}\n'})
        self.assertEqual(status, 0, printed)
        self.assertEqual((self.materials / 'Bare.md').read_text(encoding='utf-8'), committed)
        self.assertRegex(printed, r'Bare +no page written: the repository has no CITATION.cff')

    def test_missing_remark_md_gives_a_page_without_a_body(self):
        no_remark = make_repo(self.tmp / 'no-remark', {'CITATION.cff': CITATION})
        status, printed = self.build({'NoRemark': f'remote: {no_remark}\n'})
        self.assertEqual(status, 0, printed)
        metadata, body = front_matter(self.materials / 'NoRemark.md')
        self.assertEqual((metadata['title'], body), ('A Title', ''))

    def test_former_addresses_become_redirects(self):
        status, printed = self.build({'MethodOfModeration': f'remote: {self.good}\n'})
        self.assertEqual(status, 0, printed)
        metadata, _ = front_matter(self.materials / 'MethodOfModeration.md')
        self.assertEqual(metadata['redirect_from'], ['/materials/method-of-moderation/'])


if __name__ == '__main__':
    unittest.main()
