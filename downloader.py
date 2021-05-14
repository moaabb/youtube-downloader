import os
from pynotifier import Notification
from pytube import YouTube
from pytube import Playlist

url = input('Adiciona a URL do vídeo aqui: ')
while True:
    download_type = input('\nVocê quer baixar um Vídeo (V) ou uma Playilist (P)? ')
    if download_type == 'P' or download_type == 'V':
        break
    else: 
        print('\nVocê inseriu informações erradas, tente novamente')
while True:
    extension = input('\nVocê quer audio (A) ou vídeo (V)? ')
    if extension == 'V' or extension == 'A':
        break
    else: 
        print('\nVocê inseriu informações erradas, tente novamente')
    

def notify(title, description, duration = 5):
    Notification(
        title=title,
        description=description,
        icon_path='icon.ico', # On Windows .ico is required, on Linux - .png
        duration=duration,                              # Duration in seconds
        urgency='normal'
    ).send()

if not os.path.exists('downloads'):
        os.mkdir('downloads')

def downloader(url, output_folder, extension):
    video = YouTube(url)
    if extension == 'V':
        video.streams.get_highest_resolution().download(output_folder)
    elif extension == 'A':
        video.streams.get_audio_only().download(output_folder)

def video_downloader(url, extension):
    output_folder = 'downloads'
    try:
        video = YouTube(url)
        
        notify('Download está começando', f'O download de {video.title} está em andamento', 2)
        print('Seu download começou')
        
        downloader(url, output_folder, extension)
    
        notify('Download foi finalizado', f'O download de {video.title} foi concluído')
        print('Seu download foi concluído')
    except:
        print('Erro no download')
        notify('Erro no download', 'Tente novamente')

def playlist_downloader(url, extension):
    yt = Playlist(url)
    videos = yt.video_urls
    output_folder = f'downloads/{yt.title}'

    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    notify('Download está começando', f'O download de {yt.title} está em andamento', 2)

    for index, video in enumerate(videos):

        try:  
            downloader(video, output_folder, extension)
            print(f'Download Concluído! {index + 1} de {len(videos)}, iniciando o próximo!')
        except:
            print('Erro no download, iniciando o próximo!')
            continue

    notify('Download foi finalizado', f'O download de {yt.title} foi concluído')


if download_type == 'P':
    playlist_downloader(url, extension)
elif download_type == 'V':
    video_downloader(url, extension)
