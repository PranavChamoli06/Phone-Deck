package com.pranav.phone_deck.ui.navigation

sealed class AppDestination(val route: String) {

    data object Dashboard : AppDestination("dashboard")

    data object Pairing : AppDestination("pairing")

    data object Settings : AppDestination("settings")

    data object DeviceInfo : AppDestination("device_info")

    data object About : AppDestination("about")
}