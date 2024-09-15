import sys
from src.logger import logging

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
     file_name,exc_tb.tb_lineno,str(error))

    return error_message

    

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    
    def __str__(self):
        return self.error_message
    
# Test function to trigger an exception and log it
def divide_by_zero_test():
    try:
        x = 1 / 0  # This will raise a ZeroDivisionError
    except Exception as e:
        raise CustomException(str(e), sys)


if __name__ == "__main__":
    logging.info("Starting the divide by zero test.")
    divide_by_zero_test()
