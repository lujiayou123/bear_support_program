# @作用：一些工具，确保输出文件夹存在，获取路径下的所有指定类型的文件，等
# @输入：
# @输出：
# @用法：
import os
import pandas as pd
import json
import requests


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False


def getCsvFileList(input_folder):
    raw_files = []
    suffix = ".csv"
    # 读input_path下所有的suffix文件名
    for file in os.listdir(input_folder):
        file_path = os.path.join(file)
        if os.path.splitext(file_path)[1] == suffix:
            raw_files.append(file_path)
    return raw_files


def getXlsxFileList(input_folder):
    raw_files = []
    suffix = ".xlsx"
    # 读input_path下所有的suffix文件名
    for file in os.listdir(input_folder):
        file_path = os.path.join(file)
        if os.path.splitext(file_path)[1] == suffix:
            raw_files.append(file_path)
    return raw_files


def getFileList(input_folder, suffix):
    raw_files = []
    # 读input_path下所有的suffix文件名
    for file in os.listdir(input_folder):
        file_path = os.path.join(file)
        if os.path.splitext(file_path)[1] == suffix:
            raw_files.append(file_path)
    return raw_files


def xlsx_to_csv(xlsx_path, csv_path):
    data_xls = pd.read_excel(xlsx_path, index_col=0)
    data_xls.to_csv(csv_path, encoding='gbk')


# ../data/CSV
def guarantee_path_exists(path):
    if "/" in path:
        paths = path.split("/")
        # print(paths)
        path_num = len(paths)
        current_path = ''
        for i in range(path_num):
            if len(paths[i]) > 0:
                if paths[i][0] == ".":
                    current_path = current_path + paths[i] + "/"
                else:
                    current_path = current_path + paths[i] + "/"
                    if not os.path.exists(current_path):
                        os.mkdir(current_path)
    else:
        os.mkdir(path)


def remainAlpha(string):
    for j in range(len(string)):
        if string[j].isalpha():
            output_string = string[j:]
            return output_string
    print("输入字符串出错")


if __name__ == '__main__':
    path = "../data/CSV/XLS/XLSX/"
    # path = "sample"
    guarantee_path_exists(path)
