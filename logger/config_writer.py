from utils_json import *

data = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'train_formatter': {
            'class': 'logging.Formatter',
            'format': '%(asctime)s - %(name)s - %(levelname)s: %(message)s'
        },

        'model_info_formatter': {
            'class': 'logging.Formatter',
            'format': '%(levelname)s: %(message)s'
        }
    },

    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'train_formatter'
        },

        'train_file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'INFO',
            'formatter': 'train_formatter',
            "filename": "train.log"
        },

        'model_info_file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'INFO',
            'formatter': 'train_formatter',
            'filename': 'model_info.log'
        }
    },

    "loggers": {
        "console_loggers": {
            'handlers': ['console'],
            'level': "INFO",
            "propagate": False
        },

        "console_debug_loggers": {
            'handlers': ['console'],
            'level': "DEBUG",
            "propagate": False
        },

        "train_file_loggers": {
            'handlers': ['train_file'],
            'level': "INFO",
            "propagate": False
        },

        'model_file_loggers': {
            'handlers': ['model_info_file'],
            'level': 'INFO',
            'propagate': False
        }
    }
}

if __name__ == '__main__':
    data = write_json('log_config.json', data, indent=4)