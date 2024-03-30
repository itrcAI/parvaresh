from .tool.generate_plot import generate_plot
from .tool.get_all_date_spectrum import get_all_date_spectrum
from .tool.save_date_spectrum import save_date_spectrum

import pandas as pd



class extraction_information:
    def __init__(self,
                 df : pd.DataFrame) -> None :
        self.df = df
        self.date_spectrum = get_all_date_spectrum(self.df)



    def get_date_and_spectrum(self):
        return self.date_spectrum
    
    def show_date_and_spectrum(self) -> None:
        for day , spectrum in self.date_spectrum.items():
            print(f"day: {day} - spectrum: {spectrum}\n--------------------------------")

    
    def save_date_and_spectrum(self, 
                               path_destination : str) -> None:
        save_date_spectrum(self.date_spectrum, path_destination)
    
    def generate_plot(self,
                      path_destination : str) -> None:
        
        generate_plot(self.df, path_destination)
    
    
        
        
    
    
    
    