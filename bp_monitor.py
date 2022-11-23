
import argparse
from indicators import LastLow, LastHigh, MA 
import calendar_calcs
from datetime import datetime
import math
import pandas
from prettytable import PrettyTable  

WEEKDAYS = ['MON','TUE','WED','THU','FRI','SAT','SUN']

### THIS IS A CALENDAR TOOL TO IDENTIFY ACTION DAYS FOR THE BP STRATEGY
### bp (big pullback) strategy
### simple long-only strategy trading a  market etf (SPY, DIA) 
### the rules:
### buy on next open if close = min(close, lowest(low of previous 6 days))
### sell after 10 days duration
### sell if stopped out on close (using standard stop)

def adjust_prices(df):
    ## adjust the entire price bar to adjusted prices
    ## using the ratio of of Adj_Close/Close as multiplier
    data = []
    for i in range(df.shape[0]):
        bar = df.iloc[i]
        r = bar['Adj Close']/bar['Close']
        ah = bar['High'] * r
        al = bar['Low'] * r
        ao = bar['Open'] * r
        new_bar = [ao, ah, al, bar['Adj Close']]
        data.append([bar['Date']] + [round(x,6) for x in new_bar] + [bar['Volume']])

    nf = pandas.DataFrame(columns='Date Open High Low Close Volume'.split(), data=data)
    return nf, df


def show_calendar(stock, days_back):
    holidays = calendar_calcs.load_holidays()
    cal_columns = f'Date Day MA200 Low Lowest Close BP'
    cal_table = PrettyTable(cal_columns.split())
    cal_table.float_format['BP'] = ".2"
    cal_table.float_format['MA200'] = ".2"
    cal_table.float_format['Low'] = ".2"
    cal_table.float_format['Lowest'] = ".2"
    cal_table.float_format['Close'] = ".2"

    stock_file = f'/home/jcarter/sandbox/trading/data/{stock}.csv'
    print(f'Stock: {stock} -> {stock_file}')
    today = datetime.today().date()
    stock_df, orig_df = adjust_prices(pandas.read_csv(stock_file))
    stock_df.set_index('Date',inplace=True)

    SETUP_LENGTH = 6 

    ma200 = MA(200)
    last_low = LastLow(SETUP_LENGTH)
    last_high = LastHigh(SETUP_LENGTH)

    ## grab enough of the current history to do all calcs 
    gg = stock_df[-(days_back+200+SETUP_LENGTH):]
    start_pt = gg.index[-days_back]

    for i in range(gg.shape[0]):
        idate = gg.index[i]
        stock_bar = gg.loc[idate]
        cur_dt = datetime.strptime(idate,"%Y-%m-%d").date()
        cls = stock_bar['Close']
        
        ma = ma200.push(cls)
        lv = last_low.push(stock_bar['Low'])
        lh = last_high.push(stock_bar['High'])

        # calc retrace on bp signal
        rtc = ""
        if ma is not None and lv is not None and lh is not None:
            y = last_low.valueAt(1)
            if cls > ma and cls < y: rtc = math.log(cls/lh) 

        if idate >= start_pt:
            cal_table.add_row([idate, WEEKDAYS[cur_dt.weekday()], ma, stock_bar['Low'], lv, cls, rtc])
    
    print(" ")
    print("                   Big Pullback Monitor")
    print(cal_table)
    print(f'Today= {WEEKDAYS[today.weekday()]}: {today.strftime("%Y-%m-%d")}')
    print(" ")


if __name__ == '__main__':

    parser =  argparse.ArgumentParser()
    parser.add_argument("stock", help="stock to track")
    parser.add_argument("--history", type=int, help="days back fo history", default=20)
    u = parser.parse_args()

    show_calendar(u.stock, u.history)

