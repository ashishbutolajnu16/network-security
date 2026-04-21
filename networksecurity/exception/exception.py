import sys

from networksecurity.logging import logger


class NetworkSecurityException(Exception):
    def __init__(self, error_message, error_details: sys):
        self.error_message = error_message
        _,_, exec_tb = error_details.exc_info()

        self.lineno = exec_tb.tb_lineno
        self.file_name = exec_tb.tb_frame.f_code.co_filename
    
    def __str__(self):
        return f"Error occured in python script name {self.file_name} and line no {self.lineno} error message {self.error_message}"
    
# if __name__ == '__main__':
#     try:
#         logger.logging.info("testing the logger")
#         a=1/0
#         print(f"This will not be printed {a}")
#     except Exception as e:
#         raise NetworkSecurityException(e, sys)
