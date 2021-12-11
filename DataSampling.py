import statistics
import plotly.figure_factory as ff
import csv
import pandas as pd
import random

df=pd.read_csv('medium_data.csv')
data=df['reading_time'].tolist()
population_mean = statistics.mean(data)
print('population_mean',population_mean)
def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean
def setup():
    mean_list = []
    for i in range(1,100):
        set_of_means= random_set_of_mean(30)
        mean_list.append(set_of_means)
    print('samplingMean',statistics.mean(mean_list))
    show_fig(mean_list)
    

def show_fig(mean_list):
    df = mean_list
    fig = ff.create_distplot([df], ["reading_time"], show_hist=False)
    fig.show()

setup()


