import pygame
import tkinter as tk
from tkinter import filedialog

# Initialize Pygame Mixer
pygame.mixer.init()

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Custom Music Player")
        self.root.geometry("400x200")
        self.root.config(bg="lightblue")
        
        # Make window draggable
        self.root.overrideredirect(True)  # Removes default window decorations
        self.root.bind("<B1-Motion>", self.drag_window)
        
        # Create play, pause, stop buttons
        play_btn = tk.Button(self.root, text="Play", command=self.play_music, bg="green", fg="white")
        play_btn.pack(pady=20)

        pause_btn = tk.Button(self.root, text="Pause", command=self.pause_music, bg="yellow")
        pause_btn.pack(pady=10)

        stop_btn = tk.Button(self.root, text="Stop", command=self.stop_music, bg="red", fg="white")
        stop_btn.pack(pady=10)
        
        # Close button to exit app
        close_btn = tk.Button(self.root, text="X", command=self.root.quit, bg="black", fg="white")
        close_btn.place(x=370, y=10)

    def drag_window(self, event):
        self.root.geometry(f'+{event.x_root}+{event.y_root}')  # Allows window to be dragged

    def play_music(self):
        # Open file dialog to select music file
        music_file = filedialog.askopenfilename(filetypes=[("Music Files", "*.mp3 *.wav")])
        if music_file:
            pygame.mixer.music.load(music_file)
            pygame.mixer.music.play()

    def pause_music(self):
        pygame.mixer.music.pause()

    def stop_music(self):
        pygame.mixer.music.stop()

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()
