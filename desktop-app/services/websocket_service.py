from services.base_service import BaseService


class WebSocketService(BaseService):
    """
    Handles realtime communication
    with the backend.
    """

    def __init__(self, state):
        super().__init__(state)