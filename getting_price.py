import quandl
import pandas as pd
import datetime
import logging
logging.basicConfig(filename = 'getting_price.log', level = logging.DEBUG)


def get_data(x):
    return quandl.get("WIKI/" + x, start_date= start,end_date = end)

def main():
    start = datetime.datetime(2007,1,1)
    end = datetime.datetime(2012,12,31)

    stock_list = pd.read_csv('https://datahub.io/core/s-and-p-500-companies/r/constituents.csv')

    telcom = stock_list[stock_list.Sector == 'Telecommunication Services']


    telcom_data = {}
    logging.debug("Begin Loop")
    for i in telcom['Symbol']:
        logging.debug(i)
        telcom_data = {i:get_data(i)}
        logging.debug(telcom_data[i])
    logging.debug('End Loop')

logging.debug('END')

if __name__ = '__main__':
    def main():