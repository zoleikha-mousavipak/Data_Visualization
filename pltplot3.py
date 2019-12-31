import matplotlib.pyplot as plt

labels = 'python', 'c#', 'java' , 'PHP', 'Perl', 'Ruby'
size = [33,52,12,17,62,48]
separated = (1,.2,0,0,0,0)

plt.pie(size, labels=labels, autopct='%1.1f%%', explode=separated)
plt.axis('equal')
plt.show()