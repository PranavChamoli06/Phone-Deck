from state.app_state import AppState


class BaseService:
    """
    Base class for all application services.

    Provides shared access to the application's state.
    """

    def __init__(self, state: AppState):
        self.state = state