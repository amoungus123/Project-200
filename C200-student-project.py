#!/usr/bin/env python
# coding: utf-8

# # GUI APPLICATION

# In[1]:


#start of predefine code
from ipywidgets import widgets
from IPython.display import display, clear_output
import pandas as pd
from tkinter import Tk, filedialog
import matplotlib.pyplot as plt 
import numpy as np
graph_type = ['Choose one.. ','bubble','bar']
funtionality = ['Choose One','Sort','Filter']
sort_option = ['ascending','descending']
df = ''
new_df = ''
input_box = ''
input_fontsize = ''
input_title = ''
#end of predefine code


def select_files(b):
    global df
    global input_box
    clear_output()
    root = Tk()
    root.withdraw()
    file_name = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    df = pd.read_csv(file_name)
    display(df)
    function_widget = widgets.Dropdown(
        options=functionality,
        value='Choose One',
        description='Functionality:'
    )

display(function_widget)
function_widget.observe(choose_the_function, names='value')



#start of predefine code 
def display_plot(xaxis, yaxis, graph_type):
    global new_df
    global input_title
    global input_fontsize
    if(graph_type == 'bubble'):
        plt.subplots(figsize=(19,8))
        rgb = np.random.rand(3)
        #Write Condition here

        #End of write condition here 
        plt.title(input_title.value, fontsize=input_fontsize.value)
        plt.xlabel(xaxis, fontsize=input_fontsize.value)
        plt.xticks(rotation='vertical')
        plt.ylabel(yaxis, fontsize=input_fontsize.value)
        plt.show()
    elif(graph_type == 'bar'):
        plt.subplots(figsize=(19,8))
        plt.bar(new_df[xaxis], new_df[yaxis], color=['red', 'green','blue','yellow','pink'])
        plt.title(input_title.value, fontsize=input_fontsize.value)
        plt.xlabel(xaxis, fontsize=input_fontsize.value)
        plt.xticks(rotation='vertical')
        plt.ylabel(yaxis, fontsize=input_fontsize.value)
        plt.show()
    else:
        print("Choose valid graph")
fileselect = widgets.Button(description="File select")
fileselect.on_click(select_files)
display(fileselect)
#end of predefined


# In[ ]:




