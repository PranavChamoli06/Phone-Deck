from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
)

from ui.widgets.glass_panel import GlassPanel


class OTPDisplay(GlassPanel):
    """
    Displays the current pairing code using
    six individual digit boxes.
    """

    BOX_COUNT = 6
    PLACEHOLDER = "•"

    def __init__(self):
        super().__init__()

        self.setFixedHeight(120)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(12)
        layout.setAlignment(Qt.AlignCenter)

        self.digit_labels = []

        # ------------------------------------------
        # Create six OTP boxes
        # ------------------------------------------
        for _ in range(self.BOX_COUNT):
            label = QLabel(self.PLACEHOLDER)

            label.setAlignment(Qt.AlignCenter)
            label.setFixedSize(70, 82)

            font = label.font()
            font.setPointSize(200)
            font.setBold(True)
            label.setFont(font)

            label.setFrameShape(QFrame.Box)

            label.setStyleSheet("""
                QLabel {
                    background-color: rgba(255,255,255,0.06);
                    border: 1px solid rgba(255,255,255,0.18);
                    border-radius: 12px;
                    color: white;
                }
            """)

            layout.addWidget(label)
            self.digit_labels.append(label)

    # ------------------------------------------
    # Public API
    # ------------------------------------------

    def set_code(self, code: str):
        """
        Display the supplied pairing code.
        """

        code = str(code).strip()

        for i, label in enumerate(self.digit_labels):
            if i < len(code):
                label.setText(code[i])
            else:
                label.setText(self.PLACEHOLDER)

    def clear(self):
        """
        Clear the displayed pairing code.
        """

        for label in self.digit_labels:
            label.setText(self.PLACEHOLDER)