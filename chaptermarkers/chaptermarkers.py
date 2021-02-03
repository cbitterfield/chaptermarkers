#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create Chapter Markers using FFMPEG from the command line (CLI)
chapter-markers -f chapters.txt -m mpeg.mp4
"""


import re
import argparse
import sys
import os
import shutil
import time
from datetime import datetime
import subprocess


version = '1.2.2'
__version__ = version
program = 'chaptermarkers'
description = 'Chapter markers creates markers in MP4 files from friendly time marks'
epilog = '''
The default value for FFMPEGCMD is /opt/local/bin/ffmpeg [MAC Ports].
If your binary is in a different location use
export FFMPEG=/usr/bin/ffmpeg or whatever is appropriate for your shell
Temp files are written to /tmp and are remove if successful write occurs
'''

DEBUG = False
FILENAME = 'mpeg.mp4'
CHAPTERS = 'chapters.txt'
OUTPUT = None
TEMPFILE = '/tmp/FFMETADATAFILE'
TITLE = None
FFMPEGCMD = None

# Add this module's location to syspath
sys.path.insert(0, os.getcwd())

__author__ = 'Colin Bitterfield'
__email__ = 'colin@bitterfield.com'
__prog_name__ = os.path.basename(__file__)
__short_name__ = os.path.splitext(__prog_name__)[0]
__console_size_ = shutil.get_terminal_size((80, 20))[0]
__timestamp__ = time.time()
__run_datetime__ = datetime.fromtimestamp(__timestamp__)  # Today's Date


# Define Variables
chapters = list()


def main(args=None):
    """ Main entry point of chapter-markers """
    config = cli(version=__version__, program=__prog_name__)
    setup(config)
    text = ''
    print("Adding chapter markers to {filename} from chapters file {chapters}"
          .format(filename=FILENAME, chapters=CHAPTERS))
    print("Reading Chapters file and parsing")
    if DEBUG:
        print("FFMPEG Command located at {ffmpeg}".format(ffmpeg=FFMPEGCMD))

    with open(CHAPTERS, 'r') as f:
        for line in f:
            x = re.match(r"(\d{1,2}):(\d{2}):(\d{2}.\d{1,5}) (.*)", line)
            hrs = int(x.group(1))
            mins = int(x.group(2))
            secs = float(x.group(3))
            title = x.group(4)

            minutes = (hrs * 60) + mins
            seconds = secs + (minutes * 60)
            timestamp = (seconds * 1000)
            chap = {
                "title": title,
                "startTime": timestamp
            }
            if DEBUG:
                print("Chapter {chapter} at {time}"
                      .format(time=chap['startTime'], chapter=chap['title']))
            chapters.append(chap)

    # Set Master information
    text = ";FFMETADATA1\ntitle={TITLE}\n\n".format(TITLE=TITLE)

    for i in range(len(chapters) - 1):
        chap = chapters[i]
        title = chap['title']
        start = chap['startTime']
        end = chapters[i + 1]['startTime'] - 1
        text += f"""[CHAPTER]\nTIMEBASE=1/1000\nSTART={start}\nEND={end}\ntitle={title}\n\n"""

        with open(TEMPFILE, "w") as myfile:
            myfile.write(text)
    if DEBUG:
        print("Adding chapter markers to {filename} writing changes to {output}".format(filename=FILENAME,output=OUTPUT))
    writeMetada(TEMPFILE, FILENAME, OUTPUT)

    return 0


def cli(**kwargs):
    parser = argparse.ArgumentParser()
    parser.prog = program
    parser.description = description
    parser.epilog = epilog

    # Defaults for all programs
    parser.add_argument('--version',
                        action='version',
                        version='%(prog)s ' + version)

    parser.add_argument('-d', '--debug',
                        help='Turn on Debugging Mode',
                        action='store_true',
                        required=False,
                        dest='debug',
                        default=DEBUG
                        )

    parser.add_argument('-f', '--chapters-file',
                        help='Text file with chapters in it. TimeStamp space Title',
                        type=str,
                        action='store',
                        required=True,
                        dest='CHAPTERS',
                        default=CHAPTERS
                        )

    parser.add_argument('-m', '--mpeg-video',
                        help='Movie file MP4s only -- Currently no checking',
                        type=str,
                        action='store',
                        required=True,
                        dest='FILENAME',
                        default="unknown"
                        )

    parser.add_argument('-o', '--mpeg-video-markers',
                        help='default is FILENAME_chapters.mp4',
                        type=str,
                        action='store',
                        required=False,
                        dest='OUTPUT',
                        default=FILENAME + "_chapters.mp4"
                        )
    parser.add_argument('-t', '--title',
                        help='''default is My Default Movie,
                             this is the title that will show when playing''',
                        type=str,
                        action='store',
                        required=False,
                        dest='TITLE',
                        default="My Default Movie"
                        )

    parser.add_argument('--test',
                        help='''test if ffmpeg is installed and the program runs,''',
                        action='store_true',
                        required=False,
                        dest='testProgram',
                        default=False
                        )

    parse_out = parser.parse_args()
    return parse_out


def setup(configuration):
    global DEBUG
    global FILENAME
    global CHAPTERS
    global OUTPUT
    global TITLE
    global FFMPEGCMD

    FFMPEGCMD = os.getenv('FFMPEG',  findFFMEG())
    testFFMPEG = "{ffmpegcmd} -version | head -1".format(ffmpegcmd=FFMPEGCMD)

    if configuration.testProgram:
        print('FFMPEG Location: {ffmpeg}'.format(ffmpeg=FFMPEGCMD))
        resultsFFMPEG = subprocess.run(testFFMPEG, shell=True,stdout=subprocess.PIPE)
        print("FFMPEG VERSION: {ffmpegVersion}".format(ffmpegVersion=resultsFFMPEG.stdout.decode("utf-8")))
        exit(0)

    if configuration.debug:
        DEBUG = configuration.debug
        print(configuration)
        print('FFMPEG Location: {ffmpeg}'.format(ffmpeg=FFMPEGCMD))
        resultsFFMPEG = subprocess.run(testFFMPEG, shell=True,stdout=subprocess.PIPE)
        print("FFMPEG VERSION: {ffmpegVersion}".format(ffmpegVersion=resultsFFMPEG.stdout.decode("utf-8")))

    if not os.path.isfile(configuration.FILENAME):
        print('Movie Filename {filename} is missing'.format(filename=configuration.FILENAME))
        exit(1)
    else:
        FILENAME = configuration.FILENAME

    if not configuration.CHAPTERS:
        print('Chapters File {chapters} is missing'.format(chapters=configuration.CHAPTERS))
        exit(1)
    else:
        CHAPTERS = configuration.CHAPTERS
    OUTPUT = configuration.OUTPUT
    TITLE = configuration.TITLE



def writeMetada(ffmetadata, video, output):
    TEMPLATE = "{FFMPEG} -hide_banner -i '{INPUT}' -i {FFMETADATAFILE} -map_metadata 1 -codec copy '{OUTPUT}' -y".\
        format(FFMPEG=FFMPEGCMD, FFMETADATAFILE=ffmetadata, INPUT=video, OUTPUT=output)
    subprocess.run(TEMPLATE, shell=True)
    if DEBUG:
        print("TEMPLATE: {template}".format(template=TEMPLATE))
    pass

def findFFMEG(**args):
    localFFMPEG = None
    locations = ['/opt/local/bin','/usr/local/bin','/usr/local/ffmpeg', '/usr/local/opt/']
    for location in locations:
        if os.path.isfile("/".join([location,'ffmpeg'])):
            localFFMPEG="/".join([location,'ffmpeg'])
    return localFFMPEG

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
