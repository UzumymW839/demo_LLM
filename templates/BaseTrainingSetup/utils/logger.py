import logging
import logging.config
from pathlib import Path
from utils.json_handling import read_json


def setup_logging(save_dir, log_config="utils/logger_config.json", default_level=logging.INFO):
    """
    Setup logging configuration.
    
    Args:
        save_dir (str or Path): Directory to save the log file.
        log_config (str): Path to the logging configuration file.
        default_level (int): Default logging level.
    """
    log_config = Path(log_config)
    if log_config.is_file():
        config = read_json(log_config)
        # modify logging paths based on run config
        for _, handler in config['handlers'].items():
            if 'filename' in handler:
                handler['filename'] = str(save_dir / handler['filename'])
        logging.config.dictConfig(config)
    else:
        print(f"Warning: Logging configuration file {log_config} not found. Using default logging configuration.")
        logging.basicConfig(level=default_level)