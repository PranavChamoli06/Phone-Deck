from services.base_service import BaseService


class DeviceService(BaseService):
    """
    Handles paired devices.
    """

    def __init__(self, state):
        super().__init__(state)