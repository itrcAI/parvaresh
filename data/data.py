import pandas as pd
from get_report_of_data.extraction_information import extraction_information
from generate_date.generate_date import GenerateDate

class data:
    def __init__(self, data : pd.DataFrame) -> None:
        self.data = data
        self.report_data = extraction_information() 
        self.generate_date = GenerateDate
        # add more feature for this code
        
    def fit(self):
        pass
