import subprocess
import re

def convert_video_to_audio(input_video, output_audio, progress_bar=None):
    """Convierte un archivo de video a audio usando FFmpeg, muestra logs y actualiza barra de progreso"""
    
    # Comando FFmpeg para convertir video a audio
    command = ['ffmpeg', '-i', input_video, output_audio, '-y']  # '-y' sobrescribe archivos de salida
    process = subprocess.Popen(command, stderr=subprocess.PIPE, universal_newlines=True)

    # Expresiones regulares para capturar duración y tiempo de progreso
    duration_regex = re.compile(r"Duration: (\d+):(\d+):(\d+)\.(\d+)")
    time_regex = re.compile(r"time=(\d+):(\d+):(\d+)\.(\d+)")

    total_duration_seconds = 0

    # Logs iniciales
    print(f"Iniciando conversión: {input_video} -> {output_audio}")

    for line in process.stderr:
        # Imprimir log en consola
        print(line.strip())  # Muestra el log completo en consola
        
        # Encontrar la duración total del video (una sola vez al inicio)
        if not total_duration_seconds:
            duration_match = duration_regex.search(line)
            if duration_match:
                hours, minutes, seconds, _ = map(int, duration_match.groups())
                total_duration_seconds = hours * 3600 + minutes * 60 + seconds
                print(f"Duración total: {total_duration_seconds} segundos")

        # Encontrar el tiempo actual procesado
        time_match = time_regex.search(line)
        if time_match and total_duration_seconds:
            hours, minutes, seconds, _ = map(int, time_match.groups())
            current_time_seconds = hours * 3600 + minutes * 60 + seconds

            # Calcular porcentaje de progreso
            progress_percent = (current_time_seconds / total_duration_seconds) * 100

            # Actualizar barra de progreso si está habilitada
            if progress_bar is not None:
                progress_bar['value'] = progress_percent
                progress_bar.master.update_idletasks()  # Actualiza la interfaz gráfica
            
            # Imprimir log de progreso
            print(f"Progreso: {progress_percent:.2f}% completado")

    process.wait()  # Espera a que FFmpeg termine la conversión
    print(f"Conversión completada: {output_audio}")
