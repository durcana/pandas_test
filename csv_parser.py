import glob
import os
import pandas as pd


# Adds the module column to specific data set.
def add_column_themodule(file):
    file['themodule'] = pd.Series([0] * (len(file.index)))
    return file


# Combine groups of data sets together through pandas. Reset indexing to read as one full data set.
def combine_data(fileset):
    df = pd.concat(f for f in fileset).reset_index()
    return df


# Group files into two groups, wish list and check out. Exclude ugids files
def group_files():
    path = '/Users/Amy/ucg_test/'
    wl_files = glob.glob(os.path.join(path, '*wl.csv'))
    co_files = glob.glob(os.path.join(path, '*co.csv'))
    return wl_files, co_files

# Combine data from grouped files each into a single Pandas data frame.
def combine_files(file_list):
    panda_data = []
    for file in file_list:
        f = pd.read_csv(file)
        if 'themodule' not in f.columns:
            add_column_themodule(f)
        panda_data.append(f)


    return combine_data(panda_data)

wl, co = group_files()
wl = combine_files(wl)
co = combine_files(co)
