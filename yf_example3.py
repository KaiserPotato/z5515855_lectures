"""
The purpose of this module is to download stock price data for Qantas for a given year and save the information in a CSV file.
"""

import os
import toolkit_config as cfg
import yf_example2

def qan_prc_to_csv(year):
    """ Download Qantas stock prices for a given year into a CSV file

    """
    start_date = f'{year}-01-01'
    end_date = f'{year}-12-31'
    tic = 'QAN.AX'
    pth = os.path.join(cfg.DATADIR, f'qan_prc_{year}.csv')
    yf_example2.yf_prc_to_csv(tic, pth, start_date, end_date)

if __name__ == "__main__":
    qan_prc_to_csv(2020)