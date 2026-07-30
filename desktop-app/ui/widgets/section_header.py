from PySide6.QtWidgets import QLabel

from ui.theme.typography import (
    FONT_FAMILY,
    HEADING_SIZE,
    HEADING_WEIGHT,
)


class SectionHeader(QLabel):
    """
    Reusable section title used inside pages.

    Examples:
        • Status Overview
        • Quick Actions
        • Paired Devices
        • My Decks
        • Available Actions
    """

    def __init__(self, text: str):
        super().__init__(text)

        self.setStyleSheet(
            f"""
            QLabel {{
                font-family: "{FONT_FAMILY}";
                font-size: {HEADING_SIZE}px;
                font-weight: {HEADING_WEIGHT};
                color: white;
                background: transparent;
            }}
            """
        )