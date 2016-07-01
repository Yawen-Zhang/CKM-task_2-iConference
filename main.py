# -*- coding: utf-8 -*-

file_path = "iConference_edited/iConf2015.txt"

def parse_string(string):
    string = " ".join(string.split()) # remove duplicate spaces
    no_whitespace = "".join(string.split())
    index_right_a = no_whitespace.find(">") # find the index of right left angle braket
    string_key = no_whitespace[1:index_right_a].lower()
    string_value = string[index_right_a+2:]
    return string_key, string_value

# data format:
# [
# {"author": "Mathiesen, Kay",
# "title": "Indigenous Peoples' Rights to Culture and Individual Rights to Access",
# "abstract": "xxx xxx xxx",
# "ID": "iConf2015.txt-1"},
# {...}
# ]
def get_data_dict(file_path):
    with open(file_path, "r") as f:
        file = list(f)
    n = -1
    data_dict = []
    for line in file:
        line = line.strip()
        if line == "":
            n += 1
            data_dict.append({})
            data_dict[n]["ID"] = "%s-%s" % (file_path, n)
        else:
            string_key, string_value = parse_string(line)
            data_dict[n][string_key] = string_value
    return data_dict

def cleaned_and_wrong_data(data_dict):
    cleaned_data = []
    wrong_data = []
    for item in data_dict:
        if len(item['type'].split()) > 10 or item['title'] == "Accepted":
            wrong_data.append(item)
        else:
            cleaned_data.append(item)
    return cleaned_data, wrong_data

data_dict = get_data_dict(file_path)
cleaned_data, wrong_data = cleaned_and_wrong_data(data_dict)
print((cleaned_data)[:5])
print("\n\n")
print(wrong_data)

# type count
def get_specific_dict(data, key):
    result = {}
    for item in data:
        if key in item:
            value = item[key]
            if value in result:
                result[value] += 1
            else:
                result[value] = 1
    return result

print(get_specific_dict(cleaned_data, "type"))

# import matplotlib as mpl

# import matplotlib.pyplot as plt
#
# D = {u'Label1':26, u'Label2': 17, u'Label3':30}
#
# plt.bar(range(len(D)), D.values(), align='center')
# plt.xticks(range(len(D)), list(D.keys()))
#
# plt.show()

# print(mpl.get_cachedir())

print(get_specific_dict(cleaned_data, "region"))

print(get_specific_dict(cleaned_data, "country"))

def get_author_dict(data):
    result = {}
    for item in data:
        string = item["author"]
        list_author = string.split("; ")
        for item in list_author:
            if item in result:
                result[item] += 1
            else:
                result[item] = 1
    return result

print(get_author_dict(cleaned_data))

def get_keyword_dict(data):
    result = {}
    for item in data:
        if "keywords" in item:
            string = item["keywords"]
            list_keyword = string.split(", ")
            for item in list_keyword:
                if item in result:
                    result[item] += 1
                else:
                    result[item] = 1
    return result

keyword_dict = get_keyword_dict(cleaned_data)
for item in keyword_dict:
    if keyword_dict[item] >= 3:
        print("%s : %s" % (item, keyword_dict[item]))





from nltk.tokenize import word_tokenize

def get_abstract_tokens(data):
    tokens = []
    stopwords=[word.strip().lower() for word in open("english_stopwords.txt")]
    for item in data:
        if "abstract" in item:
            list_token = word_tokenize(item["abstract"])
            for item in list_token:
                item = item.strip().lower()
                if item not in stopwords and len(item) > 1:
                    tokens.append(item)
    return tokens



import nltk

tokens = get_abstract_tokens(cleaned_data)
Freq_dist_nltk=nltk.FreqDist(tokens)
print(Freq_dist_nltk.most_common(150))

import csv
f150 = Freq_dist_nltk.most_common(150)
with open("abstract_token_most_common_150.csv", "wb") as f:
    writer = csv.writer(f, quoting=csv.QUOTE_ALL)
    writer.writerows(f150.items())