# Task Plot Review

Review checklist source: `E:/Taskbeacon/skills/task-plot/references/review_checklist.md`.

## Evidence Match

- Pass: task name matches `Go/No-Go Task`.
- Pass: rows match Go and NoGo conditions.
- Pass: phase order matches `src/run_trial.py`: fixation, target response/inhibition window, conditional feedback.
- Pass: timing labels match config: 0.8-1.0 s fixation, 1.0 s target window, 0.8 s feedback.
- Pass: response mapping is correct: Go uses `SPACE`; NoGo withholds response and shows error feedback only if `SPACE` is pressed.

## Visual Quality

- Pass: fixed title and `Construct: inhibitory control / response selection` subtitle are centered in the header.
- Pass: fixed TaskBeacon logo lockup is borderless in the top-right corner and does not overlap content.
- Pass: text is readable and no generated extra title, subtitle, logo, watermark, people, or devices are present.
- Pass: `references/task_plot_timeline_raw.png` preserves the generated timeline before header/logo post-processing.

## README Embed

- Pass: `README.md` contains `## 2. Task Flow`.
- Pass: the first image under `## 2. Task Flow` is exactly `![Task Flow](task_flow.png)`.
- Pass: final image is saved at the task root as `task_flow.png`.
