==================
chaptermarkers
==================


.. image:: https://img.shields.io/pypi/v/python_boilerplate.svg
        :target: https://pypi.python.org/pypi/python_boilerplate

.. image:: https://img.shields.io/travis/fgriberi/python_boilerplate.svg
        :target: https://travis-ci.org/fgriberi/python_boilerplate

.. image:: https://readthedocs.org/projects/python-boilerplate/badge/?version=latest
        :target: https://python-boilerplate.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

chaptermarkers will creat chapter markers in MP4 files from a text file.

Get Started!
-----------------------

Here’s how to set up *chaptermarkers* for local environment.

1- Clone the *chaptermarkers* locally:

.. code-block:: console

    $ git clone https://github.com/cbitterfield/chaptermarkers.git

2- Install your local copy into a *virtualenv*. Assuming you have *virtualenvwrapper* installed, this is how you set up the package for local development:

.. code-block:: console

    $ sudo make boostrap
    $ mkvirtualenv chaptermarkers
    $ pip install -r requirements/dev.txt

3- How to enable/disable virtualenv

.. code-block:: console

    $ workon chaptermarkers
    $ ...
    $ deactivate


Usage:
------------------
usage: chaptermarkers [-h] [--version] [-d] [-f CHAPTERS] [-m FILENAME] [-o OUTPUT] [-t TITLE]

Chapter markers creates markers in MP4 files from friendly time marks

optional arguments:
  -h, --help            show this help message and exit
  --version             show program's version number and exit
  -d, --debug           Turn on Debugging Mode
  -f CHAPTERS, --chapters-file CHAPTERS
                        Text file with chapters in it. TimeStamp space Title
  -m FILENAME, --mpeg-video FILENAME
                        Movie file MP4s only -- Currently no checking
  -o OUTPUT, --mpeg-video-markers OUTPUT
                        default is FILENAME_chapters.mp4
  -t TITLE, --title TITLE
                        default is Galaxy Entertainment Movie, this is the title that will show when playing

The default value for FFMPEGCMD is /opt/local/bin/ffmpeg [MAC Ports]. If your binary is in a different location use export FFMPEG=/usr/bin/ffmpeg or
whatever is appropriate for your shell Temp files are written to /tmp and are remove if successful write occurs


Credits
-------

