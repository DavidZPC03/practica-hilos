# Conversor de Videos a Audio con Multihilos 🖥️🎧

Esta es una aplicación desarrollada en **Python** que permite convertir archivos de video (formato `.mp4`) a audio (formato `.mp3`). La aplicación ofrece dos modos de conversión:

1. **Monohilos (bloqueante):** El proceso de conversión es secuencial, y si se intenta agregar un nuevo video mientras uno está siendo convertido, el proceso actual se interrumpe.
2. **Multihilos (no bloqueante):** Los videos se convierten en paralelo sin bloquear la interfaz, permitiendo procesar varios videos a la vez.

La aplicación también incluye una **barra de progreso** visual y muestra **logs detallados** en la consola.

## Instalación y Configuración

### 1. Requisitos previos

Antes de ejecutar la aplicación, asegúrate de tener instalados los siguientes componentes:

- **Python 3.8 o superior**.
- **FFmpeg**: Este programa es necesario para realizar la conversión de videos a audios.
   - Puedes verificar si FFmpeg está instalado ejecutando `ffmpeg -version` en la terminal.
   - Si no está instalado, sigue las instrucciones a continuación para instalarlo.

### 2. Instalación de FFmpeg

#### **Windows**

1. Descarga FFmpeg desde el siguiente enlace: [Descargar FFmpeg](https://sourceforge.net/projects/ffmpeg-windows-builds/).
2. Elige la versión **`ffmpeg-release-full.7z`**.
3. Extrae el contenido del archivo descargado.
4. Ubica la carpeta `bin` dentro de la carpeta extraída (por ejemplo, `C:\ffmpeg\bin`).
5. Agrega la ruta de la carpeta `bin` a las variables de entorno de tu sistema:
   - Ve a "Este equipo" -> "Propiedades" -> "Configuración avanzada del sistema" -> "Variables de entorno".
   - En la variable `Path`, agrega la ruta completa a `C:\ffmpeg\bin`.

#### **Linux (Ubuntu/Debian)**

Ejecuta los siguientes comandos para instalar FFmpeg:

```bash
sudo apt update
sudo apt install ffmpeg
