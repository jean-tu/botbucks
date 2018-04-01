import pandas as pd
import numpy as np
import datetime
import requests
from portfoliomaker import createPortfolio
import matplotlib.pyplot as plt
import json
from itertools import islice

with open('SnP500.txt', 'r') as f:
    SnP = ''.join(f.readlines()).split()


data = {}
for stock in SnP:
    portfolioAnalysisRequest = requests.get("https://www.blackrock.com/tools/hackathon/performance?" \
                 + "betaPortfolios=SNP500&endDate=20171231&identifiers="+stock \
                 + "&riskFreeRatePortfolio=LTBILL1-3M&startDate=20170101").json()
    data[stock] = portfolioAnalysisRequest


stock_info = {}
for stock in SnP:
    if data[stock]['success'] == True:
        SecurityDataRequest = requests.get("https://www.blackrock.com/tools/hackathon/security-data?identifiers="+stock).json()
    data[stock]['resultMap']['SECURITY'] = SecurityDataRequest['resultMap']['SECURITY']


from collections import defaultdict
sectors = defaultdict(list)
for stock in SnP:
    if data[stock]['success'] == True:
        if 'gics1Sector' in data[stock]['resultMap']['SECURITY'][0]:
            sector = data[stock]['resultMap']['SECURITY'][0]['gics1Sector']
            sectors[sector].append(stock)


fig, ax1 = plt.subplots(3,4,figsize=(80,60))
ax=[]
for a in ax1:
    for i in a:
        ax.append(i)
for i, sector in enumerate(sectors.keys()):
    for stock in SnP:
        if data[stock]['success'] == True:
            if 'gics1Sector' in data[stock]['resultMap']['SECURITY'][0]:
                if data[stock]['resultMap']['SECURITY'][0]['gics1Sector'] == sector:
                    Y = [y[1] for y in islice(data[stock]['resultMap']['RETURNS'][0]['performanceChart'], 0, None, 1)]
                    X = list(range(len(Y)))
                    ax[i].plot(X, Y, linewidth=4)

        plt.yticks(size=100)
        plt.xticks(size=100, rotation=45)
        ax[i].set_title(sector)
        ax[i].legend(prop={'size': 100})
plt.tight_layout()
plt.savefig('sectors.png')
