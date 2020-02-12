import numpy as np

data = np.genfromtxt("dataset1.csv", delimiter=";", usecols=[1,2,3,4,5,6,7], converters={5: lambda s: 0 if s == b"-1" else float(s), 7: lambda s: 0 if s == b"-1" else float(s)})

data_validation = np.genfromtxt("validation1.csv", delimiter=";", usecols=[1,2,3,4,5,6,7], converters={5: lambda s: 0 if s == b"-1" else float(s), 7: lambda s: 0 if s == b"-1" else float(s)})

def get_length(data, data2):
    return pow(data[0] - data2[0], 2) + pow(data[1] - data2[1], 2) + pow(data[2] - data2[2], 2) + pow(data[3] - data2[3], 2) + pow(data[4] - data2[4], 2) + pow(data[5] - data2[5], 2) + pow(data[6] - data2[6], 2)

def scale(data, min_max_list):
    counter = 0
    for index in range(7):
        factor = min_max_list[counter+1] - min_max_list[counter]
        for sample in data:
            sample[index] = ((sample[index] - min_max_list[counter]) / factor)
        counter += 2


dates = np.genfromtxt("dataset1.csv", delimiter=";", usecols=[0])
labels = []
for label in dates:
  if label < 20000301:
    labels.append("winter")
  elif 20000301 <= label < 20000601:
    labels.append("lente")
  elif 20000601 <= label < 20000901:
    labels.append("zomer")
  elif 20000901 <= label < 20001201:
    labels.append("herfst")
  else: # from 01-12 to end of year
    labels.append("winter")

dates_validation = np.genfromtxt("validation1.csv", delimiter=";", usecols=[0])
labels_validation = []
for label in dates_validation:
  if label < 20010301:
    labels.append("winter")
  elif 20010301 <= label < 20010601:
    labels.append("lente")
  elif 20010601 <= label < 20010901:
    labels.append("zomer")
  elif 20010901 <= label < 20011201:
    labels.append("herfst")
  else: # from 01-12 to end of year
    labels.append("winter")

FG_all = []
TG_all = []
TN_all = []
TX_all = []
SQ_all = []
DR_all = []
RH_all = []

for d in data:
    FG_all.append(d[0])
    TG_all.append(d[1])
    TN_all.append(d[2])
    TX_all.append(d[3])
    SQ_all.append(d[4])
    DR_all.append(d[5])
    RH_all.append(d[6])

min_max_data = []
min_max_data.append(min(FG_all))
min_max_data.append(max(FG_all))
min_max_data.append(min(TG_all))
min_max_data.append(max(TG_all))
min_max_data.append(min(TN_all))
min_max_data.append(max(TN_all))
min_max_data.append(min(TX_all))
min_max_data.append(max(TX_all))
min_max_data.append(min(SQ_all))
min_max_data.append(max(SQ_all))
min_max_data.append(min(DR_all))
min_max_data.append(max(DR_all))
min_max_data.append(min(RH_all))
min_max_data.append(max(RH_all))

# FG_min = min(FG_all)
# FG_max = max(FG_all)
# TG_min = min(TG_all)
# TG_max = max(TG_all)
# TN_min = min(TN_all)
# TN_max = max(TN_all)
# TX_min = min(TX_all)
# TX_max = max(TX_all)
# SQ_min = min(SQ_all)
# SQ_max = max(SQ_all)
# DR_min = min(DR_all)
# DR_max = max(DR_all)
# RH_min = min(RH_all)
# RH_max = max(RH_all)

scaled_data = data

scale(data, min_max_data)
scale(data_validation, min_max_data)

#Calculates the distance from 1 validation sample to every data node
def get_distances(data, data_validation):
    distance_lists = []
    for item in data_validation:
        temp = []
        for i in data:
            temp.append(get_length(i, item))
        distance_lists.append(temp)
    return distance_lists

def sort_sub_lists(distance_lists):
    for lists in distance_lists:
        lists.sort()



# def get_lengths(data, data_validation, item):
#     date_data = {}
#     for index_val in range(len(data_validation)):
#         for index in range(len(data)):
#             date_data[dates[index]] = get_length(data[index], data_validation[index_val])
#     return date_data

#compares whole dataset to one validation point
# def get_lengths(data_set, data_validation):
#     final_data = {}
#     for items in data_set:
#         final_data[items[0]] = get_length(items, data_validation)
#     return final_data
#
# def apply_k(k, raw_data):

# def apply_k(k, data, data_validation):
#     raw_data = {}
#     for i in range(len(data_validation)):
#         raw_data.append(get_lengths(data, data_validation, i))
#     raw_data_sorted = sorted(raw_data.items(), key=lambda x: x[1])
#     filtered_values = {}
#     for i in range(k):
#         filtered_values[raw_data_sorted[i][0]] = raw_data_sorted[i][1]
#
#     return filtered_values

# def convert_to_seasons(nearest_neighbours):
#     for i in range(len(nearest_neighbours)):
#         if nearest_neighbours[i][0] < 20010301:
#             nearest_neighbours[i][0] = "winter"
#         elif nearest_neighbours[i][0] <= 20010301 < 20010601:
#             nearest_neighbours[i][0] = "lente"
#         elif nearest_neighbours[i][0] <= 20010601 < 20010901:
#             nearest_neighbours[i][0] = "lente"
#         elif nearest_neighbours[i][0] <= 20010901 < 20011201:
#             nearest_neighbours[i][0] = "lente"
#         else: nearest_neighbours[i][0] = "winter"

# def check(k, data, validation, labels_validation):
#     nearest_neighbours = apply_k(k, data, validation)
#     total = len(validation)
#     convert_to_seasons(nearest_neighbours)

# date_data = {}
# for index_val in range(len(data_validation)):
#     for index in range(len(data)):
#
#         date_data[dates[index]] = get_length(data[index], data_validation[index_val])

# date_data = get_lengths(data, data_validation)

# date_data = sorted(date_data.items(), key=lambda x: x[1])
# a = apply_k(4, data, data_validation)
# print(a)
#print("date_data: ", date_data,"\n data: ", data, "\n data_validation: ", data_validation)
# print("\n", date_data)
