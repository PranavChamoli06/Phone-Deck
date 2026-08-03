package com.pranav.phone_deck.ui.screens.pairing

import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.material3.TextButton
import androidx.compose.material3.Text
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.style.TextAlign

import com.pranav.phone_deck.ui.components.buttons.PrimaryButton
import com.pranav.phone_deck.ui.components.cards.GlassCard
import com.pranav.phone_deck.ui.components.layout.ScreenContainer
import com.pranav.phone_deck.ui.components.layout.ScreenHeader
import com.pranav.phone_deck.ui.components.otp.OtpInput
import com.pranav.phone_deck.ui.theme.PhoneDeckDimens

@Composable
fun PairingScreen() {

    var otp by remember {
        mutableStateOf("")
    }

    ScreenContainer {

        Column(
            horizontalAlignment = Alignment.CenterHorizontally
        ) {

            ScreenHeader(
                title = "Pair Your Device",
                subtitle = "Connect your Android phone securely using a one-time password."
            )

            GlassCard {

                OtpInput(
                    modifier = Modifier.fillMaxWidth(),
                    otp = otp,
                    onOtpChanged = {
                        otp = it
                    }
                )

                Spacer(
                    modifier = Modifier.height(
                        PhoneDeckDimens.LargeSpacing
                    )
                )

                Text(
                    text = "Enter the 6-digit OTP displayed on your desktop application.",
                    textAlign = TextAlign.Center,
                    modifier = Modifier.fillMaxWidth()
                )

                Spacer(
                    modifier = Modifier.height(
                        PhoneDeckDimens.ExtraLargeSpacing
                    )
                )

                PrimaryButton(
                    text = "Pair Device"
                ) {

                    // Backend integration will come next

                }

            }

            Spacer(
                modifier = Modifier.height(
                    PhoneDeckDimens.LargeSpacing
                )
            )

            TextButton(
                onClick = {
                    // Navigation comes next
                }
            ) {

                Text("← Back")

            }

        }

    }

}