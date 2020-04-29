"""Format Monefy.csv files according to my requirements
1. Remove Data older than 2018
2. Remove unnecessary columns
"""
import pandas as pd
import datetime

if __name__ == "__main__":
    path_csv = 'Monefy.Data.3-27-20.csv'

    df = pd.read_csv(path_csv)
    print(df.head(), df.shape)

    # drop unnecessary columns
    drop_columns = ['account', 'converted amount', 'currency.1']
    df = df.drop(columns=drop_columns)

    # change date format
    df['date'] = pd.to_datetime(df['date'])

    # remove data older than 2018
    df = df[(df['date'] > '2018-01-01')]
    # change the sign of amount from (minus) to (plus)
    df['amount'] = pd.to_numeric(df['amount'])*(-1)

    # remove all incomes
    df = df[(df['amount'] > 0)]

    print(df.head(), df.shape)
    # save to csv
    save_file = 'Monefy.csv'
    df.to_csv(save_file, index=False)
