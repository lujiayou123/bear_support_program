import json
import pickle
from tqdm import tqdm


class Document():
    def __init__(self,
                 text,
                 emotion_fear=0,
                 emotion_happy=0,
                 emotion_sad=0,
                 emotion_anger=0,
                 emotion_shock=0,
                 original_modality=0,
                 synesthesia_modality=0):
        self.text = text
        self.emotion_happy = emotion_happy
        self.emotion_angry = emotion_anger
        self.emotion_sad = emotion_sad
        self.emotion_shock = emotion_shock
        self.emotion_fear = emotion_fear
        self.original_modality = original_modality
        self.synesthesia_modality = synesthesia_modality


def getDocument(text, emotion):
    if emotion == "恐":
        return Document(text=text, emotion_fear=1)
    elif emotion == "喜":
        return Document(text=text, emotion_happy=1)
    elif emotion == "怒":
        return Document(text=text, emotion_anger=1)
    elif emotion == "哀":
        return Document(text=text, emotion_sad=1)
    elif emotion == "惊":
        return Document(text=text, emotion_shock=1)
    else:
        return Document(text=text)


def checkExistence(documents, document):
    if len(documents) < 1:
        return False
    for element in documents:
        if element.text == document.text:
            return True
    return False


if __name__ == '__main__':
    file_labeled_corpus = open("./data/labeled_corpus.txt",
                               "r",
                               encoding="utf-8")
    file_new_labeled_corpus = open("./data/new_corpus_label.txt",
                                   "r",
                                   encoding="utf-8")
    output_file_path = "./output/output.txt"
    output_pickle_file = open(output_file_path, "wb")
    lines_labeled_corpus = file_labeled_corpus.readlines()
    lines_new_labeled_corpus = file_new_labeled_corpus.readlines()
    # print(len(lines_labeled_corpus), len(lines_new_labeled_corpus))
    lines = lines_labeled_corpus + lines_new_labeled_corpus
    documents = []
    for line in tqdm(lines):
        if "</emo>" in line:
            emotion = line.split("</emo>")[0].split("<emo>")[1]
            text = line.split("</emo>")[1].split("<num>")[0]
        else:
            emotion = None
            text = line.split("<num>")[0]
        document = getDocument(text, emotion)
        if checkExistence(documents, document):
            continue
        else:
            documents.append(document)
    pickle.dump(documents, output_pickle_file, 0)
    output_pickle_file.close()
    # output_pickle_file.close()
    # f = open(output_file_path, "rb")
    # d = pickle.load(f)
    # documents.append(document)
