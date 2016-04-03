import glob
import os
import pandas as pd


# Adds the module column to specific data set.
def add_column_themodule(file):
    file['themodule'] = pd.Series([0] * (len(file.index)))
    return file


# Combine groups of data sets together through pandas.
def combine_data(fileset):
    df = pd.concat(f for f in fileset)
    return df


# Combine all of UncommonGood's wish list data into one data set.
def group_files():
    path = '/Users/Amy/ucg_test/'
    wl_files = glob.glob(os.path.join(path, '*wl.csv'))
    co_files = glob.glob(os.path.join(path, '*co.csv'))
    return wl_files, co_files


def combine_files(file_list):
    panda_data = []
    for file in file_list:
        f = pd.read_csv(file)
        if 'themodule' not in f.columns:
            add_column_themodule(f)
        panda_data.append(f)

    # Why is the numbering for the rows still relate to the individual csv's instead of the new combined dataset?
    # Line below comes out as 922 instead of 5000
    # print(combine_data(wl_files)[5000:5001])
    return combine_data(panda_data)

wl, co = group_files()
print(combine_files(wl))
print(combine_files(co))
