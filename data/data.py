import pandas as pd
from get_report_of_data.extraction_information import extraction_information
from generate_date.generate_date import GenerateDate

class data:
    def __init__(self,
                 data : pd.DataFrame,
                 is_save : bool,
                 path_destination : str) -> None:
        self.data = data
        self.is_save = is_save
        self.path_destination = path_destination

        self.report_data = extraction_information() 
        #self.generate_date = GenerateDate() # now we not use it
        # add more feature for this code
        
    def fit(self):
        self._get_report()
    
    
    
    def _get_report(self):
        self.report_data.fit(self.data)
        self.report_data.show_date_and_spectrum()
        
        if self.is_save :
            self.report_data.save_date_and_spectrum(self.path_destination)
            print(f"saved date and spectrums on your directory : {self.path_destination}")
        
        self.report_data.generate_plot(self.path_destination ,self.is_save)
        
        
        
        