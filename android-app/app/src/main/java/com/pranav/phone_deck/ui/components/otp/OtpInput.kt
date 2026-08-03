package com.pranav.phone_deck.ui.components.otp

import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Row
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.compose.ui.focus.FocusRequester
import androidx.compose.ui.focus.focusRequester
import com.pranav.phone_deck.ui.theme.PhoneDeckDimens

@Composable
fun OtpInput(
    modifier: Modifier = Modifier,
    otp: String,
    onOtpChanged: (String) -> Unit
) {

    val digits = remember(otp) {
        otp.padEnd(6).take(6).map { it.toString().trim() }.toMutableStateList()
    }

    val focusRequesters = remember {
        List(6) { FocusRequester() }
    }

    Row(
        modifier = modifier,
        horizontalArrangement = Arrangement.spacedBy(
            PhoneDeckDimens.SmallSpacing
        )
    ) {

        repeat(6) { index ->

            OtpBox(

                modifier = Modifier.focusRequester(
                    focusRequesters[index]
                ),

                value = digits[index],

                onValueChange = { value ->

                    digits[index] = value

                    val currentOtp =
                        digits.joinToString("")

                    onOtpChanged(currentOtp)

                    if (
                        value.isNotEmpty() &&
                        index < 5
                    ) {

                        focusRequesters[index + 1]
                            .requestFocus()

                    }

                }

            )

        }

    }

}