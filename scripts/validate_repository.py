#!/usr/bin/env python3
"""Validate portable skill identities, examples and repository links."""
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent.parent


def local_file(relative):
    path = (ROOT / relative).resolve()
    if not path.is_relative_to(ROOT) or not path.is_file():
        raise ValueError(f'Missing or out-of-scope file: {relative}')
    return path


def validate():
    catalog = json.loads(local_file('catalog.json').read_text())
    if catalog.get('schemaVersion') != 1 or catalog.get('license') != 'MIT':
        raise ValueError('Unsupported catalog version or license')
    seen = set()
    for skill in catalog['skills']:
        identity = skill['id']
        if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', identity) or len(identity) > 64 or identity in seen:
            raise ValueError(f'Invalid or duplicate skill identity: {identity}')
        seen.add(identity)
        if skill['sourcePath'] != f'skills/{identity}/SKILL.md':
            raise ValueError(f'Skill path does not match identity: {identity}')
        text = local_file(skill['sourcePath']).read_text()
        frontmatter = re.match(r'^---\n(.*?)\n---\n', text, re.S)
        if not frontmatter:
            raise ValueError(f'Missing frontmatter: {identity}')
        name = re.search(r'^name:\s*(.+)$', frontmatter[1], re.M)
        description = re.search(r'^description:\s*(.+)$', frontmatter[1], re.M)
        if not name or name[1].strip() != identity or not description or not description[1].strip():
            raise ValueError(f'Missing or mismatched skill metadata: {identity}')
        contract = skill['firstUse']
        if not contract['result'] or not contract['context'] or not contract['checks']:
            raise ValueError(f'Incomplete first-use contract: {identity}')
        example = json.loads(local_file(skill['examplePath']).read_text())
        if example['skillId'] != identity or example['workflowId'] != skill['companionWorkflowId']:
            raise ValueError(f'Example identity mismatch: {identity}')
        if not example['notice'] or not example['supplied'] or not example['output']['sections'] or not example['review']:
            raise ValueError(f'Incomplete example: {identity}')
        for field in ['title', 'talkTitle', 'requestAction', 'requestContext', 'toolingSummary', 'executionScope']:
            if not isinstance(skill.get(field), str) or not skill[field].strip():
                raise ValueError(f'Missing {field}: {identity}')
    folders = {path.parent.name for path in (ROOT / 'skills').glob('*/SKILL.md')}
    if folders != seen:
        raise ValueError('Skill folders and catalog differ')
    for document in ROOT.rglob('*.md'):
        if '.git' in document.parts:
            continue
        for match in re.finditer(r'\[[^\]]+\]\(([^\s)]+)\)', document.read_text()):
            url = urlsplit(match[1])
            if url.scheme or url.netloc or not url.path:
                continue
            resolved = (document.parent / unquote(url.path)).resolve()
            if not resolved.is_relative_to(ROOT) or not resolved.is_file():
                raise ValueError(f'Broken local link in {document.relative_to(ROOT)}: {match[1]}')
    print(f'Validated {len(seen)} skills, their examples and local Markdown links.')


if __name__ == '__main__':
    try:
        validate()
    except (KeyError, TypeError, ValueError, OSError) as error:
        print(f'Validation failed: {error}', file=sys.stderr)
        sys.exit(1)
