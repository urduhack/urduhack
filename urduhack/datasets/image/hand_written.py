# coding: utf8
"""hand written dataset"""

import numpy as np
import tensorflow_datasets.public_api as tfds

_CITATION = """
"""

_DESCRIPTION = """
"""

_DOWNLOAD_URL: str = "https://github.com/urduhack/resources/releases/download/" \
                     "urdu_handwritten_text_dataset_v1.0.0/uhat_dataset.npz"
_IMAGE_SIZE = 28
_IMAGE_SHAPE = (_IMAGE_SIZE, _IMAGE_SIZE, 1)
_NUM_CLASSES = 10
_TRAIN_EXAMPLES = 60000
_TEST_EXAMPLES = 10000


class HandWrittenDigits(tfds.core.GeneratorBasedBuilder):
    """hand written Digits"""

    VERSION = tfds.core.Version('1.0.0')

    def _info(self):
        return tfds.core.DatasetInfo(
            builder=self,
            description=_DESCRIPTION,
            features=tfds.features.FeaturesDict({
                "image": tfds.features.Image(shape=_IMAGE_SHAPE),
                "label": tfds.features.ClassLabel(num_classes=_NUM_CLASSES),
            }),
            supervised_keys=("image", "label"),
            homepage='https://www.kaggle.com/hazrat/uhat-urdu-handwritten-text-dataset',
            citation=_CITATION,
        )

    def _split_generators(self, dl_manager):
        """Returns SplitGenerators."""
        file = dl_manager.download(_DOWNLOAD_URL)

        return [
            tfds.core.SplitGenerator(
                name=tfds.Split.TRAIN,
                gen_kwargs={'file_path': file, 'image': "x_digits_train", "label": "y_digits_train"}
            ),
            tfds.core.SplitGenerator(
                name=tfds.Split.TEST,
                gen_kwargs={'file_path': file, 'image': "x_digits_test", "label": "y_digits_test"}
            ),
        ]

    def _generate_examples(self, file_path, image, label):
        """Yields examples."""
        urdu_dataset = np.load(file_path)
        images = urdu_dataset[image]
        images = np.expand_dims(images, axis=-1)
        labels = urdu_dataset[label]
        data = list(zip(images, labels))
        for index, (img, value) in enumerate(data):
            record = {"image": img, "label": value}
            yield index, record
