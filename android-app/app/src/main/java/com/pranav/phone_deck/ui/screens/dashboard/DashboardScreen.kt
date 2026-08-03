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
import com.pranav.phone_deck.model.ConnectionState
import com.pranav.phone_deck.ui.components.buttons.PrimaryButton
import com.pranav.phone_deck.ui.components.cards.ConnectionStatusCard
import com.pranav.phone_deck.ui.theme.PhoneDeckDimens
import com.pranav.phone_deck.ui.theme.PhoneDeckStrings
import androidx.lifecycle.viewmodel.compose.viewModel
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import com.pranav.phone_deck.repository.ConnectionRepository
import com.pranav.phone_deck.ui.screens.dashboard.DashboardViewModel

@Composable
fun DashboardScreen() {

    val viewModel: DashboardViewModel = viewModel()

    val uiState by viewModel.uiState.collectAsState()

    Column(
        modifier = Modifier
            .fillMaxSize()
            .padding(PhoneDeckDimens.ScreenPadding),

        horizontalAlignment = Alignment.CenterHorizontally,
        verticalArrangement = Arrangement.Top
    ) {

        Spacer(
            modifier = Modifier.height(
                PhoneDeckDimens.LargeSpacing
            )
        )

        Text(
            text = PhoneDeckStrings.AppName,
            style = MaterialTheme.typography.displayLarge
        )

        Text(
            text = PhoneDeckStrings.Companion,
            style = MaterialTheme.typography.bodyMedium
        )

        Spacer(
            modifier = Modifier.height(
                PhoneDeckDimens.ExtraLargeSpacing
            )
        )

        ConnectionStatusCard(
            connected = uiState.connectionState == ConnectionState.CONNECTED,
            desktopName = uiState.desktopName
        )

        Spacer(
            modifier = Modifier.height(
                PhoneDeckDimens.LargeSpacing
            )
        )

        PrimaryButton(
            text = PhoneDeckStrings.PairDevice
        ) {

            ConnectionRepository.updateConnection(
                ConnectionState.WAITING,
                "Pranav-PC"
            )

        }

        Spacer(
            modifier = Modifier.height(
                PhoneDeckDimens.MediumSpacing
            )
        )

        PrimaryButton(
            text = PhoneDeckStrings.Settings
        ) {

            ConnectionRepository.updateConnection(
                ConnectionState.CONNECTED,
                "Pranav-PC"
            )

        }

        Spacer(modifier = Modifier.weight(1f))

        Text(
            text = PhoneDeckStrings.Version,
            style = MaterialTheme.typography.bodyMedium
        )
    }
}