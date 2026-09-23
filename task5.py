# variable for CSV
# filename = 'data/raw/MoveBank/Satellite tracking of black-capped petrels 2019-argos.csv'
# # file object pointing to file name
# f = open(filename, 'r')
# #create a list of all the lines in the file via the file object
# line_list = f.readlines()
# #close file
# f.close()
# #print 11th item in line list
# print(line_list[10])

with open('data/raw/MoveBank/Satellite tracking of black-capped petrels 2019-argos.csv',
          'r') as f:
    line_list = f.readlines()
print(line_list[10])