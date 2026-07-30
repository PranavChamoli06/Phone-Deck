from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QLabel, QVBoxLayout

from ui.widgets.glass_panel import GlassPanel
from ui.widgets.navigation_button import NavigationButton


class Sidebar(GlassPanel):
    page_selected = Signal(str)

    def __init__(self):
        super().__init__()

        self.buttons = {}

        layout = QVBoxLayout(self)
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(8)

        title = QLabel("Phone Deck")
        title.setAlignment(Qt.AlignCenter)

        layout.addWidget(title)
        layout.addSpacing(12)

        pages = [
            ("🏠 Dashboard", "dashboard"),
            ("🔗 Connect", "connect"),
            ("📱 Devices", "devices"),
            ("🎮 Decks", "decks"),
            ("⚡ Actions", "actions"),
            ("⚙ Settings", "settings"),
        ]

        for text, page in pages:
            button = NavigationButton(text, page)

            button.clicked_page.connect(self.page_selected)

            layout.addWidget(button)

            self.buttons[page] = button

        layout.addStretch()

        self.set_active_page("dashboard")

    def set_active_page(self, page_name: str):
        for page, button in self.buttons.items():
            button.setChecked(page == page_name)