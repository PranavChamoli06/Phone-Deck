from PySide6.QtWidgets import (
    QLabel,
    QSizePolicy,
    QVBoxLayout,
)

from ui.pages.base_page import BasePage
from ui.widgets.glass_panel import GlassPanel
from ui.widgets.page_header import PageHeader
from ui.widgets.section_header import SectionHeader

from ui.theme.typography import (
    FONT_FAMILY,
    BODY_SIZE,
)


class SettingsPage(BasePage):
    def build_page(self):
        from PySide6.QtWidgets import QHBoxLayout

        self.content_layout.addWidget(
            PageHeader(
                "Settings",
                "Configure Phone Deck preferences.",
            )
        )

        # --------------------------------------------------
        # Top Row
        # --------------------------------------------------

        top_row = QHBoxLayout()
        top_row.setSpacing(20)

        top_row.addWidget(self.create_general_panel())
        top_row.addWidget(self.create_connection_panel())

        self.content_layout.addLayout(top_row)

        # --------------------------------------------------
        # Bottom Row
        # --------------------------------------------------

        self.content_layout.addWidget(
            self.create_about_panel()
        )

        self.content_layout.addStretch()

    # ---------------------------------------------------------
    # General
    # ---------------------------------------------------------

    def create_general_panel(self):
        panel = GlassPanel()
        panel.setMinimumHeight(180)
        panel.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Preferred,
        )

        layout = QVBoxLayout(panel)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(16)

        layout.addWidget(SectionHeader("General"))

        items_layout = QVBoxLayout()
        items_layout.setSpacing(8)

        for item in (
            "• Theme",
            "• Startup Behavior",
            "• Notifications",
        ):
            items_layout.addWidget(self.create_item(item))

        layout.addLayout(items_layout)

        return panel

    # ---------------------------------------------------------
    # Connection
    # ---------------------------------------------------------

    def create_connection_panel(self):
        panel = GlassPanel()
        panel.setMinimumHeight(180)
        panel.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Preferred,
        )

        layout = QVBoxLayout(panel)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(16)

        layout.addWidget(SectionHeader("Connection"))

        items_layout = QVBoxLayout()
        items_layout.setSpacing(8)

        for item in (
            "• Backend Status",
            "• Auto Reconnect",
            "• Pairing Preferences",
        ):
            items_layout.addWidget(self.create_item(item))

        layout.addLayout(items_layout)

        return panel

    # ---------------------------------------------------------
    # About
    # ---------------------------------------------------------

    def create_about_panel(self):
        panel = GlassPanel()
        panel.setMinimumHeight(120)
        panel.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Preferred,
        )

        layout = QVBoxLayout(panel)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(16)

        layout.addWidget(SectionHeader("About"))

        items_layout = QVBoxLayout()
        items_layout.setSpacing(8)

        items_layout.addWidget(self.create_item("Phone Deck"))
        items_layout.addWidget(self.create_item("Version 0.1.0"))

        layout.addLayout(items_layout)

        return panel

    # ---------------------------------------------------------
    # Helpers
    # ---------------------------------------------------------

    def create_item(self, text: str):
        label = QLabel(text)

        label.setContentsMargins(0, 0, 0, 0)

        label.setSizePolicy(
            QSizePolicy.Preferred,
            QSizePolicy.Fixed,
        )

        label.setStyleSheet(
            f"""
            QLabel {{
                font-family: "{FONT_FAMILY}";
                font-size: {BODY_SIZE}px;
                color: rgba(255,255,255,180);
                background: transparent;
            }}
            """
        )

        return label