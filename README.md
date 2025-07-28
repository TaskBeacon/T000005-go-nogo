# Go/No-Go Task

| Field                | Value                        |
|----------------------|------------------------------|
| Name                 | Go/No-Go Task       |
| Version              | main (1.0)                          |
| URL / Repository     | https://github.com/TaskBeacon/GONoGO        |
| Short Description    | A task measuring the ability to respond to target stimuli and inhibit responses to non-target stimuli. |
| Created By           | Zhipeng Cao (zhipeng30@foxmail.com) |
| Date Updated         |2025/07/24                              |
| PsyFlow Version      | 0.1.0                             |
| PsychoPy Version     | 2025.1.1                             |
|Modality            | Behavior/EEG                |
| Language | Chinese |
| Voice Name | zh-CN-YunyangNeural |

## 1. Task Overview

The Go/No-Go task is a cognitive paradigm used to assess response inhibition. In each trial, participants are presented with one of two stimuli: a "go" stimulus (a circle) or a "nogo" stimulus (a square). They are instructed to respond as quickly as possible to the "go" stimulus by pressing a key and to withhold their response to the "nogo" stimulus.

## 2. Task Flow

### Block-Level Flow

| Step                       | Description                                                                 |
|----------------------------|-----------------------------------------------------------------------------|
| Load Config                | Load YAML configuration for subject, task, timing, and stimuli             |
| Collect Subject Info       | Get subject ID, name, age, and gender                                      |
| Setup Triggers             | Initialize trigger sender (via loopback serial)                            |
| Initialize Window/Input    | Set up PsychoPy window and keyboard                                        |
| Load Stimuli               | Load all visual/text stimuli, convert instructions to audio                |
| Show Instructions          | Display instruction text + voice before starting                           |
| Loop Over Blocks           | For each of 3 blocks: run 70 trials with generated conditions               |
| Compute Block Feedback     | Show go accuracy and nogo accuracy per block                           |
| Show Goodbye               | Final message after task completion                                        |
| Save Data                  | Save full trial-level data to CSV                                          |
| Close                      | Close serial connection and PsychoPy window                                |

### Trial-Level Flow

| Step                | Description                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| Fixation            | Present fixation cross for 0.8–1.0s with trigger                            |
| Go Trial       | Present circle; wait up to 1s for a keypress; show feedback if none    |
| No-Go Trial          | Present square; wait up to 1s and record any keypresses              |

## 3. Configuration Summary

### a. Subject Info

| Field       | Meaning                        |
|-------------|--------------------------------|
| subject_id  | Unique participant number (101–999) |
| subname     | Participant name (pinyin)      |
| age         | Age (5–60)                     |
| gender      | Gender (Male or Female)        |

### b. Window Settings

| Parameter             | Value         |
|-----------------------|---------------|
| size                  | [1920, 1080]  |
| units                 | deg           |
| screen                | 1             |
| bg_color              | gray          |
| fullscreen            | True          |
| monitor_width_cm      | 60            |
| monitor_distance_cm   | 72            |

### c. Stimuli

| Name                  | Type   | Description                                         |
|------------------------|--------|-----------------------------------------------------|
| fixation               | text   | White cross "+"                                     |
| go                     | circle | White circle                                        |
| nogo                   | rect   | White square                                        |
| no_response_feedback   | text   | Message shown if participant fails to respond on a go trial       |
| block_break            | text   | Inter-block feedback with go and nogo accuracy         |
| instruction_text       | textbox| Full task instructions with keys      |
| good_bye               | textbox| Final screen thanking participant                   |

### d. Timing

| Phase                       | Duration (s)        |
|-----------------------------|---------------------|
| fixation                    | random 0.8–1.0      |
| go/nogo stimulus (max duration)  | 1.0                 |
| no-response feedback        | 0.8                 |

### e. Triggers

| Event                      | Code  |
|----------------------------|-------|
| exp_onset                  | 98    |
| exp_end                    | 99    |
| block_onset                | 100   |
| block_end                  | 101   |
| fixation_onset             | 1     |
| go_onset                   | 10    |
| go_response                | 11    |
| go_miss                    | 12    |
| nogo_onset                 | 20    |
| nogo_response              | 21    |
| nogo_miss                  | 22    |
| no_response_feedback_onset | 30    |

## 4. Methods (for academic publication)

Participants completed a Go/No-Go task designed to evaluate response inhibition. The task consisted of **3 blocks**, each containing **70 trials**, resulting in a total of **210 trials**. On each trial, participants saw either a circle ("go" stimulus) or a square ("nogo" stimulus). They were instructed to press a key as quickly and accurately as possible when they saw the circle and to withhold their response when they saw the square. On **75% of the trials**, the go stimulus was presented. Trials began with a fixation cross (0.8–1.0s), followed by a go or nogo stimulus. The stimulus remained on screen for up to 1 second. If no response occurred on a go trial, a warning message was presented. Participants received a break after each block, displaying their accuracy for both go and nogo trials.
