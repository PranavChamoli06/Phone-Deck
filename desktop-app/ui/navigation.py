from PySide6.QtWidgets import QStackedWidget

from ui.pages.actions_page import ActionsPage
from ui.pages.connect_page import ConnectPage
from ui.pages.dashboard_page import DashboardPage
from ui.pages.decks_page import DecksPage
from ui.pages.devices_page import DevicesPage
from ui.pages.settings_page import SettingsPage


class NavigationController(QStackedWidget):
    """
    Controls navigation between all application pages.
    """

    def __init__(self, state, services):
        super().__init__()

        self.state = state
        self.services = services

        self.pages = {
            "dashboard": DashboardPage(),
            "connect": ConnectPage(
                self.state,
                self.services,
            ),
            "devices": DevicesPage(),
            "decks": DecksPage(),
            "actions": ActionsPage(),
            "settings": SettingsPage(),
        }

        # --------------------------------------------------
        # Wire Page Navigation Requests
        # --------------------------------------------------
        
        for page in (
            self.pages["dashboard"],
            self.pages["connect"],
            self.pages["devices"],
        ):
            page.navigate_requested.connect(
                self.state.set_current_page
            )

        for page in self.pages.values():
            self.addWidget(page)

        self.navigate("dashboard")

    def navigate(self, page_name: str):
        """Navigate to the requested page."""

        page = self.pages.get(page_name)

        if page is None:
            return

        self.setCurrentWidget(page)