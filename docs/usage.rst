.. highlight:: shell

=========
USAGE
=========

Chapter Markers will take a file with times and titles and create chapter markers in a new mp4 file.

./chaptermarkers -f chapters.txt -m input_video.mp4 -o output_video.mp4

./chaptermarkers --help will provide additional options.

See examples file: chapters.txt for an example file

FFMPEG must be installed on your system and the environment variable FFMPEG
which needs to be set to the proper location. The program will attempt to find FFMPEG
in well know locations if the variable is not set.

=========
Dev Notes
=========


How to use python virtualenv
----------------------------

.. code-block:: console

	$ workon <virtualenv_name>
	$ [<virtualenv_name>] ...
	$ deactivate

How to run unit test
--------------------

.. code-block:: console

    $ make utest

How to run sytem test
--------------------

.. code-block:: console

	$ sudo make install
	$ make stest
	$ sudo make uninstall

How to run unit test coverage
-----------------------------

.. code-block:: console

	$ make coverage

How to run flake8 and pylint
----------------------------

.. code-block:: console

	$ make flake
	$ make pylint

How to build a docker image
---------------------------

.. code-block:: console

	$ make docker-image
