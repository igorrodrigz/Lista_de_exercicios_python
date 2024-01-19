import tkinter as tk
from tkinter import filedialog
import pygame
import os

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Disket Player")
        self.root.geometry("600x200")
        self.music_library = []
        self.current_track = None
        self.current_track_index = -1
        self.playing = False

        pygame.mixer.init()

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Disket Player", font='Helvetica 16')
        self.label.grid(row=0, column=0, columnspan=3, pady=10)

        self.btn_open = tk.Button(self.root, text="Adicionar música", command=self.add_music)
        self.btn_open.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)

        # Símbolos Unicode para os botões
        previous_symbol = "\u25C0"  # Símbolo de seta para a esquerda
        play_symbol = "\u25B6"  # Símbolo de seta para a direita

        # Usando a propriedade 'text' para definir os símbolos
        self.btn_previous = tk.Button(self.root, text=previous_symbol, command=self.play_previous_track,
                                      font=('Helvetica', 20))
        self.btn_play_pause = tk.Button(self.root, text=play_symbol, command=self.play_pause_music,
                                        font=('Helvetica', 20))
        self.btn_next = tk.Button(self.root, text=play_symbol, command=self.play_next_track,
                                  font=('Helvetica', 20))

        # Posicionamento dos botões usando grid
        self.btn_previous.grid(row=2, column=0, padx=10, pady=10, sticky=tk.E)
        self.btn_play_pause.grid(row=2, column=1, padx=10, pady=10)
        self.btn_next.grid(row=2, column=2, padx=10, pady=10, sticky=tk.W)

        # Rótulo para exibir o nome da música atual
        self.track_label = tk.Label(self.root, text="", font='Helvetica 12')
        self.track_label.grid(row=3, column=0, columnspan=3, pady=5)

    def add_music(self):
        file_paths = filedialog.askopenfilenames(filetypes=[("Arquivos de Áudio", "*.mp3")])

        if file_paths:
            self.music_library.extend(file_paths)
            if not self.current_track:
                self.play_next_track()

    def play_pause_music(self):
        if self.current_track:
            if not self.playing:
                pygame.mixer.music.unpause()
                self.playing = True
                self.btn_play_pause.config(text="Pause")
            else:
                pygame.mixer.music.pause()
                self.playing = False
                self.btn_play_pause.config(text="Play")

    def play_previous_track(self):
        if self.current_track_index > 0:
            self.current_track_index -= 1
            self.load_and_play_track()

    def play_next_track(self):
        if self.current_track_index < len(self.music_library) - 1:
            self.current_track_index += 1
            self.load_and_play_track()

    def load_and_play_track(self):
        if self.current_track:
            pygame.mixer.music.stop()

        self.current_track = self.music_library[self.current_track_index]
        pygame.mixer.music.load(self.current_track)
        pygame.mixer.music.play()
        self.playing = True
        self.btn_play_pause.config(text="Pause")
        self.update_track_label()

    def update_track_label(self):
        track_name = os.path.basename(self.current_track)
        self.track_label.config(text=f"Tocando agora: {track_name}")

if __name__ == "__main__":
    root = tk.Tk()
    music_player = MusicPlayer(root)
    root.mainloop()