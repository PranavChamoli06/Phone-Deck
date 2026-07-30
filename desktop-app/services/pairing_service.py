from services.base_service import BaseService


class PairingService(BaseService):
    """
    Handles pairing operations.
    """

    def __init__(self, state, api_client):
        super().__init__(state)
        self.api_client = api_client

    def start_pairing(self):
        """
        Starts a new pairing session.
        """

        response = self.api_client.start_pairing()

        self.state.set_pairing(
            pin=response["pin"],
            active=True,
            expires_in=response["expires_in"],
        )

        return response