Installation 
============

Virtual environment
-------------------

It is heavily recommended to isolate your development environment using either
venv utility or conda:

.. code-block:: console

    $ python -m venv .venv
    $ source .venv/bin/activate

Python dependencies
-------------------

To start developing, first install the developers requirements:

.. code-block:: console

    (.venv) $ pip install -r requirements-dev.txt

System level dependencies
-------------------------

For system level dependencies there's the **conf/** folder which contains
opencv's and picamera's dependencies. Run the scripts:

.. code-block:: console

    $ ./conf/dependencies.sh
    $ ./conf/picamera2-dependencies.sh