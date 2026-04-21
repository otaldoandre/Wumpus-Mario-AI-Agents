from __future__ import annotations

import random

from .base import BaseAgent
from ..core.actions import Action
from ..core.models import Percept


class ReactiveAgent(BaseAgent):
    """
    Agente reativo simples.

    - se houver brilho, tenta `RESCUE`;
    - se houver stink, tenta `SHOOT`.
    - caso contrário, avança em uma direção aleatório ou espera
    """

    def __init__(self, seed: int | None = None):
        self.rng = random.Random(seed)
        print("Agente Reativo!")

    def act(self, percept: Percept, legal_actions: list[Action]) -> Action:
        if percept.glitter:
            return Action.RESCUE

        if percept.has_fireball and percept.stink:
            return Action.SHOOT

        return self.rng.choice(legal_actions)

