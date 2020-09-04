import csv
import random
#print([(group.append(student)) for student, group in [entry for entry in csv.reader(open("../data/fall-20-students.tsv")\
#                               , delimiter = "\t")][1:]], [[] for x in range(int(input("#")))])
#print([test.append("Hello") for test in list([[] for x in range(10)])])


print([x for x in ["{}".format([entry for entry in csv.reader\
                                (open("../data/fall-20-students.tsv")\
                             , delimiter = "\t")][1:]) for x in range(10)]])
