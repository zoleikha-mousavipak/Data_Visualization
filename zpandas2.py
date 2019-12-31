import matplotlib.pyplot as plt
import pandas as pd

raw_data = {'names': ['Zoleikha','Panda','S', 'Ari', 'Valos'],
            'jan_ir': [124,143,112,103,156],
            'feb_ir': [100, 143, 115, 98, 62],
            'march_ir': [65, 88, 45, 12, 65]}

df = pd.DataFrame(raw_data, columns=['name', 'jan_ir', 'feb_ir', 'march_ir'])

df['total_ir'] = df['jan_ir']+df['feb_ir']+df['march_ir']

color = [(1,.4,.4), (1, .6, 1), (.5, .3, 1), (.3, 1, .5), (.7,.7,1)]

plt.pie(df['total_ir'],
        labels=['names'],
        colors=color,
        autopct='%1.1f%%')
plt.show()