# Task Plot Brief

## Evidence Sources

- `README.md`
- `main.py`
- `config/config.yaml`
- `src/run_trial.py`
- `references/task_logic_audit.md`

## Header

- Title: Go/No-Go Task
- Construct: inhibitory control / response selection

## Participant-Visible Flow

- Instruction screen explains that a circle means press `space` and a square means withhold response.
- The task has 3 blocks with 70 trials per block, 210 trials total.
- Trials are randomly sampled as Go or NoGo using config weights `go:nogo = 3:1`.
- Every trial starts with a white `+` fixation for 0.8-1.0 s.
- Go trial: a white circle appears for up to 1.0 s; pressing `SPACE` is a hit.
- Go miss: if no key is pressed, a no-response feedback screen appears for 0.8 s.
- NoGo trial: a white square appears for up to 1.0 s; participant should withhold response.
- NoGo false alarm: if `SPACE` is pressed, an error feedback screen appears for 0.8 s.
- Correct Go responses and correct NoGo withholding do not show trial feedback.
- After each block, a rest/summary screen shows Go and NoGo accuracy and waits for `space`.

## Rows

- Go: frequent target trial, press `SPACE` to the white circle.
- NoGo: rare inhibition trial, withhold response to the white square.

## Timings

- Fixation: 0.8-1.0 s.
- Target window: 1.0 s max.
- Error feedback: 0.8 s.

## Rendering Notes

- Show only the participant-visible timeline, not block setup screens.
- Show conditional feedback as the final screen in each row: Go miss only if no response, NoGo error only if `SPACE` is pressed.
- The generated raw image must contain only timeline content below a blank header band.
- The final title, `Construct: inhibitory control / response selection` subtitle, and TaskBeacon logo are added by post-processing.
