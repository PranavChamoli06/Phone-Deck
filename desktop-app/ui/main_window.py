from PySide6.QtGui import QGuiApplication
from PySide6.QtWidgets import (
    QHBoxLayout,
    QMainWindow,
    QVBoxLayout,
    QWidget,
)

from ui.content_panel import ContentPanel
from ui.header import Header
from ui.sidebar import Sidebar
from ui.status_bar import StatusBar

class MainWindow(QMainWindow):
    """
    Main application window.

    Responsible only for:
        • Creating the application shell
        • Arranging UI components
        • Wiring signals between widgets

    Business logic belongs elsewhere.
    """

    def __init__(self, state,services):
        super().__init__()

        # --------------------------------------------------
        # Application State
        # --------------------------------------------------
        self.state = state
        self.services = services

        # --------------------------------------------------
        # Window Configuration
        # --------------------------------------------------
        self.setWindowTitle("Phone Deck")
        self.resize(1200, 700)
        self._center_window()

        # --------------------------------------------------
        # Central Widget
        # --------------------------------------------------
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # --------------------------------------------------
        # Root Layout
        # --------------------------------------------------
        root_layout = QVBoxLayout(central_widget)

        # Outer margin around the application
        root_layout.setContentsMargins(18, 18, 18, 12)

        # Space between header and body
        root_layout.setSpacing(18)

        # --------------------------------------------------
        # Header
        # --------------------------------------------------
        self.header = Header()

        # --------------------------------------------------
        # Body Layout
        # --------------------------------------------------
        body = QWidget()
        body_layout = QHBoxLayout(body)

        body_layout.setContentsMargins(0, 0, 0, 0)
        body_layout.setSpacing(18)

        # --------------------------------------------------
        # Sidebar & Content
        # --------------------------------------------------
        self.sidebar = Sidebar()
        self.content = ContentPanel(self.state, self.services)

        body_layout.addWidget(self.sidebar)
        body_layout.addWidget(self.content, 1)

        # --------------------------------------------------
        # Assemble Layout
        # --------------------------------------------------
        root_layout.addWidget(self.header)
        root_layout.addWidget(body)

        # --------------------------------------------------
        # Status Bar
        # --------------------------------------------------
        self.status_bar = StatusBar()
        self.setStatusBar(self.status_bar)

        # --------------------------------------------------
        # Signal Connections
        # --------------------------------------------------
        self.sidebar.page_selected.connect(self.state.set_current_page)

        self.state.page_changed.connect(self.content.navigation.navigate)
        self.state.page_changed.connect(self.sidebar.set_active_page)

        self.state.connection_changed.connect(
            self.header.update_connection_status
        )

        self.state.connection_changed.connect(
            self.status_bar.update_connection_status
        )

    def _center_window(self):
        """
        Centers the application window on the primary screen.
        """
        screen = QGuiApplication.primaryScreen()

        if not screen:
            return

        geometry = screen.availableGeometry()

        frame = self.frameGeometry()
        frame.moveCenter(geometry.center())

        self.move(frame.topLeft())