import glob
import os
import pandas as pd


# Group files into two groups, wish list and check out. Exclude ugids files.
def group_files():
    path = '/Users/Amy/ucg_test/'
    wl_files = glob.glob(os.path.join(path, '*wl.csv'))
    co_files = glob.glob(os.path.join(path, '*co.csv'))
    return wl_files, co_files


# Combine data from grouped files each into a single Pandas data frame.
def combine_files(fileset):
    # List for data after turned into Panda series.
    panda_data = []
    for file in fileset:
        f = pd.read_csv(file)
        # Adds the module column to specific data set if needed.
        if 'themodule' not in f.columns:
            f['themodule'] = pd.Series([0] * (len(f.index)))
        panda_data.append(f)

    # Combine list of data series to single data frame. Reset indexing to read as one data set.
    return pd.concat(f for f in panda_data).reset_index()


wl, co = group_files()

# Wish list and check out data each turned into single Pandas data frame.
wl = combine_files(wl)
co = combine_files(co)
