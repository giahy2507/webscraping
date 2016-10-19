__author__ = 'HyNguyen'
import os

def concatenate_file(input_dir, ouput_file):
    filenames = os.listdir(input_dir)
    fo = open(ouput_file, mode="w")
    for filename in filenames:
        if filename[0] == ".":
            continue
        with open(input_dir+"/"+filename) as f:
            text = f.readlines()
            if len(text) == 3:
                fo.write("".join(text))
    fo.close()

def gen_tokenizer_file(input_dir, ouput_file):
    filenames = os.listdir(input_dir)
    fo = open(ouput_file, mode="w")
    fo.write("\n")
    for filename in filenames:
        if filename[0] == ".":
            continue
        with open(input_dir+"/"+filename) as f:
            text = f.readlines()
            if len(text) == 3:
                fo.write("".join(text))
    fo.close()


if __name__ == "__main__":
    # concatenate_file("/Users/HyNguyen/Documents/Research/Data/vn_express_1", "/Users/HyNguyen/Documents/Research/Data/vn_express_1.txt")
    concatenate_file("/Users/HyNguyen/Documents/Research/Data/vn_express_2", "/Users/HyNguyen/Documents/Research/Data/vn_express_2.txt")