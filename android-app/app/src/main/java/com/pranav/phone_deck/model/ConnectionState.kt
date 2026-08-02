package com.pranav.phone_deck.model

enum class ConnectionState {

    /**
     * Device has never been paired.
     */
    UNPAIRED,

    /**
     * Device is paired but the desktop is offline.
     */
    WAITING,

    /**
     * Active desktop connection.
     */
    CONNECTED

}