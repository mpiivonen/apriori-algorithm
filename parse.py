import pandas as pd

data = []

with open('data-2016.csv', 'r') as f:
    for index, line in enumerate(f):
        splitLine = line.split(' ')
        no_courses = (len(splitLine) - 1)/5
        for item in range(0, no_courses):
            newDict = {}
            newDict['student_id'] = index
            newDict['registration_year'] = splitLine[0].strip()
            newDict['course_year_and_month'] = splitLine[(item * 5) + 1].strip()
            newDict['course_code'] = splitLine[(item * 5) +2].strip()
            newDict['course_name'] = splitLine[(item * 5) + 3].strip().strip('"')
            newDict['credits'] = float( splitLine[(item * 5) + 4].strip() )
            newDict['final_grade'] = int( splitLine[(item * 5) + 5].strip() )
            data.append(newDict)
# Number of students
# 1411
# Number of entries
# 31913

df = pd.DataFrame(data)
# Unique courses
# # 380
# 7
course_codes_list = pd.unique( df.course_code)
unique_len = len(course_codes_list);
print "Unique courses", unique_len
# 8
two_combinations = (unique_len*(unique_len-1)/2)
print "Unique two course combinations", two_combinations
#9
three_combinations = (unique_len*(unique_len-1)*(unique_len-2)/6)
print "Unique three course combinations", three_combinations

two_courses = [[(j,i) for i in course_codes_list if i != j] for j in course_codes_list]
'''
for course_combinatios in two_courses:
    for courses in course_combinatios:
        print courses[0]
'''

student_list = pd.unique( df.student_id )
print len(student_list);
test2 = [df[(df.student_id == student) & (df.course_code == '582103') | (df.student_id == student) & (df.course_code == '582104')] for student in student_list]
for t in test2:
    print t
    #print df[(df.student_id == student)]
# example course ids 582103 and 582104
# example student id 1411
#course_names_list = pd.unique( df.course_code )
#print df[((df.course_code == '582103') & (df.student_id == 1411)) | (df.course_code == '582104') & (df.student_id == 1411)];
#EOF 