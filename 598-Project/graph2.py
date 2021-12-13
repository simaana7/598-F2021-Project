import json
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input')
    args = parser.parse_args()
    input_json = args.input
    dictionary = json.load(open(input_json, 'r'))
    xAxis = {}
    yAxis = {}
    for key, value in dictionary.items():
        for key1, value1 in value.items():
            xAxis = [key for key, value in value1.items()]
            yAxis = [value for key, value in value1.items()]



if __name__ == '__main__':
    main()
