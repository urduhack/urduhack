Installation
============

.. note:: Urduhack is supported on the following Python versions

+--------------+-------+-------+-------+-------+-------+
|**Python**    |**2.7**|**3.4**|**3.5**|**3.6**|**3.7**|
+--------------+-------+-------+-------+-------+-------+
|Urduhack      |       |       |       |  Yes  |  Yes  |
+--------------+-------+-------+-------+-------+-------+

Basic Installation
------------------
The easiest way to install **urduhack** is by :command:`pip` install.::

    $ pip install Urduhack


Dependencies
------------
Having so many functionality, **urduhack** depends on a number of other packages. Try to avoid any kind of conflict.
It is preferred that you create a virtual environment and install *urduhack* in that environment.

* **Tensorflow** Use for training, evaluating and testing deep neural network model. Urduhack has been tested with
   **2.0.0**, **2.0.1** versions.

* **Request** Use for downloading data for s3.

* **Click** With help of this library Urduhack commandline application developed.

* **tqdm** Use for showing progressbar while training.


Downloading Model
-----------------
To download the model weights all you have to do is run this simple command in the command line.::

    >>>urduhack download

This command will download the model which will be used by urduhack.