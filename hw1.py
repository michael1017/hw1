# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
#=======================================

# Part. 2
#=======================================
# Read cwb weather data
cwb_filename = '107060005.csv'
data = []
header = []
with open(cwb_filename) as csvfile:
    mycsv = csv.DictReader(csvfile)
    header = mycsv.fieldnames
    for row in mycsv:
        data.append(row)
#=======================================

# Part. 3
#=======================================
# Analyze data depend on your group and store it to target_data like:
# Retrive all data points which station id is "C0X260" as a list.
# target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))

# Retrive ten data points from the beginning.
target_data = data
attention_list = ['C0A880', 'C0F9A0', 'C0G640', 'C0R190', 'C0X260']
exclude_humd = ['-99.000', '-999.000']
target_data = [x for x in target_data if x['HUMD'] not in exclude_humd]
target_data = [x for x in target_data if x['station_id'] in attention_list]
result_dic = {}
result = []
for i in target_data:
    if i['station_id'] in result_dic.keys():
        result_dic[i['station_id']] += float(i['HUMD'])
    else:
        result_dic[i['station_id']] = float(i['HUMD'])

for i in attention_list:
    if i not in result_dic.keys():
        result_dic[i] = 'None'

for key, value in result_dic.items():
    result.append([key, value])
result = sorted(result)
#=======================================

# Part. 4
#=======================================
# Print result
print(result)
#========================================