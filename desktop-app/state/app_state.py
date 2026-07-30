from PySide6.QtCore import QObject, Signal


class AppState(QObject):
    """
    Central application state.

    Every part of the application reads or updates this object
    instead of communicating directly with other widgets.
    """

    # ---------- Signals ----------

    connection_changed = Signal(bool)
    page_changed = Signal(str)
    device_changed = Signal(str)
    pairing_changed = Signal()

    def __init__(self):
        super().__init__()

        self._connected = False
        self._current_page = "dashboard"
        self._current_device = ""
        self._pairing_pin = ""
        self._pairing_active = False
        self._pairing_expires_in = 0

    # ---------- Connection ----------

    @property
    def connected(self):
        return self._connected

    def set_connected(self, value: bool):
        if self._connected == value:
            return

        self._connected = value
        self.connection_changed.emit(value)

    # ---------- Current Page ----------

    @property
    def current_page(self):
        return self._current_page

    def set_current_page(self, page: str):
        if self._current_page == page:
            return

        self._current_page = page
        self.page_changed.emit(page)

    # ---------- Current Device ----------

    @property
    def current_device(self):
        return self._current_device

    def set_current_device(self, device: str):
        if self._current_device == device:
            return

        self._current_device = device
        self.device_changed.emit(device)

    # ---------- Pairing Pin ----------

    @property
    def pairing_pin(self):
        return self._pairing_pin


    @property
    def pairing_active(self):
        return self._pairing_active


    @property
    def pairing_expires_in(self):
        return self._pairing_expires_in

    def set_pairing(
    self,
    pin: str,
    active: bool,
    expires_in: int,
    ):
        self._pairing_pin = pin
        self._pairing_active = active
        self._pairing_expires_in = expires_in

        self.pairing_changed.emit()