import pandas as pd
import csv

print('FILE CLEANER :\n')
while True:
    print("OPERATIONS :\n1.REMOVE DUPLICATES \n2.REMOVE NULL \n3.BOTH \n4.VIEW \n5.EXIT")
    opr = int(input("ENTER OPERATION : "))
    if opr == 5 or opr not in (1,2,3,4):
        break
    file = input("ENTER CSV FILE NAME WITH (.CSV) :")
    try:
        data = pd.read_csv(file)
    except:
        print("$$FILE NOT FOUND ENTER CORRECT FILE NAME")
        continue
    if opr == 1:
        data = data.drop_duplicates()
    if opr == 2:
        data = data.dropna()
    if opr == 3:
        data = data.dropna()
        data = data.drop_duplicates()
    if opr == 4:
        with open(file) as fobj:
            reader = csv.reader(fobj)
            for i in reader:
                print(i)
    data.to_csv("cleaned_"+file,index = False)

with open("cleaned_dirty_students.csv") as fobj:
    reader = csv.reader(fobj)
    for i in reader:
        print(i)




