package com.pranav.phone_deck.ui.screens.dashboard

import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import com.pranav.phone_deck.ui.components.buttons.PrimaryButton
import com.pranav.phone_deck.ui.components.cards.ConnectionStatusCard

@Composable
fun DashboardScreen() {

    Column(
        modifier = Modifier
            .fillMaxSize()
            .padding(24.dp),

        horizontalAlignment = Alignment.CenterHorizontally,

        verticalArrangement = Arrangement.Top
    ) {

        Spacer(modifier = Modifier.height(24.dp))

        Text(
            text = "Phone Deck",
            style = MaterialTheme.typography.displayLarge
        )

        Text(
            text = "Android Companion",
            style = MaterialTheme.typography.bodyMedium
        )

        Spacer(modifier = Modifier.height(32.dp))

        ConnectionStatusCard(
            connected = false
        )

        Spacer(modifier = Modifier.height(24.dp))

        PrimaryButton(
            text = "Pair Device"
        ) {

        }

        Spacer(modifier = Modifier.height(16.dp))

        PrimaryButton(
            text = "Settings"
        ) {

        }

        Spacer(modifier = Modifier.weight(1f))

        Text(
            text = "Version 1.0.0",
            style = MaterialTheme.typography.bodyMedium
        )
    }
}