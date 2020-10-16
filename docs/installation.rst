Installation
============

.. note:: Urduhack is supported on the following Python versions

+------------+-------+-------+-------+-------+-------+
|**Python**  |**3.8**|**3.7**|**3.6**|**3.4**|**2.7**|
+------------+-------+-------+-------+-------+-------+
|Urduhack    |  Yes  |  Yes  |  Yes  |       |       |
+------------+-------+-------+-------+-------+-------+

Install Urduhack via pip
------------------------

.. note::

    Urduhack developed using Tensorflow. Its need Tensorflow cpu for prediction and for development and training the
    models its uses Tensorflow-gpu. following instructions will install Tensorflow

The easiest way to install **urduhack** is by :command:`pip` install.

Installing with Tensorflow **cpu** version.::

    $ pip install Urduhack[tf]

Installing with Tensorflow **gpu** version.::

    $ pip install Urduhack[tf-gpu]




Package Dependencies
--------------------
Having so many functionality, **urduhack** depends on a number of other packages. Try to avoid any kind of conflict.
It is preferred that you create a virtual environment and install *urduhack* in that environment.

* **Tensorflow > 2.0.0** Use for training, evaluating and testing deep neural network model.

* **transformers** Use for bert implementation for training and evaluation.

* **tensorflow-datasets** Use for download and prepare the dataset,read it into a model using the tf.data.Dataset API.

* **Click** With help of this library Urduhack commandline application developed.

Downloading Models
------------------

Pythonic Way
^^^^^^^^^^^^

You can download model using Urduhack code.::

    import urduhack
    urduhack.download()

Command line
^^^^^^^^^^^^

To download the models all you have to do is run this simple command in the command line.::

    $ urduhack download

This command will download the models which will be used by urduhack.