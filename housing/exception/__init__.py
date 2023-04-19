import os
import sys

class HousingException(Exception):

    def __init__(self, error_message:Exception, error_detail:sys):
        super().__init__(error_message) 
        # Make available the Exception object to parent class HousingException
        #Above line is Equivalemt to below code
        #Exception(error_message)

        self.error_messgae=HousingException.get_detailed_error_message(error_message=error_message,
                                                                        error_detail=error_detail   
                                                                                               )

    @staticmethod
    def get_detailed_error_message(error_message:Exception, error_detail:sys)->str:
        """
        error_messgae: Exception object
        errro_detail: object of sys module
        """
        _,_, exec_tb = error_detail.exc_info()
        line_number= exec_tb.tb_frame.f_lineno
        file_name= exec_tb.tb_frame.f_code.co_filename

        error_message = f"Unexpected Error in file: [{file_name}] at line number: [{line_number}]"
        return error_message
    
    def __str__(self):
        return self.error_message # Info to be made available upon printing class object is essential

    def __repr__(self)->str:
        return HousingException.__name__.str()

