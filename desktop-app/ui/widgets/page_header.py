from PySide6.QtWidgets import (
    QLabel,
    QVBoxLayout,
    QWidget,
)

from ui.theme.typography import (
    FONT_FAMILY,
    TITLE_SIZE,
    BODY_SIZE,
    TITLE_WEIGHT,
)


class PageHeader(QWidget):
    """
    Standard page header used throughout the application.

    Example:
        Dashboard
        Overview of your Phone Deck desktop application.
    """

    def __init__(
        self,
        title: str,
        subtitle: str = "",
        parent=None,
    ):
        super().__init__(parent)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(6)

        title_label = QLabel(title)

        title_label.setStyleSheet(f"""
            QLabel {{
                font-family: "{FONT_FAMILY}";
                font-size: {TITLE_SIZE}px;
                font-weight: {TITLE_WEIGHT};
                color: white;
            }}
        """)

        layout.addWidget(title_label)

        if subtitle:
            subtitle_label = QLabel(subtitle)

            subtitle_label.setStyleSheet(f"""
                QLabel {{
                    font-family: "{FONT_FAMILY}";
                    font-size: {BODY_SIZE}px;
                    color: rgba(255,255,255,170);
                }}
            """)

            subtitle_label.setWordWrap(True)

            layout.addWidget(subtitle_label)