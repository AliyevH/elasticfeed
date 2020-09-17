import logging
import coloredlogs

def dict_data(row, headers):
    """
    Create dict data from list header and row
    """
    data = {}
    for i in range(len(row)):
        data[headers[i]] = row[i]
    return data



def get_logger(log_level="DEBUG"):
    logger = logging.getLogger("elasticfeed")
    colors_config = coloredlogs.DEFAULT_LEVEL_STYLES
    coloredlogs.DEFAULT_LOG_FORMAT = '%(asctime)s %(hostname)s %(name)s %(levelname)s %(message)s'
    colors_config.update(**{'info': {"color": "white","faint":True}})
    logger.setLevel(log_level)
    coloredlogs.install(level=log_level,logger=logger)

    return logger

logger = get_logger("INFO")

