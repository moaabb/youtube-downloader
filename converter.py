import os
import subprocess

folder = input('Insira o caminho absoluto para a pasta com os arquivos para serem convertidos para mp3: ')


input_folder = os.listdir(folder)

if not os.path.exists(f'{folder}/Convertido - MP3'):
    os.mkdir(f'{folder}/Convertido - MP3')

for index, music in enumerate(input_folder):
    music_no_ext = music.split('.')[0]
    print(f'Convertendo música {index + 1} de {len(input_folder)}')
    subprocess.run(["ffmpeg",'-i', f'{folder}/{music}', f'{folder}/Convertido - MP3/{music_no_ext}.mp3', '-loglevel', 'quiet'])

print('Tudo pronto!')
