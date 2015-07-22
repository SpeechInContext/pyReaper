

import argparse

from reaper.batch_reaper import analyze_directory

def main():

    #### Parse command-line arguments
    parser = argparse.ArgumentParser(description = \
             'PyReaper: analyze directory')
    parser.add_argument('data_directory', help='Full path to wav files')
    parser.add_argument('-r', '--reaper_path', default = '', type=str, help='Path to reaper binary if not on path')
    parser.add_argument('-o', '--output_directory', default='', type=str, help='Directory to save output if not with the wav files')

    args = parser.parse_args()

    ####
    data = args.data_directory
    reaper = args.reaper_path
    if reaper == '':
        reaper = None
    output = args.output_directory
    if output == '':
        output = None
    analyze_directory(data, reaper, output)


if __name__ == '__main__':
    main()
