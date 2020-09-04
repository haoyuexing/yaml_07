import yaml


def analyze_data(file_name, case_name):
    with open("./data/" + file_name + ".yaml", "r") as f:
        content = yaml.load(f, Loader=yaml.FullLoader)[case_name]
        data_list = list()
        data_list.extend(content.values())
        return data_list



