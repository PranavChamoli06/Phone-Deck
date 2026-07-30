from ui.theme.colors import *

APP_STYLESHEET = f"""
/* ============================================================
   Main Window
============================================================ */

QMainWindow {{
    background-color: {BACKGROUND};
    color: {TEXT_PRIMARY};
}}

/* ============================================================
   Global Widgets
============================================================ */

QWidget {{
    color: {TEXT_PRIMARY};
    font-family: "Segoe UI";
    font-size: 10pt;
}}

QLabel {{
    color: {TEXT_PRIMARY};
    background: transparent;
}}

/* ============================================================
   Glass Panels
============================================================ */

#glassPanel {{
    background-color: {SURFACE};

    border: 1px solid rgba(255,255,255,0.08);

    border-radius: 20px;
}}

/* ============================================================
   Buttons
============================================================ */

QPushButton {{
    background-color: rgba(255,255,255,0.08);

    color: white;

    border: 1px solid rgba(255,255,255,0.10);

    border-radius: 12px;

    padding: 8px 18px;

    font-family: "Segoe UI";
    font-size: 10pt;
    font-weight: 600;
}}

QPushButton:hover {{
    background-color: rgba(255,255,255,0.13);

    border: 1px solid rgba(79,140,255,0.35);
}}

QPushButton:pressed {{
    background-color: rgba(79,140,255,0.20);

    border: 1px solid rgba(79,140,255,0.45);
}}

QPushButton:disabled {{
    background-color: rgba(255,255,255,0.04);

    color: rgba(255,255,255,0.35);

    border: 1px solid rgba(255,255,255,0.05);
}}

QPushButton:checked {{
    background-color: rgba(79,140,255,0.22);

    border: 1px solid rgba(79,140,255,0.45);
}}

/* ============================================================
   Navigation Buttons
============================================================ */

NavigationButton {{
    text-align: left;
    padding-left: 14px;
}}

/* ============================================================
   Status Bar
============================================================ */

QStatusBar {{
    background: transparent;
    color: {TEXT_SECONDARY};
}}

QStatusBar::item {{
    border: none;
}}
"""