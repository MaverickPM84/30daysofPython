# --- Logger Setup ---

# Create a named logger for this module (__name__ == '__main__' when run directly).
# Setting the logger level to DEBUG means it will pass all messages to its handlers;
# each handler then applies its own level filter.

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Define a shared log format: timestamp, logger name, and the message.
formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')

# FileHandler: only records ERROR and CRITICAL messages to 'sample.log'.
# Lower-severity messages (DEBUG, INFO, WARNING) are silently ignored by this handler.
file_handler = logging.FileHandler('students.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)


# Register both handlers with the logger.
logger.addHandler(file_handler)


class Student:

    def __init__(self, name, grade):

        self.name = name
        self.grade = grade

        logger.info(f"Student Created: {self.name} , {self.grade}")


student1 = Student("Anika", 9)
student2 = Student("Aditya", 5)