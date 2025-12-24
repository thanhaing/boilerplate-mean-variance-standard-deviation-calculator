import numpy.typing as npt
import numpy as np
import matplotlib.pyplot as plt

def calculate(arr: npt.NDArray[np.int8]): #: npt.NDArray[np.float64]):
    if np.array(arr).shape != (9,):
        raise ValueError("List must contain nine numbers.")

    matrix = np.array(arr, copy=True).reshape((3, 3))
    result = {    
      'mean': [np.mean(matrix,axis=0).tolist(),np.mean(matrix,axis=1).tolist(),np.mean(matrix.flatten()).item()],
      'variance': [np.var(matrix,axis=0).tolist(),np.var(matrix,axis=1).tolist(),np.var(matrix.flatten()).item()],
      'standard deviation': [np.std(matrix,axis=0).tolist(),np.std(matrix,axis=1).tolist(),np.std(matrix.flatten()).item()],
      'max': [np.max(matrix,axis=0).tolist(),np.max(matrix,axis=1).tolist(),np.max(matrix.flatten()).item()],
      'min': [np.min(matrix,axis=0).tolist(),np.min(matrix,axis=1).tolist(),np.min(matrix.flatten()).item()],
      'sum': [np.sum(matrix,axis=0).tolist(),np.sum(matrix,axis=1).tolist(),np.sum(matrix.flatten()).item()],
    }

    return result
