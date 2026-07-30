from services.base_service import BaseService


class ConnectionService(BaseService):
    """
    Handles backend connection status.
    """

    def __init__(self, state, api_client):
        super().__init__(state)
        self.api_client = api_client

    def check_backend(self):
        connected = self.api_client.health_check()
        self.state.set_connected(connected)

        return connected