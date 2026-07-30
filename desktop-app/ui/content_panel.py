from PySide6.QtWidgets import QVBoxLayout

from ui.navigation import NavigationController
from ui.widgets.glass_panel import GlassPanel


class ContentPanel(GlassPanel):
    """
    Main content area of the application.

    Hosts the navigation controller which manages
    switching between application pages.
    """

    def __init__(self, state, services):
        super().__init__()

        self.state = state
        self.services = services

        layout = QVBoxLayout(self)
        layout.setContentsMargins(32, 32, 32, 32)

        self.navigation = NavigationController(
            self.state,
            self.services,
        )

        layout.addWidget(self.navigation)