# coding: utf8
"""
Base classes for parser
"""

from abc import ABC, abstractmethod


class Parser(ABC):
    """ Base class for all parsers"""

    def __init__(self, config, pipeline):
        """setup"""
        # overall config for the processor
        self._config = None
        # pipeline building this processor (presently parsers are only meant to exist in one pipeline)
        self._pipeline = pipeline
        # UD model resources, set up is processor specific
        self._pretrain = None
        self._trainer = None
        self._vocab = None
        self._set_up(config)
        # run set up process
        # build the final config for the processor
        self._set_up_final_config(config)

    @abstractmethod
    def parse(self, document):
        """ Process a Document.  This is the main method of a processor. """

    @abstractmethod
    def _set_up(self, config):
        """model setup"""

    @property
    def config(self):
        """ Configurations for the processor """
        return self._config

    @property
    def pipeline(self):
        """ The pipeline that this processor belongs to """
        return self._pipeline

    def _set_up_final_config(self, config):
        """ Finalize the configurations for this processor, based off of values from a UD model. """
        self._config = config
