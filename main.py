from multiprocessing import Process
import pyautogui as pag
import keyboard
import sys
try:
    def func1():  
        while True:
            lis=[62,158,256,366,463,566,679,784,877,988,1082]
            
            for i in lis:
                if i==988:
                    lis2=[988,877,784,679,566,463,366,256,158,62]
                    for i in lis2:
                        pag.click(i,16,interval=3.4)
                else:
                    pag.click(i,16,interval=3.4)

            

    def func2():
        while True:
            pag.press('ctrl',interval=2.4)
        

    if __name__ == '__main__':
        p1 = Process(target=func1)
        p1.start()
        p2 = Process(target=func2)
        p2.start()
        p1.join()
        p2.join()
except KeyboardInterrupt:
    sys.exit()




    