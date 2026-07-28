import platform
import socket

from fastapi import APIRouter

router = APIRouter(tags=["Device"])


@router.get("/device")
def get_device_info():
    return {
        "hostname": socket.gethostname(),
        "os": platform.system(),
        "os_version": platform.release(),
        "architecture": platform.machine(),
    }
