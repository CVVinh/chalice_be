import logging
import os

LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(os.environ.get('log_level', 'INFO'))
