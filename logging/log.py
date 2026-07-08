import logging 


logging.basicConfig(level=logging.INFO, filename = "log.log", filemode="w", 
                    format="%(asctime)s - %(levelname)s - %(message)s")      
# level here means from what level of logging the system will start at in this it will start from INFO till CRITICAL
# the logs will be written to the log.log file and filemode = w means the logs will be overwritten over and over in that file.

logging.debug("debug")

logging.info("info")

logging.warning("warning")

logging.error("error")

logging.critical("critical")

#log a variable

x = 2

logging.info(f" the value of x is {x}")

# log Traceback

try:
    1/0
except ZeroDivisionError as e:
    logging.error("ZeroDivsionError", exc_info=True)

#another way of logging the exception/traceback
try:
    1/0
except ZeroDivisionError as e:
    logging.exception("ZeroDivsionError")


