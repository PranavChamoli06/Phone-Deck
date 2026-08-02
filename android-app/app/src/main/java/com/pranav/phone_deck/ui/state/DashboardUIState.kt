package com.pranav.phone_deck.ui.state

data class DashboardUiState(

    val connected: Boolean = false,

    val pairedDesktopName: String? = null,

    val appVersion: String = "1.0.0"

)