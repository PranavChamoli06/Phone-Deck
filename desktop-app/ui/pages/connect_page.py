from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import (
    QLabel,
    QPushButton,
    QVBoxLayout,
)

from ui.pages.base_page import BasePage
from ui.widgets.glass_panel import GlassPanel
from ui.widgets.otp_display import OTPDisplay
from ui.widgets.page_header import PageHeader

from ui.theme.typography import (
    FONT_FAMILY,
    TITLE_SIZE,
    BODY_SIZE,
    SMALL_SIZE,
    TITLE_WEIGHT,
    HEADING_WEIGHT,
)


class ConnectPage(BasePage):
    """
    Page used to pair a mobile device with the desktop application.
    """

    def __init__(self, state, services):
        self.state = state
        self.services = services

        self.remaining_seconds = 0

        super().__init__()

        # --------------------------------------------------
        # Countdown Timer
        # --------------------------------------------------
        self.countdown_timer = QTimer(self)
        self.countdown_timer.setInterval(1000)
        self.countdown_timer.timeout.connect(self.update_countdown)

        # --------------------------------------------------
        # Listen for pairing state changes
        # --------------------------------------------------
        self.state.pairing_changed.connect(
            self.update_pairing_ui
        )

    # --------------------------------------------------
    # Build Page
    # --------------------------------------------------

    def build_page(self):
        self.content_layout.addWidget(
            PageHeader(
                "Connect",
                "Pair your mobile device securely."
            )
        )

        panel = GlassPanel()

        layout = QVBoxLayout(panel)
        layout.setContentsMargins(40, 40, 40, 40)
        layout.setSpacing(24)

        
        # --------------------------------------------------
        # Description
        # --------------------------------------------------

        description = QLabel(
            "Generate a one-time pairing code and enter it\n"
            "in the Phone Deck mobile app."
        )

        description.setWordWrap(True)
        description.setAlignment(Qt.AlignCenter)
        description.setMaximumWidth(520)

        description.setStyleSheet(
            f"""
            QLabel {{
                font-family: "{FONT_FAMILY}";
                font-size: {BODY_SIZE}px;
                font-weight: {HEADING_WEIGHT};
                color: rgba(255,255,255,0.80);
            }}
            """
        )

        layout.addWidget(
            description,
            alignment=Qt.AlignHCenter,
        )

        # --------------------------------------------------
        # OTP Display
        # --------------------------------------------------

        self.otp_display = OTPDisplay()

        layout.addWidget(
            self.otp_display,
            alignment=Qt.AlignHCenter,
        )

        # --------------------------------------------------
        # Status Label
        # --------------------------------------------------

        self.status_label = QLabel(
            "Ready to generate a pairing code."
        )

        self.status_label.setAlignment(Qt.AlignCenter)

        self.status_label.setStyleSheet(
            f"""
            QLabel {{
                font-family: "{FONT_FAMILY}";
                font-size: {SMALL_SIZE}pt;
                color: rgba(255,255,255,0.75);
            }}
            """
        )

        layout.addWidget(
            self.status_label,
            alignment=Qt.AlignHCenter,
        )

        # --------------------------------------------------
        # Generate Button
        # --------------------------------------------------

        self.generate_button = QPushButton(
            "Generate Pairing Code"
        )

        self.generate_button.setFixedSize(260, 48)

        self.generate_button.clicked.connect(
            self.services.pairing.start_pairing
        )

        layout.addWidget(
            self.generate_button,
            alignment=Qt.AlignHCenter,
        )

        self.content_layout.addWidget(panel)
        self.content_layout.addStretch()

    # --------------------------------------------------
    # Pairing State Updates
    # --------------------------------------------------

    def update_pairing_ui(self):
        """
        Refresh the page whenever the pairing state changes.
        """

        if self.state.pairing_active:

            self.otp_display.set_code(
                self.state.pairing_pin
            )

            self.remaining_seconds = (
                self.state.pairing_expires_in
            )

            minutes = self.remaining_seconds // 60
            seconds = self.remaining_seconds % 60

            self.status_label.setText(
                f"Code expires in {minutes:02}:{seconds:02}"
            )

            self.generate_button.setText(
                "Generate New Code"
            )

            if not self.countdown_timer.isActive():
                self.countdown_timer.start()

        else:

            self.countdown_timer.stop()

            self.otp_display.clear()

            self.status_label.setText(
                "Ready to generate a pairing code."
            )

            self.generate_button.setText(
                "Generate Pairing Code"
            )

    # --------------------------------------------------
    # Countdown Timer
    # --------------------------------------------------

    def update_countdown(self):
        """
        Update the countdown every second.
        """

        if self.remaining_seconds <= 0:

            self.countdown_timer.stop()

            self.state.set_pairing(
                pin="",
                active=False,
                expires_in=0,
            )

            return

        self.remaining_seconds -= 1

        minutes = self.remaining_seconds // 60
        seconds = self.remaining_seconds % 60

        self.status_label.setText(
            f"Code expires in {minutes:02}:{seconds:02}"
        )