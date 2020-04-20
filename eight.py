from threading import *
import pyautogui as pag
import time
   
class First(Thread):
    def run(self):
        while True:
            print("Hello")
            lis=[72,219,359,499,652,784,922,1056] 
            for i in lis:
                if i==1056:
                    lis2=[1056,922,784,652,499,359,219,72]
                    for i in lis2:
                        pag.click(i,16,interval=1.9)
                else:
                    pag.click(i,16,interval=1.9)

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
    
                    
