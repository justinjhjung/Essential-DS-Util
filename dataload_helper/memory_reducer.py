import pandas as pd
import numpy as np

# This function is made by Josh Devlin
def mem_usage(pandas_obj):
    if isinstance(pandas_obj,pd.DataFrame):
        usage_b = pandas_obj.memory_usage(deep=True).sum()
    else: # we assume if not a df it's a series
        usage_b = pandas_obj.memory_usage(deep=True)
    usage_mb = usage_b / 1024 ** 2 # convert bytes to megabytes
    return "{:03.2f} MB".format(usage_mb)

def inthandler(column):
    if np.sum(column>0) > 0:
        column = pd.to_numeric(column, downcast='signed')
    else:
        column = pd.to_numeric(column, downcast='unsigned')
    dim_bool = 1
    return column, dim_bool 

def floathandler(column):
    column = pd.to_numeric(column, downcast='float')
    dim_bool = 1
    return column, dim_bool

def strhandler(column):


# This is the main function
def memory_reduce_factory(data):

