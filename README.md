# Mario Wumpus em Python/Pygame

<p align="center">
  <img src="mario_wumpus/mario_wumpus/assets/banner_2.png" alt="Banner" width="1000">
</p>

O Mundo do Wumpus - Mario Bros Version é uma releitura do clássico problema de Inteligência Artificial em um universo inspirado em Mario Bros. Nesta aventura, Mario explora um mapa em grade repleto de perigos ocultos, como poços e o temido Bowser, enquanto tenta encontrar e resgatar a princesa. Como no Mundo do Wumpus original, o personagem não enxerga todo o ambiente: ele precisa interpretar sinais do cenário, como brisas e odores, para tomar decisões e avançar com segurança.

## Requisitos

- Python 3.10+
- `pygame`
- `Pillow`

Instalação:

```bash
pip install -r requirements.txt
```

## Como executar

### Jogo com menu em Pygame

```bash
python main.py
```

### Rodar um agente no terminal

```bash
python scripts/run_agent.py
```

### Rodar em modo manual direto, sem menu

```bash
python scripts/play_manual.py
```

## Controles

### Menu
- Mouse: clicar nos botões
- `ESC`: sair

### Jogo
- `WASD`: mover Mario
- `Setas`: ajustar a direção da fireball sem mover
- `F`: atirar fireball na direção atual
- `SPACE`: resgatar a princesa na célula atual
- `TAB`: revelar/esconder o mapa inteiro
- `R`: reiniciar episódio
- `ESC`: voltar ao menu

## Estrutura do projeto

```text
mario_wumpus_pygame/
├── main.py
├── README.md
├── requirements.txt
├── maps/
│   └── fixed_4x4.json
├── scripts/
│   ├── play_manual.py
│   └── run_agent.py
└── mario_wumpus/
    ├── __init__.py
    ├── app.py
    ├── config.py
    ├── core/
    │   ├── actions.py
    │   ├── env.py
    │   ├── generator.py
    │   └── models.py
    ├── agents/
    │   ├── base.py
    │   ├── greedy.py
    │   └── manual.py
    ├── render/
    │   ├── assets.py
    │   ├── renderer.py
    │   └── ui.py
    └── assets/
        └── ...
```

## Conceitos do ambiente

- **Mario** = agente
- **Bowser** = Wumpus
- **Princesa** = objetivo
- **Poços** = armadilhas
- **Brisa** = vento perto de poços
- **Fedor** = presença de Bowser
- **Brilho** = princesa está na célula atual
- **Fireball** = “flecha” do mundo do Wumpus

O ambiente é parcialmente observável: o agente não recebe o mapa inteiro, apenas um `Percept`.

## API do ambiente

Uso típico:

```python
from mario_wumpus.core.env import WumpusEnv
from mario_wumpus.core.actions import Action
from mario_wumpus.config import WorldConfig

env = WumpusEnv(WorldConfig(size=6))
percept = env.reset()

done = False
while not done:
    action = Action.WAIT
    transition = env.step(action)
    percept = transition.percept
    done = transition.done
```

## Como criar um agente novo

Crie uma classe derivada de `BaseAgent` e implemente `act`.

```python
from mario_wumpus.agents.base import BaseAgent
from mario_wumpus.core.actions import Action

class MeuAgente(BaseAgent):
    def reset(self):
        self.count = 0

    def act(self, percept, legal_actions):
        self.count += 1
        return Action.WAIT
```
