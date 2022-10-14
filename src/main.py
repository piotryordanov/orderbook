from fetch_books import fetch_books
import pandas as pd


coinbase_book = fetch_books("coinbase")
gemini_book = fetch_books("gemini")

def get_coinbase_book(col):
    df = pd.DataFrame(coinbase_book[col], columns=['price', 'size', 'num_orders'])
    df = df.drop("num_orders", axis=1)
    df['exchange'] = 'coinbase'
    return df

def get_gemini_book(col):
    df = pd.DataFrame(gemini_book[col], columns=['price', 'amount', 'timestamp'])
    df = df.rename(columns={"amount": "size"})
    df = df.drop("timestamp", axis=1)
    df['exchange'] = 'gemini'
    return df


def get_combined_orderbook(col):
    gemini_df = get_gemini_book(col)
    coinbase_df = get_coinbase_book(col)

    # Combine the dataframes
    # I am taking the coinbase head 50 because gemini doesnt have more than 50
    df = pd.concat([gemini_df, coinbase_df.head(50)])

    # Sort the dataframe by prices
    df.sort_values(by=['price'], inplace=True, ascending=False)

    # Convert size to float to allow numerical operations
    df = df.astype({'size':'float', 'price': 'float'})
    return df


def do_orderbook_to_purchase_amount(df, amount=10):
    cummulative_size = 0
    max_head = 0
    i = 0
    for row in df.iterrows():
        if cummulative_size > amount and max_head == 0:
            max_head = i
        cummulative_size = cummulative_size + row[1]['size']
        i = i + 1
    return df.head(max_head)


def calculate_average_price(df):
    def fn(group):
        group['average_price'] = group['price'] * group['size'] / group['size'].sum()
        return group
    d_agg = {'average_price':'sum' ,'size':'sum'}
    df = df.groupby('exchange', group_keys=False, sort=False).apply(fn).groupby('exchange').agg(d_agg)
    return df


def run(col):
    df = get_combined_orderbook(col)
    df = do_orderbook_to_purchase_amount(df)
    print("The {0} order book is:".format(col))
    print('')
    print(df)
    print('')
    print("The total amount purchased is: {0}".format(df['size'].sum()))
    print('')
    print("The average price per exchange is:")
    print(calculate_average_price(df))


run('asks')
print('==========')
print('')
print('')
print('')
print('==========')
run('bids')
