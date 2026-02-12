from functools import partial
from psyflow import StimUnit

def run_trial(
    win,
    kb,
    settings,
    condition: str,           # 'go' or 'nogo'
    stim_bank: dict,          # must contain 'fixation', 'go', and 'nogo'
    trigger_runtime=None,
):
    """
    Single Go/No-Go trial:
      - fixation 
        go/nogo 
        record acc/RT
    Returns:
      trial_data dict with fields 'condition','acc','rt','response', + timing/triggers.
    """
    trial_data = {'condition': condition}
    make_unit = partial(StimUnit, win=win, kb=kb,  runtime=trigger_runtime)

    fix_stim  = stim_bank.get('fixation')
    # 1) Fixation (500 ms)
    make_unit(unit_label='fixation') \
        .add_stim(fix_stim) \
        .show(
            duration=settings.fixation_duration,
            onset_trigger=settings.triggers.get('fixation_onset')
        ) \
        .to_dict(trial_data)

    # 2) Go trial branch
    if condition == 'go':
        go_stim   = stim_bank.get('go')
        go_unit = make_unit(unit_label='go') \
            .add_stim(go_stim) \
            .capture_response(
                keys=settings.key_list,
                duration=settings.go_duration,
                onset_trigger=settings.triggers.get('go_onset'),
                response_trigger=settings.triggers.get('go_response'),
                timeout_trigger=settings.triggers.get('go_miss'),
                terminate_on_response=True
            )
        go_unit.to_dict(trial_data)
        resp = go_unit.get_state('response', False)
        if not resp: 
            make_unit(unit_label='no_response_feedback') \
            .add_stim(stim_bank.get('no_response_feedback')) \
            .show(
                duration=settings.no_response_feedback_duration,
                onset_trigger=settings.triggers.get('no_response_feedback_onset')
            ) \
            .to_dict(trial_data)

    # 3) No-go trial branch
    else:
        nogo_stim = stim_bank.get('nogo')
        nogo_unit = make_unit(unit_label='nogo') \
            .add_stim(nogo_stim) \
            .capture_response(
                keys=settings.key_list,
                duration=settings.go_duration,
                onset_trigger=settings.triggers.get('nogo_onset'),
                response_trigger=settings.triggers.get('nogo_response'),
                timeout_trigger=settings.triggers.get('nogo_miss'),
                terminate_on_response=True
            )
        nogo_unit.to_dict(trial_data)
        resp = nogo_unit.get_state('response', False)
        if resp:
            make_unit(unit_label='nogo_error_feedback') \
                .add_stim(stim_bank.get('nogo_error_feedback')) \
                .show(
                    duration=settings.nogo_error_feedback_duration,
                    onset_trigger=settings.triggers.get('nogo_error_feedback_onset')
                ) \
                .to_dict(trial_data)

    return trial_data
