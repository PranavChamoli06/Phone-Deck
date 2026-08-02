package com.pranav.phone_deck.ui.components.buttons

import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.material3.Button
import androidx.compose.material3.ButtonDefaults
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import com.pranav.phone_deck.ui.theme.Primary
import com.pranav.phone_deck.ui.theme.TextPrimary

@Composable
fun PrimaryButton(
    text: String,
    modifier: Modifier = Modifier,
    onClick: () -> Unit
) {

    Button(
        onClick = onClick,
        modifier = modifier
            .fillMaxWidth()
            .height(54.dp),

        shape = MaterialTheme.shapes.medium,

        colors = ButtonDefaults.buttonColors(
            containerColor = Primary,
            contentColor = TextPrimary
        )
    ) {

        Text(
            text = text,
            style = MaterialTheme.typography.labelLarge
        )

    }
}