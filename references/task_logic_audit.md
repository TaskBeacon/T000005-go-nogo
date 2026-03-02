# Task Logic Audit

## 1. Paradigm Intent

This task implements a classic Go/No-Go response-inhibition paradigm for behavioral and EEG contexts. The core manipulation is a prepotent Go stream with less frequent NoGo trials, such that inhibitory control can be estimated via NoGo false alarms and Go omissions.

Evidence anchors:
- `W2114411261`: Go/No-Go trial-type frequency and response-conflict framing.
- `W2124906793`: inhibition-window timing context from response-inhibition literature.
- `W2101475053`: dissociation of inhibition/control processes, used to justify explicit NoGo error outcome handling.

## 2. Block/Trial Workflow

Block workflow:
1. Show instruction screen and wait for continue key.
2. For each block, generate trial conditions from config labels and weights.
3. Emit block start trigger.
4. Run trials sequentially.
5. Emit block end trigger.
6. Show block feedback summary with Go and NoGo accuracy.

Trial workflow:
1. `pre_target_fixation`: show fixation for jittered interval (`0.8-1.0 s`).
2. Branch by condition:
   - `go_response_window`: show circle, capture response up to `1.0 s`.
   - `nogo_inhibition_window`: show square, capture/withhold response up to `1.0 s`.
3. Optional brief error feedback:
   - Go miss: show `no_response_feedback`.
   - NoGo false alarm: show `nogo_error_feedback`.
4. Return trial dictionary for block-level aggregation.

## 3. Condition Semantics

| Condition | Behavioral Rule | Outcome Semantics |
|---|---|---|
| `go` | Press `space` during `go_response_window` | Hit if response observed; miss if timeout occurs. |
| `nogo` | Withhold response during `nogo_inhibition_window` | Correct withhold if timeout; false alarm if response observed. |

Condition generation:
- Labels are loaded from `task.conditions`.
- Weights are loaded from `task.condition_weights` and resolved by `TaskSettings.resolve_condition_weights()`.
- Current configured ratio is `go:nogo = 3:1`.

## 4. Response and Scoring Rules

- Valid key set is `task.key_list` (current task profile: `space`).
- Go scoring:
  - `go_hit=True` when response is present within deadline.
  - `go_hit=False` and trigger `go_miss` on timeout.
- NoGo scoring:
  - `nogo_hit=True` when response is present (false alarm).
  - `nogo_hit=False` on timeout (correct withhold), with trigger `nogo_miss`.
- Block metrics in `main.py`:
  - Go accuracy = `sum(go_hit) / N_go`
  - NoGo accuracy = `sum(not nogo_hit) / N_nogo`

## 5. Stimulus Layout Plan

- Window units: `deg`.
- Centered single-object layout per stage.
- `fixation`: centered white `+` text.
- `go`: centered white circle (`size=3`).
- `nogo`: centered white square (`size=[3,3]`).
- Feedback screens:
  - Text-only centered warning for Go omission.
  - Text-only centered warning for NoGo false alarm.
- Block and instruction screens use centered text/textbox layouts with consistent Chinese font (`SimHei`) for participant-facing text stimuli.

## 6. Trigger Plan

| Phase/Event | Trigger Key | Code |
|---|---|---:|
| Experiment start | `exp_onset` | 98 |
| Experiment end | `exp_end` | 99 |
| Block start | `block_onset` | 100 |
| Block end | `block_end` | 101 |
| Fixation onset | `fixation_onset` | 1 |
| Go onset | `go_onset` | 10 |
| Go response | `go_response` | 11 |
| Go timeout | `go_miss` | 12 |
| NoGo onset | `nogo_onset` | 20 |
| NoGo response (false alarm) | `nogo_response` | 21 |
| NoGo timeout (correct withhold) | `nogo_miss` | 22 |
| Go miss feedback onset | `no_response_feedback_onset` | 30 |
| NoGo error feedback onset | `nogo_error_feedback_onset` | 31 |

## 7. Architecture Decisions (Auditability)

- Runtime mode wiring is centralized in `main.py` (`human|qa|sim`).
- Trial logic is isolated in `src/run_trial.py` and phase-labeled using `set_trial_context(...)` for audit traceability.
- Participant-facing wording is config-driven (`stimuli` text/textbox entries), not hardcoded in trial runtime.
- Condition weighting is explicit in config and resolved through `TaskSettings.resolve_condition_weights()`.
- Sampler entrypoint is standardized via `responders/task_sampler.py`.

## 8. Inference Log

| Decision | Type | Rationale |
|---|---|---|
| Keep explicit brief feedback for Go omissions and NoGo false alarms | inferred | This task variant already operationalized feedback and trigger channels; retained as a deliberate adaptation while preserving Go/NoGo core structure. |
| Use `go:nogo = 3:1` weighting in config | inferred | Frequent-go prepotency is required for inhibition pressure; explicit config ratio improves auditability versus hardcoded weights. |
| Use single-key response (`space`) mapping | inferred | Matches existing task implementation and preserves minimal motor complexity for broad participant populations. |
