from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QPushButton,
    QSizePolicy,
)

from ui.widgets.glass_panel import GlassPanel


class Header(GlassPanel):
    """
    Application header shown at the top of the window.
    """

    def __init__(self):
        super().__init__()

        # Slightly taller header for better visual balance
        self.setFixedHeight(64)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(20, 10, 20, 10)
        layout.setSpacing(12)

        # --------------------------------------------------
        # Title
        # --------------------------------------------------

        self.title = QLabel("Phone Deck")
        self.title.setAlignment(Qt.AlignVCenter)

        # --------------------------------------------------
        # Connection Status
        # --------------------------------------------------

        self.status = QLabel("🔴 Disconnected")
        self.status.setAlignment(Qt.AlignVCenter)

        # --------------------------------------------------
        # Settings Button
        # --------------------------------------------------

        self.settings_button = QPushButton("⚙")

        # Don't let the global QPushButton stylesheet make it huge
        self.settings_button.setFixedSize(36, 36)
        self.settings_button.setSizePolicy(
            QSizePolicy.Fixed,
            QSizePolicy.Fixed,
        )

        self.settings_button.setStyleSheet("""
            QPushButton {
                border-radius: 10px;
                padding: 0px;
                font-size: 16px;
            }
        """)

        # --------------------------------------------------
        # Layout
        # --------------------------------------------------

        layout.addWidget(self.title)

        layout.addStretch()

        layout.addWidget(self.status)

        layout.addSpacing(8)

        layout.addWidget(
            self.settings_button,
            alignment=Qt.AlignVCenter,
        )

    def update_connection_status(self, connected: bool):
        if connected:
            self.status.setText("🟢 Connected")
        else:
            self.status.setText("🔴 Disconnected")