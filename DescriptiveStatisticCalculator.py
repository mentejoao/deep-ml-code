import numpy as np 

# Write a Python function to calculate various descriptive statistics metrics for a given dataset.
# The function should take a list or NumPy array of numerical values and return a dictionary containing mean,
# median, mode, variance, standard deviation, percentiles (25th, 50th, 75th), and interquartile range (IQR). 

def descriptive_statistics(data):
    mean = np.mean(data)
    variance = np.var(data)
    std_dev = np.std(data)
    
    median = np.median(data)
    mode = np.bincount(data).argmax()  # Para encontrar o valor mais frequente
    percentiles = np.percentile(data, [25, 50, 75])
    iqr = percentiles[2] - percentiles[0]
    
    stats_dict = {
        "mean": mean,
        "median": median,
        "mode": mode,
        "variance": np.round(variance, 4),
        "standard_deviation": np.round(std_dev, 4),
        "25th_percentile": percentiles[0],
        "50th_percentile": percentiles[1],
        "75th_percentile": percentiles[2],
        "interquartile_range": iqr
    }
    
    return stats_dict