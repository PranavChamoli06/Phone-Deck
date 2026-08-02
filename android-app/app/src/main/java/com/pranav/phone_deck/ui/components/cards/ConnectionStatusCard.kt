package com.pranav.phone_deck.ui.components.cards

import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import com.pranav.phone_deck.ui.components.indicators.StatusIndicator
import com.pranav.phone_deck.ui.theme.TextSecondary

@Composable
fun ConnectionStatusCard(
    connected: Boolean,
    desktopName: String? = null
) {

    PhoneDeckCard(
        title = if (connected) "Connected" else "Ready to Connect"
    ) {

        StatusIndicator(
            connected = connected
        )

        Text(
            text =
                if (connected)
                    "Connected to $desktopName"
                else
                    "Pair your desktop to begin.",
            style = MaterialTheme.typography.bodyMedium,
            color = TextSecondary,
            modifier = Modifier.fillMaxWidth()
        )
    }
}