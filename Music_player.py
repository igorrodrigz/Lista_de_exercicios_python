import tkinter as tk
from tkinter import filedialog
import pygame

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music player")
        self.root.geometry("300x150")
        self.current_track = None
        self.playing = False

        pygame.mixer.init()

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Player de Música", font='Helvetica 16')
        self.label.pack(pady=10)

        self.btn_open = tk.Button(self.root, text="Abrir música", command=self.open_music)
        self.btn_open.pack(pady=5)

        self.btn_play_pause = tk.Button(self.root, text="Play", command=self.play_pause_music)
        self.btn_play_pause.pack(pady=5)

        self.btn_stop = tk.Button(self.root, text="Stop", command=self.stop_music)
        self.btn_play_pause.pack(pady=5)

    def open_music(self):
        file_path = filedialog.askopenfile(filetypes=[("Arquivos de Áudio", "*.mp3")])

        if file_path:
            self.current_track = file_path
            pygame.mixer.music.load(file_path)
            self.playing = False
            self.btn_play_pause.config(text="Play")

    def play_pause_music(self):
        if self.current_track:
            if not self.playing:
                pygame.mixer.music.play()
                self.playing = True
                self.btn_play_pause.config(text="Pause")
            else:
                pygame.mixer.music.pause()
                self.playing = False
                self.btn_play_pause.config(text="play")
    def stop_music(self):
        if self.current_track:
            pygame.mixer.music.stop()
            self.playing = False
            self.btn_play_pause.config(text="Play")
if __name__ == "__main__":
    root = tk.Tk()
    music_player = MusicPlayer(root)
    root.mainloop()

