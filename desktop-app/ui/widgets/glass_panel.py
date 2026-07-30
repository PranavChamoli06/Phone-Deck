from PySide6.QtGui import QColor
from PySide6.QtWidgets import (
    QFrame,
    QGraphicsDropShadowEffect,
    QSizePolicy,
)


class GlassPanel(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setObjectName("glassPanel")

        self.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Maximum,
        )

        shadow = QGraphicsDropShadowEffect(self)

        shadow.setBlurRadius(18)
        shadow.setOffset(0, 3)
        shadow.setColor(QColor(0, 0, 0, 45))

        self.setGraphicsEffect(shadow)