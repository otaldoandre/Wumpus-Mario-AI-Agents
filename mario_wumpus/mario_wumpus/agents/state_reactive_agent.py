from __future__ import annotations

import random

from .base import BaseAgent
from ..core.actions import Action
from ..core.models import Percept


class StateReactiveAgent(BaseAgent):
    """
    Agente baseado em modelos, ou seja, usa percepção atual + memória do passado

    No caso do game atual, permite a utilização de 'percept.visited' e 'percept.position'.

    Estratégia:
    - se vê brilho, usa o `RESCUE`;
    - se sente fedor e ainda tem fireball, atira com base na percepção das casas já visitadas;
    - se sentir brisa, volta para casa anterior já visitada
    - prefere movimentos para células ainda não visitadas;

    """

    def __init__(self, seed: int | None = None):
        self.rng = random.Random(seed)
        self.shoot_dir = None

        # adicionar ultima posicao p lidr com breeze


    def reset(self) -> None:
        return None

    def act(self, percept: Percept, legal_actions: list[Action]) -> Action:

        # A posição de todos os candidatos são todas as casas adjascentes (exceto diagonais) à posição atual!!
        row, col = percept.position.as_tuple()
        candidates = [
            (Action.MOVE_UP, (row - 1, col)),
            (Action.MOVE_RIGHT, (row, col + 1)),
            (Action.MOVE_DOWN, (row + 1, col)),
            (Action.MOVE_LEFT, (row, col - 1)),
        ]

        candidates_for_shoot = [
            (Action.AIM_UP, (row - 1, col)),
            (Action.AIM_RIGHT, (row, col + 1)),
            (Action.AIM_DOWN, (row + 1, col)),
            (Action.AIM_LEFT, (row, col - 1)),
        ]


        if percept.glitter:
            return Action.RESCUE

        # Ao mirar em casas não vistadas (ou seja, que temos certeza que o Bowser não está lá), temos mais
        # chances de acertar o Bowser!
        unseen_options_to_aim = [act for act, pos in candidates_for_shoot if pos not in percept.visited]
        if percept.stink and percept.has_fireball:
            if self.shoot_dir:
                self.shoot_dir = None
                return Action.SHOOT
            else:
                self.shoot_dir = self.rng.choice(unseen_options_to_aim)
                return self.shoot_dir


        # Ao considerar apenas se mover para casas ainda não visitadas, evitamos que o Mario entre em loops!
        unseen = [act for act, pos in candidates if pos not in percept.visited]
        if unseen:
            return self.rng.choice(unseen)

        # Caso as posições adjacentes estejam visitadas, escolher ação aleatória
        return self.rng.choice(legal_actions)
