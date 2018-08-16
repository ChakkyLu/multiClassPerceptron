import math
import socket
from test import getFUllInfo,GenTrainSet,getTestData
from classifier.multiClassPerceptron import MulticlassPerceptron as MultiClassPerceptron
from feature_data.position_example import GenerateData
from sklearn.externals import joblib
from sklearn.ensemble import RandomForestRegressor
import numpy as np

HOST = socket.gethostbyname(socket.gethostname())
PORT = 3674
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1)
filename = "original_data.txt"
fw = open(filename, 'a+')
flag = 1
# position_classifier = MultiClassPerceptron.load_classifier("position_classifier")
count = 0

'''
    flag = 0: Train Mode
    flag = 1: Test Mode
'''

GenTrainSet(filename)
position_classes, mac_list, TrainSet = GenerateData()
position_classifier = MultiClassPerceptron(position_classes, mac_list, TrainSet, 1.0, 20)
position_classifier.train()
# position_classifier.save_classifier("position_classifier")

while 1:
    conn, addr = s.accept()
    while 1:
        if count==0:
            print("Server catched client")
            count += 1

        data = conn.recv(50048)

        if data == "-1":
            flag = 1
            GenTrainSet(filename)
            position_classes, mac_list, TrainSet = GenerateData()
            position_classifier = MultiClassPerceptron(position_classes, mac_list, TrainSet)
            position_classifier.train()
            position_classifier.save_classifier("position_classifier")
            p_d = joblib.load("TrainSet.dat")
            rf = RandomForestRegressor()
            rf.fit(p_d['data'], p_d['target'])  # 进行模型的训练

        if data and flag == 0:
            data = str(data, encoding='utf-8')
            print("data " + data)
            fw.write(data)
            if data[-1] == "#":
                fw.write("\r\n")

        if data and flag == 1:
            test_data = str(data, encoding='utf-8')
            test_data, test_data4rf = getTestData(test_data)
            print(test_data)
            predict_p = position_classifier.predict(test_data)
            # b2 = bytes(predict_p+"\n", encoding='utf8')
            # conn.send(b2)
            print("Perceptron prediction: " + predict_p)
            # h = np.array([test_data4rf])
            # print("randomforest prediction: " + rf.predict(h))

        # if data and flag==0:
        #     data = str(data, encoding='utf-8')
        #     print("data " + data)
        #     fw.write(data)
        #     if data[-1] == "#":
        #         fw.write("\r\n")

conn.close()

