from sklearn import datasets
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

digits = datasets.load_digits(return_X_y=True)
digits_dataset_X = digits[0]
digits_dataset_y = digits[1]
N = len(digits_dataset_X)

print("attr1_num,attr2_num,attr3_num,attr4_num,attr5_num,attr6_num,attr7_num,attr8_num,attr9_num,attr10_num,attr11_num,attr12_num,attr13_num,attr14_num,attr15_num,attr16_num,attr17_num,attr18_num,attr19_num,attr20_num,attr21_num,attr22_num,attr23_num,attr24_num,attr25_num,attr26_num,attr27_num,attr28_num,attr29_num,attr30_num,attr31_num,attr32_num,attr33_num,attr34_num,attr35_num,attr36_num,attr37_num,attr38_num,attr39_num,attr40_num,attr41_num,attr42_num,attr43_num,attr44_num,attr45_num,attr46_num,attr47_num,attr48_num,attr49_num,attr50_num,attr51_num,attr52_num,attr53_num,attr54_num,attr55_num,attr56_num,attr57_num,attr58_num,attr59_num,attr60_num,attr61_num,attr62_num,attr63_num,attr64_num,label")

for i in range(N):
    # Convert the feature vector to a string and remove brackets and spaces
    feature_str = ','.join(map(str, digits_dataset_X[i]))
    # Convert the label to a string
    label_str = str(digits_dataset_y[i])
    
    print(f"{feature_str}", end=',')
    print(f"{label_str}")
