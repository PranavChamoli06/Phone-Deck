from PySide6.QtWidgets import (
    QLabel,
    QWidget,
    QGridLayout,
    QVBoxLayout,
    QPushButton,
    QHBoxLayout,
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


class DashboardPage(BasePage):
    def build_page(self):
        self.content_layout.addWidget(
            PageHeader(
                "Dashboard",
                "Overview of your Phone Deck desktop application."
            )
        )

        self.content_layout.addWidget(
            self.create_status_grid()
        )

        self.content_layout.addWidget(
            self.create_quick_actions_panel()
        )

        self.content_layout.addStretch()

    # ---------------------------------------------------------
    # Status Grid
    # ---------------------------------------------------------

    def create_status_grid(self):
        container = QWidget()

        grid = QGridLayout(container)
        grid.setContentsMargins(0, 0, 0, 0)
        grid.setHorizontalSpacing(20)
        grid.setVerticalSpacing(20)

        cards = [
            self.create_info_panel(
                "Backend Status",
                "Online",
                status=True,
            ),
            self.create_info_panel(
                "Connected Devices",
                "0",
            ),
            self.create_info_panel(
                "Active Deck",
                "None",
            ),
            self.create_info_panel(
                "Mobile Status",
                "Waiting...",
            ),
        ]

        grid.addWidget(cards[0], 0, 0)
        grid.addWidget(cards[1], 0, 1)
        grid.addWidget(cards[2], 1, 0)
        grid.addWidget(cards[3], 1, 1)

        grid.setColumnStretch(0, 1)
        grid.setColumnStretch(1, 1)

        return container

    # ---------------------------------------------------------
    # Generic Info Panel
    # ---------------------------------------------------------

    def create_info_panel(
        self,
        title: str,
        value: str,
        status: bool = False,
    ):
        panel = GlassPanel()

        panel.setMinimumHeight(110)
        panel.setMaximumHeight(110)

        layout = QVBoxLayout(panel)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(10)

        title_label = QLabel(title)
        title_label.setStyleSheet(f"""
            QLabel {{
                font-family: "{FONT_FAMILY}";
                font-size: {BODY_SIZE}px;
                color: rgba(255,255,255,170);
            }}
        """)

        layout.addWidget(title_label)

        if status:
            status_layout = QHBoxLayout()
            status_layout.setSpacing(8)

            dot = QLabel("●")
            dot.setStyleSheet("""
                QLabel {
                    color: #22C55E;
                    font-size: 18pt;
                }
            """)

            value_label = QLabel(value)
            value_label.setStyleSheet(f"""
                QLabel {{
                    font-family: "{FONT_FAMILY}";
                    font-size: {HEADING_SIZE}pt;
                    font-weight: {HEADING_WEIGHT};
                    color: white;
                }}
            """)

            status_layout.addWidget(dot)
            status_layout.addWidget(value_label)
            status_layout.addStretch()

            layout.addLayout(status_layout)

        else:
            value_label = QLabel(value)
            value_label.setStyleSheet(f"""
                QLabel {{
                    font-family: "{FONT_FAMILY}";
                    font-size: {HEADING_SIZE}pt;
                    font-weight: {HEADING_WEIGHT};
                    color: white;
                }}
            """)

            layout.addWidget(value_label)

        return panel

    # ---------------------------------------------------------
    # Quick Actions
    # ---------------------------------------------------------

    def create_quick_actions_panel(self):
        panel = GlassPanel()

        layout = QVBoxLayout(panel)
        layout.setContentsMargins(20, 16, 20, 16)
        layout.setSpacing(12)

        layout.addWidget(
            SectionHeader("Quick Actions")
        )

        buttons = QHBoxLayout()
        buttons.setSpacing(15)

        pair_btn = QPushButton("🔗 Pair Device")
        deck_btn = QPushButton("🗂 Create Deck")
        settings_btn = QPushButton("⚙ Settings")

        pair_btn.clicked.connect(
            lambda: self.navigate_requested.emit("connect")
        )

        deck_btn.clicked.connect(
            lambda: self.navigate_requested.emit("decks")
        )

        settings_btn.clicked.connect(
            lambda: self.navigate_requested.emit("settings")
        )

        for button in (
            pair_btn,
            deck_btn,
            settings_btn,
        ):
            button.setMinimumHeight(42)
            buttons.addWidget(button)

        layout.addLayout(buttons)

        layout.addStretch()

        return panel