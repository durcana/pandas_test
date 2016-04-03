import pandas as pd


# Adds the module column to specific data set.
def add_column_themodule(file):
    data = pd.read_csv(file)
    data['themodule'] = pd.Series([0 for x in range(len(data.index))])
    return data


# Combine groups of data sets together through pandas.
def combine_data(fileset):
    df = pd.concat(f for f in fileset)
    return df


def combine_wl():
    fileset_wl = []

    # Open data with pandas, or add the module column if necessary (data returned is through pandas).
    test = pd.read_csv('test_wl.csv')
    before = add_column_themodule('before_wl.csv')
    after = add_column_themodule('after_wl.csv')

    # Append all data sets into one list.
    fileset_wl.append(before)
    fileset_wl.append(after)
    fileset_wl.append(test)

    # Why is the numbering for the rows still relate to the individual csv's instead of the new combined dataset?
    # Line below comes out as 922 instead of 5000
    # print(combine_data(fileset_wl)[5000:5001])

    # Combine data for wish list. Will still be able to assess when data was taken by time stamp.
    return combine_data(fileset_wl)

# Now do some analysis via pandas with this data. Use combine_wl output as parameters.

combine_wl()
