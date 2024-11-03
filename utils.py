import pandas as pd

def reasons_of_player_absences(data):
    """
    This function takes a dataframe and returns a dataframe with the reasons of player absences.
    """
    
    column_name = data.columns[0]
    
    data = data[column_name].str.split('-', expand=True)
    
    return data
    