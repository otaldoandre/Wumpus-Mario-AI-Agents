from __future__ import annotations

import random

from .base import BaseAgent
from ..core.actions import Action
from ..core.actions import Direction
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
        print(percept.facing)
        if percept.glitter:
            return Action.RESCUE

        if percept.has_fireball and percept.stink:
            return Action.SHOOT

        # Lida com a percepção do Breeze com base na informação de direção da percepção atual.
        if percept.breeze:
            opposite_direction = {
                Direction.UP: Action.MOVE_DOWN,
                Direction.RIGHT: Action.MOVE_LEFT,
                Direction.DOWN: Action.MOVE_UP,
                Direction.LEFT: Action.MOVE_RIGHT,
            }

            # Lida com o bug de loop infinito quando há dois poços adjacentes adicionando aleatoriedade
            if opposite_direction[percept.facing] in legal_actions and self.rng.random() > 0.05:
                return opposite_direction.get(percept.facing)

        # Evita tomar ações que retirem pontos como mirar e esperar
        return self.rng.choice(
            [Action.MOVE_UP, Action.MOVE_RIGHT, Action.MOVE_DOWN, Action.MOVE_LEFT]
        )

