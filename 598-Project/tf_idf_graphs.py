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
    for key,value in dictionary.items():
        xAxis = [key for key, value in value.items()]
        yAxis = [value for key, value in value.items()]
        plt.figure(figsize=(10, 5))
        matplotlib.rc('xtick', labelsize=8)
        matplotlib.rc('ytick', labelsize=8)
        plt.plot(xAxis, yAxis)
        plt.xlabel('Words')
        plt.ylabel('TF-IDF Values')
        plt.savefig(str(key)+"_new.png")






if __name__ == '__main__':
    main()