import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 996494546 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    return max(x), \
           (max(x) - 0.083) / (p**(1/len(x)))+0.083
