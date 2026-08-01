# Phone Deck Architecture

## Overview

Phone Deck is a cross-platform remote control system inspired by the Elgato Stream Deck.

The desktop/laptop acts as the **Host**, while the Android phone acts as the **Controller**.

Communication is performed over WebSockets using a custom JSON protocol.

---

# High-Level Architecture

```
+---------------------+
|    Android App      |
|  (Controller)       |
+----------+----------+
           |
           | WebSocket
           |
+----------v----------+
|     FastAPI Host    |
|   Communication     |
+----------+----------+
           |
           |
+----------v----------+
|   Message Handler   |
+----------+----------+
           |
      +----+----+
      |         |
      |         |
+-----v--+  +---v---------+
| Auth   |  | Action      |
|Handler |  | Handler     |
+-----+--+  +------+------+
      |            |
      |            |
      |      +-----v------+
      |      | Action     |
      |      | Registry   |
      |      +-----+------+
      |            |
      |            |
      |      +-----v------+
      |      | Plugins    |
      |      +-----+------+
      |            |
      |            |
      +------------v
        Operating System
```

---

# Communication Flow

Android

↓

WebSocket

↓

Protocol Validation

↓

Message Handler

↓

Specific Handler

↓

Action Registry

↓

Plugin

↓

Operating System

---

# Authentication Flow

Phone requests pairing.

↓

Laptop generates OTP.

↓

Phone sends OTP_VERIFY.

↓

Pairing module validates OTP.

↓

Client session becomes authenticated.

↓

Authenticated client can execute actions.

---

# Action Execution Flow

Phone sends:

ACTION_EXECUTE

↓

ActionHandler

↓

ActionRegistry.execute()

↓

Plugin

↓

Operating System

---

# Runtime System

RuntimeStateManager stores the current runtime state.

Current implementation:

- Buttons
- Runtime Events

Future implementation:

- Runtime Snapshot
- Profiles
- Pages
- Live Synchronization

---

# Plugin Architecture

Every capability is implemented as a plugin.

Examples:

- Media
- Keyboard
- Mouse
- System
- Applications

The communication layer never executes OS operations directly.

Instead:

WebSocket

↓

Action Registry

↓

Plugin

↓

Operating System

---

# Future Components

Mobile App

- Jetpack Compose
- Material 3
- MVVM
- WebSocket Client

Desktop App

- PySide6
- Profile Editor
- Plugin Manager
- Settings

---

# Current Status

✅ Communication Layer

✅ Authentication

✅ Action Execution

✅ Plugin Architecture

🚧 Android Application

🚧 Dynamic Runtime Synchronization

🚧 Profiles

🚧 Pages

🚧 Live Updates

🚧 Plugin Marketplace