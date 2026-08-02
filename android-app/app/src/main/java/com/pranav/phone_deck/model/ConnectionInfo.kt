package com.pranav.phone_deck.model

data class ConnectionInfo(

    val state: ConnectionState = ConnectionState.UNPAIRED,

    val desktopName: String? = null

)