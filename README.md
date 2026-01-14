# Kraken-Testing

Yet another game... made in kraken engine...

## What is this Project?

This is a game make using the [Kraken-Engine](https://github.com/Kraken-Engine/PyKraken) in python. This is a more of a demo project than a game as it only explores different functionalities of the kraken engine.

Currently the game has-

- A top down 2D graphics
- Fully animated player and movement system
- Player character customization

## Structure-

```
kraken-tesing/
│
├───assets/                  # All of the game's assets.
│
├───core/                    # Core common functionalities.
│   ├───animator.py          # Animation utility for the player.
│   ├───constants.py         # Overall game constants.
│   ├───player_data.py       # Enums for different player states.
│   └───types.py             # Common custom annotation types.
│
├───entities/                # Entities of the game.
│   ├───base_entity.py       # The abstract blueprint of all entities.
│   └───player.py            # The main player logic.
│
├───states/                  # Files related to the state system.
│   ├───meta/                # Systems that actual states borrow from.
│   │   ├───base_manager.py  # Custom base manager.
│   │   ├───base_state.py    # Custom base state.
│   │   ├───loader.py        # Loads all game assets and then switches to the main game.
│   │   └───state_enums.py   # Enums for different game states.
│   └───game.py              # The main gameplay state.
│
└───main.py                  # The main entry point of the game. 
```

## Demo Video-

https://github.com/user-attachments/assets/3ea0194e-1bca-4b6b-9cf4-a27ce42b2f52

## How to Run-

Clone the project-
```
git clone https://github.com/Jiggly-Balls/kraken-testing.git
cd kraken-testing
```

Download all dependancies (via [uv](https://docs.astral.sh/uv/))-
```
uv sync --no-dev
```

Run the project-
```
uv run main.py
```

## Controls

W - Move forward
A - Move left
S - Move down
D - Move right

E - Change hair

Left Shift - While moving press Left Shift to run

## Credit

Assets from [Sunny Side World](https://danieldiggle.itch.io/sunnyside) by [danieldiggle](https://itch.io/profile/danieldiggle)
