import pandas as pd
import argparse
from collections import Counter
import json


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output')
    parser.add_argument('-d', '--dialog')
    args = parser.parse_args()
    dialog = args.dialog
    output_file = args.output
    word_counts(dialog, output_file)


def word_counts(dialog, output_file):
    d1 = pd.read_csv(dialog, sep='\t')
    x = d1.topic.value_counts()
    with open(output_file, "w") as out:
        json.dump(x.to_dict(), out, indent=2)

    return json.dumps(x.to_dict(), indent=2)


if __name__ == '__main__':
    main()
