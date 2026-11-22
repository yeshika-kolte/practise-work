'''26. Media Player

Abstract:

MediaPlayer

Derived:

AudioPlayer
VideoPlayer

Implement play functionality.'''



from abc import *

class MediaPlayer(ABC):

    @abstractmethod
    def play(self):
        pass


class AudioPlayer(MediaPlayer):

    def __init__(self, song_name):
        self.song_name = song_name

    def play(self):
        print(f"Playing audio: {self.song_name}")


class VideoPlayer(MediaPlayer):

    def __init__(self, video_name):
        self.video_name = video_name

    def play(self):
        print(f"Playing video: {self.video_name}")

a1 = AudioPlayer("Shape of You")
v1 = VideoPlayer("Python Tutorial")

a1.play()
v1.play()