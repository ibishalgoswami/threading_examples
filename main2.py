from threading import *
import pyautogui as pag
import time
   
class First(Thread):
    def run(self):
        while True:
            print("Hello")
            lis=[62,158,256,366,463,566,679,784,877,988,1082] 
            for i in lis:
                if i==988:
                    lis2=[988,877,784,679,566,463,366,256,158,62]
                    for i in lis2:
                        pag.click(i,16,interval=2.5)
                else:
                    pag.click(i,16,interval=2.5)

class Second(Thread):
    def run(self):
        while True:
            print("World")
            pag.press('ctrl',interval=1.5)
              
if __name__ == '__main__':
    
    p1 = First()
    p2 = Second()
    p1.start()
    time.sleep(1)
    p2.start()
    p1.join()
    p2.join()
    
                    
