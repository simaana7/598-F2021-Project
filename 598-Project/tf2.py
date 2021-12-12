import argparse
import json
import math


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--input')
    parser.add_argument('-n', '--num')
    parser.add_argument('-o','--output')
    args = parser.parse_args()
    input_file = args.input
    num_words = args.num
    output = args.output
    tfidf(input_file,num_words,output)
    #print(out)


def tfidf(input_file, num_words,output):
    with open(input_file, "r") as inp:
        dic = json.loads(inp.read())
        no_ponies = len(dic.keys())
        dic_u = {}
        dic_tfidf = {}
        for key, value in dic.items():
            for key1, value1 in value.items():
                dic_tfidf[key1] = value1 * math.log10(no_ponies / count_no_word(dic, key1))
            dic_tfidf = dict(sorted(dic_tfidf.items(), key=lambda item: item[1], reverse=True))
            dic_u[key] = dic_tfidf
            dic_tfidf = {}

        for key, value in dic_u.items():
            n = int(num_words)
            first_n = {k: value[k] for k in list(value)[:n]}
            dic_u[key] = list(first_n.keys())

        with open(output,"w") as out:
            json.dump(dic_u,out,indent=2)


def count_no_word(dic, word):
    count = 0
    for key, value in dic.items():
        for key1, value1 in value.items():
            if key1 == word:
                count += 1
    return count


if __name__ == '__main__':
    main()
