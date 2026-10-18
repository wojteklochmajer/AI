"""
Uczenie maszynowe i sieci neuronowe
Ćwiczenia 1.

Moduł testing
Narzędzia pomocnicze do testowania poprawności kodu źródłowego.
"""

import numpy as np

eps_test = np.power(10., -10)
datawrong = {"xi": np.array([0]), "yi": np.array([0])}
datamismatch = {"xi": np.array([0, 1]), "yi": np.array([0, 1, 2])}
dataempty = {"xi": np.array([]), "yi": np.array([])}
data0 = {"xi": np.array([0, 0]), "yi": np.array([0, 0])}
data1 = {"xi": np.array([1, 2]), "yi": np.array([2, 3])}

def sigma_check(lst, mu, sigma):
    """Maksymalny błąd udziałów próbek w przedziałach 1, 2 i 3 sigma (sigma > 0).

    To przybliżony sprawdzian, a nie pełny test normalności rozkładu.
    """
    if len(lst) == 0 or sigma <= 0 or not np.all(np.isfinite(lst)):
        return np.inf
    onesigma = 0
    twosigma = 0
    threesigma = 0
    for element in lst:
        if abs(element - mu) < sigma:
            onesigma += 1
        if abs(element - mu) < 2 * sigma:
            twosigma += 1
        if abs(element - mu) < 3 * sigma:
            threesigma += 1
    return np.max(np.abs(np.array([
        onesigma / len(lst) - 0.6826894921370859,
        twosigma / len(lst) - 0.9544997361036416,
        threesigma / len(lst) - 0.9973002039367398
    ])))