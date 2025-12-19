import pykraken as kn
from game_state import StateManager
from pykraken import Vec2

from core.constants import GAME_TITLE, WINDOW_HEIGHT, WINDOW_WIDTH
from states import GameState
from states.meta import BaseState, StateEnum


def main() -> None:
    manager = StateManager(bound_state_type=BaseState)
    manager.load_states(GameState)
    manager.change_state(StateEnum.GAME)

    assert manager.current_state

    kn.init()
    kn.window.create(GAME_TITLE, Vec2(WINDOW_WIDTH, WINDOW_HEIGHT))

    while kn.window.is_open():
        kn.renderer.clear(kn.color.PURPLE)
        dt = kn.time.get_delta()

        for event in kn.event.poll():
            manager.current_state.process_event(event)
        manager.current_state.process_update(dt)

        kn.renderer.present()


if __name__ == "__main__":
    main()
