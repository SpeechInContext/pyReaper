import sys
from setuptools import setup

import reaper

def readme():
    with open('README.md') as f:
        return f.read()


setup(name='reaper',
      version=reaper.__version__,
      description='',
      long_description='',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering',
        'Topic :: Text Processing :: Linguistic',
      ],
      keywords='pitch google-reaper',
      url='https://github.com/SpeechInContext/pyReaper',
      author='Michael McAuliffe',
      author_email='michael.e.mcauliffe@gmail.com',
      packages=['reaper',
                'reaper.command_line'],
      entry_points = {
        'console_scripts': ['batch_reaper=reaper.command_line.batch_reaper:main',],
    }
      )
