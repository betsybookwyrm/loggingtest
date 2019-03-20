import logging
from external import fn

logger = logging.getLogger(__name__)


def innerfunction(input):
    logger.info('inner function doing a thing info')
    fn(input)
    logger.debug('inner function all done debug')
