
bp: Big Pullback Strategy
    Aims to capture corrections after as significant retrace in the general uptrend
    Rules:
    1. close > 200dayMA
    2. if close = min(close, lowest(low of previous 6 days) - enter long on open
    3. time stop = 10 days
    4. chandelier volatility stop

2022-11-19:

    Ran initial tests using the SPY and ^GSPC and it looks to have promise.
    I think what needs to be done is trade a leveraged index base on the signals given by SPY or ^GSPC

2022-11-20:

    Trading the leveraged ETF improves profitability but destroys the sharpe"

    ## trading the UPRO based on SPY signals

    (base) jcarter@DESKTOP-9FLM66K:~/sandbox/trading/strats/bert$ tail -15 spy_upro.out
    | 2022-11-11 | 398.510010 | 37.780000  |   ---   |  ---   |    None   |   ---   |    0     |    None    |        0 | 21192.65 |
    | 2022-11-14 | 395.120000 | 36.820000  |   ---   |  ---   |    None   |   ---   |    0     |    None    |        0 | 21192.65 |
    | 2022-11-15 | 398.489990 | 37.750000  |   ---   |  ---   |    None   |   ---   |    0     |    None    |        0 | 21192.65 |
    | 2022-11-16 | 395.450010 | 36.870000  |   ---   |  ---   |    None   |   ---   |    0     |    None    |        0 | 21192.65 |
    | 2022-11-17 | 394.239990 | 36.470000  |   ---   |  ---   |    None   |   ---   |    0     |    None    |        0 | 21192.65 |
    | 2022-11-18 | 396.030000 | 36.960000  |   ---   |  ---   |    None   |   ---   |    0     |    None    |        0 | 21192.65 |
    +------------+------------+------------+---------+--------+-----------+---------+----------+------------+----------+----------+

    {'CAGR': 0.07066403346181516,
     'MaxDD': 1.0214428093028265,
      'Sharpe': 0.260586612416749,
       'TotalRtn': 1.1192654188,
        'Trades': 93,
         'WinPct': 0.5913978494623656,
          'Years': 11}

    ## trading the SPY based on SPY signals

      (base) jcarter@DESKTOP-9FLM66K:~/sandbox/trading/strats/bert$ tail -15 spy.out
      | 2022-11-11 | 398.510010 |    UP   |  ---  |    None    |  ---   |    0     |    None    |       0 | 18519.14 |
      | 2022-11-14 | 395.120000 |    UP   |  ---  |    None    |  ---   |    0     |    None    |       0 | 18519.14 |
      | 2022-11-15 | 398.489990 |    UP   |  ---  |    None    |  ---   |    0     |    None    |       0 | 18519.14 |
      | 2022-11-16 | 395.450010 |    UP   |  ---  |    None    |  ---   |    0     |    None    |       0 | 18519.14 |
      | 2022-11-17 | 394.239990 |    UP   |  ---  |    None    |  ---   |    0     |    None    |       0 | 18519.14 |
      | 2022-11-18 | 396.030000 |    UP   |  ---  |    None    |  ---   |    0     |    None    |       0 | 18519.14 |
      +------------+------------+---------+-------+------------+--------+----------+------------+---------+----------+

      {'CAGR': 0.05761882296473342,
       'MaxDD': 0.12232528151069677,
        'Sharpe': 0.7013088046347381,
         'TotalRtn': 0.8519143085000003,
          'Trades': 98,
           'WinPct': 0.5714285714285714,
            'Years': 11}

     -- note CAGR goes up (duh) when trading the UPRO but Sharpe drops significantly.  
     -- **** Seems like I should trade this using options to gain leverage.
             1. Deep ITM, expiring shortly after 10day investment horizon - ie. 3 weeks
             2. Look at being ITM as much as would be your Vol Stop. ???
             3. look at historical rtn distrubutions of the SPY over the horizon you are trading! -
                - helps to pick the best option.

     -- took a quick look at the distribution of returns of the SPY over a 10day horizon
           1. std = 0.03
               -- thus 3stds = .09
               -- given this info I should be able to pick the correct ITM option 
                    -- say 0.075 risk (0.03 * 2.5) in the money with 10days until expiry

2022-11-21

    -- another idea is to look at retracements over N days as a function of N day volatility
       i.e. take a 200day moving average of N day volatility and enter when:
             1. log(close/close[N]) / avg N day vol  <= Zscore threshold (say -2.5) 
             2. close > 200day MA 
      then enter.

    -- tried it - doesn't do much - have to think why the last_low version works better.
    
    -- for current bert strategy --horizon=8 works best.

2022-11-22
    - testing the strategy without 200dayMA fiter

    --  BASELINE
    | 2022-10-31 | 386.209990 |   ---   |  ---  |    None    |  ---   |    0     |    None    |        0 | 29627.65 |
    | 2022-11-01 | 384.519990 |   ---   |  ---  |    None    |  ---   |    0     |    None    |        0 | 29627.65 |
    | 2022-11-02 | 374.870000 |   ---   |  ---  |    None    |  ---   |    0     |    None    |        0 | 29627.65 |
    | 2022-11-03 | 371.010010 |   ---   |  ---  |    None    |  ---   |    0     |    None    |        0 | 29627.65 |
    | 2022-11-04 | 376.350010 |   ---   |  ---  |    None    |  ---   |    0     |    None    |        0 | 29627.65 |
    | 2022-11-07 | 379.950010 |   ---   |  ---  |    None    |  ---   |    0     |    None    |        0 | 29627.65 |
    | 2022-11-08 | 382.000000 |   ---   |  ---  |    None    |  ---   |    0     |    None    |        0 | 29627.65 |
    | 2022-11-09 | 374.130000 |   ---   |  ---  |    None    |  ---   |    0     |    None    |        0 | 29627.65 |
    | 2022-11-10 | 394.690000 |   ---   |  ---  |    None    |  ---   |    0     |    None    |        0 | 29627.65 |
    | 2022-11-11 | 398.510010 |   ---   |  ---  |    None    |  ---   |    0     |    None    |        0 | 29627.65 |
    | 2022-11-14 | 395.120000 |   ---   |  ---  |    None    |  ---   |    0     |    None    |        0 | 29627.65 |
    | 2022-11-15 | 398.489990 |   ---   |  ---  |    None    |  ---   |    0     |    None    |        0 | 29627.65 |
    | 2022-11-16 | 395.450010 |   ---   |  ---  |    None    |  ---   |    0     |    None    |        0 | 29627.65 |
    | 2022-11-17 | 394.239990 |   ---   |  ---  |    None    |  ---   |    0     |    None    |        0 | 29627.65 |
    | 2022-11-18 | 396.030000 |   ---   |  ---  |    None    |  ---   |    0     |    None    |        0 | 29627.65 |
    | 2022-11-21 | 394.590000 |   ---   |  ---  |    None    |  ---   |    0     |    None    |        0 | 29627.65 |
    +------------+------------+---------+-------+------------+--------+----------+------------+----------+----------+
     
    {'CAGR': 0.05060819419445117,
     'MaxDD': 0.1786754606326133,
     'Sharpe': 0.6780726196891721,
     'TotalRtn': 1.962765252000004,
     'Trades': 157,
     'WinPct': 0.5987261146496815,
     'Years': 22}

     - without 200day filter
| 2022-10-31 | 386.209990 |   ---   |  ---  |    None    |  ---   |    0     |    None    |        0 | 32962.69 |
| 2022-11-01 | 384.519990 |   ---   |  ---  |    None    |  ---   |    0     |    None    |        0 | 32962.69 |
| 2022-11-02 | 374.870000 |   ---   |  ---  |    None    |  ---   |    0     |    None    |        0 | 32962.69 |
| 2022-11-03 | 371.010010 |   ---   |  BUY  |   371.47   |  ---   |    88    | 332.889102 |   -40.48 | 32922.21 |
| 2022-11-04 | 376.350010 |   ---   |  ---  |   371.47   |  ---   |    88    | 338.825117 |   429.44 | 33392.13 |
| 2022-11-07 | 379.950010 |   ---   |  ---  |   371.47   |  ---   |    88    | 342.189073 |   746.24 | 33708.93 |
| 2022-11-08 | 382.000000 |   ---   |  ---  |   371.47   |  ---   |    88    | 349.319249 |   926.64 | 33889.33 |
| 2022-11-09 | 374.130000 |   ---   |  ---  |   371.47   |  ---   |    88    | 350.477543 |   234.08 | 33196.77 |
| 2022-11-10 | 394.690000 |   ---   |  ---  |   371.47   |  ---   |    88    | 361.370466 |  2043.36 | 35006.05 |
| 2022-11-11 | 398.510010 |   ---   |  ---  |   371.47   |  ---   |    88    | 365.910565 |  2379.52 | 35342.21 |
| 2022-11-14 | 395.120000 |   ---   |  ---  |   371.47   |  ---   |    88    | 366.518013 |  2081.20 | 35043.89 |
| 2022-11-15 | 398.489990 |   ---   |  ---  |   371.47   |  ---   |    88    | 368.729527 |  2377.76 | 35340.45 |
| 2022-11-16 | 395.450010 |   ---   |  ---  |   371.47   |  EXP   |    88    | 368.729527 |  2110.24 | 35072.93 |
| 2022-11-17 | 394.239990 |   ---   |  ---  |    None    |  ---   |    0     |    None    |        0 | 35072.93 |
| 2022-11-18 | 396.030000 |   ---   |  ---  |    None    |  ---   |    0     |    None    |        0 | 35072.93 |
| 2022-11-21 | 394.590000 |   ---   |  ---  |    None    |  ---   |    0     |    None    |        0 | 35072.93 |
+------------+------------+---------+-------+------------+--------+----------+------------+----------+----------+
 
{'CAGR': 0.05869645533809664,
 'MaxDD': 0.5684729785870515,
 'Sharpe': 0.3817219347511025,
 'TotalRtn': 2.507293400899996,
 'Trades': 270,
 'WinPct': 0.5740740740740741,
 'Years': 22}

 -- signal on close below lower closes
| 2022-10-31 | 386.209990 |   ---   |  ---  |    None    |  ---   |    0     |    None    |        0 | 29565.28 |
| 2022-11-01 | 384.519990 |   ---   |  ---  |    None    |  ---   |    0     |    None    |        0 | 29565.28 |
| 2022-11-02 | 374.870000 |   ---   |  ---  |    None    |  ---   |    0     |    None    |        0 | 29565.28 |
| 2022-11-03 | 371.010010 |   ---   |  ---  |    None    |  ---   |    0     |    None    |        0 | 29565.28 |
| 2022-11-04 | 376.350010 |   ---   |  ---  |    None    |  ---   |    0     |    None    |        0 | 29565.28 |
| 2022-11-07 | 379.950010 |   ---   |  ---  |    None    |  ---   |    0     |    None    |        0 | 29565.28 |
| 2022-11-08 | 382.000000 |   ---   |  ---  |    None    |  ---   |    0     |    None    |        0 | 29565.28 |
| 2022-11-09 | 374.130000 |   ---   |  ---  |    None    |  ---   |    0     |    None    |        0 | 29565.28 |
| 2022-11-10 | 394.690000 |   ---   |  ---  |    None    |  ---   |    0     |    None    |        0 | 29565.28 |
| 2022-11-11 | 398.510010 |   ---   |  ---  |    None    |  ---   |    0     |    None    |        0 | 29565.28 |
| 2022-11-14 | 395.120000 |   ---   |  ---  |    None    |  ---   |    0     |    None    |        0 | 29565.28 |
| 2022-11-15 | 398.489990 |   ---   |  ---  |    None    |  ---   |    0     |    None    |        0 | 29565.28 |
| 2022-11-16 | 395.450010 |   ---   |  ---  |    None    |  ---   |    0     |    None    |        0 | 29565.28 |
| 2022-11-17 | 394.239990 |   ---   |  ---  |    None    |  ---   |    0     |    None    |        0 | 29565.28 |
| 2022-11-18 | 396.030000 |   ---   |  ---  |    None    |  ---   |    0     |    None    |        0 | 29565.28 |
| 2022-11-21 | 394.590000 |   ---   |  ---  |    None    |  ---   |    0     |    None    |        0 | 29565.28 |
+------------+------------+---------+-------+------------+--------+----------+------------+----------+----------+
 
{'CAGR': 0.050507550924723255,
 'MaxDD': 0.22270742755656836,
 'Sharpe': 0.62006152485252,
 'TotalRtn': 1.9565275143999932,
 'Trades': 215,
 'WinPct': 0.6046511627906976,
 'Years': 22}

  -- CONCLUSION - the original is the best.
