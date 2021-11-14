import json

json_path = './technical_test_data_analyst.json'

json_dict = {}

with open(json_path) as json_file:
    json_dict = json.load(json_file)

str_file = ''

for i in json_dict['id']:
    normalized_dict = {}

    for j in json_dict.keys():
        normalized_dict[j] = json_dict[j][i]

    str_file += str(normalized_dict) + '\n'

    if i == '0':
        print(str_file)


with open('goods_data_cleaned_athena_db_ready.json', 'w') as f:
    f.write(str_file)
