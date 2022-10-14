### Installation
The recommended way of running this repo is by using `poetry` and `npm`.
Run `npm install` and `poetry install`

If you don't want, you can run:

```bash
npm install nodemon

pip install pandas
pip install requests
```


### Running

You can run the demo with `npm start`.
It will fire a `nodemon` server that will watch for changes


### Sample results

```bash
The asks order book is:

       price     size exchange
49  19655.99  0.30500   gemini
48  19653.17  0.30500   gemini
47  19650.96  1.52782   gemini
46  19649.04  0.00005   gemini
45  19648.22  0.30500   gemini
44  19647.90  2.56400   gemini
43  19645.08  0.20411   gemini
42  19644.27  0.30500   gemini
41  19640.89  0.30500   gemini
40  19639.20  0.20411   gemini
39  19638.50  1.33300   gemini
38  19638.32  0.10000   gemini
37  19638.31  0.30500   gemini
36  19635.03  0.30500   gemini
35  19633.32  0.20411   gemini
34  19632.98  0.30500   gemini
33  19632.10  0.30000   gemini
32  19629.82  0.30500   gemini
31  19627.84  0.30500   gemini
30  19627.44  0.20411   gemini
29  19625.16  0.30500   gemini
28  19624.50  0.64300   gemini

The total amount purchased is: 10.639310000000002

The average price per exchange is:
         exchange  weighted_avg      size      price
exchange                                            
gemini     gemini  19641.589001  10.63931  432058.04
==========



==========
The bids order book is:

       price      size  exchange
0   19603.18  0.000013    gemini
1   19603.13  0.258941    gemini
0   19601.67  0.050000  coinbase
1   19601.03  0.050000  coinbase
2   19600.83  0.005578  coinbase
3   19600.82  1.223377  coinbase
4   19600.51  0.050416  coinbase
5   19600.50  0.025510  coinbase
6   19599.97  0.117274  coinbase
7   19599.96  0.255103  coinbase
8   19599.91  0.038082  coinbase
9   19599.20  0.060000  coinbase
10  19598.93  0.010155  coinbase
11  19598.82  0.170000  coinbase
12  19598.81  1.244177  coinbase
13  19598.57  0.400000  coinbase
14  19598.53  0.060000  coinbase
15  19598.17  1.000000  coinbase
16  19598.16  0.988760  coinbase
17  19598.12  0.510253  coinbase
18  19598.11  1.666505  coinbase
19  19597.93  0.100000  coinbase
20  19597.83  1.013800  coinbase
21  19597.82  0.801934  coinbase

The total amount purchased is: 10.099878610000001

The average price per exchange is:
          exchange  weighted_avg      size      price
exchange                                             
coinbase  coinbase  19598.663787  9.840924  431184.20
gemini      gemini  19603.130003  0.258954   39206.31
```

### Notes
+ There is an error in the pdf: The Coinbase docs should be [here](https://docs.cloud.coinbase.com/exchange/reference/exchangerestapi_getproductbook-1)
+ I did not trim the result, essentially taking anything that's on the last level. This is why for example, the total amount purchased on bid/ask is respectively 10.09 and 10.63
+ Adding kraken would have been similar to the rest:
  + Fetch the data. Align the data columns to `price, size, exchange`, then concat.
  + For 3+ exchanges, I'd have added some more automation to concat. (Currently it's manual)
