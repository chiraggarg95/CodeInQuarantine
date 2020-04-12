import csv
import numpy as np


def RankFetcher(RollNo, FileName):

    reader=csv.reader(open(FileName, 'r'))

    rank_vs_marks=dict()
    count=dict()

    for row in reader:
        k, v = row
        rank_vs_marks[int(k)]=float(v)
        count[float(v)]=count.get(float(v), 0)+1

    marks=rank_vs_marks[RollNo]
    tie=count[marks]
    rank= [i+1 for i, value in enumerate(sorted(count.items(), reverse=True)) if value == (marks, tie)]

    return marks, tie, rank[0]

Data_file='marksheet.csv'

while(True):
    Student_roll_no=input('Enter Roll Number: ')

    if Student_roll_no == "stop":
        break

    else:
        Student_roll_no=int(Student_roll_no)
        student_marks, tie_between, student_rank = RankFetcher(Student_roll_no, Data_file)

        print('Marks: {}, Rank: {}, Tied Between: {}'.format(student_marks, student_rank, tie_between))

