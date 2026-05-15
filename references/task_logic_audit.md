# Task Logic Audit

## 1. Paradigm Intent

- Task: Go/No-Go Task.
- Runtime: PsyFlow/PsychoPy.
- Purpose: measure inhibitory control with frequent Go trials and infrequent NoGo withholding trials.
- Primary conditions: `go`, `nogo`.

## 2. Block/Trial Workflow

- `README.md` documents the Go/NoGo procedure, block flow, trial flow, timing, and trigger mapping.
- `references/parameter_mapping.md` maps condition weights, trial counts, timing, and trigger codes to selected source papers.
- `references/stimulus_mapping.md` maps each condition to fixation, target, and feedback stimuli.
- `references/task_plot_audit.md` records the extracted task-flow evidence used for the rendered task plot.

## 3. Condition Semantics

- `task.conditions` defines `go` and `nogo`.
- `task.condition_weights` defines a 3:1 Go-to-NoGo ratio to create a prepotent response tendency.
- `timing.fixation_duration` is a jittered pre-target fixation interval.
- `timing.go_duration` is shared by Go response and NoGo inhibition windows.
- `triggers.map` separates fixation, Go, NoGo, response, miss, feedback, block, and experiment events.

## 4. Response and Scoring Rules

- `main.py` loads the selected config profile and initializes participant/session state.
- Each block uses `BlockUnit.generate_conditions(...)` with config-defined condition weights.
- The generated condition labels are passed into `src/run_trial.py`.
- Block summaries report Go and NoGo accuracy before continuing.

## 5. Stimulus Layout Plan

- Every trial starts with `pre_target_fixation`.
- Go trials show the circle stimulus during `go_response_window`.
- NoGo trials show the square stimulus during `nogo_inhibition_window`.
- Go keypresses are scored as hits; Go timeouts are scored as misses.
- NoGo keypresses are scored as false alarms; NoGo timeouts are scored as correct withholds.
- Error feedback is shown after Go omissions and NoGo commission errors.

## 6. Trigger Plan

- The configured valid response key is `space`.
- Go accuracy is based on keypress during Go trials.
- NoGo accuracy is based on withholding during NoGo trials.
- Trial outputs include condition, trial index, response state, hit state, timing, and trigger context fields.

## 7. Architecture Decisions (Auditability)

- Experiment, block, fixation, target onset, response/timeout, feedback, and ending triggers are configured in `config/*.yaml`.
- QA mode uses mock triggers and writes structured traces under `outputs/qa`.
- Simulation mode writes responder event streams under `outputs/sim`.
- `set_trial_context(...)` is used before participant-visible phases so output rows remain auditable.

## 8. Inference Log

- The 3:1 condition weighting is an implementation decision aligned with common Go/NoGo prepotency designs.
- Feedback after errors is a task-specific adaptation documented in stimulus and parameter mappings.
- No adaptive controller is used in this version.
- The task plot audit notes that feedback-branch parsing is inferred, while the main Go/NoGo timeline is explicit.
