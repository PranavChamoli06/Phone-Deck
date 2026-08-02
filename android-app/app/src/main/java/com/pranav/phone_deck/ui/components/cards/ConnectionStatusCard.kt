package com.pranav.phone_deck.ui.components.cards

import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import com.pranav.phone_deck.ui.components.indicators.StatusIndicator
import com.pranav.phone_deck.ui.theme.PhoneDeckStrings
import com.pranav.phone_deck.ui.theme.TextSecondary

@Composable
fun ConnectionStatusCard(
    connected: Boolean,
    desktopName: String? = null
) {

    PhoneDeckCard(
        title = if (connected)
            "Connected"
        else
            PhoneDeckStrings.ReadyToConnect
    ) {

        StatusIndicator(
            connected = connected
        )

        Text(
            modifier = Modifier.fillMaxWidth(),

            text =
                if (connected)
                    "Connected to $desktopName"
                else
                    PhoneDeckStrings.PairDesktop,

            style = MaterialTheme.typography.bodyMedium,

            color = TextSecondary
        )
    }
}