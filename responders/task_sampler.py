from __future__ import annotations

from typing import Any

from psyflow.sim.contracts import Action, Feedback, Observation, SessionInfo

from .go_nogo_sampler import GoNoGoSamplerResponder


class TaskSamplerResponder:
    """Contract-standard sampler entrypoint for this task."""

    def __init__(self, **kwargs: Any):
        self._impl = GoNoGoSamplerResponder(**kwargs)

    def start_session(self, session: SessionInfo, rng: Any) -> None:
        self._impl.start_session(session, rng)

    def act(self, obs: Observation) -> Action:
        return self._impl.act(obs)

    def on_feedback(self, fb: Feedback) -> None:
        self._impl.on_feedback(fb)

    def end_session(self) -> None:
        self._impl.end_session()
