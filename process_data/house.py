import os
import random


# Price Class
# from top to end:
#     five classes,
#     six classes,
#     three classes
price_classes = ["very poor", "poor", "fair", "good", "excellent"]
# price_classes = ["very poor", "poor", "fair", "more than fair", "good", "excellent"]
# price_classes = ["low", "medium", "high"]


# Feature List
house_feature_list = ["location", "height", "floor", "size", "architecture", "station_distance", "old"]


# Preprocessing Original Data
# price_level: levelize the price
# floor_level: levelize the floor
# size_level: levelize the size
# age_level
# station_level: distance from house to nearest station

def price_level(price):
    if price<800:
        return price_classes[-5]
    if price<2000:
        return price_classes[-4]
    if price<6000:
        return price_classes[-3]
    if price<10000:
        return price_classes[-2]
    return price_classes[-1]
    # if price<1000:
    #     return price_classes[-4]
    # if price<4000:
    #     return price_classes[-3]
    # if price<8000:
    #     return price_classes[-2]
    # return price_classes[-1]
    # if price<1000:
    #     return price_classes[0]
    # if price<2000:
    #     return price_classes[1]
    # if price<3000:
    #     return price_classes[2]
    # if price<5000:
    #     return price_classes[3]
    # if price<7000:
    #     return price_classes[4]
    # else:
    #     return price_classes[5]


def price_level_rf(price):
    if price<1000:
        return 0
    if price<2000:
        return 1
    if price<6000:
        return 2
    return 3


def floor_level(floor):
    if floor < 5:
        return 0
    if floor < 10:
        return 1
    if floor < 20:
        return 2
    return 3


def size_level(size):
    if size<30:
        return 0
    if size<50:
        return 1
    if size<70:
        return 2
    if size<100:
        return 3
    return 4


def age_level(age):
    return int(age/10)


def station_level(station):
    if station<=5:
        return 0
    if station<=10:
        return 1
    return 2


def generate_data():
    fr = open(os.path.abspath(os.path.join(os.getcwd()))+"/data/house.csv")
    # fr = open(os.path.abspath(os.path.join(os.getcwd()))+"/house.txt")
    price_feature_data = []

    house_feature_data = []
    price_info = []
    # adjust the number of features here
    for line in fr.readlines():
        line = line.strip().split(",")
        if len(line)!=8 or '' in line: continue
        house_info = line[0:-1]
        house_info_list = []
        price = price_level(int(line[-1]))
        house_info_list.append(int(house_info[0]))
        house_info_list.append(floor_level(int(house_info[1])))
        house_info_list.append(int(house_info[2]))
        house_info_list.append(size_level(int(house_info[3])))
        house_info_list.append(int(house_info[4]))
        house_info_list.append(station_level(int(house_info[5])))
        house_info_list.append(age_level(int(house_info[6])))
        price_feature_data.append((price, house_info_list))
        house_feature_data.append(house_info_list)
        price_info.append(price)

    return price_classes, price_feature_data, price_info, house_feature_data


if __name__ == "__main__":
    print(generate_data()[1])
