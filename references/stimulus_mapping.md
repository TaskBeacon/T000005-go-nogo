# Stimulus Mapping

## Mapping Table

| Condition | Stage/Phase | Stimulus IDs | Participant-Facing Content | Source Paper ID | Evidence (quote/figure/table) | Implementation Mode | Asset References | Notes |
|---|---|---|---|---|---|---|---|---|
| `go` | `pre_target_fixation -> go_response_window -> feedback_if_miss` | `fixation`, `go`, `no_response_feedback` | Fixation cross, then white circle requiring space-key response, with brief warning text after omission. | `W2114411261` | Go trial stream establishes prepotent response tendency and conflict context. | `psychopy_builtin` | `n/a` | `no_response_feedback` is a task-specific adaptation for omission awareness. |
| `nogo` | `pre_target_fixation -> nogo_inhibition_window -> feedback_if_false_alarm` | `fixation`, `nogo`, `nogo_error_feedback` | Fixation cross, then white square requiring response withholding, with brief warning text after commission error. | `W2114411261` | NoGo trials probe inhibitory control under prepotent Go response tendency. | `psychopy_builtin` | `n/a` | `nogo_error_feedback` is a task-specific adaptation for explicit error signaling. |

Accepted implementation modes:
- `psychopy_builtin`
- `generated_reference_asset`
- `licensed_external_asset`
