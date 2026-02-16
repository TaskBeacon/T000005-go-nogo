from __future__ import annotations

from typing import Any

from psyflow.sim.contracts import Action, Feedback, Observation, SessionInfo


class GoNoGoSamplerResponder:
    """Task-specific Go/No-Go sampler responder."""

    def __init__(
        self,
        *,
        go_key: str = "space",
        p_hit_go: float = 0.92,
        p_false_alarm_nogo: float = 0.18,
        p_miss_go: float = 0.04,
        rt_go_mean_s: float = 0.31,
        rt_sd_s: float = 0.05,
        rt_min_s: float = 0.12,
        continue_rt_s: float = 0.25,
    ):
        self.go_key = str(go_key)
        self.p_hit_go = float(p_hit_go)
        self.p_false_alarm_nogo = float(p_false_alarm_nogo)
        self.p_miss_go = float(p_miss_go)
        self.rt_go_mean_s = float(rt_go_mean_s)
        self.rt_sd_s = max(1e-6, float(rt_sd_s))
        self.rt_min_s = max(0.0, float(rt_min_s))
        self.continue_rt_s = float(continue_rt_s)
        self._rng: Any = None

    def start_session(self, session: SessionInfo, rng: Any) -> None:
        self._rng = rng

    def _pick_key(self, valid_keys: list[str], preferred: str | None = None) -> str | None:
        if not valid_keys:
            return None
        if preferred and preferred in valid_keys:
            return preferred
        return valid_keys[0]

    def _sample_rt(self) -> float:
        if self._rng is None:
            return max(self.rt_min_s, self.rt_go_mean_s)
        return max(self.rt_min_s, float(self._rng.gauss(self.rt_go_mean_s, self.rt_sd_s)))

    def _deadline(self, obs: Observation) -> float | None:
        if obs.deadline_s is not None:
            return float(obs.deadline_s)
        if obs.response_window_s is not None:
            return float(obs.response_window_s)
        return None

    def act(self, obs: Observation) -> Action:
        if isinstance(obs, dict):
            obs = Observation.from_dict(obs)
        valid_keys = list(obs.valid_keys or [])
        phase = str(obs.phase or "").strip().lower()

        if phase in ("instruction_text", "block", "goodbye", "block_feedback"):
            key = self._pick_key(valid_keys)
            if key is None:
                return Action(key=None, rt_s=None, meta={"source": "go_nogo_sampler", "reason": "no_valid_key"})
            return Action(key=key, rt_s=max(0.01, self.continue_rt_s), meta={"source": "go_nogo_sampler", "phase": phase})

        if phase != "target" or self._rng is None:
            return Action(key=None, rt_s=None, meta={"source": "go_nogo_sampler", "phase": phase, "reason": "withhold"})

        condition = str(obs.condition_id or "").strip().lower()

        if condition == "go":
            if float(self._rng.random()) < self.p_miss_go:
                return Action(key=None, rt_s=None, meta={"source": "go_nogo_sampler", "condition": condition, "outcome": "miss"})
            if float(self._rng.random()) <= self.p_hit_go:
                key = self._pick_key(valid_keys, preferred=self.go_key)
                outcome = "go_hit"
            else:
                alt_keys = [k for k in valid_keys if k != self.go_key]
                key = self._pick_key(alt_keys)
                outcome = "go_error"
                if key is None:
                    return Action(key=None, rt_s=None, meta={"source": "go_nogo_sampler", "condition": condition, "outcome": "miss"})
            rt_s = self._sample_rt()
            deadline = self._deadline(obs)
            if deadline is not None and rt_s > deadline:
                return Action(key=None, rt_s=None, meta={"source": "go_nogo_sampler", "condition": condition, "outcome": "late"})
            return Action(key=key, rt_s=rt_s, meta={"source": "go_nogo_sampler", "condition": condition, "outcome": outcome})

        if condition == "nogo":
            if float(self._rng.random()) < self.p_false_alarm_nogo:
                key = self._pick_key(valid_keys, preferred=self.go_key)
                rt_s = self._sample_rt()
                deadline = self._deadline(obs)
                if deadline is not None and rt_s > deadline:
                    return Action(key=None, rt_s=None, meta={"source": "go_nogo_sampler", "condition": condition, "outcome": "late"})
                return Action(key=key, rt_s=rt_s, meta={"source": "go_nogo_sampler", "condition": condition, "outcome": "false_alarm"})
            return Action(key=None, rt_s=None, meta={"source": "go_nogo_sampler", "condition": condition, "outcome": "correct_withhold"})

        return Action(key=None, rt_s=None, meta={"source": "go_nogo_sampler", "condition": condition, "outcome": "unknown"})

    def on_feedback(self, fb: Feedback) -> None:
        return None

    def end_session(self) -> None:
        return None
