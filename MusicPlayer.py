import pygame
import os

class MusicPlayer:
    def __init__(self, music_folder):
        pygame.mixer.init()
        self.music_folder = music_folder
        self.playlist = [f for f in os.listdir(music_folder) if f.endswith('.mp3')]
        self.current_index = 0
        if not self.playlist:
            print("No music files found in the folder.")
            exit()

    def play(self):
        pygame.mixer.music.load(os.path.join(self.music_folder, self.playlist[self.current_index]))
        pygame.mixer.music.play()
        print(f"Playing: {self.playlist[self.current_index]}")

    def pause(self):
        pygame.mixer.music.pause()
        print("Music paused.")

    def unpause(self):
        pygame.mixer.music.unpause()
        print("Music resumed.")

    def stop(self):
        pygame.mixer.music.stop()
        print("Music stopped.")

    def next(self):
        self.current_index = (self.current_index + 1) % len(self.playlist)
        self.play()

    def previous(self):
        self.current_index = (self.current_index - 1) % len(self.playlist)
        self.play()

if __name__ == "__main__":
    music_folder = input("Enter the path to your music folder: ")
    player = MusicPlayer(music_folder)

    print("\nCommands: play, pause, unpause, stop, next, prev, quit")
    while True:
        command = input("Enter command: ").strip().lower()
        if command == "play":
            player.play()
        elif command == "pause":
            player.pause()
        elif command == "unpause":
            player.unpause()
        elif command == "stop":
            player.stop()
        elif command == "next":
            player.next()
        elif command == "prev":
            player.previous()
        elif command == "quit":
            player.stop()
            print("Exiting music player.")
            break
        else:
            print("Invalid command.")