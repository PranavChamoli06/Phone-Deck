package com.pranav.phone_deck.ui.components.otp

import androidx.compose.foundation.BorderStroke
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.OutlinedTextField
import androidx.compose.material3.TextFieldDefaults
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.input.KeyboardOptions
import androidx.compose.ui.text.input.KeyboardType
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.sp
import androidx.compose.foundation.text.KeyboardActions
import androidx.compose.material3.Text
import androidx.compose.ui.text.font.FontWeight
import com.pranav.phone_deck.ui.theme.PhoneDeckDimens
import com.pranav.phone_deck.ui.theme.Primary
import com.pranav.phone_deck.ui.theme.Surface
import com.pranav.phone_deck.ui.theme.TextPrimary

@Composable
fun OtpBox(
    value: String,
    onValueChange: (String) -> Unit,
    modifier: Modifier = Modifier
) {

    OutlinedTextField(
        value = value,
        onValueChange = {

            if (it.length <= 1 && it.all(Char::isDigit)) {
                onValueChange(it)
            }

        },

        modifier = modifier.size(PhoneDeckDimens.OtpBoxSize),

        singleLine = true,

        textStyle = androidx.compose.ui.text.TextStyle(
            textAlign = TextAlign.Center,
            fontSize = 22.sp,
            fontWeight = FontWeight.Bold,
            color = TextPrimary
        ),

        shape = RoundedCornerShape(
            PhoneDeckDimens.CornerRadius
        ),

        keyboardOptions = KeyboardOptions(
            keyboardType = KeyboardType.Number
        ),

        keyboardActions = KeyboardActions(),

        colors = TextFieldDefaults.colors(
            focusedContainerColor = Surface.copy(alpha = 0.90f),
            unfocusedContainerColor = Surface.copy(alpha = 0.90f),

            focusedIndicatorColor = Primary,
            unfocusedIndicatorColor = Color.White.copy(alpha = 0.12f),

            cursorColor = Primary
        )
    )
}