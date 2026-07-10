"""
Demonstrates named loggers with separate handlers.

Using `logging.getLogger(__name__)` instead of `logging.basicConfig()` creates
a named logger tied to this module. This is essential when multiple files import
each other — it lets you tell at a glance which file produced each log entry.

Two handlers are attached:
  - FileHandler  → writes ERROR (and above) logs to 'sample.log'
  - StreamHandler → prints DEBUG (and above) logs to the console
"""

import logging
import students

# --- Logger Setup ---

# Create a named logger for this module (__name__ == '__main__' when run directly).
# Setting the logger level to DEBUG means it will pass all messages to its handlers;
# each handler then applies its own level filter.
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Define a shared log format: timestamp, logger name, and the message.
formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

# FileHandler: only records ERROR and CRITICAL messages to 'sample.log'.
# Lower-severity messages (DEBUG, INFO, WARNING) are silently ignored by this handler.
file_handler = logging.FileHandler('sample.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)

# StreamHandler: prints all messages at DEBUG level and above to the console (stderr).
# No level is set explicitly, so it inherits the logger's level (DEBUG).
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

# Register both handlers with the logger.
logger.addHandler(file_handler)
logger.addHandler(stream_handler)


# --- Functions ---

def area(length, breadth):
    """Return the area of a rectangle given its length and breadth."""
    return length * breadth


def division(a, b):
    """
    Divide a by b and return the result.
    Logs an exception (with full traceback) if b is zero instead of crashing.
    """
    try:
        result = a / b
    except ZeroDivisionError:
        logger.exception('Tried to divide by zero')
    else:
        return result


# --- Main Execution ---

area_of_rect = area(5, 4)
logger.debug(f"Area of rectangle is {area_of_rect}")

num1 = 4
num2 = 0

div_result = division(num1, num2)
logger.debug('Div: {} / {} = {}'.format(num1, num2, div_result))
