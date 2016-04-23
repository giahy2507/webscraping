import pickle

if __name__ == "__main__":
    with open("title.save.pickle", mode="rb") as f:
        data = pickle.load(f)
        print (len(data))
