from services.api_client import APIClient
from services.connection_service import ConnectionService
from services.device_service import DeviceService
from services.pairing_service import PairingService
from services.websocket_service import WebSocketService
from services.backend_monitor import BackendMonitor

class ServiceContainer:
    """
    Central registry for all application services.

    Creates shared service instances and exposes them
    throughout the application.
    """

    def __init__(self, state):
        # Shared clients
        self.api_client = APIClient()

        # Services
        self.connection = ConnectionService(state, self.api_client)
        self.pairing = PairingService(state, self.api_client)
        self.device = DeviceService(state)
        self.websocket = WebSocketService(state)
        self.backend_monitor = BackendMonitor(self.connection)