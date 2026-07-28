import secrets
import time

PAIRING_PIN_EXPIRY_SECONDS = 300
MAX_PAIRING_ATTEMPTS = 5

_current_pairing_pin: str | None = None
_pairing_pin_created_at: float | None = None
_failed_attempts = 0


def clear_pairing_pin() -> None:
    global _current_pairing_pin
    global _pairing_pin_created_at
    global _failed_attempts

    _current_pairing_pin = None
    _pairing_pin_created_at = None
    _failed_attempts = 0


def generate_pairing_pin() -> str:
    global _current_pairing_pin
    global _pairing_pin_created_at
    global _failed_attempts

    _current_pairing_pin = f"{secrets.randbelow(1_000_000):06d}"
    _pairing_pin_created_at = time.time()
    _failed_attempts = 0

    return _current_pairing_pin


def get_pairing_pin_status() -> dict:
    if _current_pairing_pin is None or _pairing_pin_created_at is None:
        return {
            "active": False,
            "expires_in": 0,
            "attempts_remaining": 0,
        }

    elapsed = time.time() - _pairing_pin_created_at

    if elapsed >= PAIRING_PIN_EXPIRY_SECONDS:
        clear_pairing_pin()

        return {
            "active": False,
            "expires_in": 0,
            "attempts_remaining": 0,
        }

    remaining = PAIRING_PIN_EXPIRY_SECONDS - int(elapsed)

    return {
        "active": True,
        "expires_in": remaining,
        "attempts_remaining": MAX_PAIRING_ATTEMPTS - _failed_attempts,
    }


def verify_pairing_pin(pin: str) -> dict:
    global _failed_attempts

    if _current_pairing_pin is None or _pairing_pin_created_at is None:
        return {
            "success": False,
            "reason": "inactive",
        }

    elapsed = time.time() - _pairing_pin_created_at

    if elapsed >= PAIRING_PIN_EXPIRY_SECONDS:
        clear_pairing_pin()

        return {
            "success": False,
            "reason": "expired",
        }

    if secrets.compare_digest(pin, _current_pairing_pin):
        clear_pairing_pin()

        return {
            "success": True,
            "reason": "success",
        }

    _failed_attempts += 1

    attempts_remaining = MAX_PAIRING_ATTEMPTS - _failed_attempts

    if attempts_remaining <= 0:
        clear_pairing_pin()

        return {
            "success": False,
            "reason": "attempts_exceeded",
            "attempts_remaining": 0,
        }

    return {
        "success": False,
        "reason": "invalid",
        "attempts_remaining": attempts_remaining,
    }
