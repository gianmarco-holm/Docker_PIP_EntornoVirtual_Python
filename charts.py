import matplotlib.pyplot as plt

def generate_bar_chart(labels, values):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.savefig('./imgs/bar.png')
  plt.close()

def generate_pie_chart(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')
  plt.savefig('./imgs/pie.png')
  plt.close()

'''
values = [10, 40, 800]
generate_bar_chart(labels, values)
#generate_pie_chart(labels, values)
'''
