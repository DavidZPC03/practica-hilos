import tkinter as tk
from tkinter import filedialog, ttk
from threading import Thread
import os
import ffmpeg_utils
import subprocess

# Variables globales
video_files = []  # Lista de videos seleccionados
multithreading_enabled = False  # Para activar o desactivar multihilos
processing = False  # Indicador si está en proceso de conversión

# Función para seleccionar videos
def select_videos():
    global video_files, processing
    files = filedialog.askopenfilenames(filetypes=[("Video files", "*.mp4")])
    if files:
        video_files.extend(files)
        update_video_list()
        if not multithreading_enabled and processing:
            print("Interrumpiendo la conversión actual...")
            processing = False

# Función para actualizar la lista de videos en la UI
def update_video_list():
    video_list.delete(0, tk.END)
    for video in video_files:
        video_list.insert(tk.END, os.path.basename(video))

# Función para actualizar la barra de progreso
def update_progress_bar():
    progress_bar['value'] = 0
    root.update_idletasks()  # Refrescar la interfaz

# Conversión en modo monohilo (secuencial)
def convert_videos_monohilo():
    global processing
    if not video_files:
        return
    processing = True
    while video_files and processing:
        video = video_files.pop(0)
        output_audio = video.replace(".mp4", ".mp3")
        update_progress_bar()  # Resetear la barra de progreso
        ffmpeg_utils.convert_video_to_audio(video, output_audio, progress_bar)
        update_video_list()
    processing = False

# Conversión en modo multihilos (paralelo)
def convert_videos_multihilo():
    global processing
    if not video_files:
        return
    processing = True
    while video_files and processing:
        video = video_files.pop(0)
        output_audio = video.replace(".mp4", ".mp3")
        update_progress_bar()  # Resetear la barra de progreso
        thread = Thread(target=ffmpeg_utils.convert_video_to_audio, args=(video, output_audio, progress_bar))
        thread.start()
        update_video_list()
    processing = False

# Función para manejar la conversión (dependiendo del modo)
def start_conversion():
    if multithreading_enabled:
        Thread(target=convert_videos_multihilo).start()
    else:
        Thread(target=convert_videos_monohilo).start()

# Función para activar/desactivar multihilos
def toggle_multithreading():
    global multithreading_enabled
    multithreading_enabled = not multithreading_enabled
    threading_button.config(text="Multihilos: ON" if multithreading_enabled else "Multihilos: OFF")

# Crear la interfaz gráfica
root = tk.Tk()
root.title("Conversor de Videos a Audio")

# Botones y lista
select_button = tk.Button(root, text="Seleccionar Videos", command=select_videos)
select_button.pack()

video_list = tk.Listbox(root, width=50)
video_list.pack()

start_button = tk.Button(root, text="Iniciar Conversión", command=start_conversion)
start_button.pack()

threading_button = tk.Button(root, text="Multihilos: OFF", command=toggle_multithreading)
threading_button.pack()

# Barra de progreso
progress_bar = ttk.Progressbar(root, orient="horizontal", length=400, mode="determinate")
progress_bar.pack(pady=10)

# Iniciar la app
root.mainloop()
