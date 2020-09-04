import yaml

with open("./python_data.yaml", "r") as f:
    content = yaml.load(f, Loader=yaml.FullLoader)["test_py1"]
    data_list = list()
    for i in content.values():
        data_list.append(i)
    print(data_list)
    # return data_list

