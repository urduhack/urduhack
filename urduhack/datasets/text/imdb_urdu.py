# coding: utf8
"""Imdb 50k movies Urdu reviews datasets"""

import csv
import os

import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """\
@InProceedings{maas-EtAl:2011:ACL-HLT2011,
  author    = {Maas, Andrew L. and Daly,nRaymond E. and Pham, Peter T. and Huang, Dan and Ng, Andrew Y...},
  title     = {Learning Word Vectors for Sentiment Analysis},
  month     = {June},
  year      = {2011},
  address   = {Portland, Oregon, USA},
  publisher = {Association for Computational Linguistics},
  pages     = {142--150},
  url       = {http://www.aclweb.org/anthology/P11-1015}
}
"""

_DESCRIPTION = """\
Large Movie translated Urdu Reviews Dataset.
This is a dataset for binary sentiment classification containing substantially more data than previous\
benchmark datasets. We provide a set of 40,000 highly polar movie reviews for training, and 10,000 for testing.\
To increase the availability of sentiment analysis dataset for a low recourse language like Urdu,\
we opted to use the already available IMDB Dataset. we have translated this dataset using google translator.\
This is a binary classification dataset having two classes as positive and negative.\
The reason behind using this dataset is high polarity for each class.\
It contains 50k samples equally divided in two classes.\
"""

_DOWNLOAD_URL: str = "https://github.com/urduhack/urdu-datasets/releases/download/" \
                     "imdb_urdu_reviews_v1.0.0/imdb_urdu_reviews.zip"

CHECKSUM_DIR = os.path.join(os.path.dirname(__file__), '..', 'url_checksums/')
CHECKSUM_DIR = os.path.normpath(CHECKSUM_DIR)
tfds.download.add_checksums_dir(CHECKSUM_DIR)


class ImdbUrdu(tfds.core.GeneratorBasedBuilder):
    """IMDB movie Urdu reviews dataset."""

    VERSION = tfds.core.Version('1.0.0')

    def _info(self):
        return tfds.core.DatasetInfo(
            builder=self,
            description=_DESCRIPTION,
            features=tfds.features.FeaturesDict({
                'review': tfds.features.Text(),
                'sentiment': tfds.features.ClassLabel(names=["positive", "negative"])
            }),
            supervised_keys=('review', 'sentiment'),
            homepage='https://www.kaggle.com/akkefa/imdb-dataset-of-50k-movie-translated-urdu-reviews',
            citation=_CITATION,
        )

    def _split_generators(self, dl_manager):
        """Returns SplitGenerators."""
        folder_path = dl_manager.download_and_extract(_DOWNLOAD_URL)
        train_file = os.path.join(folder_path, "imdb_urdu_reviews", "imdb_urdu_reviews_train.csv")
        test_file = os.path.join(folder_path, "imdb_urdu_reviews", "imdb_urdu_reviews_test.csv")

        return [
            tfds.core.SplitGenerator(
                name=tfds.Split.TRAIN,
                gen_kwargs={'file_path': train_file}
            ),
            tfds.core.SplitGenerator(
                name=tfds.Split.TEST,
                gen_kwargs={'file_path': test_file}
            ),
        ]

    def _generate_examples(self, file_path):
        """Yields examples."""

        with tf.io.gfile.GFile(file_path) as file:
            reader = csv.DictReader(file)
            for index, row in enumerate(reader):
                yield index, {
                    "sentiment": row['sentiment'],
                    "review": row['review']
                }
