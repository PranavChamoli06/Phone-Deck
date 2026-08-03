package com.pranav.phone_deck.ui.components.cards

import androidx.compose.foundation.BorderStroke
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.PaddingValues
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.unit.dp
import com.pranav.phone_deck.ui.theme.PhoneDeckDimens
import com.pranav.phone_deck.ui.theme.Surface
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.height

@Composable
fun GlassCard(
    modifier: Modifier = Modifier,
    title: String? = null,
    contentPadding: PaddingValues = PaddingValues(
        PhoneDeckDimens.CardPadding
    ),
    content: @Composable () -> Unit
) {

    Card(
        modifier = modifier.fillMaxWidth(),

        shape = MaterialTheme.shapes.large,

        colors = CardDefaults.cardColors(
            containerColor = Surface.copy(alpha = 0.88f)
        ),

        border = BorderStroke(
            width = 1.dp,
            color = Color.White.copy(alpha = 0.08f)
        ),

        elevation = CardDefaults.cardElevation(
            defaultElevation = 4.dp
        )
    ) {

        Column(
            modifier = Modifier.padding(contentPadding)
        ) {

            if (title != null) {

                Text(
                    text = title,
                    style = MaterialTheme.typography.titleMedium
                )

                Spacer(
                    modifier = Modifier.height(
                        PhoneDeckDimens.MediumSpacing
                    )
                )
            }

            content()

        }

    }

}