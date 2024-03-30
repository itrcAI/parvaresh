from .tool.generate_date_step_step import generate_date
from .tool.save_json import save_json

class GenerateDate:
    def __init__(self, 
                 info : dict,
                 start_date, 
                 step : int) -> None:
        
        self.iter = len(info.keys())
        self.start_date = start_date
        self.step = step
        
    
    def generate_and_save(self, 
                          path_destination : str = "None"):
        dates = generate_date(self.start_date , self.step, self.iter)
        save_json(dates, self.iter, path_destination)       
        
        
        
    
    
    
        