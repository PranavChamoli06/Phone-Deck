package com.pranav.phone_deck.ui.components.layout

import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.style.TextAlign
import com.pranav.phone_deck.ui.theme.PhoneDeckDimens
import com.pranav.phone_deck.ui.theme.TextSecondary

@Composable
fun ScreenHeader(
    title: String,
    subtitle: String,
    modifier: Modifier = Modifier
) {

    Column(
        modifier = modifier
            .fillMaxWidth()
            .padding(bottom = PhoneDeckDimens.ExtraLargeSpacing)
    ) {

        Text(
            text = title,
            modifier = Modifier.fillMaxWidth(),
            textAlign = TextAlign.Center,
            style = MaterialTheme.typography.displaySmall
        )

        Text(
            text = subtitle,
            modifier = Modifier
                .fillMaxWidth()
                .padding(top = PhoneDeckDimens.SmallSpacing),
            textAlign = TextAlign.Center,
            style = MaterialTheme.typography.bodyLarge,
            color = TextSecondary
        )

    }
}