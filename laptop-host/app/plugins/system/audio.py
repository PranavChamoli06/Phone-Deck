from pycaw.pycaw import AudioUtilities


class AudioController:
    def __init__(self):
        self._volume = None

    def _endpoint(self):
        if self._volume is None:
            device = AudioUtilities.GetSpeakers()
            self._volume = device.EndpointVolume
        return self._volume

    def get_volume(self) -> int:
        level = self._endpoint().GetMasterVolumeLevelScalar()
        return round(level * 100)

    def set_volume(self, percent: int) -> int:
        percent = max(0, min(100, percent))
        self._endpoint().SetMasterVolumeLevelScalar(percent / 100, None)
        return percent

    def volume_up(self, step: int = 5) -> int:
        return self.set_volume(self.get_volume() + step)

    def volume_down(self, step: int = 5) -> int:
        return self.set_volume(self.get_volume() - step)

    def mute(self):
        self._endpoint().SetMute(True, None)

    def unmute(self):
        self._endpoint().SetMute(False, None)

    def toggle_mute(self):
        endpoint = self._endpoint()
        endpoint.SetMute(not bool(endpoint.GetMute()), None)

    def is_muted(self) -> bool:
        return bool(self._endpoint().GetMute())


audio_controller = AudioController()
