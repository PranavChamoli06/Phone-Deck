package com.pranav.phone_deck.ui.theme

import androidx.compose.foundation.isSystemInDarkTheme
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.darkColorScheme
import androidx.compose.material3.lightColorScheme
import androidx.compose.runtime.Composable

private val PhoneDeckDarkColorScheme = darkColorScheme(
    primary = Primary,
    onPrimary = TextPrimary,

    background = Background,
    onBackground = TextPrimary,

    surface = Surface,
    onSurface = TextPrimary,

    surfaceVariant = SurfaceLight,
    onSurfaceVariant = TextSecondary,

    error = Error,
    onError = TextPrimary
)

private val PhoneDeckLightColorScheme = lightColorScheme(
    primary = Primary,
    onPrimary = TextPrimary,

    background = Background,
    onBackground = TextPrimary,

    surface = Surface,
    onSurface = TextPrimary,

    surfaceVariant = SurfaceLight,
    onSurfaceVariant = TextSecondary,

    error = Error,
    onError = TextPrimary
)

@Composable
fun PhoneDeckTheme(
    darkTheme: Boolean = isSystemInDarkTheme(),
    content: @Composable () -> Unit
) {

    val colorScheme =
        if (darkTheme) PhoneDeckDarkColorScheme
        else PhoneDeckLightColorScheme

    MaterialTheme(
        colorScheme = colorScheme,
        typography = PhoneDeckTypography,
        shapes = PhoneDeckShapes,
        content = content
    )
}