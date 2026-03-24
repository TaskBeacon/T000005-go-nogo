# 任务流程图审计

- generated_at: 2026-03-23T22:51:32
- mode: existing
- task_path: E:\xhmhc\TaskBeacon\benchmark\runs\task_plot_redo\T000005-go-nogo

## 1. 输入与来源

- E:\xhmhc\TaskBeacon\benchmark\runs\task_plot_redo\T000005-go-nogo\README.md
- E:\xhmhc\TaskBeacon\benchmark\runs\task_plot_redo\T000005-go-nogo\config\config.yaml
- E:\xhmhc\TaskBeacon\benchmark\runs\task_plot_redo\T000005-go-nogo\src\run_trial.py

## 2. 从 README 提取的证据

- `pre_target_fixation`：显示注视十字，时长为 `0.8-1.0 s`。
- `go_response_window`：显示 Go 圆形刺激，最长 `1.0 s`；按键视为命中，超时视为漏报。
- `nogo_inhibition_window`：显示 NoGo 方形刺激，最长 `1.0 s`；按键视为误按，保持不反应视为正确抑制。
- 错误反馈阶段：Go 漏报或 NoGo 误按后，显示简短反馈。

## 3. 从 config/source 提取的证据

- go: phase=pre target fixation, deadline_expr=settings.fixation_duration, response_expr=n/a, stim_expr='fixation'
- go: phase=go response window, deadline_expr=settings.go_duration, response_expr=settings.go_duration, stim_expr='go'
- nogo: phase=pre target fixation, deadline_expr=settings.fixation_duration, response_expr=n/a, stim_expr='fixation'
- nogo: phase=nogo inhibition window, deadline_expr=settings.go_duration, response_expr=settings.go_duration, stim_expr='nogo'

## 3b. 规范化说明

- `nogo` 刺激在源码里是 `rect`，但初次推断会落到注释文本。这里将其规范化为白色方形图元，保证图面表达和实际参与者刺激一致。
- 由于 `run_trial.py` 中有条件分支反馈逻辑，错误反馈屏幕仍以说明文字记录，不展开成独立时间线。

## 4. 映射到 task_plot_spec

- timeline collection: one representative timeline per unique trial logic
- phase flow inferred from run_trial set_trial_context order and branch predicates
- participant-visible show() phases without set_trial_context are inferred where possible and warned
- duration/response inferred from deadline/capture expressions
- stimulus examples inferred from stim_id + config stimuli
- conditions with equivalent phase/timing logic collapsed and annotated as variants
- root_key: task_plot_spec
- spec_version: 0.2

## 5. 样式决策与理由

- 采用单一时间线集合视图：每个条件一条时间线，便于对比 Go 与 NoGo。
- 将条件显示名统一为 `NoGo`，并将阶段显示名扩展为 `Go Response Window` / `NoGo Inhibition Window`，提高可读性与可追溯性。

## 6. 渲染参数与约束

- output_file: task_flow.png
- dpi: 300
- max_conditions: 2
- screens_per_timeline: 3
- screen_overlap_ratio: 0.1
- screen_slope: 0.08
- screen_slope_deg: 25.0
- screen_aspect_ratio: 1.4545454545454546
- qa_mode: local
- auto_layout_feedback:
  - layout pass 1: crop-only; left=0.035, right=0.045, blank=0.138
- auto_layout_feedback_records:
  - pass: 1
    metrics: {'left_ratio': 0.0348, 'right_ratio': 0.0447, 'blank_ratio': 0.1385}
    vision_model: None
    issues: []
    adjustments: {}

## 7. 输出文件与校验和

- E:\xhmhc\TaskBeacon\benchmark\runs\task_plot_redo\T000005-go-nogo\references\task_plot_spec.yaml: sha256=26a075839f0e1af9800b4f4c7885555c1b8be5d7df1d1a47b99723c4a6906478
- E:\xhmhc\TaskBeacon\benchmark\runs\task_plot_redo\T000005-go-nogo\references\task_plot_spec.json: sha256=5541acf7df0332529ca677a12de252a2ac157a65216aa175d2f33cf7ece7fb7e
- E:\xhmhc\TaskBeacon\benchmark\runs\task_plot_redo\T000005-go-nogo\references\task_plot_source_excerpt.md: sha256=96d8b0d22fdd444d20ad7250cb6b403adc221c78fc395cdf6d28afa8afa05158
- E:\xhmhc\TaskBeacon\benchmark\runs\task_plot_redo\T000005-go-nogo\task_flow.png: sha256=9617f722c4aeffccac341ee80387ad558a1d515335ebd4de98d693bfb4b6e408

## 8. 推断/不确定项

- unparsed if-tests defaulted to condition-agnostic applicability: nogo_unit.get_state('response', False); not go_unit.get_state('response', False)
- 这两个条件分支仅影响反馈屏幕，主流程时间线不受影响。
