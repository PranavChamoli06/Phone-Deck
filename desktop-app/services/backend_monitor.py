from PySide6.QtCore import QObject, QTimer


class BackendMonitor(QObject):
    """
    Periodically checks whether the backend is available.
    """

    def __init__(self, connection_service, interval=3000):
        super().__init__()

        self.connection_service = connection_service

        self.timer = QTimer(self)
        self.timer.setInterval(interval)
        self.timer.timeout.connect(
            self.connection_service.check_backend
        )

    def start(self):
        """Start monitoring."""
        self.connection_service.check_backend()
        self.timer.start()

    def stop(self):
        """Stop monitoring."""
        self.timer.stop()