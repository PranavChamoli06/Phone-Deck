package com.pranav.phone_deck.ui.components.indicators

import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import com.pranav.phone_deck.ui.theme.Error
import com.pranav.phone_deck.ui.theme.Success

@Composable
fun StatusIndicator(
    connected: Boolean,
    modifier: Modifier = Modifier
) {

    val indicatorColor =
        if (connected) Success else Error

    val statusText =
        if (connected) "Connected" else "Disconnected"

    Row(
        modifier = modifier,
        verticalAlignment = Alignment.CenterVertically,
        horizontalArrangement = Arrangement.spacedBy(8.dp)
    ) {

        androidx.compose.foundation.layout.Box(
            modifier = Modifier
                .size(12.dp)
                .background(
                    color = indicatorColor,
                    shape = CircleShape
                )
        )

        Text(
            text = statusText,
            style = MaterialTheme.typography.bodyLarge,
            color = MaterialTheme.colorScheme.onSurface
        )
    }
}