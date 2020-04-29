"""Format Monefy.csv files according to my requirements
1. Remove Data older than 2018
2. Remove unnecessary columns
"""
import pandas as pd
import datetime
from skylynx.utils import cli_args
import dateutil

if __name__ == "__main__":
    # argparse
    cli_params = dict(task=0
                      )

    args = cli_args(cli_params)
    task = int(args['task'])

    print(pd.__version__)

    # Init format
    if task == 1:
        path_csv = 'Bank 2019.csv'

        df = pd.read_csv(path_csv)
        print(df.head(), df.shape)

        # drop unnecessary columns
        drop_columns = ['Name', 'Income Note',
                        'Exp. Notes', 'Balance per Month', 'More Notes']
        df = df.drop(columns=drop_columns)

        # change date format
        df['Date'] = pd.to_datetime(df['Date'])

        df = df.fillna(0)

        print(df.head(), df.shape)

        # save to csv
        save_file = 'Bank 2019 New.csv'
        df.to_csv(save_file, index=False)

    # Group by date
    if task == 2:

        path_csv = 'Bank 2019 New.csv'

        df = pd.read_csv(path_csv)

        # change date format
        # df['Date'] = pd.to_datetime(df['Date'])

        df['Date'] = df['Date'].apply(dateutil.parser.parse)

        # df = df.set_index('Date')

        print(df.head(), df.shape)

        # group by month and day
        df1 = df.groupby([df['Date'].dt.year.rename('year'),
                          df['Date'].dt.month.rename('month')]).sum()

        df1['Total Income'] = df1['Income Home'] + df1['Shabu']
        df1['Total Expenses'] = df1['Expenses'] + df1['Rent']

        # drop unnecessary columns
        drop_columns = ['Income Home', 'Shabu', 'Expenses', 'Rent']
        df1 = df1.drop(columns=drop_columns)

        df1 = df1.round(2)

        print(df1)

        df1.to_csv('balance.csv')
