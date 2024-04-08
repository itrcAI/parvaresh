import numpy as np
import pandas as pd
import os

from tool.extract_date_and_spectrum import extract_date_and_spectrum
from tool.get_all_spectrum import get_all_spectrum
from tool.get_all_day import get_all_day
from tool.create_folder import create_folder

class convert_data:
    def __init__(self,
                 df : pd.DataFrame, 
                 class_column : str,
                 start_date : str,
                 geomfeat_columns : tuple,
                 path : str) -> None:
        
        self.df = df
        self.class_column = class_column
        self.start_date = start_date
        self.geomfeat_column = geomfeat_columns
        self.folder_path_data , self.folder_path_META = create_folder(path)
        
        self.date_and_spectrum = extract_date_and_spectrum(df)
        self.all_spectrum = get_all_spectrum(self.date_and_spectrum)
        self.all_day = get_all_day(self.date_and_spectrum)
        
        
    def fit(self) -> np.array:
        for index in range(self.df.shape[0]):
            vector = list()
            for day in self.all_day:
                spectrum_vector = self._create_vector_spectrum()
                vector_day = self._make_vector_day(index, day, spectrum_vector)
                vector.append(vector_day)
                print(f"{index} --> {day}")
            vector = np.array(vector)
            path =  self.folder_path_data + f"/{index}.npy"
            np.save(path, vector)
                    
    def _make_vector_day(self, 
                        index : int,
                        day : int,
                        spectrum_vector : dict) -> np.array:
        for spectrum in spectrum_vector:
            if spectrum in self.date_and_spectrum[day]:
                column = f"{day}_{spectrum}"
                spectrum_vector[spectrum] = self.df.iloc[index][column]

        return np.array(
                        list(spectrum_vector.values())
                           )
                
            
        
    def _create_vector_spectrum(self) -> dict:
        return {spectrum: np.nan for spectrum in self.all_spectrum}

    
    def _create_folder(self, 
                       path : str) -> None:
        
        os.makedirs(path, exist_ok=True)
        folder_path_root = os.path.abspath(path)
        
        self.folder_path_data =  folder_path_root = "/data"
        os.makedirs(self.folder_path_data, exist_ok=True)

        self.folder_path_META =  folder_path_root = "/META"
        os.makedirs(self.folder_path_META, exist_ok=True)
        
df = pd.read_excel("/home/reza/Desktop/data sets/BAHAR_DATA_S1_S2_0301_0630.xlsx")

model = convert_data(df, 
                 class_column = None,
                 start_date = None,
                 geomfeat_columns = None,
                 path = "/home/reza/Desktop/output")

model.fit()