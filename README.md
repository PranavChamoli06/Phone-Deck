<div align="center">

# 📱 Phone Deck

### Turn Your Smartphone into a Powerful Desktop Control Deck

*A modern, open-source alternative to the Elgato Stream Deck that transforms your Android phone into a customizable control surface for your Windows PC.*

![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PySide6](https://img.shields.io/badge/PySide6-Desktop-41CD52?style=for-the-badge&logo=qt&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)
![Status](https://img.shields.io/badge/Status-Phase%202%20Complete-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

</div>

---

# 📖 Overview

Phone Deck is an open-source ecosystem that lets you securely connect your Android phone to your Windows PC and use it as a customizable desktop control deck.

Inspired by the **Elgato Stream Deck**, Phone Deck aims to provide a powerful automation platform without requiring dedicated hardware.

The project consists of three major components:

- 🖥 **Desktop Application (PySide6)** – Modern desktop interface for managing devices, decks and actions.
- ⚡ **FastAPI Backend** – Pairing, communication and device management server.
- 📱 **Android Application** *(In Development)* – Mobile control surface used to trigger desktop actions.

The application follows a **modular and event-driven architecture**, making it easy to extend with new actions, plugins and integrations.

> **Current Status**
>
> ✅ **Phase 1 — Backend Foundation** completed.
>
> ✅ **Phase 2 — Desktop UI Foundation** completed.
>
> 🚧 Currently working on **Phase 3 — Communication Layer**.

---

# ✨ Features

## ✅ Implemented

### Backend

- 🔐 OTP-based secure device pairing
- 🌐 REST API built with FastAPI
- 🔄 WebSocket communication
- ❤️ Backend health monitoring
- ⚡ Asynchronous architecture

### Desktop Application

- 🖥 Modern PySide6 desktop application
- 📊 Dashboard
- 🔗 Device pairing page
- 📱 Device management
- 🎮 Deck management
- ⚡ Actions page
- ⚙ Settings page
- 🧭 Sidebar navigation
- 📡 Backend connection monitoring
- 🎨 Reusable UI component library
- 🌙 Modern dark theme

---

## 🚧 Currently In Development

- Android application
- Desktop ↔ Android communication layer
- Persistent paired devices
- Device heartbeat
- Deck editor
- Action execution engine

---

## 📅 Planned

- Multi-page decks
- Custom icons & themes
- OBS Studio integration
- Spotify integration
- Discord integration
- Plugin marketplace
- Cloud synchronization
- AI-powered smart actions
- Cross-platform support

---

# 🏗 Architecture

```text
                  Android Application
                   (Under Development)
                           │
                   REST / WebSockets
                           │
        ┌──────────────────┴──────────────────┐
        │                                     │
        ▼                                     ▼
 Desktop Application                  FastAPI Backend
      (PySide6)                    Pairing & API Server
        │
        ▼
 Windows Automation Engine
        │
        ▼
 Windows Operating System
```

---

# 🛠 Tech Stack

| Category | Technologies |
|-----------|--------------|
| Desktop | Python, PySide6 (Qt) |
| Backend | Python, FastAPI |
| Communication | REST API, WebSockets |
| UI | Qt Widgets |
| Architecture | Modular, Event-driven |
| Platform | Windows |

---

# 📂 Repository Structure

```text
Phone-Deck/
│
├── desktop-app/
│   ├── ui/
│   ├── services/
│   ├── state/
│   ├── assets/
│   └── app.py
│
├── laptop-host/
│   ├── app/
│   ├── plugins/
│   ├── requirements/
│   └── requirements.txt
│
├── shared/
│
├── docs/
│
├── LICENSE
└── README.md
```

---

# 🚀 Getting Started

## 1. Clone the repository

```bash
git clone https://github.com/PranavChamoli06/Phone-Deck.git

cd Phone-Deck
```

---

## 2. Run the Backend

```bash
cd laptop-host

python -m venv .venv

.venv\Scripts\activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```

Backend URLs:

- Swagger → `http://127.0.0.1:8000/docs`
- ReDoc → `http://127.0.0.1:8000/redoc`

---

## 3. Run the Desktop Application

```bash
cd desktop-app

python -m venv .venv

.venv\Scripts\activate

pip install -r requirements.txt

python app.py
```

---

# 📸 Screenshots

## Dashboard

![Dashboard](assets/screenshots/dashboard.png)

---

## Device Pairing

![Connect](assets/screenshots/connect.png)

---

## Device Management

![Devices](assets/screenshots/devices.png)

---

## Deck Management

![Decks](assets/screenshots/decks.png)

---

## Action Library

![Actions](assets/screenshots/actions.png)

---

## Settings

![Settings](assets/screenshots/settings.png)

---

# 🗺 Development Roadmap

| Phase | Status |
|--------|--------|
| ✅ Phase 1 | Backend Foundation |
| ✅ Phase 2 | Desktop UI Foundation |
| 🚧 Phase 3 | Communication Layer |
| 📅 Phase 4 | Android Application |
| 📅 Phase 5 | Deck Editor |
| 📅 Phase 6 | Windows Automation Engine |
| 📅 Phase 7 | Plugin System |
| 📅 Phase 8 | Cloud Sync & AI Features |

---

# 🎯 Upcoming Milestone

The next milestone focuses on implementing real communication between the desktop application and Android device.

This includes:

- Device registration
- Persistent paired devices
- Heartbeat mechanism
- WebSocket messaging protocol
- Action dispatcher
- First executable desktop actions

---

# 🤝 Contributing

Contributions, feature requests and bug reports are always welcome.

If you'd like to contribute:

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Open a Pull Request.

---

# 📄 License

This project is licensed under the **MIT License**.

---

<div align="center">

## 👨‍💻 Author

**Pranav Chamoli**

If you found this project interesting, consider giving it a ⭐ on GitHub.

</div>