import matplotlib.pyplot as plt
import pandas as pd

# data = [{
#     'name': 'Zoleikha',
#     'jan_ir': 124,
#     'feb_ir': 100,
#     'march_ir': 165
#         },
#         {
#         'name': 'Panda',
#         'jan_ir': 112,
#         'feb_ir': 143,
#         'march_ir': 3
#     }]

raw_data = {'name' : ['Zoleikha','Panda','S', 'Ari', 'Valos'],
            'jan_ir': [124,143,112,103,156],
            'feb_ir': [100, 143, 115, 98, 62],
            'march_ir': [65, 88, 45, 12, 65]}

df = pd.DataFrame(raw_data, columns=['name', 'jan_ir', 'feb_ir', 'march_ir'])
df['total_ir'] = df['jan_ir']+df['feb_ir']+df['march_ir']
print(df)
