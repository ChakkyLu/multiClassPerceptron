from classifier.multiClassPerceptron import MulticlassPerceptron as MulticlassPerceptron
from sklearn.linear_model import Perceptron
from sklearn import datasets
from sklearn.neural_network import MLPClassifier
from process_data.house import generate_data
from process_data.position import GenerateData
import random

if __name__ == "__main__":
    # -----------------iris data--------------------
    iris = datasets.load_iris()
    X = iris.data[:, :5]
    y = iris.target
    iris_class = iris.target_names
    o = [i for i in range(len(X))]
    random.shuffle(o)
    ratio = 0.7
    ol = int(len(o)*ratio)

    X_train = [X[i] for i in o[:ol]]
    X_test = [X[i] for i in o[ol:]]
    y_train = [y[i] for i in o[:ol]]
    y_test = [y[i] for i in o[ol:]]

    errors = 0
    print("=======skit-learn==========")
    model = Perceptron(max_iter=50)
    model.fit(X_train, y_train)
    predicted = model.predict(X_test)

    for i in range(len(predicted)):
        if predicted[i] != y_test[i]:
            errors += 1
    print("accuracy:", str(1 - errors*1.0/len(predicted)))

    print("=========My Model==========")
    y = [iris_class[i] for i in y]
    y_train = [y[i] for i in o[:ol]]
    y_test = [y[i] for i in o[ol:]]
    iris_model = MulticlassPerceptron(epoch=50, early_stopping=True)
    iris_model.fit(X_train, y_train, iris_class)
    iris_model.model_analysis(X_test, y_test)
    # --------------------end---------------------

    # ------------------------plot iris data----------------------
    # x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
    # y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5
    # plt.figure(2, figsize=(8, 6))
    # plt.clf()
    #
    # # Plot the training points
    #
    # plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Set1,
    #         edgecolor='k')
    #
    # plt.xlabel('Sepal length')
    # plt.ylabel('Sepal width')
    #
    # plt.xlim(x_min, x_max)
    # plt.ylim(y_min, y_max)
    # plt.xticks(())
    # plt.yticks(())
    #
    # plt.savefig('result.png')
    # ---------------------------------------------------------


    # ----------------house data-------------------
    m, o, n, p = generate_data()
    print(len(n))
    print(len(p))
    ratio = 0.7
    i, j, ii, jj = [], [], [], []
    random.shuffle(o)
    lens = int(len(o)*ratio)
    X_train = [t[1] for t in o[:lens]]
    y_train = [t[0] for t in o[:lens]]
    X_test = [t[1] for t in o[lens:]]
    y_test = [t[0] for t in o[lens:]]
    print("=========My Model=============")
    model = MulticlassPerceptron(epoch=50, early_stopping=True)
    model.fit(X_train, y_train, m)
    model.model_analysis(X_test, y_test)

    print("=======skit-learn==========")
    model = Perceptron(max_iter=50)
    model.fit(X_train, y_train)
    predicted = model.predict(X_test)
    errors = 0

    for i in range(len(predicted)):
        if predicted[i] != y_test[i]:
            errors += 1
    print("accuracy:", str(1 - errors*1.0/len(predicted)))
    # # ---------------------------------------------
    #
    #
    # # -----------------position data------------------
    # m, mac_list, X_train, y_train, X_test, y_test = GenerateData()
    # m, X_train, y_train = GenerateData()
    # model = MulticlassPerceptron(epoch=100, early_stopping=True)
    # y_train = [str(k) for k in y_train]
    # print(X_train)
    # print(y_train)
    # print("========My model===========")
    # model.fit(X_train, y_train, m)
    # model.model_analysis(X_train, y_train)
    #
    # print("=======skit-learn==========")
    # model = Perceptron(max_iter=50)
    # model.fit(X_train, y_train)
    # predicted = model.predict(X_train)
    # errors = 0
    #
    # for i in range(len(predicted)):
    #     if predicted[i] != y_train[i]:
    #         errors += 1
    # print("accuracy:", str(1 - errors * 1.0 / len(predicted)))
    # # ------------------------------------------------
    #
    #
