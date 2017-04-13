import requests
import sys
import time
import os
def download(URL,DIR,Name,Type):
        HideLayer = True
        x = URL
        z = DIR
        y = Name 
        r = requests.get(URL,stream=True)
        try : 
                k = r.headers.get('content-length')
                k = float(k)
                c = round(k/(1024*1024),3)
                t1 = 1
        except :
                if not os.path.exists(y):
                        os.makedirs(y)
                with open ( str(z) +'\\' + str(y) +'.'+Type, 'wb') as file :
                    for chunk in r.iter_content(chunk_size=1024*1024):
                            file.write(chunk)
                            if (HideLayer == True):
                                continue 
                            rate = round(1/(time.clock()-t1),3)
                            print ('RATE = ' +str(rate) +' MB/s')
                            t1 = time.clock()
                            size = round(float(os.path.getsize(str(z)+'\\'+ str(y) +'.'+Type))/(1024*1024),3)
                            print ('DOWNLOADED = ' + str(size) + ' of '+ str(c) + '\n Percentage = ' + str(round((size/c)*100,3))+' \n ETA: ' + str(round(((c - size)/rate)/60,3))+ ' Mins')

