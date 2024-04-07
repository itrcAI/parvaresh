import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json

from .find_date_spectrum import find_date_spectrum 


def get_all_date_spectrum(df : pd.DataFrame) -> dict:

    """
    
        In this function, we separate all the days and return a text file 
        indicating which spectra are available for each day. 
 
    """
    
    
    with open('stopwords.json', 'r') as file:
        stopwords_data = json.load(file)

    stopwords = stopwords_data['stopwords']


    columns = list(df.columns)
    columns = [col for col in columns if col not in stopwords]

    print(columns)
    columns = list(map(find_date_spectrum, columns))
    info = dict()
    for information in columns:
        day , spectrum = int(information[0]) , information[1]
        if day in info:
            info[day].add(spectrum)
        elif day not in info:
            info[day] = set()
            info[day].add(spectrum)
            
    info = dict(sorted(info.items(), key=lambda item : item[0]))
    return info
    
    

                


            

