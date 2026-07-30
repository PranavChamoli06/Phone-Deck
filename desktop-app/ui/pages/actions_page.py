from PySide6.QtWidgets import (
    QLabel,
    QVBoxLayout,
    QGridLayout,
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


class ActionsPage(BasePage):
    def build_page(self):
        self.content_layout.addWidget(
            PageHeader(
                "Actions",
                "Configure the actions available for your control decks."
            )
        )

        self.content_layout.addWidget(
            self.create_actions_panel()
        )

        self.content_layout.addStretch()

    # ---------------------------------------------------------
    # Actions Panel
    # ---------------------------------------------------------

    def create_actions_panel(self):
        panel = GlassPanel()

        layout = QVBoxLayout(panel)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(20)

        layout.addWidget(
            SectionHeader("Available Actions")
        )
        
        grid = QGridLayout()
        grid.setHorizontalSpacing(20)
        grid.setVerticalSpacing(20)

        categories = [
            ("⌨", "Keyboard"),
            ("🖱", "Mouse"),
            ("🎵", "Media"),
            ("⚡", "System"),
            ("🚀", "Applications"),
            ("📜", "Macros"),
        ]

        row = 0
        column = 0

        for icon, name in categories:
            card = self.create_action_card(icon, name)

            grid.addWidget(card, row, column)

            column += 1

            if column > 2:
                column = 0
                row += 1

        layout.addLayout(grid)

        message = QLabel(
            "Select an action category to continue."
        )

        message.setStyleSheet(f"""
            QLabel {{
                font-family: "{FONT_FAMILY}";
                font-size: {BODY_SIZE}px;
                color: rgba(255,255,255,170);
            }}
        """)

        layout.addWidget(message)

        return panel

    # ---------------------------------------------------------
    # Action Card
    # ---------------------------------------------------------

    def create_action_card(self, icon: str, title: str):
        card = GlassPanel()

        card.setMinimumHeight(120)

        layout = QVBoxLayout(card)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(10)

        icon_label = QLabel(icon)
        icon_label.setStyleSheet("""
            QLabel {
                font-size: 26pt;
            }
        """)

        name_label = QLabel(title)
        name_label.setStyleSheet(f"""
            QLabel {{
                font-family: "{FONT_FAMILY}";
                font-size: {BODY_SIZE}px;
                font-weight: {HEADING_WEIGHT};
                color: white;
            }}
        """)

        layout.addWidget(icon_label)
        layout.addWidget(name_label)
        layout.addStretch()

        return card