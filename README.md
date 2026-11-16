<div align="center">
  <p><img src="docs/logo.png" alt="VoiceStudio" width="72" height="72" /></p>
  <h1>VoiceStudio by Transformaiton.com</h1>
  <p><strong>Clone your own voice on your own computer. Free to use. Your recordings stay on that machine.</strong></p>
  <p>A local voice studio for small businesses: avatar-video voiceovers, ads, and training, in your own voice, with your consent.</p>
  <p>
    <a href="https://transformaiton.com/">transformaiton.com</a>
    · <a href="mailto:info@transformaiton.com">info@transformaiton.com</a>
    · <a href="https://github.com/Transformaiton">GitHub</a>
    · <a href="docs/INSTALL.md">Install</a>
    · <a href="docs/VOICE-CLONING-GUIDE.md">Clone your voice</a>
  </p>
  <p>
    <a href="LICENSE"><img src="https://img.shields.io/badge/license-AGPL--3.0-52525b?style=flat-square&amp;labelColor=27272a" alt="AGPL-3.0" /></a>
  </p>
</div>

This guide is English only. It is Transformaiton.com’s public copy of [VoiceStudio](https://github.com/debpalash/VoiceStudio), an open-source desktop app for voice cloning, voice design, dubbing, and transcription. The app runs on the computer in front of you. Audio and voice recordings stay on that machine unless you copy them somewhere yourself.

**Only clone a voice you own, or a voice whose owner has given you permission.** A client, employee, or anyone else needs to agree before their voice is cloned. See [Consent](#consent).

## What it does

VoiceStudio turns a short recording of a real person into new speech in that voice. You type the words, pick a language, and the app speaks them on your machine.

You can also:

- Design a new voice from a written description
- Dub a video into another language, timed to the original
- Transcribe speech and dictate into other apps
- Narrate longer scripts, stories, and queued jobs

The default engine is **VoiceStudio** (default, powered by k2-fsa/OmniVoice). It clones from one clean clip across hundreds of languages, without training a new model. Other engines are optional and install only when you choose them. Details: [engine catalog](docs/engines/README.md).

The pictures below are the Electron demo captures already in this repository (default dark theme, bundled demo voice). They show the real app. This copy does not replace the in-app name or icons.

<p align="center">
  <a href="docs/media/electron/voicestudio.mp4">
    <img src="docs/media/electron/voicestudio.gif" alt="Tour of VoiceStudio: voice cloning, voice design, dubbing, and model management in the demo workspace" width="100%" />
  </a><br />
  <sub>Demo workspace · <a href="docs/media/electron/voicestudio.mp4">Watch the tour</a></sub>
</p>

| | |
| --- | --- |
| <a href="docs/media/electron/voice-cloning.png"><img src="docs/media/electron/voice-cloning.webp" alt="Voice cloning workspace with a script, a saved demo voice, and a Synthesize audio button" width="100%" /></a><br />**Voice cloning.** Record or upload a clip, type a script, then synthesize. | <a href="docs/media/electron/dubbing.png"><img src="docs/media/electron/dubbing.webp" alt="Video dubbing workspace" width="100%" /></a><br />**Dubbing.** Translate a video and fit the new speech to the picture. |
| <a href="docs/media/electron/voice-design.png"><img src="docs/media/electron/voice-design.webp" alt="Voice design workspace" width="100%" /></a><br />**Voice design.** Describe a voice and generate it. | <a href="docs/media/electron/models.png"><img src="docs/media/electron/models.webp" alt="Model library for local speech engines" width="100%" /></a><br />**Local models.** Download only the engines you need. |

## Use cases

Built for an owner who wants their own voice on video, without sending that voice to a vendor.

- **Avatar videos.** Record yourself once, then generate the lines for an AI avatar. Export the audio and drop it into the video tool you already use.
- **Ads and social posts.** Write a new offer and hear it in your voice the same day, on the office computer.
- **Training and how-to videos.** Narrate a course or a product walkthrough without booking a booth for every rewrite.
- **A voice you have permission to use.** A partner or spokesperson can record a reference clip and approve the scripts you generate from it.

The first clone is a short recording plus a typed script. The full path is [Clone your own voice](docs/VOICE-CLONING-GUIDE.md).

## Consent

Clone only a voice you own, or a voice you have permission to use.

- For your own avatar, ads, and training, record yourself.
- Do not upload a client’s, employee’s, or stranger’s voice unless they have agreed to that use.
- Keep the reference clip. If someone withdraws permission, stop using that profile and delete it in the app.
- VoiceStudio’s licence does not grant rights in someone else’s voice, likeness, or recording.

The upstream project states the same limit: users must not use the app for unauthorized cloning, impersonation, fraud, or scams, and must follow the laws that apply to them.

## Hardware

A normal office laptop is enough. A GPU makes speech faster. The CPU path works on its own.

| | |
| --- | --- |
| Disk | About **10 GB** free for the app, the Python runtime, and model weights. A CPU-only setup needs about **5 GiB**. An NVIDIA CUDA setup needs about **9 GiB**. |
| Memory | Close other heavy apps on a small laptop. Preparing a clone reference on the CPU uses roughly 0.75 GB plus 0.07 GB for each second of the clip. A 5–15 second clip is the recommended length. |
| Processor | 64-bit Windows, Apple Silicon, or 64-bit Linux. |
| GPU (optional) | NVIDIA CUDA on Windows and Linux. Apple Silicon uses Metal automatically. Selected AMD cards can opt in to Windows ROCm. Without a GPU the app runs on the CPU, slower, and downloads the smaller CPU libraries. |
| Microphone | Needed only if you record inside the app. A quiet room and a close mic beat a long, echoey clip. |
| Network | First launch downloads the runtime, and each model downloads when you accept it. After that, cloning works offline. |

Intel Macs are not supported for the local engines. The app window can open; speech has to run on another computer (Apple Silicon, Windows, or Linux). There is no Linux ARM package. Windows on ARM is experimental: the window is native, and the engine runs on the CPU under emulation.

More detail: [Install](docs/INSTALL.md#what-you-need) · [Windows](docs/install/windows.md) · [macOS](docs/install/macos.md) · [Linux](docs/install/linux.md) · [AMD ROCm](docs/install/windows-rocm.md).

## Install

Desktop installers are published on the upstream [GitHub Releases](https://github.com/debpalash/VoiceStudio/releases/latest) page. This copy does not host a second set of installers, and it does not change the app’s update feed. Check `SHA256SUMS.txt` on that release before you run a download.

The full click-by-click guide is [docs/INSTALL.md](docs/INSTALL.md). Short version:

### Windows

Windows 10 or 11, 64-bit.

1. Download `VoiceStudio-<version>-win-x64.exe` from the [latest release](https://github.com/debpalash/VoiceStudio/releases/latest).
2. Compare it with `SHA256SUMS.txt` from the same release.
3. Run the installer. It installs for the current user and does not need an administrator account.
4. Open **VoiceStudio**. On the first launch, choose whether to send optional product analytics. **No** keeps the app fully local.
5. Let setup download the local runtime when you start it. Voice models download later, only after you accept each one.

Or, in a normal PowerShell window, the upstream installer script picks the package and checks the checksum:

```powershell
irm https://voicestudio.sh/install.ps1 | iex
```

Windows on ARM can try `VoiceStudio-<version>-win-arm64.exe`. Treat that build as experimental. [Windows guide](docs/install/windows.md).

### macOS

macOS 13.3 or newer on Apple Silicon (any M-series chip).

1. Download `VoiceStudio-<version>-mac-arm64.dmg` from the [latest release](https://github.com/debpalash/VoiceStudio/releases/latest).
2. Open the disk image and drag **VoiceStudio** into **Applications**.
3. Open **VoiceStudio** from Applications. If macOS says the app is damaged, the download is usually fine and Gatekeeper has quarantined it. See [the Gatekeeper fix](docs/install/macos.md#gatekeeper-quarantine).
4. Answer the analytics question, then start the local runtime setup.

Intel Macs are not supported for local speech. Install the `mac-x64` build only if you will connect the window to a VoiceStudio engine on another computer. [macOS guide](docs/install/macos.md).

One-command install on Apple Silicon, from Terminal:

```sh
curl -fsSL https://voicestudio.sh/install | sh
```

### Linux

64-bit Linux with a graphical desktop.

**AppImage** (any distribution):

1. Download `VoiceStudio-<version>-linux-x64.AppImage` from the [latest release](https://github.com/debpalash/VoiceStudio/releases/latest).
2. In the download folder:

```sh
chmod +x VoiceStudio-*-linux-x64.AppImage
./VoiceStudio-*-linux-x64.AppImage
```

**Debian, Ubuntu, or Mint:** download `VoiceStudio-<version>-linux-x64.deb`, then `sudo apt install ./VoiceStudio-<version>-linux-x64.deb`.

**Snap:** `sudo snap install voicestudio`, then `sudo snap connect voicestudio:audio-record` so recording can hear the microphone.

The upstream shell installer downloads the AppImage and checks it:

```sh
curl -fsSL https://voicestudio.sh/install | sh
```

[Linux guide](docs/install/linux.md).

### Docker

Optional, for a server on the same machine. Images are `ghcr.io/debpalash/voicestudio`. Open http://localhost:3900 and use the API key this prints.

```sh
export OMNIVOICE_API_KEY="$(openssl rand -hex 32)"
docker run -d --name omnivoice \
  -p 127.0.0.1:3900:3900 \
  -e OMNIVOICE_API_KEY \
  -e OMNIVOICE_DATA_DIR=/app/omnivoice_data \
  -v omnivoice-data:/app/omnivoice_data \
  ghcr.io/debpalash/voicestudio:stable
printf 'API key: %s\n' "$OMNIVOICE_API_KEY"
```

[NVIDIA, AMD, and Compose](docs/install/docker.md).

## Clone your own voice

Full guide: [docs/VOICE-CLONING-GUIDE.md](docs/VOICE-CLONING-GUIDE.md).

1. Open **VoiceStudio** and finish the first-run runtime setup if it is still waiting.
2. Open **Voice cloning** from Home or the sidebar.
3. In **Voice sample**, choose **Record** or **Upload audio**. Use 5–15 seconds of one person speaking, close to the mic, in a quiet room, with no music. WAV, MP3, M4A, FLAC, OGG, AAC, and WebM are accepted.
4. Open **Optional details**. If you know the words in the clip, type them under **Transcript**. You can leave this empty and let the engine listen.
5. Choose **Save as voice profile**, name it (for example “Alex — office mic”), and save. You can reuse this profile without uploading the clip again.
6. In **Script**, type the line the avatar, ad, or lesson should say. Pick the language.
7. Click **Synthesize audio**. The first time, accept the model download if the app asks. Generation runs locally.
8. When **Latest take** appears, use **Save as…** and export a WAV. Import that file into your avatar or video editor.

Generate a second take with the same profile when the script changes. You do not re-record unless you want a cleaner reference.

## Troubleshooting

| What you see | What to do |
| --- | --- |
| macOS says VoiceStudio is damaged or the developer cannot be verified | Gatekeeper quarantined the app. Check the checksum, then clear quarantine. [Fix](docs/install/macos.md#gatekeeper-quarantine). |
| Windows setup stops, or Smart App Control blocks the engine | [Troubleshooting](docs/install/troubleshooting.md). Smart App Control has no per-app exception. You can turn it off, or run the engine on another computer. |
| Setup says the disk is full | Free space on the drive that holds the app. Plan on about 10 GB, or about 5 GiB for CPU-only libraries. **Settings → Storage** shows what is using space. |
| The first launch sits on “Installing” for a long time | The runtime is several GB. Later launches are faster. Leave the window open until the log moves. |
| Cloning asks for a transcript or a speech-to-text model | Type the reference words under **Transcript**, or install the speech-to-text model the page offers. Nothing downloads until you confirm. |
| The take is slow or the app runs out of memory | Use a 5–15 second clip, close other apps, or pick CPU under **Settings → Performance & Device**. A lighter engine (the setup screen’s CPU preset) is the better fit without a GPU. |
| Snap installs, but recording is silent | `sudo snap connect voicestudio:audio-record`, then reopen the app. |
| Intel Mac cannot install the local engine | Expected. Use an Apple Silicon Mac, Windows, or Linux for speech, or connect this Mac’s window to a backend on one of those machines. |

In the app: **Settings → About → Run self-check**. For a problem this table does not list, email [info@transformaiton.com](mailto:info@transformaiton.com) with the self-check result and the app version. The longer upstream list is [docs/install/troubleshooting.md](docs/install/troubleshooting.md).

## Contact

Transformaiton.com is an AI consultancy for small businesses. This repository is the VoiceStudio tool we share with customers.

| | |
| --- | --- |
| Website | [https://transformaiton.com/](https://transformaiton.com/) |
| Email | [info@transformaiton.com](mailto:info@transformaiton.com) |
| GitHub | [https://github.com/Transformaiton](https://github.com/Transformaiton) |
| This copy | [https://github.com/Transformaiton/VoiceStudio](https://github.com/Transformaiton/VoiceStudio) |

Questions about installing this copy, cloning your own voice, or using the audio in an avatar video: email info@transformaiton.com.

Software defects in VoiceStudio itself can also be reported on the upstream tracker: [github.com/debpalash/VoiceStudio/issues](https://github.com/debpalash/VoiceStudio/issues). The upstream community chat is [Discord](https://discord.gg/bzQavDfVV9).

## Credits and licence

VoiceStudio is free software by Palash Debnath and the VoiceStudio contributors.

- Original project: [https://github.com/debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio)
- Licence: [GNU AGPL-3.0](LICENSE) (the licence text is unchanged)
- Copyright notices in the source, and the notice in [LICENSE-NOTICE.md](LICENSE-NOTICE.md), stay in place
- Modifications by Transformaiton.com, 16 November 2026: this English customer guide (`README.md`, `docs/INSTALL.md`, `docs/VOICE-CLONING-GUIDE.md`) and the branding on the public documentation pages. The application, its update feed, and the installer download URLs are unchanged.

AGPL-3.0 lets you use, copy, and modify the app, including for commercial work, if you follow the licence. If you run a modified copy as a network service, you must offer users the source of that modified version. Model weights have their own licences, shown in the app’s model manager. Those terms are separate from the AGPL.

**Consent, again:** only clone voices you own or have permission to use.

## For developers

This repository is the Transformaiton.com fork. To run it from source:

```bash
git clone https://github.com/Transformaiton/VoiceStudio.git
cd VoiceStudio
bun run dev
```

`bun run dev` installs the JavaScript dependencies and, on a supported machine, the Python environment, then opens Electron. Developer setup: [electron/README.md](electron/README.md).

Upstream agent skills install with `npx skills add debpalash/VoiceStudio`. An agent installing the desktop app should follow [docs/install/agent.md](docs/install/agent.md). People who send code to the upstream project sign the Contributor License Agreement first: [contribution licensing](.github/CONTRIBUTING.md#contribution-licensing).

All guides: [docs/README.md](docs/README.md).
