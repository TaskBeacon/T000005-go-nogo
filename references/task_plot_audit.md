# Task Plot Audit

- generated_at: 2026-03-10T00:17:24
- mode: existing
- task_path: E:\Taskbeacon\T000005-go-nogo

## 1. Inputs and provenance

- E:\Taskbeacon\T000005-go-nogo\README.md
- E:\Taskbeacon\T000005-go-nogo\config\config.yaml
- E:\Taskbeacon\T000005-go-nogo\src\run_trial.py

## 2. Evidence extracted from README

- | Stage | Description |
- |---|---|
- | `pre_target_fixation` | Show fixation cross for jittered duration (`0.8-1.0 s`). |
- | `go_response_window` | Go circle shown up to `1.0 s`; keypress is hit, timeout is miss. |
- | `nogo_inhibition_window` | NoGo square shown up to `1.0 s`; keypress is false alarm, timeout is correct withhold. |
- | Error feedback stage | Show brief feedback for Go miss or NoGo false alarm. |

## 3. Evidence extracted from config/source

- go: phase=pre target fixation, deadline_expr=settings.fixation_duration, response_expr=n/a, stim_expr='fixation'
- go: phase=go response window, deadline_expr=settings.go_duration, response_expr=settings.go_duration, stim_expr='go'
- nogo: phase=pre target fixation, deadline_expr=settings.fixation_duration, response_expr=n/a, stim_expr='fixation'
- nogo: phase=nogo inhibition window, deadline_expr=settings.go_duration, response_expr=settings.go_duration, stim_expr='nogo'

## 4. Mapping to task_plot_spec

- timeline collection: one representative timeline per unique trial logic
- phase flow inferred from run_trial set_trial_context order and branch predicates
- participant-visible show() phases without set_trial_context are inferred where possible and warned
- duration/response inferred from deadline/capture expressions
- stimulus examples inferred from stim_id + config stimuli
- conditions with equivalent phase/timing logic collapsed and annotated as variants
- root_key: task_plot_spec
- spec_version: 0.2

## 5. Style decision and rationale

- Single timeline-collection view selected by policy: one representative condition per unique timeline logic.

## 6. Rendering parameters and constraints

- output_file: task_flow.png
- dpi: 300
- max_conditions: 4
- screens_per_timeline: 6
- screen_overlap_ratio: 0.1
- screen_slope: 0.08
- screen_slope_deg: 25.0
- screen_aspect_ratio: 1.4545454545454546
- qa_mode: local
- auto_layout_feedback:
  - layout pass 1: crop-only; left=0.057, right=0.057, blank=0.171
- auto_layout_feedback_records:
  - pass: 1
    metrics: {'left_ratio': 0.0574, 'right_ratio': 0.0574, 'blank_ratio': 0.1715}

## 7. Output files and checksums

- E:\Taskbeacon\T000005-go-nogo\references\task_plot_spec.yaml: sha256=d10e680e34119d9adaf29c2dbdaa77b22c683689d60568aebaae9bbf6f3f12d6
- E:\Taskbeacon\T000005-go-nogo\references\task_plot_spec.json: sha256=a45b2d09f9dc80b78c796a90b78ca553808e079ce2098c379f25d2838cec747a
- E:\Taskbeacon\T000005-go-nogo\references\task_plot_source_excerpt.md: sha256=b3061d9bb824b8c2788a37a0ffd20de9a669cd7c6a8f6614a2c36bb220491daa
- E:\Taskbeacon\T000005-go-nogo\task_flow.png: sha256=175c75777ec3f4ac911566bfe41578be3d62f2c2e1494fec5ae64fadc104ecfd

## 8. Inferred/uncertain items

- unparsed if-tests defaulted to condition-agnostic applicability: nogo_unit.get_state('response', False); not go_unit.get_state('response', False)
