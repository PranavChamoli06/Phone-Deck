from PySide6.QtWidgets import QStatusBar


class StatusBar(QStatusBar):
    def __init__(self):
        super().__init__()

        self.showMessage("Ready")

    def update_connection_status(self, connected: bool):
        """
        Updates the backend connection status shown in the status bar.
        """
        if connected:
            self.showMessage("Backend: Connected")
        else:
            self.showMessage("Backend: Disconnected")