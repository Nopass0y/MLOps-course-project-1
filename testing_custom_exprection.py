from src.customer_exception import CustomerException
from src.logger import get_logger
import sys

logger = get_logger("__name__")

def division(a,b):
    try:
        result = a/b 
        logger.info("Divisding Two Numbers")
        return result
    except Exception as e:
        logger.error("Error occured")
        raise CustomerException("Custom Error Zero", sys)

if __name__ == "__main__" :
    try : 
        logger.info("Stating main program")
        division(10,2)
    except CustomerException as ce :
        logger.error(str(ce))
