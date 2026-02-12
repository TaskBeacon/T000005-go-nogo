from psyflow import BlockUnit,StimBank, StimUnit,SubInfo,TaskSettings,initialize_triggers
from psyflow import load_config,count_down, initialize_exp
import pandas as pd
from psychopy import core
from src import run_trial

# 1. Load config
cfg = load_config()

# 2. Collect subject info
subform = SubInfo(cfg['subform_config'])
subject_data = subform.collect()

# 3. Load task settings
settings = TaskSettings.from_dict(cfg['task_config'])
settings.add_subinfo(subject_data)

# 4. setup triggers
settings.triggers = cfg['trigger_config']
trigger_runtime = initialize_triggers(cfg)

# 5. Set up window & input
win, kb = initialize_exp(settings)
# 6. Setup stimulus bank
stim_bank = StimBank(win,cfg['stim_config'])\
    .convert_to_voice(['instruction_text'], voice=settings.voice_name)\
        .preload_all()

# 7. Start experiment
StimUnit('instruction_text',win,kb)\
    .add_stim(stim_bank.get('instruction_text'))\
    .add_stim(stim_bank.get('instruction_text_voice'))\
    .wait_and_continue()
all_data = []
for block_i in range(settings.total_blocks):
    count_down(win, 3, color='white')
    # 8. setup block
    block = BlockUnit(
        block_id=f"block_{block_i}",
        block_idx=block_i,
        settings=settings,
        window=win,
        keyboard=kb)\
    .generate_conditions(
        condition_labels=['go', 'nogo'],
        weights=[3, 1],
        order='random')\
    .on_start(lambda b: trigger_runtime.send(settings.triggers.get("block_onset")))\
    .on_end(lambda b: trigger_runtime.send(settings.triggers.get("block_end")))\
    .run_trial(func=run_trial, stim_bank=stim_bank, trigger_runtime=trigger_runtime)\
    .to_dict(all_data)
    
    # get block data and statistics
    go_trials = block.get_trial_data(key='condition', pattern='go')
    nogo_trials = block.get_trial_data(key='condition', pattern='nogo')

    # --- For go trials ---
    num_go = len(go_trials)
    num_go_hit = sum(trial.get('go_hit', False) for trial in go_trials)
    go_accuracy = num_go_hit / num_go if num_go > 0 else 0

    # --- For nogo trials ---
    num_nogo = len(nogo_trials)
    num_nogo_correct = sum(not trial.get('nogo_hit', False) for trial in nogo_trials)
    nogo_accuracy = num_nogo_correct / num_nogo if num_nogo > 0 else 0

    # show block break screen and statistics
    StimUnit('block',win,kb).add_stim(stim_bank.get_and_format('block_break', 
                                                             block_num=block_i+1,
                                                             total_blocks=settings.total_blocks,
                                                             go_accuracy=go_accuracy,
                                                             nogo_accuracy=nogo_accuracy)).wait_and_continue()
# end of experiment
StimUnit('block',win,kb).add_stim(stim_bank.get('good_bye')).wait_and_continue(terminate=True)
    
# 9. Save data
df = pd.DataFrame(all_data)
df.to_csv(settings.res_file, index=False)

# 10. Close everything
trigger_runtime.close()
core.quit()


