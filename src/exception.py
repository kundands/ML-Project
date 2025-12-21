"""
Purpose:
---------
This module provides a custom exception handling mechanism for the project.

What this code does:
--------------------
1. Captures detailed exception information using sys.exc_info().
2. Extracts the Python file name and line number where the error occurred.
3. Formats a clear, readable error message for debugging and logging.
4. Defines a CustomException class to standardize error handling
   across the entire application.

Why this is useful:
-------------------
- Makes debugging easier by showing exact file and line number.
- Avoids vague error messages during production failures.
- Ensures consistent exception messages across modules.
- Can be easily integrated with logging systems.
"""


import sys
from src.logger import logging

def error_message_detail(error,error_detail:sys):
    # Give all info where and which line an exception has occured
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name,exc_tb.tb_lineno,str(error))
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message= error_message_detail(error_message, error_detail=error_detail)


    def __str__(self):
        return self.error_message
    

