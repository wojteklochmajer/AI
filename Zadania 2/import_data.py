import csv
import numpy as np

def load_data(input_data,cut,cut2):
    with open(input_data, newline='') as csvfile:
        data = list(csv.reader(csvfile))
        labels = data[0:cut]
        #print(len(data))
        array_data = np.array(data[cut:cut2], dtype="float").T
        dict={"Xi":array_data[0:-1],"Yi": np.array(array_data[-1].reshape(1,cut2-cut))}

        return labels, dict

def load_data_split(data_source,data_train_end=600,data_test_start=601,data_test_end =700):

    _,data_train = load_data(data_source,2,data_train_end)
    _, data_test = load_data(data_source,data_test_start,data_test_end)
    return data_train, data_test