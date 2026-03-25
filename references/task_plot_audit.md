# Task Plot Audit

- generated_at: 2026-03-24T19:33:58.5310829+08:00
- mode: existing
- task_path: E:\xhmhc\TaskBeacon\T000005-go-nogo

## 1. Inputs and provenance

- `E:\xhmhc\TaskBeacon\T000005-go-nogo\README.md`
- `E:\xhmhc\TaskBeacon\T000005-go-nogo\config\config.yaml`
- `E:\xhmhc\TaskBeacon\T000005-go-nogo\src\run_trial.py`

## 2. Evidence extracted from README

- `pre_target_fixation`: fixation cross for `0.8-1.0 s`.
- `go_response_window`: white circle, keypress = hit, timeout = miss.
- `nogo_inhibition_window`: white square, withholding = correct, keypress = false alarm.
- Error feedback: brief prompt after Go miss or No-Go false alarm.

## 3. Evidence extracted from config/source

- `go`: phase=`pre_target_fixation`, deadline=`settings.fixation_duration`, response=`n/a`, stim=`fixation`
- `go`: phase=`go_response_window`, deadline=`settings.go_duration`, response=`settings.go_duration`, stim=`go`
- `nogo`: phase=`pre_target_fixation`, deadline=`settings.fixation_duration`, response=`n/a`, stim=`fixation`
- `nogo`: phase=`nogo_inhibition_window`, deadline=`settings.go_duration`, response=`settings.go_duration`, stim=`nogo`
- `nogo` stimulus in config is `rect` with `size: [3, 3]`, which is rendered here as a square.

## 4. Mapping to task_plot_spec

- root_key: `task_plot_spec`
- spec_version: `0.2`
- one timeline per condition
- one phase screen per timeline step

## 5. Style decision and rationale

- Shortened phase labels to `Go` and `No Go` to avoid overlap with the timeline cards.
- Kept the source stimulus type as `rect`, but rendered it as a square because the configured size is equal in both dimensions (`[3, 3]`).
- Kept condition labels compact to preserve readable left-column annotations.

## 6. Rendering parameters and constraints

- output_file: `task_flow.png`
- dpi: `300`
- max_conditions: `2`
- screens_per_timeline: `3`
- screen_overlap_ratio: `0.1`
- screen_slope: `0.08`
- screen_slope_deg: `25.0`
- screen_aspect_ratio: `1.4545454545454546`
- qa_mode: `local`

## 7. Output files and checksums

- `E:\xhmhc\TaskBeacon\T000005-go-nogo\references\task_plot_spec.yaml`: `sha256=7867CD6F4997860045F61CE13FFD59F57DCD04D5B240CFF354D3D12E1A47AFED`
- `E:\xhmhc\TaskBeacon\T000005-go-nogo\references\task_plot_spec.json`: `sha256=E0F5468906B4276BC2109EB79A04C3220848D7712D2DC84AF36AAA24DF9A0830`
- `E:\xhmhc\TaskBeacon\T000005-go-nogo\references\task_plot_source_excerpt.md`: `sha256=CE493EAA8FC4461F673B6CB89C8BA9302F5C4ADA7D6955C5004B1B5E34605C70`
- `E:\xhmhc\TaskBeacon\T000005-go-nogo\task_flow.png`: `sha256=0BBD3A2C4AE7AEE75278C65A36DF9AE0665E450FEEF9DBDBC4E4B16B5E69E5B1`

## 8. Inferred / uncertain items

- `unparsed if-tests defaulted to condition-agnostic applicability: nogo_unit.get_state('response', False); not go_unit.get_state('response', False)`
- This only affects the feedback branch; the main trial timeline is unchanged.
