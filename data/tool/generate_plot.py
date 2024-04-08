from get_all_spectrum import get_all_spectrum
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

def generate_plot(date_and_spectrum : dict) -> None:
    
    all_spectrum = get_all_spectrum(date_and_spectrum)
    
    result = {}
    for day , spectrum in date_and_spectrum.items():
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
    

        
    if path_destination != "None":
        path_destination += "/plot.png"
    else:
        plt.savefig("plot.png")
        
    print(f"saved plot for date and spectrums on your directory : {path_destination}")