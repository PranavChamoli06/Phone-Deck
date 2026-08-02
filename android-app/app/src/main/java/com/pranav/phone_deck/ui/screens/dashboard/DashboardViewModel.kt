package com.pranav.phone_deck.ui.screens.dashboard

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.pranav.phone_deck.repository.ConnectionRepository
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.launch

class DashboardViewModel : ViewModel() {

    private val _uiState =
        MutableStateFlow(DashboardUiState())

    val uiState: StateFlow<DashboardUiState> =
        _uiState.asStateFlow()

    init {

        viewModelScope.launch {

            ConnectionRepository.connectionInfo.collect {

                _uiState.value = DashboardUiState(
                    connectionState = it.state,
                    desktopName = it.desktopName
                )

            }

        }

    }

}