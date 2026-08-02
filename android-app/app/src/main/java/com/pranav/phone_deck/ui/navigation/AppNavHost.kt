package com.pranav.phone_deck.ui.navigation

import androidx.compose.runtime.Composable
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.compose.rememberNavController
import com.pranav.phone_deck.ui.screens.dashboard.DashboardScreen

@Composable
fun AppNavHost() {

    val navController = rememberNavController()

    NavHost(
        navController = navController,
        startDestination = AppDestination.Dashboard.route
    ) {

        composable(AppDestination.Dashboard.route) {
            DashboardScreen()
        }

    }

}