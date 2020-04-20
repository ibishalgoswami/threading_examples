# from multiprocessing import Process
# from threading import *
# import pyautogui as pag
# import time

# class First(Thread):
#     def run(self):
#         while True:
#             print("Hello",time.time())
#             time.sleep(2)
    
# class Second(Thread):
#     def run(self):
#         while True:
#             print("World",time.time())
#             time.sleep(2)
    

# if __name__ == '__main__':
#     p1 = First()
#     p2 = Second()
#     p1.start()
#     time.sleep(1)
#     p2.start()
#     p1.join()
#     p2.join()




import pyautogui
print(pyautogui.displayMousePosition())



import time
import keyboard

i=1
while i<10:
    print("Python")
    i=i+1
    time.sleep(2)
    if keyboard.is_pressed("p"):
        print("You pressed p")
        break



