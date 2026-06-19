# Task Plot Review

Review checklist source: `E:/Taskbeacon/skills/task-plot/references/review_checklist.md`.

## Evidence Match

- Pass: task name matches `Go/No-Go Task`.
- Pass: condition rows are `Go` and `NoGo`, matching config conditions.
- Pass: phase order matches `src/run_trial.py`: fixation, target response/inhibition window, conditional error feedback.
- Pass: timing labels match config: fixation `0.8-1.0 s`, target window `1.0 s max`, feedback `0.8 s`.
- Pass: visible screen content uses participant-facing `+`, circle, square, `Miss`, and `Error` screens.
- Pass: response instructions match runtime logic: Go presses `SPACE`; NoGo withholds response; NoGo error appears only if `SPACE` is pressed.

## Visual Quality

- Pass: text is readable at document preview size.
- Pass: rows and arrows clearly imply temporal order.
- Pass: screens, timing labels, and condition labels do not overlap.
- Pass: the figure is a scientific workflow diagram with restrained styling.
- Pass: fixed TaskBeacon logo lockup is borderless in the top-right corner and does not overlap content.
- Pass: no extra generated logo, watermark, people, devices, or decorative scenery are present.

## README Embed

- Pass: `README.md` contains `## 2. Task Flow`.
- Pass: the first image under `## 2. Task Flow` is exactly `![Task Flow](task_flow.png)`.
- Pass: final image is saved at the task root as `task_flow.png`.
