# Install VoiceStudio

**VoiceStudio by Transformaiton.com.** This is the step-by-step install for customers who want a local voice studio on Windows, Mac, or Linux. The project page is the [README](../README.md). After the app is open, follow [Clone your own voice](VOICE-CLONING-GUIDE.md). Only clone a voice you own or have permission to use.

Installers are the desktop builds published by the upstream project on [GitHub Releases](https://github.com/debpalash/VoiceStudio/releases/latest). This copy does not publish a second installer and does not change the in-app updater. Those download URLs are what the app and the install scripts use.

Modifications by Transformaiton.com, 16 November 2026. The [AGPL-3.0 licence](../LICENSE) and the upstream copyright notices are unchanged.

## What you need

| | Windows | Mac | Linux |
| --- | --- | --- | --- |
| System | Windows 10 or 11, 64-bit | macOS 13.3 or newer, Apple Silicon | 64-bit Linux with a graphical desktop |
| Disk | About 10 GB free. About 5 GiB if setup picks the CPU libraries, about 9 GiB if it picks NVIDIA CUDA. | Same | Same |
| GPU | Optional. NVIDIA CUDA is used when a driver is present. AMD ROCm is opt-in for selected cards. | Apple Silicon uses Metal automatically. | Optional NVIDIA CUDA. Some GGUF engines can use Vulkan. |
| Account | None. Optional analytics is a Yes/No question, and **No** leaves the app fully local. | Same | Same |

Intel Macs are not supported for the local engines. The window can still open and connect to VoiceStudio on another computer. There is no Linux ARM package. Windows on ARM is experimental.

You do not install Python, FFmpeg, or a voice model by hand for the packaged app. The first launch sets up the runtime after you start it, and each model downloads only after you accept it.

## Before you install

1. Confirm the disk has the free space in the table above.
2. On a laptop, plug in power. The first download is large.
3. Download only from the [latest release](https://github.com/debpalash/VoiceStudio/releases/latest), or use the upstream install script shown below. Both paths check the release checksum when you follow them.
4. Read `SHA256SUMS.txt` on that release and compare it with the file you downloaded before you open it.

## Windows

1. Open the [latest release](https://github.com/debpalash/VoiceStudio/releases/latest).
2. Download `VoiceStudio-<version>-win-x64.exe`.
3. Compare the file with `SHA256SUMS.txt` from the same release (PowerShell):

```powershell
Get-FileHash .\VoiceStudio-*-win-x64.exe -Algorithm SHA256
```

4. Run the installer. The default is a per-user install, with no administrator password. You can pick the folder.
5. Open **VoiceStudio** from the Start menu.
6. If the app asks about product analytics, choose **Yes** or **No**. They are equal choices. **No**, or skipping, leaves analytics off.
7. Start the local runtime setup when the app offers it. Wait until it finishes. The first run can take several minutes.
8. Leave voice-model downloads for the cloning step. The app asks before each one.

The upstream script does steps 2–4 for you, from a normal (not Administrator) PowerShell:

```powershell
irm https://voicestudio.sh/install.ps1 | iex
```

**Windows on ARM.** The experimental installer is `VoiceStudio-<version>-win-arm64.exe`. The window is native. The engine runs as 64-bit Windows under emulation, on the CPU. Expect it to be slower than an Intel or AMD PC.

**No NVIDIA GPU.** Setup installs the smaller CPU build of PyTorch. Speech still works. Pick a light engine when the model list offers a CPU preset.

**AMD GPU.** The default is CPU. Opt-in ROCm for selected RDNA 2 cards is a separate guide: [Windows ROCm](install/windows-rocm.md).

Platform notes that go deeper: [Windows install](install/windows.md).

## macOS

Use this path on Apple Silicon (any M-series chip).

1. Open **Apple menu → About This Mac** and confirm the chip is Apple Silicon.
2. Download `VoiceStudio-<version>-mac-arm64.dmg` from the [latest release](https://github.com/debpalash/VoiceStudio/releases/latest).
3. Compare the checksum:

```bash
shasum -a 256 ~/Downloads/VoiceStudio-*-mac-arm64.dmg
```

4. Open the DMG and drag **VoiceStudio** into **Applications**.
5. Open **VoiceStudio** from Applications.
6. Answer the analytics question, then start the runtime setup and wait for it to finish.

**“VoiceStudio is damaged and can’t be opened.”** That message is Gatekeeper, not a broken download. If the checksum matched, clear the quarantine flag once:

```bash
xattr -dr com.apple.quarantine "/Applications/VoiceStudio.app"
```

Then open the app again. The longer explanation is [Gatekeeper quarantine](install/macos.md#gatekeeper-quarantine).

**Intel Macs are not supported** for a local engine. PyTorch no longer publishes the wheels this app needs for Intel macOS. You can open the `mac-x64` build and point it at a VoiceStudio backend on an Apple Silicon Mac, a Windows PC, or a Linux PC. Do not expect local cloning on the Intel Mac itself.

One-command install on Apple Silicon:

```sh
curl -fsSL https://voicestudio.sh/install | sh
```

Platform notes: [macOS install](install/macos.md).

## Linux

64-bit only, with a desktop session (X11 or Wayland).

### AppImage

1. Download `VoiceStudio-<version>-linux-x64.AppImage` from the [latest release](https://github.com/debpalash/VoiceStudio/releases/latest).
2. Compare it with `SHA256SUMS.txt` (`sha256sum VoiceStudio-*-linux-x64.AppImage`).
3. Start it:

```sh
chmod +x VoiceStudio-*-linux-x64.AppImage
./VoiceStudio-*-linux-x64.AppImage
```

The AppImage does not need FUSE. On first launch, answer the analytics question and start the runtime setup.

### Debian, Ubuntu, and Mint

1. Download `VoiceStudio-<version>-linux-x64.deb`.
2. Install it:

```sh
sudo apt install ./VoiceStudio-<version>-linux-x64.deb
```

3. Open **VoiceStudio** from the app menu.

A `.deb` does not update itself when you quit. Install the newer `.deb`, or use **Restart** when the app offers an update.

### Snap

```sh
sudo snap install voicestudio
sudo snap connect voicestudio:audio-record
```

The second command lets the app hear the microphone. Without it, recording and dictation stay silent.

### Upstream script

On a distribution where you want the AppImage installed for your user:

```sh
curl -fsSL https://voicestudio.sh/install | sh
```

**No NVIDIA driver.** Setup installs the CPU libraries (about 5 GiB) instead of the CUDA set. Speech works on the CPU.

Platform notes: [Linux install](install/linux.md).

## After you install

1. Open **VoiceStudio**.
2. Finish runtime setup if it is not already done.
3. Open **Voice cloning**.
4. Follow [Clone your own voice](VOICE-CLONING-GUIDE.md).

The app does not upload your recording as part of setup. Model files download from their publishers only after you accept them.

## Troubleshooting

| Symptom | Next step |
| --- | --- |
| Checksum does not match `SHA256SUMS.txt` | Delete the file and download it again from the same release. Do not run it. |
| macOS: damaged app, or developer cannot be verified | [Gatekeeper](install/macos.md#gatekeeper-quarantine) |
| Windows: Smart App Control or an antivirus blocks setup | [Install troubleshooting](install/troubleshooting.md). Exclusions do not bypass Smart App Control. |
| “Not enough disk space” | Free space on the drive that holds VoiceStudio. **Settings → Storage** lists the large pieces. |
| Setup runs for a long time on the first launch | Normal for a multi-gigabyte runtime. Wait while the log is still advancing. |
| Intel Mac stops before installing Python | Expected. Use Apple Silicon, Windows, or Linux for the engine, or connect to a remote backend. [macOS guide](install/macos.md). |
| Snap cannot record | `sudo snap connect voicestudio:audio-record` |
| You need the long list of error codes | [Install troubleshooting](install/troubleshooting.md). In the app: **Settings → About → Run self-check**. |

Still stuck with this copy: [info@transformaiton.com](mailto:info@transformaiton.com).

## Source checkout

Customers who want the published app should use the installers above. A source checkout is for people who need this repository itself:

```bash
git clone https://github.com/Transformaiton/VoiceStudio.git
cd VoiceStudio
bun run dev
```

Requirements and the Python setup are in [Electron setup](../electron/README.md). The upstream installer’s extra flags (`--version`, `--main`, `--uninstall`) are documented in [the installer script guide](install/script.md).

## Docker

For a local server rather than the desktop window, use the image the upstream project publishes:

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

Open http://localhost:3900. GPU and Compose variants: [Docker install](install/docker.md).
