import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(color_codes=True)
import datetime
import requests

def apiRequest(identifiers, startDate, endDate):
    portfolioAnalysisRequest = requests.get("https://www.blackrock.com/tools/hackathon/performance?" \
                 + "betaPortfolios=SNP500&endDate="+endDate+"&identifiers="+",".join(identifiers)\
                 + "&riskFreeRatePortfolio=LTBILL1-3M&startDate="+startDate).json()
    return portfolioAnalysisRequest


def calculateGrowth(investment, portfolioAnalysisRequest):
    results = portfolioAnalysisRequest['resultMap']['RETURNS']
    Y = [0]*len(results[0]['performanceChart'])
    for i in range(len(results[0]['performanceChart'])):
        y = 0
        for company in range(len(results)):
            y += results[company]['performanceChart'][i][1]
        Y[i] = investment*(y/len(results))
    X = list(range(len(Y)))
    return X,Y


def _date(dateString):
    y,m,d = int(dateString[0:4]), int(dateString[4:6]), int(dateString[6:8])
    return datetime.date(y,m,d)


def plotGrowth(X, Y, xlabels, identifiers, startDate, endDate, ax=None):
    if ax == None:
        fig, ax = plt.subplots(figsize=(30,15))
    title = "{} performance from {} to {}".format("/".join(identifiers),_date(startDate),_date(endDate))
    plt.xlim(0,len(X))
    plt.ylabel('Return on Investment', fontsize=26)
    plt.yticks(size=26)
    plt.xticks(np.arange(len(X)), xlabels, size=26, rotation=45) #np.arange(len(X)), month_name[1:13],
    for index, label in enumerate(ax.xaxis.get_ticklabels()):
        if index % 30 != 0:
            label.set_visible(False)
    ax.plot(X, Y, c='red', label='Performance', linewidth=4)
    plt.suptitle(title,fontsize=40)
    ax.axhline(Y[-1], label='Investment value= ${:.2f}'.format(Y[-1]), linewidth=4, c='green')
    ax.legend(prop={'size': 26}, loc=4)
    plt.tight_layout()
    plt.savefig('figure.png')


def createPortfolio(investment=1000, identifiers=['GOOG','BLK','AMZN'], startDate='20170101', endDate='20171231'):
    portfolioAnalysisRequest = apiRequest(identifiers, startDate, endDate)
    X,Y = calculateGrowth(investment, portfolioAnalysisRequest)
    xlabels = [str(i[0:4])+"-"+str(i[4:6]) for i in portfolioAnalysisRequest['resultMap']['RETURNS'][0]['returnsMap']]
    plotGrowth(X,Y, xlabels, identifiers, startDate, endDate)


if __name__ == '__main__':
    createPortfolio()
