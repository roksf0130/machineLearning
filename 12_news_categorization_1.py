import os
import re
import math
from collections import OrderedDict

def get_file_list(dir_name) :
    return os.listdir(dir_name)

def get_conetents(file_list) :
    y_class = []
    x_text = []
    class_dict = {1:"0", 2:"0", 3:"0", 4:"0", 5:"1", 6:"1", 7:"1", 8:"1"}

    for file_name in file_list :
        try :
            # 파일을 읽어와서 파일명의 시작이 1, 2, 3, 4 이면 0으로, 5, 6, 7, 8이면 1로 구분하여 y_class 리스트에 추가하고
            # 파일내용은 x_text 리스트에 추가
            f = open(file_name, "r",  encoding = "cp949")
            category = int(file_name.split(os.sep)[1].split("_")[0])
            y_class.append(class_dict[category])
            x_text.append(f.read())
            f.close()
        except UnicodeDecodeError as e:
            print(e)
            print(file_name)
    return x_text, y_class

def get_cleaned_text(text) :
    # 정규식표현 중 \W 는 알파벳과 숫자를 제외한  문자는 나타냄
    text = re.sub('\W+','', text.lower())
    return text

def get_corpus_dict(text) :
    # 파일내용을 split 하여 단어 단위로 나누고 text 리스트 생성
    text = [sentence.split() for sentence in text]
    # text 리스트는 중첩리스트이므로 두 번의 for 문을 이용하여 문자열형태의 단어만 추출하고 정제하여 리스트를 생성
    cleaned_words = [get_cleaned_text(word) for words in text for word in words]
    corpus_dict = OrderedDict()
    # set 으로 중복단어를 제거하고 enumerate 로 단어의 인덱스를 생성하여 OrderedDict 인 corpus_dict 에 추가
    for i, v in enumerate(set(cleaned_words)) :
        corpus_dict[v] = i
    return corpus_dict

def get_count_vector(text, corpus) :
    # 파일내용을 split 하여 단어 단위로 나누고 text 리스트 생성
    text = [sentence.split() for sentence in text]
    # text 리스트는 중첩리스트이므로 두 번의 for 문을 이용하여 문자열형태의 단어만 추출하고
    # 추출후 정제된 단어가 corpus 에 존재하면 해당 단어의 밸류값(인덱스)를 추출하여 word_number_list 리스트를 생성
    word_number_list = [[corpus[get_cleaned_text(word)] for word in words] for words in text]
    # 0으로 초기화된 x_vector 리스트를 생성. 각 파일의 단어수만큼의 리스트를 80개(파일 수) 가진 중첩 리스트
    x_vector = [[0 for _ in range(len(corpus))] for x in range(len(text))]

    #  중첩 for 문으로 x_vector 에 단어 빈도수를 셋팅하는 로직
    for i, text in enumerate(word_number_list) :
        for word_number in text :
            x_vector[i][word_number] += 1
    return x_vector

def get_cosine_similarity(v1, v2) :
    "compute cosine similarity of v1 to v2: (v1 dot v2)/{||v1||*||v2||)"
    sumxx, sumxy, sumyy = 0, 0, 0
    for i in range(len(v1)) :
        x = v1[i]; y = v2[i]
        sumxx += x * x
        sumyy += y * y
        sumxy += x * y
    return sumxy / math.sqrt(sumxx * sumyy)

def get_similarity_score(x_vector, source) :
    source_vector = x_vector[source]
    similarity_list = []
    for target_vector in x_vector :
        similarity_list.append(
            get_cosine_similarity(source_vector, target_vector))
    return similarity_list

def get_top_n_similarity_news(similarity_score, n) :
    import operator
    x = {i:v for i, v in enumerate(similarity_score)}
    sorted_x = sorted(x.items(), key=operator.itemgetter(1))
    return list(reversed(sorted_x))[1:n+1]

def get_accuracy(similarity_list, y_class, source_news) :
    source_class = y_class[source_news]
    return sum([source_class == y_class[i[0]] for i in similarity_list]) / len(similarity_list)

if __name__ == "__main__" :
    # news_data 경로에 존재하는 전체 파일을 리스트로 가져오고
    # 파일명과 경로를 os.path.join 으로 연결하여 새로운 리스트 생성
    # os.path.join 은 윈도우 운영체제에서는 '\', 리눅스 운영체제에서는 '/' 로 연결함
    dir_name = "news_data"
    file_list = get_file_list(dir_name)
    file_list = [os.path.join(dir_name, file_name) for file_name in file_list]

    # 파일 내용은 x_text, 파일구분은 y_class 에 리스트로 저장
    x_text, y_class = get_conetents(file_list)

    # 중복이 제거된 단어를 키값으로 가지고 인덱스를 밸류값으로 가지는 OrderedDict 인 corpus 생성
    corpus = get_corpus_dict(x_text)
    print("Number of words : {0}".format(len(corpus)))
    x_vector = get_count_vector(x_text, corpus)
    source_number = 10

    result = []

    for i in range(80) :
        source_number = i
        similarity_score = get_similarity_score(x_vector, source_number)
        similarity_news = get_top_n_similarity_news(similarity_score, 10)
        accuracy_score = get_accuracy(similarity_news, y_class, source_number)
        result.append(accuracy_score)
    print(sum(result) / 80)
