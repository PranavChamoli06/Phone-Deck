from __future__ import annotations

import ctypes
import subprocess
from ctypes import POINTER, byref, wintypes
from pathlib import Path
from uuid import UUID

from app.action_registry import registry

# ---------------------------------------------------------------------------
# Windows Known Folder IDs
# ---------------------------------------------------------------------------

KNOWN_FOLDER_IDS = {
    "desktop": UUID("{B4BFCC3A-DB2C-424C-B029-7FE99A87C641}"),
    "documents": UUID("{FDD39AD0-238F-46AF-ADB4-6C85480369C7}"),
    "downloads": UUID("{374DE290-123F-4565-9164-39C4925E467B}"),
    "pictures": UUID("{33E28130-4E1E-4676-835A-98395C3BC3BB}"),
    "music": UUID("{4BD8D571-6D19-48D3-BE97-422220080E43}"),
    "videos": UUID("{18989B1D-99B5-455B-841C-AB7C74E4DDFC}"),
}


# ---------------------------------------------------------------------------
# Windows GUID structure
# ---------------------------------------------------------------------------


class GUID(ctypes.Structure):
    _fields_ = [
        ("Data1", wintypes.DWORD),
        ("Data2", wintypes.WORD),
        ("Data3", wintypes.WORD),
        ("Data4", ctypes.c_ubyte * 8),
    ]

    @classmethod
    def from_uuid(cls, value: UUID) -> GUID:
        return cls(
            value.time_low,
            value.time_mid,
            value.time_hi_version,
            (ctypes.c_ubyte * 8)(*value.bytes[8:]),
        )


# ---------------------------------------------------------------------------
# Windows Shell API
# ---------------------------------------------------------------------------

shell32 = ctypes.windll.shell32
ole32 = ctypes.windll.ole32

shell32.SHGetKnownFolderPath.argtypes = [
    POINTER(GUID),
    wintypes.DWORD,
    wintypes.HANDLE,
    POINTER(ctypes.c_wchar_p),
]

shell32.SHGetKnownFolderPath.restype = wintypes.HRESULT

ole32.CoTaskMemFree.argtypes = [ctypes.c_void_p]
ole32.CoTaskMemFree.restype = None


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def get_known_folder(name: str) -> Path:
    """
    Returns the actual Windows location of a known folder.
    Supports redirected folders (OneDrive, custom locations, etc.).
    """

    folder_uuid = KNOWN_FOLDER_IDS.get(name.lower())

    if folder_uuid is None:
        raise ValueError(f"Unknown known folder: {name}")

    folder_id = GUID.from_uuid(folder_uuid)

    path_ptr = ctypes.c_wchar_p()

    hr = shell32.SHGetKnownFolderPath(
        byref(folder_id),
        0,
        None,
        byref(path_ptr),
    )

    if hr != 0:
        raise OSError(
            f"SHGetKnownFolderPath failed for '{name}' " f"(HRESULT=0x{hr:08X})"
        )

    try:
        return Path(path_ptr.value)
    finally:
        ole32.CoTaskMemFree(path_ptr)


def open_path(path: str | Path):
    """
    Open a file or directory in Windows File Explorer.
    """

    path = Path(path).expanduser()

    if not path.exists():
        return {
            "status": "error",
            "message": f"Path '{path}' does not exist.",
        }

    subprocess.Popen(
        ["explorer.exe", str(path)],
        shell=False,
    )

    return {
        "status": "success",
        "path": str(path),
    }


def reveal_path(path: str | Path):
    path = Path(path).expanduser()

    if not path.exists():
        return {
            "status": "error",
            "message": f"Path '{path}' does not exist.",
        }

    target = path

    if path.is_dir():
        target = path.resolve()

    subprocess.Popen(
        [
            "explorer.exe",
            f"/select,{target}",
        ],
        shell=False,
    )

    return {
        "status": "success",
        "path": str(path),
    }


# ---------------------------------------------------------------------------
# Actions
# ---------------------------------------------------------------------------


async def open_explorer(path: str, **kwargs):
    return open_path(path)


async def open_desktop(**kwargs):
    return open_path(get_known_folder("desktop"))


async def open_documents(**kwargs):
    return open_path(get_known_folder("documents"))


async def open_downloads(**kwargs):
    return open_path(get_known_folder("downloads"))


async def open_pictures(**kwargs):
    return open_path(get_known_folder("pictures"))


async def open_music(**kwargs):
    return open_path(get_known_folder("music"))


async def open_videos(**kwargs):
    return open_path(get_known_folder("videos"))


async def reveal_explorer(path: str, **kwargs):
    return reveal_path(path)


# ---------------------------------------------------------------------------
# Registration
# ---------------------------------------------------------------------------


def register_explorer_actions() -> None:
    registry.register(
        name="explorer.open",
        action=open_explorer,
        description="Open a folder or file in File Explorer.",
        category="explorer",
    )

    registry.register(
        name="explorer.open_desktop",
        action=open_desktop,
        description="Open the Desktop folder.",
        category="explorer",
    )

    registry.register(
        name="explorer.open_documents",
        action=open_documents,
        description="Open the Documents folder.",
        category="explorer",
    )

    registry.register(
        name="explorer.open_downloads",
        action=open_downloads,
        description="Open the Downloads folder.",
        category="explorer",
    )

    registry.register(
        name="explorer.open_pictures",
        action=open_pictures,
        description="Open the Pictures folder.",
        category="explorer",
    )

    registry.register(
        name="explorer.open_music",
        action=open_music,
        description="Open the Music folder.",
        category="explorer",
    )

    registry.register(
        name="explorer.open_videos",
        action=open_videos,
        description="Open the Videos folder.",
        category="explorer",
    )

    registry.register(
        name="explorer.reveal",
        action=reveal_explorer,
        description="Reveal a file or folder in File Explorer.",
        category="explorer",
    )
