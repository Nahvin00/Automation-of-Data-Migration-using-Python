import datetime
import os
import glob
import zipfile
import sys

from prettytable import PrettyTable
import numpy as np


def doc_sort(elem):
    return elem[0]


def progressbar(it, prefix="", size=60, out=sys.stdout):
    count = len(it)

    def show(j):
        a = int(size * j / count)
        b = round((j / count * 100), 2)
        print("{}[{}{}] {}%".format(prefix, u"█" * a, "." * (size - a), b),
              end='\r', file=out, flush=True)

    show(0)
    for i, item in enumerate(it):
        yield item
        show(i + 1)
    print("\n", flush=True, file=out)


os.system('cls')
path = input("Enter the file path: ")
glob_max = []
prog = 0
file_num = 0
filter_file = []
bad_zip = []
due_date = datetime.datetime(2023, 4, 16, 00, 00, 00)
print("Wait for files to load...")

for d in glob.glob(os.path.join(path, '*.ZIP')):
    prog += 1
os.system('cls')
if prog == 0:
    print(path, "does not exist!")
    exit(0)

for d, filename in zip(progressbar(range(prog), "Filtering files: "), glob.glob(os.path.join(path, '*.ZIP'))):
    fd = datetime.datetime.fromtimestamp(os.path.getmtime(filename))
    if fd < due_date:
        file_num += 1
        filter_file.append(filename)
if len(filter_file) == 0:
    print("No files before", due_date.date())
    exit(0)

for d, filename in zip(progressbar(range(len(filter_file)), "Analyzing files: "),
                       filter_file):
    try:
        with zipfile.ZipFile(filename, mode="r") as archive:
            text = archive.read('TEMP/README.TXT').decode(encoding="utf-8")
            for i in text.split('\n'):
                if len(i.split()) > 7:
                    f_name = i.split()[5]
                    f_name_2 = i.split()[4]
                    check = 0
                    if (f_name.startswith('EVT_') or f_name.startswith('EARC_') or f_name.startswith(
                            'STD_')) and f_name.count('_') > 1:
                        f_value = int(i.split()[6])
                        check = 1
                    elif (f_name_2.startswith('EVT_') or f_name_2.startswith('EARC_') or f_name_2.startswith(
                            'STD_')) and f_name_2.count('_') > 1:
                        f_name = f_name_2
                        f_value = int(i.split()[5])
                        check = 1
                    if check == 1:
                        f_file = filename.rsplit('\\', 1)[1].strip('.zip')
                        check = 0
                        for x in glob_max:
                            if x[0] == f_name:
                                check = 1
                                if int(x[1]) < f_value:
                                    x[1] = f_value
                                    x[2] = f_file
                                break
                        if check == 0:
                            glob_max.append([f_name, f_value, f_file])
    except zipfile.BadZipfile:
        bad_zip.append(filename)

file_num = 0
if len(bad_zip) != 0:
    with open('log.txt', 'w') as f:
        f.write("BAD ZIP\n")
        for h in bad_zip:
            file_num += 1
            ln = "\n"+str(file_num)+".\t"+str(h)
            f.write(ln)

os.system('cls')
print("Analysis completed.")
glob_max.sort(key=doc_sort)
_doc, _value, _filename = [], [], []
for i in glob_max:
    _doc.append(i[0])
    _value.append(i[1])
    _filename.append(i[2])

res = PrettyTable()
res.title = 'Results'
res.add_column('Doc', _doc)
res.add_column('Value', _value)
res.add_column('Filename', _filename)

np.savetxt("result.csv", glob_max, delimiter=",", fmt='% s')
print(res)
