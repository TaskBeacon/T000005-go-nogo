# CHANGELOG

All notable development changes for `T000005-go-nogo` are documented here.

## [Unreleased]

### Changed
- Refactored `src/run_trial.py` to use `psyflow`'s native `next_trial_id()` and removed legacy internal `_next_trial_id` and `_deadline_s` boilerplate.

## [1.2.0] - 2026-03-02

### Added
- Added contract-required reference artifacts:
  - `references/references.yaml`
  - `references/references.md`
  - `references/parameter_mapping.md`
  - `references/stimulus_mapping.md`
  - `references/task_logic_audit.md`
- Added `responders/task_sampler.py` as the contract-standard sampler entrypoint.

### Changed
- Updated `main.py` condition generation to use config-defined labels and `TaskSettings.resolve_condition_weights()`.
- Added explicit `task.condition_weights` to all config profiles.
- Updated sampler responder import path in `config/config_sampler_sim.yaml` to `responders.task_sampler:TaskSamplerResponder`.
- Rewrote `README.md` to standardized structure including `### Controller Logic`.
- Updated `taskbeacon.yaml` release metadata and evidence bindings.

### Fixed
- Aligned sampler phase handling with task runtime context phases (`go_response_window`, `nogo_inhibition_window`).

## [1.1.1] - 2026-02-18
- Refactored responder context phase names in `src/run_trial.py` to task-specific labels (removed generic MID-style phase naming).
- Updated stage comments in `src/run_trial.py` to phase-aligned labels for cleaner auditability.
- Updated `README.md` to keep runtime phase documentation aligned with the implemented trial context phases.

### Fixed
- Removed legacy stage comment patterns (`cue/anticipation/target/feedback`) from trial runtime code.

## [1.1.0] - 2026-02-16

### Added
- Added standardized multi-mode entry flow in `main.py` for `human`, `qa`, and `sim`.
- Added mode-specific runtime configs:
  - `config/config_qa.yaml`
  - `config/config_scripted_sim.yaml`
  - `config/config_sampler_sim.yaml`
- Added task-local sampler responder module under `responders/`.
- Added task contract adoption metadata in `taskbeacon.yaml` (`contracts.psyflow_taps: v0.1.0`).

### Changed
- Refactored `main.py` to use `TaskRunOptions`, `parse_task_run_options(...)`, `context_from_config(...)`, and `runtime_context(...)`.
- Updated trigger config to structured schema (`triggers.map`, `triggers.driver`, `triggers.policy`, `triggers.timing`).
- Updated `src/run_trial.py` to inject standardized trial context with `set_trial_context(...)` before response windows.
- Added QA/sim artifact ignore/output scaffolding (`.gitignore`, `outputs/.gitkeep`).

### Fixed
- Aligned task runtime with responder plugin seam for deterministic QA/simulation execution.
