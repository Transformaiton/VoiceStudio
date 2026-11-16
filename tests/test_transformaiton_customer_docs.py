"""The Transformaiton.com customer pages stay in English and keep the AGPL notices."""
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]


def test_customer_readme_names_transformaiton_and_keeps_the_licence():
    readme = (_ROOT / "README.md").read_text(encoding="utf-8")
    assert "VoiceStudio by Transformaiton.com" in readme
    assert "https://transformaiton.com/" in readme
    assert "info@transformaiton.com" in readme
    assert "https://github.com/Transformaiton" in readme
    assert "https://github.com/debpalash/VoiceStudio" in readme
    assert "Modifications by Transformaiton.com, 16 November 2026" in readme
    assert "only clone voices you own or have permission to use" in readme.lower()
    assert "https://voicestudio.sh/pro" not in readme
    assert "https://app.voicestudio.sh" not in readme
    for shot in (
        "docs/media/electron/voicestudio.gif",
        "docs/media/electron/voice-cloning.webp",
        "docs/media/electron/dubbing.webp",
        "docs/media/electron/voice-design.webp",
        "docs/media/electron/models.webp",
    ):
        assert shot in readme
        assert (_ROOT / shot).is_file()


def test_install_and_cloning_guides_exist_and_credit_upstream():
    install = (_ROOT / "docs" / "INSTALL.md").read_text(encoding="utf-8")
    cloning = (_ROOT / "docs" / "VOICE-CLONING-GUIDE.md").read_text(encoding="utf-8")
    for text in (install, cloning):
        assert "VoiceStudio by Transformaiton.com" in text
        assert "info@transformaiton.com" in text
        assert "16 November 2026" in text
        assert "github.com/debpalash/VoiceStudio" in text
        assert "only clone a voice you own" in text.lower() or "Only clone a voice you own" in text
    assert "win-x64.exe" in install
    assert "mac-arm64.dmg" in install
    assert "linux-x64.AppImage" in install
    assert "Synthesize audio" in cloning
    assert "Save as voice profile" in cloning
    assert "media/electron/voice-cloning.webp" in cloning
    notice = (_ROOT / "LICENSE-NOTICE.md").read_text(encoding="utf-8")
    assert "Copyright 2024-present Palash Debnath and VoiceStudio contributors." in notice
    assert "## Modifications by Transformaiton.com" in notice
    assert "info@transformaiton.com" in notice
