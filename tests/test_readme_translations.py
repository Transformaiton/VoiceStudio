"""The translated READMEs live in docs/readme/; their relative links must still resolve."""
from __future__ import annotations

import html
import re
from pathlib import Path

import pytest

_ROOT = Path(__file__).resolve().parents[1]
_TRANSLATIONS = sorted((_ROOT / "docs" / "readme").glob("README_*.md"))
_TARGET = re.compile(r'(?:src(?:set)?="|href="|\]\()([^")\s]+)')
_FENCE = re.compile(r"^```([^\n]*)\n(.*?)^```[ \t]*$", re.MULTILINE | re.DOTALL)
_EXPECTED = {
    f"README_{code}.md"
    for code in ("AR", "CN", "DE", "ES", "FR", "HI", "ID", "IT", "JA", "KO",
                 "NL", "PL", "PT", "RU", "TH", "TR", "TW", "UK", "VI")
}


def test_translations_are_present_and_the_customer_readme_is_english():
    """This copy's customer page is English. Upstream translations stay in docs/readme/."""
    assert _EXPECTED <= {p.name for p in _TRANSLATIONS}, "English plus 19 translations must be available"
    root = (_ROOT / "README.md").read_text(encoding="utf-8")
    assert "VoiceStudio by Transformaiton.com" in root
    assert "This guide is English only." in root
    assert not list(_ROOT.glob("README_*.md")), "translations belong in docs/readme/, not the repo root"


@pytest.mark.parametrize("path", _TRANSLATIONS, ids=lambda p: p.name)
def test_every_translation_links_to_english_and_every_other_translation(path):
    """The language switcher must stay complete when a translation is added."""
    text = path.read_text(encoding="utf-8")
    expected = {"../../README.md"} | {p.name for p in _TRANSLATIONS if p != path}
    missing = sorted(t for t in expected if f'href="{t}"' not in text)
    assert not missing, f"{path.name} language switcher is missing: {missing}"


@pytest.mark.parametrize("path", _TRANSLATIONS, ids=lambda p: p.name)
def test_every_relative_link_in_a_translation_resolves(path):
    missing = []
    for target in _TARGET.findall(path.read_text(encoding="utf-8")):
        if re.match(r"(https?:|mailto:|#|//|data:)", target):
            continue
        if not (path.parent / target.split("#")[0]).resolve().exists():
            missing.append(target)
    assert not missing, f"{path.name} links to files that do not exist: {missing}"


@pytest.mark.parametrize("path", _TRANSLATIONS, ids=lambda p: p.name)
def test_translation_pages_keep_install_urls_and_point_marketing_at_transformaiton(path):
    """Installer downloads stay on the upstream host. Website, Pro and Cloud links do not."""
    text = path.read_text(encoding="utf-8")
    assert "https://voicestudio.sh/install" in text, path.name
    assert "VoiceStudio by Transformaiton.com" in text.split("\n", 1)[0] or text.startswith("> **VoiceStudio by Transformaiton.com.**")
    for target in re.findall(r'href="(https://[^"]+)"', text):
        assert not target.startswith("https://voicestudio.sh/pro"), path.name
        assert not target.startswith("https://app.voicestudio.sh"), path.name
        assert not target.startswith("https://voicestudio.sh/?"), path.name
        if "voicestudio.sh" in target:
            assert "/install" in target, f"{path.name} still links a marketing page: {target}"


@pytest.mark.parametrize("path", _TRANSLATIONS, ids=lambda p: p.name)
def test_translation_navigation_anchors_resolve(path):
    text = _FENCE.sub("", path.read_text(encoding="utf-8"))
    anchors = set(re.findall(r'\bid="([^"]+)"', text))
    for heading in re.findall(r"^#{1,6}\s+(.+)$", text, re.MULTILINE):
        heading = html.unescape(re.sub(r"<[^>]+>|[`*]", "", heading)).lower()
        anchors.add(re.sub(r"[^\w\s-]", "", heading).strip().replace(" ", "-"))
    missing = [target for target in _TARGET.findall(text) if target.startswith("#") and target[1:] not in anchors]
    assert not missing, f"{path.name} has broken navigation anchors: {missing}"


