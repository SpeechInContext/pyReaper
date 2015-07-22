# pyReaper
Python wrapper for Google-REAPER

Installation
------------

1. Install Google-REAPER (https://github.com/google/REAPER)
2. Clone repository or download zip file (https://github.com/SpeechInContext/pyReaper/archive/master.zip)
3. Unzip and open terminal in the the `pyReaper/` directory
4. Install the package (`python setup.py install` or `sudo python setup.py install` if necessary)
5. The command `batch_reaper` should be available from the terminal

Use
---

The following command is used:

`batch_reaper /path/to/wav/files -r /path/to/reaper/binary -o /path/to/save/output`

The only required argument is the data directory containing the wav files to be analyzed.  The script will inspect all subfolders recursively and find all wav files in the directory. The path to the reaper binary and the path to save output are optional.  If no reaper path is specified, the command will assume that `reaper` is on the system path and can be run from a terminal.  If no output path is specified, the output files will be saved alongside the wav files in the data directory.  If an output directory is specified, it will create the directory if it doesn't exist already and save the output files in the same directory structure as the data directory.
