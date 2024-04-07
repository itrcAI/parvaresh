import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns


from .get_all_date_spectrum import get_all_date_spectrum
from .get_all_spectrum import get_all_spectrum


    
def generate_plot(df : pd.DataFrame,
                  path_destination : str = "None",
                  is_save : bool = True) -> None:
    
    """
    
        This function deals with generating a plot that first calculates the total 
        spectra and tells how many spectra are missing for each day. 
        If a directory is specified, the plot will be saved in that directory; otherwise, 
        it will be saved in the current execution location.
        
    """
    
    
    data = get_all_date_spectrum(df)
    all_spectrum = get_all_spectrum(data)

    

    result = {}
    for day , spectrum in data.items():
        result[day] = len(all_spectrum) - len(spectrum)
            

    plt.figure(figsize = (30 , 10))
    plots = sns.barplot(x = list(result.keys())[-20 : ], y = list(result.values())[-20 : ], color='black')
    plots.set_xticklabels(plots.get_xticklabels(),rotation = 90)
    for bar in plots.patches:
        plots.annotate(format(bar.get_height(), '.0f'),
                        (bar.get_x() + bar.get_width() / 2,
                            bar.get_height()), ha='center', va='center',
                        size=15, xytext=(0, 8),
                        textcoords='offset points')
    
    if is_save:
        
        if path_destination != "None":
            path_destination += "/plot.png"
            plt.savefig(path_destination)
        else:
            plt.savefig("plot.png")
        
        print(f"saved plot for date and spectrums on your directory : {path_destination}")

            

         
