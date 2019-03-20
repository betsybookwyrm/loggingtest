import logging
import logging.config
import yaml
from loggingtest.innermodule import innerfunction

logger = logging.getLogger('loggingtest')  # try with both __name__ and 'loggingtest'


logging_config_type = 'dict'  # PICK ONE: 'dict', 'yaml' or 'basic'

# Dictionary logging config
# See https://docs.python.org/3/library/logging.config.html#logging.config.dictConfig
# and https://docs.python.org/3/library/logging.config.html#logging-config-dictschema
# Can be put in a yaml or json file and loaded from there
logging_config_dict = {
    'version': 1,  # Required (1 is only possible value at present)
    'disable_existing_loggers': False,  # Widely recommended, don't entirely understand
    # This is trying to mimic the formatter created by default logging.basicConfig()
    'formatters': {
        'basic': {
            'format': logging.BASIC_FORMAT
        }
    },
    # Should be equivalent to logging.basicConfig(level=logging.DEBUG)
    'handlers': {
        'stream': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'basic'
        }
    },
    'loggers': {
        # Try removing either of these loggers
        # Behaviour defaults to root logger defined at the end if no logger name here
        # matches the logger name in use, logger name matching uses module-style
        # inheritance
        'loggingtest': {
            'level': 'DEBUG',
            'propagate': True
        },
        'external': {
            'level': 'WARNING',
            'propagate': True
        }
    },
    # Some people put this as logger '' in loggers section, but docs example has it here
    'root': {
        'level': 'INFO',
        'handlers': ['stream']
    }
}


def main():
    logger.info('logging test info')
    innerfunction('hi')
    logger.debug('logging test debug')


if __name__ == '__main__':
    if logging_config_type == 'basic':
        logging.basicConfig(level=logging.INFO)

    elif logging_config_type == 'dict':
        logging.config.dictConfig(logging_config_dict)

    elif logging_config_type == 'yaml':
        with open('logging.yaml', 'r') as f:
            logging_config = yaml.safe_load(f.read())
        logging.config.dictConfig(logging_config)

    logger.info('starting up')

    main()

    logger.info('all done!')
