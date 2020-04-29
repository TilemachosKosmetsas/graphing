import matplotlib.pyplot as plt
import numpy as np
import time
import datetime
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
from matplotlib.finance import candlestick_ohlc as candlestick
plt.rcParams.update({'font.size': 12 })


eachstock = 'ETE.AT'



def graphData(stock):
    try:
        stockFile = 'C:\\Users\\tiel_\\Desktop\\highlow\\'+stock+'.txt'

        date, closep, highp, lowp, openp, volume = np.loadtxt(stockFile, delimiter=',',unpack= True,
                                                             converters={0 : mdates.bytespdate2num('%Y%m%d')})    #oles oi metavlhtes apo to arxeio, tis pairnei
                                                                                                                #to nympy kai tis sumazzeuei
                                                                                                                # kanei convert to time stamp ,
                                                                                                                #se kati pou na mporei na katalavainei to numpy
                                                                                                                # pio sygkekrimena apo bytes se str
        x=0
        y=len(date) # to date einai pleon array ,me tin entolh unpacked True exoun ginei transposed ta stoixeia "date" se ena array
        candleAr = []
        while x < y:
            appendLine = date[x],openp[x],highp[x],lowp[x],closep[x],volume[x] # me auth th seira ta pairnei swsta to ohlc
            candleAr.append(appendLine)
            
            
            x+=1
        

        
        fig = plt.figure(figsize=(12,8))
        ax1 =  plt.subplot2grid((8,8),(0,0), rowspan=5,colspan=8)   #4by 4 grid, starting point 0,0
        candlestick(ax1,candleAr,width=0.7, colorup='g', colordown='r')

        ax1.grid(True)
        plt.ylabel('Stock Price')

        ax2=plt.subplot2grid((4,4),(3,0),sharex=ax1,rowspan=1,colspan=4)
        ax2.bar(date,volume)
        #ax2.axes.yaxis.set_ticklabels([]) eksafanizei ton ogko twn synallagwn (noumero)
        ax2.axes.yaxis.labelpad = 15 # paei tin leksh volume pio mesa
        ax2.axes.xaxis.labelpad = 20 # paei ti leksh date ligo pio katw
        ax1.axes.yaxis.labelpad = 10
        
        ax2.grid(True)
        
        


        plt.subplots_adjust(left=.10, bottom=.22,top=.95, right=.93 ,wspace=.20, hspace=.01)
        ax1.xaxis.set_major_locator(mticker.MaxNLocator(10)) #na entopiseis ston aksona x 15 theseis gia tis hmeromhnies
        ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))   # na valeis tis imeromhnies , oi opoies etsi  tha mpainoun orizontia kai einai xalia
        for label in ax1.xaxis.get_ticklabels():
            label.set_rotation(45)
        for label in ax2.xaxis.get_ticklabels():
            label.set_rotation(45)

        
        
        plt.xlabel('Date')
        plt.ylabel('Volume')
        plt.suptitle(stock+' Stock Price')

        
        #ax2.axes.yaxis.set_ticklabels([]) #eksafanizei ta panta ston aksona
        plt.setp(ax1.get_xticklabels(),visible=False) #eksafanizei ton xrono ston x panw aksona
        plt.show()
        #fig.savefig(stock+'.png') #swzei eikona se png arxeio


    except Exception as e :
        print ('failed main loop', str(e))


graphData(eachstock)



