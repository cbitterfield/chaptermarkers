.. highlight:: shell

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
