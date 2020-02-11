import numpy as np

data = np.genfromtxt("dataset1.csv", delimiter=";", usecols=[1,2,3,4,5,6,7], converters={5: lambda s: 0 if s == b"-1" else float(s), 7: lambda s: 0 if s == b"-1" else float(s)})

def get_length(data, data2):
    return pow(data[0] - data[0], 2) + pow(data[1] - data[1], 2) + pow(data[2] - data[2], 2) + pow(data[3] - data[3], 2) + pow(data[4] - data[4], 2) + pow(data[5] - data[5], 2) + pow(data[6] - data[6], 2)

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

date_data = {}
for index in range(len(data)):
    date_data[dates[index]] = get_length(data[index], data[index])

date_data = sorted(date_data.items(), key=lambda x: x[1])
print(date_data)
#print(data)