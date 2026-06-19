# Task Plot Brief

## Evidence Sources

- `README.md`
- `main.py`
- `config/config.yaml`
- `src/run_trial.py`
- `references/task_logic_audit.md`

## Task

- Name: Go/No-Go Task
- Goal measured: inhibitory control
- Runtime: PsyFlow/PsychoPy behavioral/EEG task
- Structure: 3 blocks, 70 trials per block, 210 trials total
- Condition scheduling: random weighted generation with `go:nogo = 3:1`
- Response key: `space`
- Controller: no adaptive controller; timing and condition mix are config-driven

## Participant-Visible Flow

- Instruction screen explains circle means press space and square means withhold.
- Each block starts after countdown in human mode.
- Trials are randomly sampled as Go or NoGo using the 3:1 weights.
- Every trial starts with a white `+` fixation for 0.8-1.0 s.
- Go trial: white circle appears for up to 1.0 s; pressing `space` is a hit and ends the response window.
- Go miss: if no key is pressed, a no-response feedback screen appears for 0.8 s.
- NoGo trial: white square appears for up to 1.0 s; participant should withhold all keypresses.
- NoGo false alarm: if `space` is pressed, an error feedback screen appears for 0.8 s.
- Correct Go response and correct NoGo withholding do not show feedback.
- After each block, a rest/summary screen shows Go and NoGo accuracy and waits for `space`.
- A goodbye screen ends the task.

## Diagram Rows

- Go trial: frequent target trial, press `SPACE` to circle.
- NoGo trial: rare inhibition trial, withhold response to square.

## Timing Labels

- Fixation: `0.8-1.0 s`
- Target window: `1.0 s max`
- Error feedback: `0.8 s`

## Visual Labels To Preserve

- `Go`
- `NoGo`
- `+`
- `white circle`
- `white square`
- `SPACE`
- `0.8-1.0 s`
- `1.0 s max`
- `0.8 s`
