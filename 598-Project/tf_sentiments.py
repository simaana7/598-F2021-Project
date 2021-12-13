import pandas as pd
import argparse
from collections import Counter
import json


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input')
    parser.add_argument('-d', '--dataset')
    parser.add_argument('-o', '--output')
    args = parser.parse_args()
    input_file = args.input
    data_set = args.dataset
    output = args.output

    with open(data_set, "r") as inp:
        df = pd.read_csv(inp, sep="\t")
        js = json.load(open(input_file, "r"))
        dic_toret = {}
        lis = ['"CV"', '"CS"', '"CP"', '"CR"', '"CT"', '"PL"', '"CY"', '"CL"']
        for key, value in js.items():
            count_neu = 0
            count_pos = 0
            count_neg = 0
            dic_inside = {}
            for key1, value1 in value.items():
                for row in df.iterrows():
                    if key1 in row[1]['text']:
                        if row[1]['sentiment'] == "/":
                            count_neu += 1
                        if row[1]['sentiment'] == "+":
                            count_pos += 1
                        if row[1]['sentiment'] == "-":
                            count_neg += 1
                    dic_inside[key1] = {"neutral": count_neu, "positive": count_pos, "negative": count_neg}
                dic_toret[key] = dic_inside
        with open(output, "w") as out:
            json.dump(dic_toret, out, indent=2)

if __name__ == '__main__':
    main()
