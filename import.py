import shutil
import zipfile
import os
import numpy as np


def doc_sort(elem):
    return elem


def rem_file():
    print("Clearing files...")
    try:
        shutil.rmtree(exp_path + "\\TEMP")
    except:
        print("File is already empty!")


file_path = "" # insert file path
exp_path = "" # insert export path
db_add = "" # insert database address
from_user = "" # insert from user
to_user = "" # insert to user

csv_file = "result.csv"
arr = []
file_ls = []
rem_file()
arr = np.genfromtxt(csv_file, delimiter=",", dtype=str)
for i in arr:
    if i[2] not in file_ls:
        file_ls.append(i[2])

file_ls.sort(key=doc_sort, reverse=1)

for i in file_ls:
    print(i, "is being extracted...")
    with zipfile.ZipFile(str(file_path + i), 'r') as zip_ref:
        zip_ref.extract('TEMP/FULL_TABLES.DMP', path=exp_path)
    for j in arr:
        if str(j[2]) == i:
            cm_script = 'imp \'' + db_add + '\' file=' + exp_paIth + '\\TEMP\\FULL_TABLES.DMP fromuser=' + from_user + \
                        ' touser=' + to_user + ' tables=' + str(j[0]) + ' ignore =y '
            os.system(cm_script)
    rem_file()
