import logging

import employee

# TYPES OF LOGGINGS:
# 1. DEBUG: Detailed information, typically of interest only when diagnosing problems.

# 2. INFO: Confirmation that things are working as expected.

# 3. WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.

# 4. ERROR: Due to a more serious problem, the software has not been able to perform some function.

# 5. CRITICAL: A serious error, indicating that the program itself may be unable to continue running.

# logging.basicConfig(filename='test.log', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')
# ## It will save the logs in a file "test.log"
# ## By using the format we can actually change the format of log


##advanced
logger = logging.getLogger(__name__)

logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('sample.log')

file_handler.setFormatter(formatter)
file_handler.setLevel(logging.ERROR)
logger.addHandler(file_handler)



def add(x, y):
    """Add Function"""
    return x + y


def subtract(x, y):
    """Subtract Function"""
    return x - y


def multiply(x, y):
    """Multiply Function"""
    return x * y


def divide(x, y):
    """Divide Function"""
    try:
        result = x/y
    except ZeroDivisionError:
        # logger.error('Tried to devide by 0')
        logger.exception('Tried to devide by 0')
    else:
        return result


num_1 = 20
num_2 = 0

# add_result = add(num_1, num_2)
# # print('Add: {} + {} = {}'.format(num_1, num_2, add_result))
# # for debug
# logging.debug('Add: {} + {} = {}'.format(num_1, num_2, add_result))

# sub_result = subtract(num_1, num_2)
# # print('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))
# #for debug
# logging.debug('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))

# mul_result = multiply(num_1, num_2)
# # print('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))
# # for debug
# logging.debug('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))

# div_result = divide(num_1, num_2)
# # print('Div: {} / {} = {}'.format(num_1, num_2, div_result))
# # for debug
# logging.debug('Div: {} / {} = {}'.format(num_1, num_2, div_result))


# advanced

add_result = add(num_1, num_2)
# print('Add: {} + {} = {}'.format(num_1, num_2, add_result))
# for debug
logger.debug('Add: {} + {} = {}'.format(num_1, num_2, add_result))

sub_result = subtract(num_1, num_2)
# print('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))
#for debug
logger.debug('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))

mul_result = multiply(num_1, num_2)
# print('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))
# for debug
logger.debug('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))

div_result = divide(num_1, num_2)
# print('Div: {} / {} = {}'.format(num_1, num_2, div_result))
# for debug
logger.debug('Div: {} / {} = {}'.format(num_1, num_2, div_result))