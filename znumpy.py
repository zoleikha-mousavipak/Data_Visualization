import matplotlib.pyplot as plt
import numpy as np

col_count = 3
bar_width = .2

Korea_scores = (544,536,538)
canada_scores = (600,570,500)

index =np.arange(col_count)
k1 = plt.bar(index, Korea_scores, bar_width, alpha=.4, label = "Korea")
c1 = plt.bar(index+bar_width, canada_scores, bar_width, alpha = .4, label="Canada")


def Createlabels(data):
    for item in data:
        height = item.get_height()
        plt.text(item.get_x() + item.get_width() / .2, height*1.05,
                 '%d' % int(height),
                 ha='center', va='bottom')

Createlabels(k1)
Createlabels(c1)

plt.xticks(index + .3 / 2, ("Mathematic", "Reading", "Science"))
plt.legend(frameon=False, bbox_to_anchor=(1,1), loc=2)
plt.grid(True)
plt.title("Test Scores by Country")
plt.xlabel("Subjects")
plt.ylabel("Mean Score in PISA 2012")
plt.show()