

def find_date_spectrum(text : str) -> list:
    
    
    """
    
        The column names in our dataset are in the format : 
        (Number_of_day)_(spectrum), 
        where these two components are separated by an underscore. 
        Therefore, we split these two and return them as separate items in a list.    
        
    """
    
    index = None
    for index_temp ,char in enumerate(text):
        if char == "_":
            index = index_temp
            break
        
    return [text[ : index] , text[index + 1: ]]
                