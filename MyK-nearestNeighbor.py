import numpy as np
import panda as pd

def manhattanDistance(a,b):
    distance = np.sum(np.abs(a-b))
    return distance
def euclideanDistance(a,b):
    distance = np.sqrt(np.sum((a-b)**2))
    return distance



def predictOne(x_train, y, input, k):
    #implement distances from input to every other datapoint
    for x in x_train:
        distances
    return label



train=pd.read_csv("data/optics/opt.trn")
test=pd.read_csv("data/optics/opt.tst")