import sys
import logging
class Krishmitra(Exception):
    """
    
    A custom exception class for handling project related errors.
    """
    def __init__(self,error_message,error_details:sys):
        super().__init__(error_message)
        self.error_message = error_message
        _,_,exc_tb = error_details.exc_info()
        self.lineno = exc_tb.tb_lineno
        self.filename = exc_tb.tb_frame.f_code.co_filename
    
    def __str__(self):
        return "error occured in python scriptname [{0}] at line number [{1}] error message [{2}]".format(
            self.filename,
            self.lineno,
            str(self.error_message)
        )


if __name__ == "__main__":
    try:
        a = 1/0
    except Exception as e:
        logging.error("divide by zero error")
        raise Krishmitra(e,sys)


    