# Parameter Mapping

## Mapping Table

| Parameter ID | Config Path | Implemented Value | Source Paper ID | Evidence (quote/figure/table) | Decision Type | Notes |
|---|---|---|---|---|---|---|
| `conditions` | `task.conditions` | `[go, nogo]` | `W2114411261` | Go/NoGo trial-type manipulation is the paradigm core. | `source_bound` | Two-condition structure is implemented explicitly in config and runtime. |
| `condition_weights` | `task.condition_weights` | `{go: 3, nogo: 1}` | `W2114411261` | Trial-type frequency is used to induce response conflict/prepotency. | `inferred` | Explicit 3:1 weighting is configured and resolved via `TaskSettings.resolve_condition_weights()`. |
| `total_blocks` | `task.total_blocks` | `3` | `W2114411261` | Multi-block runs are standard for stable ERP/behavior estimates. | `inferred` | Block count selected for practical EEG session duration. |
| `total_trials` | `task.total_trials` | `210` | `W2114411261` | Frequent-go design requires sufficient samples per condition. | `inferred` | Set as 70 trials x 3 blocks for robust condition counts. |
| `trial_per_block` | `task.trial_per_block` | `70` | `W2114411261` | Balanced per-block workload supports stable attention and break scheduling. | `inferred` | Matched to `total_trials / total_blocks`. |
| `fixation_duration` | `timing.fixation_duration` | `[0.8, 1.0]` | `W2124906793` | Pre-stimulus stabilization interval is used before inhibition decisions. | `inferred` | Jittered fixation reduces temporal expectancy. |
| `go_duration` | `timing.go_duration` | `1.0` | `W2124906793` | Response-inhibition paradigms use bounded response windows. | `inferred` | Single response window shared across Go and NoGo handling. |
| `no_response_feedback_duration` | `timing.no_response_feedback_duration` | `0.8` | `W2101475053` | Error-related control signals motivate explicit miss/error feedback interpretation. | `inferred` | Task-specific adaptation: brief feedback for Go omissions. |
| `nogo_error_feedback_duration` | `timing.nogo_error_feedback_duration` | `0.8` | `W2101475053` | False alarms are inhibitory-control failures. | `inferred` | Task-specific adaptation: brief feedback for NoGo commission errors. |
| `go_onset` | `triggers.map.go_onset` | `10` | `W2114411261` | Go and NoGo events are analyzed separately in event-locked signals. | `inferred` | Distinct marker retained for EEG epoching. |
| `nogo_onset` | `triggers.map.nogo_onset` | `20` | `W2114411261` | Go and NoGo events are analyzed separately in event-locked signals. | `inferred` | Distinct marker retained for EEG epoching. |
| `go_response` | `triggers.map.go_response` | `11` | `W2114411261` | Response outcomes must be disambiguated by trial type. | `inferred` | Marks Go keypress events. |
| `nogo_response` | `triggers.map.nogo_response` | `21` | `W2101475053` | Commission responses on NoGo map to inhibitory control failures. | `inferred` | Marks false alarm responses. |
| `go_miss` | `triggers.map.go_miss` | `12` | `W2114411261` | Omission errors are behaviorally distinct outcomes. | `inferred` | Timeout path marker for Go misses. |
| `nogo_miss` | `triggers.map.nogo_miss` | `22` | `W2101475053` | Correct withholding on NoGo is an inhibitory success outcome. | `inferred` | Timeout path marker for NoGo correct withhold. |
