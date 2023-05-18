
import statistics 
import turtle  
import sys 

from util_datafun_logger import setup_logger
logger, logname = setup_logger(__file__)

# Descriptive: Univariant Data..................................
# univariant data (one varabile, many readings)
page_count_data = [
    33,
    172,
    263,
    436,
    90,
    523,
    244,
    345,
    190,
    222
]
logger.info("page_count_data = " + str(page_count_data))

# Descriptive: Averages and measures of central tendency
mean = statistics.mean(page_count_data)
median = statistics.median(page_count_data)
mode = statistics.mode(page_count_data)

# Descriptive: Measures of spread
var = statistics.variance(page_count_data)
stdev = statistics.stdev(page_count_data)
lowest = min(page_count_data)
highest = max(page_count_data)
