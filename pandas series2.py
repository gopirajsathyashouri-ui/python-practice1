import pandas as pd 

def analyze_weights(weights):
    weight_series = pd.Series(weights)
    max_weights = weight_series.max()
    min_weights = weight_series.min()

    print(max_weights)
    print(min_weights)

weights = eval(input())
analyze_weights(weights)
