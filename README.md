# Go/No-Go Task

![Maturity: smoke_tested](https://img.shields.io/badge/Maturity-smoke_tested-d97706?style=for-the-badge&labelColor=c2410c)

| Field | Value |
|---|---|
| Name | Go/No-Go Task |
| Version | main (1.2.0) |
| URL / Repository | https://github.com/TaskBeacon/T000005-go-nogo |
| Short Description | Response inhibition task with prepotent Go trials and NoGo withholding. |
| Created By | Zhipeng Cao (zhipeng30@foxmail.com) |
| Date Updated | 2026-03-02 |
| PsyFlow Version | 0.1.8 |
| PsychoPy Version | 2025.1.1 |
| Modality | Behavior/EEG |
| Language | Chinese |
| Voice Name | zh-CN-YunyangNeural |

## 1. Task Overview

This Go/No-Go implementation measures inhibitory control by requiring a key press to frequent Go stimuli and response withholding to infrequent NoGo stimuli. The runtime uses condition-weighted generation (`go:nogo = 3:1`) from config and records both behavioral outcomes and trigger streams for EEG-aligned analysis.

## 2. Task Flow

![Task Flow](task_flow.png)

### Block-Level Flow

| Step | Description |
|---|---|
| Load config | Read `window/task/stimuli/timing/triggers` and mode-specific section (`qa` or `sim`). |
| Collect participant context | Human mode uses `SubInfo`; QA/sim inject deterministic IDs. |
| Initialize runtime | Create PsychoPy window/keyboard, trigger runtime, and stimulus bank. |
| Instruction stage | Show localized instruction screen (and voice in human mode). |
| Block loop | For each block, generate weighted conditions and run all trials. |
| Block feedback | Show block summary with Go and NoGo accuracy. |
| End stage | Show goodbye screen, send experiment end trigger, save CSV. |

### Trial-Level Flow

| Stage | Description |
|---|---|
| `pre_target_fixation` | Show fixation cross for jittered duration (`0.8-1.0 s`). |
| `go_response_window` | Go circle shown up to `1.0 s`; keypress is hit, timeout is miss. |
| `nogo_inhibition_window` | NoGo square shown up to `1.0 s`; keypress is false alarm, timeout is correct withhold. |
| Error feedback stage | Show brief feedback for Go miss or NoGo false alarm. |

### Controller Logic

No adaptive controller is used in this task version. Timing and condition mix are fully config-driven and deterministic given the task seed mode.

## 3. Configuration Summary

### a. Subject Info

| Field | Meaning |
|---|---|
| `subject_id` | Participant ID (3-digit range in current config). |
| `subname` | Participant name (pinyin). |
| `age` | Age metadata field. |
| `gender` | Categorical participant metadata field. |

### b. Window Settings

| Parameter | Value |
|---|---|
| `size` | `[1920, 1080]` |
| `units` | `deg` |
| `screen` | `1` |
| `bg_color` | `gray` |
| `fullscreen` | `true` |
| `monitor_width_cm` | `60` |
| `monitor_distance_cm` | `72` |

### c. Stimuli

| Stimulus ID | Type | Participant-facing content |
|---|---|---|
| `fixation` | `text` | White `+` fixation marker |
| `go` | `circle` | White circle target |
| `nogo` | `rect` | White square non-target |
| `no_response_feedback` | `text` | Prompt shown after Go timeout |
| `nogo_error_feedback` | `text` | Prompt shown after NoGo false alarm |
| `block_break` | `text` | Block progress plus Go/NoGo accuracy |
| `instruction_text` | `textbox` | Localized task instructions |
| `good_bye` | `textbox` | Localized closing message |

### d. Timing

| Parameter | Value |
|---|---|
| `fixation_duration` | `[0.8, 1.0]` |
| `go_duration` | `1.0` |
| `no_response_feedback_duration` | `0.8` |
| `nogo_error_feedback_duration` | `0.8` |

### e. Triggers

| Event | Code |
|---|---:|
| `exp_onset` | 98 |
| `exp_end` | 99 |
| `block_onset` | 100 |
| `block_end` | 101 |
| `fixation_onset` | 1 |
| `go_onset` | 10 |
| `go_response` | 11 |
| `go_miss` | 12 |
| `nogo_onset` | 20 |
| `nogo_response` | 21 |
| `nogo_miss` | 22 |
| `no_response_feedback_onset` | 30 |
| `nogo_error_feedback_onset` | 31 |

## 4. Methods (for academic publication)

Participants completed a Go/No-Go paradigm with a prepotent Go stream and infrequent NoGo events. The task comprised 3 blocks with 70 trials per block (210 total). Trials started with a jittered fixation interval, followed by either a Go circle or a NoGo square for up to 1.0 s. Participants pressed the space key for Go trials and withheld responses for NoGo trials. Condition generation used a 3:1 Go-to-NoGo weighting to induce response prepotency. Behavioral outcomes included Go hits/misses and NoGo false alarms/correct withholds, with block-level accuracy summaries and synchronized event triggers.
