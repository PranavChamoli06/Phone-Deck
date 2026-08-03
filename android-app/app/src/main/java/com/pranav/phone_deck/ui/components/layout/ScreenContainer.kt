package com.pranav.phone_deck.ui.components.layout

import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.PaddingValues
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.verticalScroll
import androidx.compose.material3.Scaffold
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.unit.dp
import com.pranav.phone_deck.ui.theme.Background
import com.pranav.phone_deck.ui.theme.PhoneDeckDimens

@Composable
fun ScreenContainer(
    modifier: Modifier = Modifier,
    contentPadding: PaddingValues = PaddingValues(
        PhoneDeckDimens.ScreenPadding
    ),
    content: @Composable () -> Unit
) {

    Scaffold(
        containerColor = Background
    ) { innerPadding ->

        Box(
            modifier = modifier
                .fillMaxSize()
                .background(
                    brush = Brush.verticalGradient(
                        colors = listOf(
                            Background,
                            Background.copy(alpha = 0.96f)
                        )
                    )
                )
                .padding(innerPadding)
                .padding(contentPadding)
                .verticalScroll(rememberScrollState())
        ) {
            content()
        }
    }
}