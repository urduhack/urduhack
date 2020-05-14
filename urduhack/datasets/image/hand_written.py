# coding: utf8
"""hand written dataset"""

import numpy as np
import tensorflow_datasets.public_api as tfds

_CITATION = """
"""

_DESCRIPTION = """
"""

_DOWNLOAD_URL: str = "https://github.com/urduhack/urdu-datasets/releases/download/" \
                     "urdu_handwritten_text_dataset_v1.0.0/uhat_dataset.npz"


class HandWrittenDigits(tfds.core.GeneratorBasedBuilder):
    """hand written Digits"""

    VERSION = tfds.core.Version('1.0.0')

    def _info(self):
        return tfds.core.DatasetInfo(
            builder=self,
            description=_DESCRIPTION,
            features=tfds.features.FeaturesDict({
                "image": tfds.features.Image(),
                "label": tfds.features.ClassLabel(num_classes=10),
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
        labels = urdu_dataset[label]
        data = list(zip(images, labels))
        for index, (image, label) in enumerate(data):
            record = {"image": image, "label": label}
            yield index, record

# builder = HandWrittenDigits()
# dl_config = tfds.download.DownloadConfig(register_checksums=True)
# builder.download_and_prepare(download_config=dl_config)
# dataset = builder.as_dataset()
# dataset = dataset['train']
# sample = dataset.take(1)
# print(sample)
