datasets
============
This modules enables urduhack to utilize different datasets. To utilize a dataset, we will instantiate that dataset class
and download the dataset. All the dataset classes are based on `tensorflow-datasets <https://github.com/tensorflow/datasets>`_ framework.
For example to utilize IMDB Urdu Movie Reviews dataset, we will use the :py:class:`~urduhack.datasets.text.imdb_urdu.ImdbUrduReviews` class.::

    >>>from urduhack.datasets.text.imdb_urdu import ImdbUrduReviews
    >>>builder = ImdbUrduReviews()
    >>>builder.download_and_prepare()
    >>>dataset = builder.as_dataset()
    >>>dataset = dataset['train']
    >>>sample = dataset.take(1)
    >>>print(sample)
    <TakeDataset shapes: {review: (), sentiment: ()}, types: {review: tf.string, sentiment: tf.int64}>
