import logging

def setup_logger() -> logging.Logger:
    """
    Sets up and configures the logger for the application

    Returns:
        logging.Logger: Configured logger object.
    """
    
    # Create a logger
    logger = logging.getLogger('gta_sa_trainer')
    logger.setLevel(logging.INFO)

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)

    logger.addHandler(ch)

    return logger

