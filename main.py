import pykraken as kn
from pykraken import Vec2

from core.constants import GAME_TITLE, WINDOW_HEIGHT, WINDOW_WIDTH
from states import GameState
from states.meta import BaseManager, BaseState, LoaderState, StateEnum


def main() -> None:
    kn.init()
    kn.window.create(GAME_TITLE, Vec2(WINDOW_WIDTH, WINDOW_HEIGHT))

    manager = BaseManager(
        post_init_state=StateEnum.GAME,
        bound_state_type=BaseState,
    )
    manager.load_states(LoaderState, GameState)
    manager.change_state(StateEnum.LOADER)

    assert manager.current_state

    while kn.window.is_open():
        kn.renderer.clear(kn.color.PURPLE)
        dt = kn.time.get_delta()

        for event in kn.event.poll():
            manager.current_state.process_event(event, dt)
        manager.current_state.process_update(dt)

        kn.renderer.present()

    kn.quit()


if __name__ == "__main__":
    main()
