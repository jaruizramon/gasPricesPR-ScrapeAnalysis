
import requests as req
import numpy as np
from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt
import csv
import datetime
from bs4 import BeautifulSoup



def countLines(fileName): # get index for x-values
    
    with open(fileName) as fN:
        for i, l in enumerate(fN):
            pass
        return i + 1



def refineData(dieselRAW, regularRAW, premiumRAW):
    
    dateScraped = datetime.datetime.now()
    
    for romantic in 'abcdefghijklmnopqrstuvwxyz ':
        
        dieselRAW = dieselRAW.replace(romantic, '')
        regularRAW = regularRAW.replace(romantic, '')
        premiumRAW = premiumRAW.replace(romantic, '')
        print(premiumRAW)
        
        # EL ESPACIO ENTRE LOS DOS NUMEROS REPRESENTA \xa0
        
    diesel = dieselRAW.replace('\xa0' , ' , ')
    regular = regularRAW.replace('\xa0\xa0' , ' , ')
    premium = premiumRAW.replace('\xa0\xa0' , ' , ')
    
    iVar = countLines("gasData.csv") #get line number
    
    csvFriend = diesel +", "+ regular+", "+ premium + ", " + dateScraped.strftime("%m/%d/%Y") + ", " + str(iVar)
    print(csvFriend) # para debuggear
    return csvFriend
    

def plotData():
    
    dL = []
    dH = []
    rL = []
    rH = []
    pL = []
    pH = []
    dT = []
    
    
    with open('gasData.csv' , 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            dL.append(float(row[0]))
            dH.append(float(row[1]))
            rL.append(float(row[2]))
            rH.append(float(row[3]))
            pL.append(float(row[4]))
            pH.append(float(row[5]))
            dT.append(int(row[7]))
        csvfile.close()    
        
    plt.plot(dT, dL, label='diesel low')
    plt.plot(dT, dH, label='diesel high')
    plt.plot(dT, pL, label='premium low')
    plt.plot(dT, pH, label='premium high')
    plt.plot(dT, rL, label='regular low')
    plt.plot(dT, rH, label='regular high')
    
    
       
    plt.xlabel('fetch date')
    plt.ylabel('gas prices')
    plt.title('stat_graph')
    plt.legend()
    plt.show()
        
    


def getScrapedData():
    url = 'http://daco.pr.gov/servicios/precios_combustibles/precios_gasolina'
    r = req.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    
    results = soup.find_all('div' , attrs={'class' : 'span12'})
    
    len(results)
    results[1]
    
    p_res = results[1]
    
    p_res.findAll('p')
    
    regularRAW = p_res.find_all('p')[0].text
    premiumRAW = p_res.find_all('p')[1].text
    dieselRAW = p_res.find_all('p')[2].text
    
    refinedShit = refineData(dieselRAW, regularRAW, premiumRAW)
    
    return refinedShit
  
    
#main  
newData = getScrapedData()

updateFile = open("gasData.csv", "a")
updateFile.write(newData + "\n")
updateFile.close()
plotData()


        