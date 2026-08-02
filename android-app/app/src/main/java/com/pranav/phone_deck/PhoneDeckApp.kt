package com.pranav.phone_deck

import androidx.compose.material3.Surface
import androidx.compose.runtime.Composable
import com.pranav.phone_deck.ui.navigation.AppNavHost
import com.pranav.phone_deck.ui.theme.PhoneDeckTheme

@Composable
fun PhoneDeckApp() {

    PhoneDeckTheme {

        Surface {

            AppNavHost()

        }

    }

}