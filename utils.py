import pandas as pd

def prepare_data(base_Url):
    end_Url = '?&format=json'
    raw_data = pd.read_json(base_Url+end_Url)
    data = pd.DataFrame()
    for i in range(len(raw_data)):
        series = pd.Series(raw_data.iloc[i][0])
        data[i] = series
    return data.T
