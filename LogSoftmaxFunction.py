import numpy as np

# referencia: https://medium.com/@AbhiramiVS/softmax-vs-logsoftmax-eb94254445a2

def log_softmax(scores: list) -> np.ndarray:
    scores = np.array(scores)
    scores_e = np.exp(scores) 
    denom = np.log(np.sum(scores_e))  
    log_softmax_values = scores - denom  # log(a/b), em que a = e^zi e b = e^(z1 + ... + zi). Portanto, z1 - log(sum(e^zj))
    
    return log_softmax_values
	