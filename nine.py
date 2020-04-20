from threading import *
import pyautogui as pag
import time
   
class First(Thread):
    def run(self):
        while True:
            print("Hello")
            lis=[64,201,320,443,580,679,802,940,1070] 
            for i in lis:
                if i==1070:
                    lis2=[1070,940,802,679,580,443,320,201,64]
                    for i in lis2:
                        pag.click(i,16,interval=2.1)
                else:
                    pag.click(i,16,interval=2.1)

class Second(Thread):
    def run(self):
        while True:
            print("World")
            pag.press('ctrl',interval=1.9)
              
if __name__ == '__main__':
    
    p1 = First()
    p2 = Second()
    p1.start()
    time.sleep(1)
    p2.start()
    p1.join()
    p2.join()
    

                    
