import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.externals import joblib
from process_data.position import GenerateData


def getFUllInfo(data):
    FullData = data.split("$")
    label = FullData[-1].split('#')[0]
    FullData = FullData[0:-1]
    dict = {}
    for fulldata in FullData:
        fulldata = fulldata.split("%")
        if len(fulldata) > 1:
            dict[fulldata[0]] = fulldata[1]
    return dict, label


def GenTrainSet(filename):
    fr = open(filename)
    dicts, labels = [], []
    standard_dict = []
    fw = open("standard_mac.csv", "w")
    fw_pd = open('position_data.txt', 'w')

    for line in fr.readlines():
        line = line.strip()
        dict, label = getFUllInfo(line)
        dicts.append(dict)
        labels.append(label)

    for ssid in dicts[0]:
        a = 1
        for i in range(1, len(dicts)):
            if ssid not in dicts[i]:
                a = 0
                break
        if a == 1:
            standard_dict.append(ssid)

    Trainset = []
    Trainset_val = []

    for i in range(len(dicts)):
        dict = {}
        for ssid in standard_dict:
            dict[ssid] = int(dicts[i][ssid])
        Trainset.append((labels[i], dict))
        Trainset_val.append(list(dict.values()))

    ssids_bar = [[int(row[ssid]) for row in dicts] for ssid in standard_dict]

    ssids_bar_dict = {}

    for i in range(len(standard_dict)):
        ssid = standard_dict[i]
        ssids_bar_dict[ssid] = int(sum(ssids_bar[i]) / len(ssids_bar[i]))
        fw.write(ssid + "," + str(ssids_bar_dict[ssid]) + "\n")

    position_data = {}
    position_data['data'] = np.array(Trainset_val)
    position_data['target'] = np.array(labels, dtype=int)
    position_data['target_names'] = np.array(labels)
    position_data['feature_names'] = standard_dict
    joblib.dump(position_data, 'TrainSet.dat')
    fw_pd.write(str(Trainset))

    fw.close()
    fw_pd.close()


def getTestData(test_data):
    fr = open("standard_mac.csv")
    standard_dict = []
    ssids_bar_dict = {}
    test_data_val = []

    for line in fr.readlines():
        line = line.strip().split(',')
        ssid = line[0]
        ssid_bar = int(line[1])
        standard_dict.append(line[0])
        ssids_bar_dict[ssid] = ssid_bar

    test_dict, b = getFUllInfo(test_data)
    dict = {}

    for ssid in standard_dict:
        if ssid in test_dict:
            dict[ssid] = int(test_dict[ssid])
            test_data_val.append(int(test_dict[ssid]))
        else:
            dict[ssid] = ssids_bar_dict[ssid]
            test_data_val.append(dict[ssid])

    test_data_val = test_data_val

    return dict, test_data_val


if __name__ == "__main__":
    test_data = "00:f6:63:0e:61:ae%-63$cc:16:7e:b6:80:ce%-70$00:f6:63:0e:61:a1%-46$00:c8:8b:13:f7:fe%-80$00:c8:8b:13:f7:f1%-66$cc:16:7e:b6:80:c1%-63$70:db:98:7a:f2:11%-75$70:db:98:7a:f2:1e%-86$00:f6:63:0e:61:ab%-49$cc:16:7e:b6:80:cf%-69$cc:16:7e:b6:80:cb%-69$cc:16:7e:b6:80:ca%-69$00:f6:63:0e:61:a5%-52$00:f6:63:0e:61:a0%-57$00:f6:63:0e:61:a4%-51$08:17:35:c7:86:0b%-77$08:17:35:c7:86:04%-77$cc:16:7e:b6:80:c5%-64$cc:16:7e:b6:80:c4%-64$cc:16:7e:b6:80:c0%-61$00:f6:63:0e:61:a3%-51$08:17:35:c7:86:06%-77$cc:16:7e:b6:80:c3%-63$cc:16:7e:b6:80:cc%-69$00:c8:8b:13:f7:fc%-79$08:17:35:c7:86:0c%-67$08:17:35:c7:86:09%-77$08:17:35:c7:86:05%-77$00:c8:8b:13:f7:fa%-79$00:c8:8b:13:f7:fb%-74$08:17:35:c7:86:01%-70$00:c8:8b:13:f7:ff%-74$08:17:35:c7:86:0f%-85$08:17:35:c7:86:0a%-83$08:17:35:c7:86:0d%-86$00:c8:8b:13:f7:f0%-66$00:c8:8b:13:f7:f5%-66$00:c8:8b:13:f7:f4%-66$08:17:35:c7:4f:42%-74$08:17:35:c7:4f:49%-78$70:db:98:7a:f2:1a%-79$70:db:98:7a:f2:1f%-80$70:db:98:7a:f2:1b%-79$08:17:35:c7:4f:44%-84$5a:52:8a:19:95:f4%-80$58:52:8a:19:95:f3%-88$08:17:35:c7:4f:4e%-89$58:52:8a:19:95:f4%-79$34:bd:c8:55:ea:60%-88$00:c8:8b:13:f7:f3%-67$70:db:98:7a:f2:1c%-79$08:17:35:c7:4f:45%-74$08:17:35:c7:4f:4a%-81$08:17:35:c7:4f:43%-90$34:bd:c8:55:ea:65%-87$00:f6:63:0e:61:af%-49$08:17:35:c7:4f:4b%-79$08:17:35:c7:4f:41%-79$08:17:35:c7:4f:46%-78$08:17:35:c7:4f:4c%-73$08:17:35:c7:86:02%-69$70:db:98:7a:f2:15%-73$70:db:98:7a:f2:14%-74$70:db:98:7a:f2:10%-74$00:a0:de:9e:18:88%-83$08:86:3b:b2:cf:3a%-87$00:f6:63:0e:61:ac%-64$70:db:98:7a:f2:13%-74$00:c8:8b:1b:93:f3%-87$0#"
    p_d = joblib.load("TrainSet.dat")
    rf=RandomForestRegressor()
    rf.fit(p_d['data'], p_d['target'])#进行模型的训练
    print(p_d['data'], p_d['target'])

