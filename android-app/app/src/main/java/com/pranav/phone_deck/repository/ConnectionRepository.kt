package com.pranav.phone_deck.repository

import com.pranav.phone_deck.model.ConnectionInfo
import com.pranav.phone_deck.model.ConnectionState
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow

object ConnectionRepository {

    private val _connectionInfo =
        MutableStateFlow(ConnectionInfo())

    val connectionInfo: StateFlow<ConnectionInfo> =
        _connectionInfo.asStateFlow()

    fun updateConnection(
        state: ConnectionState,
        desktopName: String? = null
    ) {

        _connectionInfo.value = ConnectionInfo(
            state = state,
            desktopName = desktopName
        )

    }

    fun disconnect() {

        _connectionInfo.value =
            _connectionInfo.value.copy(
                state = ConnectionState.WAITING
            )

    }

    fun clearPairing() {

        _connectionInfo.value =
            ConnectionInfo()

    }

}