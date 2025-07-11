import matplotlib.pyplot as plt
import seaborn as sns

i=sns.load_dataset('iris')

x=i.iloc[:10,0:4]


sns.heatmap(x,annot=True)

plt.show()
