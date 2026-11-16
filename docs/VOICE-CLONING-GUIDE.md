# Clone your own voice

**VoiceStudio by Transformaiton.com.** Use this after [install](INSTALL.md). It walks through cloning the voice you will use for avatar videos, ads, and training, on your own computer.

The picture is an existing Electron capture from this repository: the voice-cloning workspace in the demo, with the bundled demo voice and the default dark theme.

<p align="center">
  <a href="media/electron/voice-cloning.png"><img src="media/electron/voice-cloning.webp" alt="Voice cloning workspace: script editor, Demo Voice sample, and Synthesize audio" width="100%" /></a>
</p>

Modifications by Transformaiton.com, 16 November 2026. Licence: [AGPL-3.0](../LICENSE). Original project: [github.com/debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio).

## Consent

Only clone a voice you own, or a voice you have permission to use.

- Your own avatar, ad, or course: record yourself.
- Anyone else: get a clear yes for this use before you upload or record them. A voice pulled from a podcast, a sales call, or a social clip is not yours to clone just because you can download the audio.
- If permission is withdrawn, delete that voice profile in the app and stop shipping audio made from it.
- The AGPL covers the software. It does not give you rights in another person’s voice.

## Record a reference

The clone copies the clip, not a studio ideal. Room echo, background music, and a second speaker show up in the result.

Do this:

1. Use a quiet room. A closet or a parked car is often cleaner than an open office.
2. Sit close to the microphone, as you would for a video call. A headset mic is enough.
3. Speak the way you want the avatar to sound: pace, energy, and accent.
4. Record **5–15 seconds** of continuous speech. About 8 seconds is a good target. One speaker only. No music.
5. Read a couple of ordinary sentences. You do not need to sing or act out emotions.

The cloning screen accepts up to 75 seconds, but the default engine uses the best stretch of speech, up to about 15 seconds. A longer file does not make a closer clone. Clip length by engine: [reference clip length](engines/README.md#reference-clip-length).

Accepted files: WAV, MP3, M4A, FLAC, OGG, AAC, and WebM.

If you already have a clean voiceover from a previous video, you can use 5–15 seconds of that file instead of recording again, as long as it is your voice or a voice you have permission to use.

## In the app

1. Open **VoiceStudio**. If this is the first launch, finish runtime setup first. [Install](INSTALL.md#after-you-install).
2. Open **Voice cloning**. Home has a Voice cloning card. The sidebar has the same destination.
3. Find **Voice sample**.
   - **Record** — speak the reference now. Allow the microphone if the system asks.
   - **Upload audio** — or drop a file on “Drop audio here”. 
4. Play the clip back with the sample’s play control. If you hear noise, echo, or another person, record again before you generate.
5. Open **Optional details**.
   - **Transcript** — type the exact words in the clip when you know them. This is the usual fix when generation says the reference has no transcript.
   - You may leave the transcript empty. The engine can listen, which needs a speech-to-text model. The page offers **Install** for the recommended model. It downloads only after you click.
6. Choose **Save as voice profile**. Enter a name you will recognize later, such as “Jordan — headset, quiet room”. Choose **Save**. The profile is stored on this computer.
7. Click the **Script** field. Type the line the avatar or ad should say. Placeholder text in the app is “What should this voice say?”.
8. Set **Language** to the language of that script.
9. Click **Synthesize audio**. The first accepted model download can take a while. Later takes start faster. Generation stays on this machine.
10. Read **Latest take**. Play it. If it is the take you want, choose **Save as…** and save a WAV (the lossless option).

To say a different line in the same voice, edit the script and synthesize again. Do not upload the clip a second time.

**Save as…** writes a file you own. Import that file into the avatar or editor you use for the video (the tool’s voice or audio track). VoiceStudio does not upload the WAV to an avatar service for you.

## Export for an avatar video

1. Write the on-screen line in **Script**, in the language the viewer will hear.
2. Synthesize with your saved profile.
3. **Save as…** a WAV.
4. In the avatar or video tool, replace the avatar’s audio with that WAV, or drop it on the timeline under the picture.
5. Export the video from that tool. Keep the WAV if you may need to re-cut the video later.

For a page of training narration, generate one take per paragraph so a rewrite does not force you to redo the whole lesson. Stories and batch jobs exist in the app for longer work; the single-take path above is the one to learn first.

## If the voice does not sound like you

Work through these in order:

1. **The clip is the problem.** Re-record 5–15 seconds, closer to the mic, in a quieter room. Echo in the clip becomes echo in the clone.
2. **The transcript does not match the clip.** Retype the words you actually said, or clear the transcript and let the engine listen.
3. **The script is much more energetic, or much flatter, than the clip.** Record a new reference in the tone you want, then save a second profile.
4. **The take is slow or harsh on a laptop without a GPU.** Shorten the script, leave other apps closed, and try the CPU preset the model list recommends. Quality and speed by machine are described in [performance](performance.md).

A longer reference than 15 seconds will not close the gap. The default engine does not use the whole file.

## Common problems

| Message or symptom | What to do |
| --- | --- |
| No speech-to-text model, or `REFERENCE_STT_MISSING` | Type the clip’s words into **Transcript**, or install the speech-to-text model the page offers. |
| Not enough memory | Use a 3–10 second clip, close other apps, and retry. On CPU, reference preparation needs about 0.75 GB plus 0.07 GB per second of audio. |
| The disk filled up during the model download | Free space under **Settings → Storage**, then retry. Plan on several GB for the first model. |
| **Synthesize audio** stays busy on the first take | The model is downloading or loading. Wait. The next take is quicker. |
| Recording stays silent on a Snap install | `sudo snap connect voicestudio:audio-record`, then reopen VoiceStudio. |
| You uploaded someone else’s voice “just to try” | Stop. Delete the profile. Clone only a voice you own or have permission to use. |

More codes: [install troubleshooting](install/troubleshooting.md). Help with this copy: [info@transformaiton.com](mailto:info@transformaiton.com).
