import numpy as np

eps_test = np.power(10., -10)
eps_test2 = np.power(10., -6)
dim_test = 10
datawrong = {"xi": np.array([0]), "yi": np.array([0])}
data0 = {"xi": np.array([0, 0]), "yi": np.array([0, 0])}
data1 = {"xi": np.array([1, 2]), "yi": np.array([2, 3])}

params_test = np.array([[ 0.01788628,  0.0043651],
 [ 0.00096497, -0.01863493],
 [-0.00277388, -0.00354759],
 [-0.00082741, -0.00627001]])

grads_test = {"dW": np.array( [[0.99669649],
       [2.38962755]]), "db":0.002179331440145519}
cost_test  = 4.603273926562363
optimize_A_test = np.array([[0.19033591],
 [0.12259159]])
optimize_b_test = 1.9253598300845747
optimize_dA_test = np.array([[0.67752042],
 [1.41625495]])
optimize_db_test = 0.21919450454067657


def sigma_check(lst, mu, sigma):
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
    return sum(np.array([round(onesigma / len(lst), 3) - 0.693, round(twosigma / len(lst), 3) - 0.958,
                         round(threesigma / len(lst), 3) - 0.997]))
