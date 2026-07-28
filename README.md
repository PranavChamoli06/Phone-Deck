<div align="center">

# 📱 Phone Deck

### Turn Your Smartphone into a Powerful Desktop Control Deck

*A modern, open-source alternative to the Elgato Stream Deck that transforms your Android phone into a customizable control surface for your Windows PC.*

![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)
![Status](https://img.shields.io/badge/Status-Phase%201%20Complete-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

</div>

---

## 📖 Overview

Phone Deck is an open-source ecosystem that lets you securely connect your Android phone to your Windows PC and use it as a customizable control deck. Inspired by the Elgato Stream Deck, it aims to provide powerful desktop automation without requiring dedicated hardware.

The project is built around a **plugin-first architecture**, making it easy to extend with new actions, integrations, and workflows.

> **Current Status:** ✅ Phase 1 (FastAPI Backend) is complete. Android client and desktop host are planned for future phases.

---

## ✨ Features

### ✅ Implemented (Phase 1)

- 🔐 OTP-based secure device pairing
- 🎛 Button & profile management
- ⚡ Async runtime engine
- 🔄 Real-time WebSocket synchronization
- 🔌 Plugin framework
- 🎵 Media controls
- 🔊 Volume controls
- 🪟 Window management
- 📁 File Explorer shortcuts
- 💡 Display & screenshot controls
- 📋 Clipboard actions
- ⚡ Power controls (shutdown, restart, sleep, lock)

### 🚧 Planned

- Android application
- Windows desktop host
- Multi-page decks
- Custom icons & themes
- Plugin marketplace
- OBS Studio integration
- Spotify integration
- Discord integration
- AI-powered smart actions
- Cloud profile synchronization
- Cross-platform support

---

## 🏗 Architecture

```text
                 Android App (Future)
                         │
              HTTP / WebSockets
                         │
                         ▼
               FastAPI Backend
                         │
          Runtime Engine & Plugin Manager
                         │
                         ▼
               Windows System Plugins
                         │
                         ▼
                 Windows Operating System
```

---

## 🛠 Tech Stack

| Category | Technologies |
|----------|--------------|
| Backend | Python, FastAPI, AsyncIO |
| Communication | REST API, WebSockets |
| Windows Integration | pywin32, keyboard, ctypes, subprocess |
| Architecture | Plugin-based, Async-first, Event-driven |

---

## 📂 Repository Structure

```text
Phone-Deck/
│
├── laptop-host/      # ✅ FastAPI Backend
├── android/          # 🚧 Android Client (Planned)
├── desktop/          # 🚧 Windows Desktop Host (Planned)
├── docs/             # Documentation
├── assets/           # Images & screenshots
├── LICENSE
└── README.md
```

---

## 🚀 Getting Started

### Clone the repository

```bash
git clone https://github.com/PranavChamoli06/Phone-Deck.git

cd Phone-Deck/laptop-host
```

### Create a virtual environment

```bash
python -m venv .venv
```

### Activate it

```bash
.venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Configure environment

```bash
cp .env.example .env
```

### Run the backend

```bash
uvicorn app.main:app --reload
```

Visit:

- Swagger UI → `http://127.0.0.1:8000/docs`
- ReDoc → `http://127.0.0.1:8000/redoc`

---

## 🗺 Roadmap

- ✅ Phase 1 — FastAPI Backend
- 🚧 Phase 2 — Android Client
- 🚧 Phase 3 — Windows Desktop Host
- 🚧 Phase 4 — Plugin Marketplace
- 🚧 Phase 5 — Cloud Sync & AI Features

---

## 🤝 Contributing

Contributions, ideas, bug reports, and feature requests are always welcome.

If you'd like to contribute, feel free to fork the repository, create a feature branch, and open a pull request.

---

## 📄 License

This project is licensed under the **MIT License**.

---

<div align="center">

### 👨‍💻 Author

**Pranav Chamoli**

⭐ If you find this project interesting, consider giving it a star!

</div>