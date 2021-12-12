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
    dic = {"Covid Vaccination": {}, "Covid Spread": {}, "Covid Precautions": {}, "Covid Restrictions": {},
           "Covid Variant Types": {}, "Post Covid Life": {}, "Covid and Society": {}, "Covid and Politics": {}}

    stopwords = ['a', 'am', 'yes', 'about', 'above', 'across', 'after', 'again', 'against', 'all', 'almost', 'alone',
                 'along', 'ago', 'already', 'also', 'although', 'always', 'among', 'an', 'and', 'another', 'any',
                 'anybody', 'anyone',
                 'anything', 'anywhere', 'are', 'area', 'areas', 'around', 'as', 'ask', 'asked', 'asking', 'asks', 'at',
                 'away', 'b', 'back', 'backed', 'backing', 'backs', 'be', 'became', 'because', 'become', 'becomes',
                 'been', 'before', 'began', 'behind', 'being', 'beings', 'best', 'better', 'between', 'big', 'both',
                 'but', 'by', 'c', 'came', 'can', 'cannot', 'case', 'cases', 'certain', 'certainly', 'clear', 'clearly',
                 'come', 'could', 'd', 'did', 'differ', 'different', 'differently', 'do', 'does', 'done', 'down',
                 'down', 'downed', 'downing', 'downs', 'during', 'e', 'each', 'early', 'either', 'end', 'ended',
                 'ending', 'ends', 'enough', 'even', 'evenly', 'ever', 'every', 'everybody', 'everyone', 'everything',
                 'everywhere', 'f', 'face', 'faces', 'fact', 'facts', 'far', 'felt', 'few', 'find', 'finds', 'first',
                 'for', 'four', 'from', 'full', 'fully', 'further', 'furthered', 'furthering', 'furthers', 'g', 'gave',
                 'general', 'generally', 'get', 'gets', 'give', 'given', 'gives', 'go', 'going', 'good', 'goods', 'got',
                 'great', 'greater', 'greatest', 'group', 'grouped', 'grouping', 'groups', 'h', 'had', 'has', 'have',
                 'having', 'he', 'her', 'here', 'herself', 'high', 'high', 'high', 'higher', 'highest', 'him',
                 'himself', 'his', 'how', 'however', 'i', 'if', 'important', 'in', 'interest', 'interested',
                 'interesting', 'interests', 'into', 'is', 'it', 'its', 'itself', 'j', 'just', 'k', 'keep', 'keeps',
                 'kind', 'knew', 'know', 'known', 'knows', 'l', 'large', 'largely', 'last', 'later', 'latest', 'least',
                 'less', 'let', 'lets', 'like', 'likely', 'long', 'longer', 'longest', 'm', 'made', 'make', 'making',
                 'man', 'many', 'may', 'me', 'member', 'members', 'men', 'might', 'more', 'most', 'mostly', 'mr', 'mrs',
                 'much', 'must', 'my', 'myself', 'n', 'necessary', 'need', 'needed', 'needing', 'needs', 'never', 'new',
                 'new', 'newer', 'newest', 'next', 'no', 'nobody', 'non', 'noone', 'not', 'nothing', 'now', 'nowhere',
                 'number', 'numbers', 'o', 'of', 'off', 'often', 'old', 'older', 'oldest', 'on', 'once', 'one', 'only',
                 'open', 'opened', 'opening', 'opens', 'or', 'order', 'ordered', 'ordering', 'orders', 'other',
                 'others', 'our', 'out', 'over', 'p', 'part', 'parted', 'parting', 'parts', 'per', 'perhaps', 'place',
                 'places', 'point', 'pointed', 'pointing', 'points', 'possible', 'present', 'presented', 'presenting',
                 'presents', 'problem', 'problems', 'put', 'puts', 'q', 'quite', 'r', 'rather', 'really', 'right',
                 'right', 'room', 'rooms', 's', 'said', 'same', 'saw', 'say', 'says', 'second', 'seconds', 'see',
                 'seem', 'seemed', 'seeming', 'seems', 'sees', 'several', 'shall', 'she', 'should', 'show', 'showed',
                 'showing', 'shows', 'side', 'sides', 'since', 'small', 'smaller', 'smallest', 'so', 'some', 'somebody',
                 'someone', 'something', 'somewhere', 'state', 'states', 'still', 'still', 'such', 'sure', 't', 'take',
                 'taken', 'than', 'that', 'the', 'their', 'them', 'then', 'there', 'therefore', 'these', 'they',
                 'thing', 'things', 'think', 'thinks', 'this', 'those', 'though', 'thought', 'thoughts', 'three',
                 'through', 'thus', 'to', 'today', 'together', 'too', 'took', 'toward', 'turn', 'turned', 'turning',
                 'turns', 'two', 'u', 'under', 'until', 'up', 'upon', 'us', 'use', 'used', 'uses', 'v', 'very', 'w',
                 'want', 'wanted', 'wanting', 'wants', 'was', 'way', 'ways', 'we', 'well', 'wells', 'went', 'were',
                 'what', 'when', 'where', 'whether', 'which', 'while', 'who', 'whole', 'whose', 'why', 'will', 'with',
                 'within', 'without', 'work', 'worked', 'working', 'works', 'would', 'x', 'y', 'year', 'years', 'yet',
                 'you', 'young', 'younger', 'youngest', 'your', 'yours', 'z', 'https', 'dr', 'sunday', 'iowans', 'st',
                 'fine', 'move', '', "bad", "demand", "wear", "demand", "believe", "panel", "count", "name", "north",
                 "confirmed", "hit", "million", "bad", "offer", "hope", "team", "half", "please", "hard", "lost", "ass","friday", "thanks", "thank", "november"
                 ]

    with open(dialog, "r") as inp:
        df = pd.read_csv(inp, sep="\t")
        lis = ['"CV"', '"CS"', '"CP"', '"CR"', '"CT"', '"PL"', '"CY"', '"CL"']
        to_remove = ''
        for s in lis:
            to_remove += (df.query('topic == ' + s)["text"]).str.cat(sep=' ')

        pun = '()[],-.?!:;#&'
        for ele in to_remove:
            if ele in pun:
                to_remove = to_remove.replace(ele, " ")
        count1 = Counter(to_remove.lower().split(" "))

        dr = []
        for key, value in count1.items():
            if value < 5:
                dr.append(key)

        lis = ['"CV"', '"CS"', '"CP"', '"CR"', '"CT"', '"PL"', '"CY"', '"CL"']
        list2 = ["Covid Vaccination", "Covid Spread", "Covid Precautions", "Covid Restrictions",
                 "Covid Variant Types", "Post Covid Life", "Covid and Society", "Covid and Politics"]

        i = 0
        for s in lis:
            string = (df.query('topic == ' + s)["text"]).str.cat(sep=' ')
            pun = '()[],-.?!:;#&'
            for ele in string:
                if ele in pun:
                    string = string.replace(ele, " ")

            count = Counter(string.lower().split(" "))
            d = {}
            for key, value in count.items():
                if (key not in dr) & (key not in stopwords) & (key.isalpha()):
                    d[key] = value
            dic[list2[i]] = d
            i += 1

    with open(output_file, "w") as out:
        json.dump(dic, out, indent=2)

    return json.dumps(dic, indent=2)


if __name__ == '__main__':
    main()
