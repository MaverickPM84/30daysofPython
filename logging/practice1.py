import logging

logging.basicConfig(filename="add.log", level=logging.INFO, format='%(asctime)s:%(filename)s:%(lineno)d:%(message)s')

def add(a,b):
    return a + b
    


result = add(4, 3)

logging.info(result)
