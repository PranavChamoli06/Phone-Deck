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


class DecksPage(BasePage):
    def build_page(self):
        self.content_layout.addWidget(
            PageHeader(
                "Decks",
                "Create and manage your control decks."
            )
        )

        self.content_layout.addWidget(
            self.create_decks_panel()
        )

        self.content_layout.addStretch()

    # ---------------------------------------------------------
    # Decks Panel
    # ---------------------------------------------------------

    def create_decks_panel(self):
        panel = GlassPanel()

        layout = QVBoxLayout(panel)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(16)

        layout.addWidget(
            SectionHeader("My Decks")
        )

        message = QLabel(
            "No decks have been created yet."
        )

        message.setWordWrap(True)

        message.setStyleSheet(f"""
            QLabel {{
                font-family: "{FONT_FAMILY}";
                font-size: {BODY_SIZE}px;
                color: rgba(255,255,255,170);
            }}
        """)

        layout.addWidget(message)

        layout.addStretch()

        create_button = QPushButton(
            "🗂 Create New Deck"
        )

        create_button.setMinimumHeight(42)

        create_button.clicked.connect(
            lambda: self.navigate_requested.emit("actions")
        )

        layout.addWidget(create_button)

        return panel