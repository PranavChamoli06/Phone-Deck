import sys

from PySide6.QtWidgets import QApplication

from PySide6.QtCore import Qt
from PySide6.QtGui import QGuiApplication

from ui.main_window import MainWindow

from ui.theme.stylesheet import APP_STYLESHEET

from state.app_state import AppState

from services.service_container import ServiceContainer

def main():

    QGuiApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough
    )
    app = QApplication(sys.argv)

    app.setStyleSheet(APP_STYLESHEET)

    state = AppState()
    services = ServiceContainer(state)

    window = MainWindow(state, services)
    window.show()

    services.backend_monitor.start()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main()