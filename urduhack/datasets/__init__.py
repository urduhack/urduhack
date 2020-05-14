# coding: utf8
"""Datasets Entry point"""
import os

import tensorflow_datasets.public_api as tfds

CHECKSUM_DIR = os.path.join(os.path.dirname(__file__), 'url_checksums/')
CHECKSUM_DIR = os.path.normpath(CHECKSUM_DIR)
tfds.download.add_checksums_dir(CHECKSUM_DIR)
