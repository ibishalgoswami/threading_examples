from threading import *
import pyautogui as pag
import time
   
class First(Thread):
    def run(self):
        try:

            while True:
                print("Hello")
                lis=[53,142,241,336,422,521,610,708,812,896,983,1084] 
                for i in lis:
                    if i==1084:
                        lis2=[1084,983,896,812,708,610,521,422,336,241,142,53]
                        for i in lis2:
                            pag.click(i,16,interval=2.1)
                    else:
                        pag.click(i,16,interval=2.1)
        except KeyboardInterrupt:
            print('\n')

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

