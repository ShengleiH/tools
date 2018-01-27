import subprocess
from os import walk

def get_files(root_path):
    all_files = []
    path = ''

    for root, dirs, files in walk(root_path):
        path = root

    for file in files:
        new_file_path = path + '/' + file
        all_files.append(new_file_path)

    return sorted(all_files)

if __name__ == '__main__':
    source_path = 'mp3_data'
	  distination_path = 'wav_data'
	  files = get_files(root_path=source_path)

	  for i, wav_file in enumerate(files):
		    print('Processing file {}/{}'.format(i, len(files)))
		    wav_name = wav_file.split('/')[-1].split('.')[0]
		    to_wav_command = 'ffmpeg -i {} -acodec pcm_u8 -ar 16000 {}/{}'.format(wav_file, distination_path, wav_name+'.wav')
		    subprocess.call(to_wav_command, shell=True)
