import os
import subprocess

reaper_path = r''

data_directory = r''

output_directory = r''

def analyze_directory(data_directory, reaper_path = None, output_directory = None,
                    min_pitch = 80, max_pitch = 600, time_step = 0.005):
    if reaper_path is None:
        reaper_path = 'reaper'
    elif not os.path.exists(reaper_path):
        raise(OSError('Reaper binary was not found at \'{}\'.'.format(reaper_path)))

    if not os.path.exists(data_directory):
        raise(OSError('The data directory \'{}\' was not found.'.format(data_directory)))

    if output_directory is not None and not os.path.exists(output_directory):
        os.makedirs(output_directory)

    processed = 1

    for root, dir, files in os.walk(data_directory):
        for f in files:
            if not f.lower().endswith('.wav'):
                continue
            print('Processing wav file {}: {}'.format(processed, f))
            wav_path = os.path.join(root, f)
            base_name = os.path.splitext(f)[0]
            if output_directory is None:
                output_path = os.path.join(root, base_name + '.f0')
                pm_path = os.path.join(root, base_name + '.pm')
            else:
                new_root = root.replace(data_directory, output_directory)
                if not os.path.exists(new_root):
                    os.makedirs(new_root)
                output_path = os.path.join(new_root, base_name + '.f0')
                pm_path = os.path.join(new_root, base_name + '.pm')
            subprocess.call([reaper_path, '-i', wav_path, '-f',
                        output_path, '-p', pm_path, '-a',
                        '-e', str(time_step), '-u', str(time_step),
                        '-x', str(max_pitch), '-m', str(min_pitch)])
            processed += 1

if __name__ == '__main__':
    main()
