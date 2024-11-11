import os
import yt_dlp

output_folder = "AudiosBaixados"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

def download_audio(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
        'postprocessors': [],  # Remove pós-processamento para evitar necessidade de ffmpeg
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Download concluído! O áudio está salvo na pasta:", output_folder)
    except Exception as e:
        print("Ocorreu um erro durante o download:", e)

while True:
    audio_url = input("Cole aqui a sua URL (ou digite 'sair' para encerrar): ")
    if audio_url.lower() == 'sair':
        print("Programa encerrado.")
        break
    download_audio(audio_url)
