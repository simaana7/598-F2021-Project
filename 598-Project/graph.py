d = {
  "CV": 262,
  "CY": 183,
  "CS": 162,
  "CT": 110,
  "CL": 75,
  "CP": 73,
  "CR": 71,
  "PL": 64
}
import matplotlib.pyplot as plt
lists = sorted(d.items()) # sorted by key, return a list of tuples

x, y = zip(*lists) # unpack a list of pairs into two tuples

plt.plot(x, y)
plt.xlabel("Topics")
plt.ylabel("Number of Tweets")
plt.savefig('counts.png')
