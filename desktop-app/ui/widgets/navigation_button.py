from PySide6.QtCore import Signal
from PySide6.QtWidgets import QPushButton


class NavigationButton(QPushButton):
    clicked_page = Signal(str)

    def __init__(self, text: str, page: str):
        super().__init__(text)

        self.page = page

        self.setCheckable(True)
        self.setMinimumHeight(44)

        self.clicked.connect(self._emit_page)

    def _emit_page(self):
        self.clicked_page.emit(self.page)