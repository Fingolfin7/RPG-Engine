from pygame import mixer
import os
import time  # for the sleep functions


def play_song(song_path=""):
    mixer.init()
    mixer.music.load(os.path.normpath(song_path))
    mixer.music.play()

    while mixer.music.get_busy():
        time.sleep(10)

    mixer.music.stop()

# play_song(glob("C:/Users/Kuda/Music/edIT Ants.mp3")[0])
# play_song("C:\\Users\\Kuda\\Documents\\Programming\\Python\\Campaign Creator\\Minecraft FULL SOUNDTRACK (2016).mp3")
