import os
from pytube import YouTube
from pytube import Playlist
import re

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


if not os.path.exists('downloads'):
    os.mkdir('downloads')

def downloader(url, output_folder, extension):
    video = YouTube(url)
    if extension == 'V':
        video.streams.get_highest_resolution().download(output_folder, filename=re.sub('[!,*)@#%(&$_?^|/\\\]', '', f'{video.title}.mp4'))

    elif extension == 'A':
        video.streams.get_audio_only().download(output_folder, filename=re.sub('[!,*)@#%(&$_?^|/\\\]', '', f'{video.title}.mp3'))


def video_downloader(url, extension):
    output_folder = 'downloads'
    try:

        print('Seu download começou')

        downloader(url, output_folder, extension)

        print('Seu download foi concluído')
    except:
        print('Erro no download')

def playlist_downloader(url, extension):
    yt = Playlist(url)
    videos = yt.video_urls
    playlist_name = re.sub('[!,*)@#%(&$_?.^|/\\\]', '', yt.title)
    output_folder = f'downloads/{playlist_name}'

    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    for index, video in enumerate(videos):

        try:
            downloader(video, output_folder, extension)
            print(f'Download Concluído! {index + 1} de {len(videos)}, iniciando o próximo!')
        except:
            print('Erro no download, iniciando o próximo!')
            continue


if download_type == 'P':
    playlist_downloader(url, extension)
elif download_type == 'V':
    video_downloader(url, extension)
