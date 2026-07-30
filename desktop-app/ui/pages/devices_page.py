from PySide6.QtWidgets import (
    QLabel,
    QPushButton,
    QVBoxLayout,
)

from ui.pages.base_page import BasePage
from ui.widgets.glass_panel import GlassPanel
from ui.widgets.page_header import PageHeader
from ui.widgets.section_header import SectionHeader

from ui.theme.typography import (
    FONT_FAMILY,
    BODY_SIZE,
    HEADING_SIZE,
    HEADING_WEIGHT,
)


class DevicesPage(BasePage):
    def build_page(self):
        self.content_layout.addWidget(
            PageHeader(
                "Devices",
                "Manage paired and connected devices."
            )
        )

        self.content_layout.addWidget(
            self.create_devices_panel()
        )

        self.content_layout.addStretch()

    # ---------------------------------------------------------
    # Devices Panel
    # ---------------------------------------------------------

    def create_devices_panel(self):
        panel = GlassPanel()

        layout = QVBoxLayout(panel)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(16)

        layout.addWidget(
            SectionHeader("Paired Devices")
        )

        message = QLabel("No paired devices found.")
        message.setStyleSheet(f"""
            QLabel {{
                font-family: "{FONT_FAMILY}";
                font-size: {BODY_SIZE}px;
                color: rgba(255,255,255,170);
            }}
        """)

        message.setWordWrap(True)
        layout.addWidget(message)

        layout.addStretch()

        pair_button = QPushButton("🔗 Pair New Device")
        pair_button.setMinimumHeight(42)
        pair_button.clicked.connect(
            lambda: self.navigate_requested.emit("connect")
        )

        layout.addWidget(pair_button)

        return panel