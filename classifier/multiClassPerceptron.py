import pickle
import random
from math import floor
import copy
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt


class MulticlassPerceptron():
    def __init__(self, BIAS=1, epoch=30, lr=0.1, early_stopping=False):
        self.BIAS = BIAS
        self.epoch = epoch
        self.lr = lr
        self.early_stopping = early_stopping

    def fit(self, X, y, classes):
        #---------training the model-------------
            # classes: the kind of class
            # X: training data without label
            # y: label of training data
        #--------------------------------------
        self.classes = classes
        self.weights = {c: np.array([0.0 for _ in range(len(X[0])+1)]) for c in self.classes}
        self.cost = []
        for j in range(self.epoch):
            cost = 0
            for i in range(len(X)):
                if isinstance(X[i], list):
                    x_ = X[i].copy()
                    x_.append(self.BIAS)
                    x_ = np.array(x_)
                else:
                    x_ = np.append(X[i], [self.BIAS])
                arg_max, yp = 0, self.classes[0]
                y_ = y[i]
                for c in self.classes:
                    current_activation = np.dot(x_, self.weights[c])
                    if current_activation >= arg_max:
                        arg_max, yp = current_activation, c
                if not (y_ == yp):
                    self.weights[y_] += x_*self.lr
                    self.weights[yp] -= x_*self.lr
            for i in range(len(X)):
                y_ = y[i]
                if self.predict(X[i]) != y_:
                    cost += 1
            self.cost.append(1*(cost==0))
            print("====epoch %d, cost %s====" % (j, str(cost*1.0/len(X))))
            if self.early_stopping and sum(self.cost)>=5:
                break

    def predict(self, X_):
        if isinstance(X_, list):
            X = X_.copy()
            X.append(self.BIAS)
            X = np.array(X)
        else:
            X = np.append(X_, [0])
        arg_max, predicted_class = 0, self.classes[0]
        for c in self.classes:
            current_activation = np.dot(X, self.weights[c])
            if current_activation >= arg_max:
                arg_max, predicted_class = current_activation, c
        return predicted_class

    def model_analysis(self, testData, testLabel):
        """
        Calculates the accuracy of the classifier by running algorithm against test set and comparing
        the output to the actual categorization.
        """
        correct, incorrect = 0, 0
        for i in range(len(testData)):
            actual_class = testLabel[i]
            predicted_class = self.predict(testData[i])
            if actual_class == predicted_class:
                correct += 1
            else:
                incorrect += 1
        print("ACCURACY:")
        print("Model Accuracy:", (correct * 1.0) / ((correct + incorrect) * 1.0))
