from functools import partial

from psyflow import StimUnit, set_trial_context, next_trial_id

# trial stages use task-specific phase labels via set_trial_context(...)

def run_trial(
    win,
    kb,
    settings,
    condition: str,
    stim_bank: dict,
    trigger_runtime=None,
    block_id=None,
    block_idx=None,
):
    """Run one Go/No-Go trial."""
    trial_id = next_trial_id()
    trial_data = {"condition": condition}
    make_unit = partial(StimUnit, win=win, kb=kb, runtime=trigger_runtime)

    # phase: pre_target_fixation
    fix_unit = make_unit(unit_label="fixation").add_stim(stim_bank.get("fixation"))
    set_trial_context(
        fix_unit,
        trial_id=trial_id,
        phase="pre_target_fixation",
        deadline_s=settings.fixation_duration,
        valid_keys=list(settings.key_list),
        block_id=block_id,
        condition_id=str(condition),
        task_factors={"condition": str(condition), "stage": "pre_target_fixation", "block_idx": block_idx},
        stim_id="fixation",
    )
    fix_unit.show(
        duration=settings.fixation_duration,
        onset_trigger=settings.triggers.get("fixation_onset"),
    ).to_dict(trial_data)

    # phase: go_response_window
    if condition == "go":
        go_unit = make_unit(unit_label="go").add_stim(stim_bank.get("go"))
        set_trial_context(
            go_unit,
            trial_id=trial_id,
            phase="go_response_window",
            deadline_s=settings.go_duration,
            valid_keys=list(settings.key_list),
            block_id=block_id,
            condition_id=str(condition),
            task_factors={"condition": str(condition), "stage": "go_response_window", "block_idx": block_idx},
            stim_id="go",
        )
        go_unit.capture_response(
            keys=settings.key_list,
            duration=settings.go_duration,
            onset_trigger=settings.triggers.get("go_onset"),
            response_trigger=settings.triggers.get("go_response"),
            timeout_trigger=settings.triggers.get("go_miss"),
            terminate_on_response=True,
        )
        go_unit.to_dict(trial_data)

        if not go_unit.get_state("response", False):
            make_unit(unit_label="no_response_feedback").add_stim(stim_bank.get("no_response_feedback")).show(
                duration=settings.no_response_feedback_duration,
                onset_trigger=settings.triggers.get("no_response_feedback_onset"),
            ).to_dict(trial_data)
    else:
        nogo_unit = make_unit(unit_label="nogo").add_stim(stim_bank.get("nogo"))
        set_trial_context(
            nogo_unit,
            trial_id=trial_id,
            phase="nogo_inhibition_window",
            deadline_s=settings.go_duration,
            valid_keys=list(settings.key_list),
            block_id=block_id,
            condition_id=str(condition),
            task_factors={"condition": str(condition), "stage": "nogo_inhibition_window", "block_idx": block_idx},
            stim_id="nogo",
        )
        nogo_unit.capture_response(
            keys=settings.key_list,
            duration=settings.go_duration,
            onset_trigger=settings.triggers.get("nogo_onset"),
            response_trigger=settings.triggers.get("nogo_response"),
            timeout_trigger=settings.triggers.get("nogo_miss"),
            terminate_on_response=True,
        )
        nogo_unit.to_dict(trial_data)

        if nogo_unit.get_state("response", False):
            make_unit(unit_label="nogo_error_feedback").add_stim(stim_bank.get("nogo_error_feedback")).show(
                duration=settings.nogo_error_feedback_duration,
                onset_trigger=settings.triggers.get("nogo_error_feedback_onset"),
            ).to_dict(trial_data)

    # outcome display
    return trial_data
