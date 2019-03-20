import logging


logger = logging.getLogger(__name__)


def fn(input):
    logger.info('external thing info')
    logger.warning('external thing warning')
    logger.debug('external thing debug')
