import pickle
from txt_to_data_structure import Document
if __name__ == '__main__':
    output_file_path = "./output/output.txt"
    f = open(output_file_path, "rb")
    d = pickle.load(f)
    pass
