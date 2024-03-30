
def get_all_spectrum(data : dict) -> list:
    
    """
    
        In this function, we retrieve all spectra.
    
    """
    result = list()
    for _, spectrum in data.items():
        result.extend(list(spectrum))
    return list(set(result))