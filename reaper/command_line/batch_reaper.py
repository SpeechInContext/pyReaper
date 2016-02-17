

import argparse

from reaper.batch_reaper import analyze_directory

def main():

    #### Parse command-line arguments
    parser = argparse.ArgumentParser(description = \
             'PyReaper: analyze directory')
    parser.add_argument('data_directory', help='Full path to wav files')
    parser.add_argument('-r', '--reaper_path', default = '', type=str, help='Path to reaper binary if not on path')
    parser.add_argument('-o', '--output_directory', default='', type=str, help='Directory to save output if not with the wav files')
    parser.add_argument('-t', '--time_step', default=0.001, type=float, help='Interval between pitch marks')
    parser.add_argument('-x', '--max_pitch', default=600, type=int, help='Maximum pitch (in Hz) to look for')
    parser.add_argument('-m', '--min_pitch', default=80, type=int, help='Minimum pitch (in Hz) to look for')

    args = parser.parse_args()

    ####
    data = args.data_directory
    reaper = args.reaper_path
    if reaper == '':
        reaper = None
    output = args.output_directory
    if output == '':
        output = None
    kwargs = {}
    step = args.time_step
    if step:
        kwargs['time_step'] = step
    mp = args.max_pitch
    if mp:
        kwargs['max_pitch'] = mp
    mp = args.min_pitch
    if mp:
        kwargs['min_pitch'] = mp
    analyze_directory(data, reaper, output, **kwargs)


if __name__ == '__main__':
    main()
