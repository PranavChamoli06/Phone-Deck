from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtCore import Signal

class BasePage(QWidget):
    navigate_requested = Signal(str)
    def __init__(self):
        super().__init__()

        self.content_layout = QVBoxLayout(self)
        self.content_layout.setContentsMargins(30, 18, 30, 24)
        self.content_layout.setSpacing(20)

        self.build_page()

    def build_page(self):
        """Override in child classes."""
        pass