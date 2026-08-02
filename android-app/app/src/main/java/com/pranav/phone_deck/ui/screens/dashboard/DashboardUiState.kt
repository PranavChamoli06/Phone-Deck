package com.pranav.phone_deck.ui.screens.dashboard

import com.pranav.phone_deck.model.ConnectionState

data class DashboardUiState(

    val connectionState: ConnectionState = ConnectionState.UNPAIRED,

    val desktopName: String? = null,

    val isLoading: Boolean = false

)