import logging
encoding='utf-8'

logging.basicConfig(
    level=logging.INFO,
    filename='mylog.log',
    format="%(asctime)s - [%(levelname)s] - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s",
    datefmt='%H:%M:%S',
    encoding = "UTF-8"
)
