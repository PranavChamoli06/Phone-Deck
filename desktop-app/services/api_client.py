import requests

class APIClient:
    """
    Handles HTTP communication with the laptop backend.
    """

    def __init__(self, base_url="http://127.0.0.1:8000"):
        self.base_url = base_url.rstrip("/")


    def health_check(self) -> bool:
        """
        Returns True if the backend is reachable.
        """
        try:
            response = requests.get(
                f"{self.base_url}/health",
                timeout=3,
            )

            return response.status_code == 200

        except requests.RequestException:
            return False


    def start_pairing(self) -> dict:
        """
        Starts a new pairing session.

        Returns the backend response as a dictionary.
        """

        response = requests.post(
            f"{self.base_url}/pairing/start",
            timeout=5,
        )

        response.raise_for_status()

        return response.json()