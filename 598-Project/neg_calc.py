from collections import Counter
import json
import pandas
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input')
    parser.add_argument('-o', '--output')
    args = parser.parse_args()
    dialog = args.input
    output = args.output
    dic = {"Covid Vaccination": {}, "Covid Spread": {}, "Covid Precautions": {}, "Covid Restrictions": {},
           "Covid Variant Types": {}, "Post Covid Life": {}, "Covid and Society": {}, "Covid and Politics": {}}
    with open(dialog, "r") as inp:
        df = pandas.read_csv(inp, sep="\t")
        lis = ['"CV"', '"CS"', '"CP"', '"CR"', '"CT"', '"PL"', '"CY"', '"CL"']
        list2 = ["Covid Vaccination", "Covid Spread", "Covid Precautions", "Covid Restrictions",
                 "Covid Variant Types", "Covid Life Impact", "Covid and Society", "Covid and Politics"]
        i = 0
        for s in lis:
            string = (df.query('topic == ' + s)["sentiment"]).str.cat(sep=' ')
            count = Counter(string.lower().split(" "))
            d = {}
            for key, value in count.items():
                    d[key] = value
            dic[list2[i]] = d
            i += 1
    with open(output, "w") as out:
        json.dump(dic, out, indent=3)



if __name__ == '__main__':
    main()
