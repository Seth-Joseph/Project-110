import pandas as pd
import csv
import statistics as st
import plotly.figure_factory as ff
import random

df = pd.read_csv('medium_data.csv')
data = df['reading_time'].tolist()

population_mean = st.mean(data)

#fig = ff.create_distplot([data],['average'],show_hist = False)
#fig.show()

# To find out stdev of 100 random numbers
def random_set_of_mean(counter):
    data_set = []

    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        data_set.append(value)

    mean = st.mean(data_set)
    return mean

def show_figure(mean_list):
    df = mean_list
    fig = ff.create_distplot([df],['reading_time'],show_hist = False,curve_type = 'normal')
    fig.show()

def setup():
    mean_list = []
    for i in range(0,1000):
        set_of_mean = random_set_of_mean(100)
        mean_list.append(set_of_mean)
    
    show_figure(mean_list)
    n = st.mean(mean_list)
    print('Mean of Sample:',n)
setup()

#stdev

def random_set_of_stdev():
    mean_list = []
    for i in range(0,1000):
        set_of_mean = random_set_of_mean(100)
        mean_list.append(set_of_mean)

    a = st.stdev(mean_list)
    print('Standard Deviation of Sample:',a)
random_set_of_stdev()