from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api
import numpy as np
import win32con
import cv2 


def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(np.random.uniform(.4,.6))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


time.sleep(10)

if pyautogui.locateOnScreen('search.png', confidence=.8) != None:
      zerocor = pyautogui.locateOnScreen('search.png', confidence=.8)
      print(zerocor)
      m = zerocor[0]
      n = zerocor[1]
      o =  m + zerocor[2]
      p = n + zerocor[3]
      # Set the top-left and bottom-right coordinates of the box
      top_left = (m,n)
      bottom_right = (o,p)
      # Generate a random x-coordinate within the box
      q = np.random.randint(top_left[0], bottom_right[0])
      # Generate a random y-coordinate within the box
      r = np.random.randint(top_left[1], bottom_right[1])
      # Move the mouse cursor to the random coordinates and click
      print(q,r)
      click(q,r)
      time.sleep(np.random.randint(3,8))
     
else:
      print('not found search')
      
      
if pyautogui.locateOnScreen('recent.png', confidence=.8) != None:
          recentcor = pyautogui.locateOnScreen('recent.png', confidence=.8)
          print(recentcor)
          a = recentcor[0]
          b = recentcor[1] + recentcor[3]+ 10
          c =  a + recentcor[2]
          d = b + recentcor[3]
          # Set the top-left and bottom-right coordinates of the box
          top_leftrecent = (a,b)
          bottom_rightrecent = (c,d)
          # Generate a random x-coordinate within the box
          e = np.random.randint(top_leftrecent[0], bottom_rightrecent[0])
          # Generate a random y-coordinate within the box
          f = np.random.randint(top_leftrecent[1], bottom_rightrecent[1])
          # Move the mouse cursor to the random coordinates and click
          print(e,f)
          click(e,f)
          print('clicked on hashtag')
          time.sleep(np.random.randint(3,8))
else:
          print('didnot find recent ')

mostr = None

while mostr is None:
    win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0,  np.random.randint(-400, -300))
    mostr = pyautogui.locateOnScreen('mostr.png', confidence=.8)
    print('rr')
    print(mostr)
    time.sleep(np.random.randint(2,5))
              

print('mostr is not none executed')
a1 = mostr[0]+15
b1 = mostr[1]+10
c1 = a1 + 80
d1 = b1 + 80
top_leftrecent1 = (a1,b1)
bottom_rightrecent1 = (c1,d1)
# Generate a random x-coordinate within the box
e1 = np.random.randint(top_leftrecent1[0], bottom_rightrecent1[0])
# Generate a random y-coordinate within the box
f1 = np.random.randint(top_leftrecent1[1], bottom_rightrecent1[1])
# Move the mouse cursor to the random coordinates and click
print(e1,f1)
click(e1,f1)
print('clicked on post in recent')
time.sleep(np.random.randint(3,8))


region = (812,650,400,400)
if pyautogui.locateOnScreen('like.png',region=region) != None:
        print("found most like")
        like = pyautogui.locateOnScreen('like.png',region=region)
        a2 = like[0]
        b2 = like[1]
        c2 = a2 + like[2]
        d2 = b2 + like[3]
        top_leftlike1 = (a2,b2)
        bottom_rightlike1 = (c2,d2)
        # Generate a random x-coordinate within the box
        e2 = np.random.randint(top_leftlike1[0], bottom_rightlike1[0])
    
        # Generate a random y-coordinate within the box
        f2 = np.random.randint(top_leftlike1[1], bottom_rightlike1[1])

        # Move the mouse cursor to the random coordinates and click
        print(e2,f2)
        click(e2,f2)
        print('liked the post')
        time.sleep(np.random.randint(3,8))

for i in range(10):
  if pyautogui.locateOnScreen('nextp.png',confidence=.8) != None:
        print("found next picture")
        nextp = pyautogui.locateOnScreen('nextp.png')
        a3 = nextp[0]
        b3 = nextp[1]
        c3 = a3 + nextp[2]
        d3 = b3 + nextp[3]
        top_leftnextp = (a3,b3)
        bottom_rightnextp = (c3,d3)   
        # Generate a random x-coordinate within the box
        e3 = np.random.randint(top_leftnextp[0], bottom_rightnextp[0])
        # Generate a random y-coordinate within the box
        f3 = np.random.randint(top_leftnextp[1], bottom_rightnextp[1])
        # Move the mouse cursor to the random coordinates and click
        print(e3,f3)
        click(e3,f3)
        print('clicked next picture')
        time.sleep(np.random.randint(3,8))
  if random.random() < 0.5:
    region = (812,650,400,400)
    if pyautogui.locateOnScreen('like.png',region=region) != None:
        print("found most like")
        like = pyautogui.locateOnScreen('like.png',region=region)
        a2 = like[0]
        b2 = like[1]
        c2 = a2 + like[2]
        d2 = b2 + like[3]
        top_leftlike1 = (a2,b2)
        bottom_rightlike1 = (c2,d2)   
        # Generate a random x-coordinate within the box
        e2 = np.random.randint(top_leftlike1[0], bottom_rightlike1[0])
        # Generate a random y-coordinate within the box
        f2 = np.random.randint(top_leftlike1[1], bottom_rightlike1[1])
        # Move the mouse cursor to the random coordinates and click
        print(e2,f2)
        click(e2,f2)
        print('liked the post')
    if pyautogui.locateOnScreen('comment.png',confidence=.8) != None:
            print("found comment")
            comment = pyautogui.locateOnScreen('comment.png',confidence=.8)
            a8 = comment[0]
            b8 = comment[1]
            c8 = a8 + comment[2]
            d8 = b8 + comment[3]
            top_leftcomment1 = (a8,b8)
            bottom_rightcomment1 = (c8,d8)   
            # Generate a random x-coordinate within the box
            e8 = np.random.randint(top_leftcomment1[0], bottom_rightcomment1[0])
            # Generate a random y-coordinate within the box
            f8 = np.random.randint(top_leftcomment1[1], bottom_rightcomment1[1])
            # Move the mouse cursor to the random coordinates and click
            print(e8,f8)
            click(e8,f8)
            print('clicked on comment')
            # Press the "P" key
            win32api.keybd_event(ord('P'), 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)
            time.sleep(np.random.uniform(.2,.4))
            # Release the "P" key
            win32api.keybd_event(ord('P'), 0, win32con.KEYEVENTF_KEYUP, 0)
            # Press the "o" key
            win32api.keybd_event(ord('O'), 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)
            time.sleep(np.random.uniform(.2,.4))
            # Release the "o" key
            win32api.keybd_event(ord('O'), 0, win32con.KEYEVENTF_KEYUP, 0)
            # Press the "s" key
            win32api.keybd_event(ord('S'), 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)
            time.sleep(np.random.uniform(.2,.4))
            # Release the "s" key
            win32api.keybd_event(ord('S'), 0, win32con.KEYEVENTF_KEYUP, 0)
            # Press the "t" key
            win32api.keybd_event(ord('T'), 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)
            time.sleep(np.random.uniform(.4,.6))
            # Release the "t" key
            win32api.keybd_event(ord('T'), 0, win32con.KEYEVENTF_KEYUP, 0)
            # Press the "O" key
            win32api.keybd_event(ord('O'), 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)
            time.sleep(np.random.uniform(.4,.6))
            # Release the "O" key
            win32api.keybd_event(ord('O'), 0, win32con.KEYEVENTF_KEYUP, 0)
            # Press the "n" key
            win32api.keybd_event(ord('N'), 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)
            time.sleep(np.random.uniform(.4,.6))
            # Release the "n" key
            win32api.keybd_event(ord('N'), 0, win32con.KEYEVENTF_KEYUP, 0)
            # Press the " " key
            win32api.keybd_event(ord(' '), 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)
            time.sleep(np.random.uniform(.4,.6))
            # Release the " " key
            win32api.keybd_event(ord(' '), 0, win32con.KEYEVENTF_KEYUP, 0)
            # Press the "Shift" key
            win32api.keybd_event(win32con.VK_SHIFT, 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)
            time.sleep(np.random.uniform(.3,.5))
            # Press the "2" key
            win32api.keybd_event(ord('2'), 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)
            time.sleep(np.random.uniform(.3,.5))
            # Release the "2" key
            win32api.keybd_event(ord('2'), 0, win32con.KEYEVENTF_KEYUP, 0)
            time.sleep(np.random.uniform(.3,.5))
            # Release the "Shift" key
            win32api.keybd_event(win32con.VK_SHIFT, 0, win32con.KEYEVENTF_KEYUP, 0)
            time.sleep(np.random.uniform(.3,.5))
            # Press the "r" key
            win32api.keybd_event(ord('R'), 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)
            time.sleep(np.random.uniform(.4,.6))
            # Release the "r" key
            win32api.keybd_event(ord('R'), 0, win32con.KEYEVENTF_KEYUP, 0)
            # Press the "o" key
            win32api.keybd_event(ord('O'), 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)
            time.sleep(np.random.uniform(.4,.6))
            # Release the "o" key
            win32api.keybd_event(ord('O'), 0, win32con.KEYEVENTF_KEYUP, 0)
            # Press the "y" key
            win32api.keybd_event(ord('Y'), 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)
            time.sleep(np.random.uniform(.4,.6))
            # Release the "y" key
            win32api.keybd_event(ord('Y'), 0, win32con.KEYEVENTF_KEYUP, 0)
            # Press the "a" key
            win32api.keybd_event(ord('A'), 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)
            time.sleep(np.random.uniform(.4,.6))
            # Release the "a" key
            win32api.keybd_event(ord('A'), 0, win32con.KEYEVENTF_KEYUP, 0)
            # Press the "l" key
            win32api.keybd_event(ord('L'), 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)
            time.sleep(np.random.uniform(.4,.6))
            # Release the "l" key
            win32api.keybd_event(ord('L'), 0, win32con.KEYEVENTF_KEYUP, 0)
            # Press the "c" key
            win32api.keybd_event(ord('C'), 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)
            time.sleep(np.random.uniform(.4,.6))
            # Release the "c" key
            win32api.keybd_event(ord('C'), 0, win32con.KEYEVENTF_KEYUP, 0)
            # Press the "r" key
            win32api.keybd_event(ord('R'), 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)
            time.sleep(np.random.uniform(.4,.6))
            # Release the "r" key
            win32api.keybd_event(ord('R'), 0, win32con.KEYEVENTF_KEYUP, 0)
            # Press the "a" key
            win32api.keybd_event(ord('A'), 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)
            time.sleep(np.random.uniform(.4,.6))
            # Release the "a" key
            win32api.keybd_event(ord('A'), 0, win32con.KEYEVENTF_KEYUP, 0)
            # Press the "f" key
            win32api.keybd_event(ord('F'), 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)
            time.sleep(np.random.uniform(.4,.6))
            # Release the "f" key
            win32api.keybd_event(ord('F'), 0, win32con.KEYEVENTF_KEYUP, 0)
            # Press the "t" key
            win32api.keybd_event(ord('T'), 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)
            time.sleep(np.random.uniform(.4,.6))
            # Release the "t" key
            win32api.keybd_event(ord('T'), 0, win32con.KEYEVENTF_KEYUP, 0)
            # Press the "s" key
            win32api.keybd_event(ord('S'), 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)
            time.sleep(np.random.uniform(.4,.6))
            # Release the "s" key
            win32api.keybd_event(ord('S'), 0, win32con.KEYEVENTF_KEYUP, 0)
            # Press the "o" key
            win32api.keybd_event(ord('O'), 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)
            time.sleep(np.random.uniform(.4,.6))
            # Release the "o" key
            win32api.keybd_event(ord('O'), 0, win32con.KEYEVENTF_KEYUP, 0)
            # Press the "f" key
            win32api.keybd_event(ord('F'), 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)
            time.sleep(np.random.uniform(.4,.6))
            # Release the "f" key
            win32api.keybd_event(ord('F'), 0, win32con.KEYEVENTF_KEYUP, 0)
            # Press the "i" key
            win32api.keybd_event(ord('I'), 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)
            time.sleep(np.random.uniform(.4,.6))
            # Release the "i" key
            win32api.keybd_event(ord('I'), 0, win32con.KEYEVENTF_KEYUP, 0)
            # Press the "n" key
            win32api.keybd_event(ord('N'), 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)
            time.sleep(np.random.uniform(.4,.6))
            # Release the "n" key
            win32api.keybd_event(ord('N'), 0, win32con.KEYEVENTF_KEYUP, 0)
            # Press the "d" key
            win32api.keybd_event(ord('D'), 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)
            time.sleep(np.random.uniform(.4,.6))
            # Release the "d" key
            win32api.keybd_event(ord('D'), 0, win32con.KEYEVENTF_KEYUP, 0)
            # Press the "i" key
            win32api.keybd_event(ord('I'), 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)
            time.sleep(np.random.uniform(.4,.6))
            # Release the "i" key
            win32api.keybd_event(ord('I'), 0, win32con.KEYEVENTF_KEYUP, 0)
            # Press the "a" key
            win32api.keybd_event(ord('A'), 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)
            time.sleep(np.random.uniform(.4,.6))
            # Release the "a" key
            win32api.keybd_event(ord('A'), 0, win32con.KEYEVENTF_KEYUP, 0)
            time.sleep(np.random.randint(3,8))
    if pyautogui.locateOnScreen('post.png',confidence=.8) != None:
                print("found post")
                post = pyautogui.locateOnScreen('post.png',confidence=.8)
                a9 = post[0]
                b9 = post[1]
                c9 = a9 + post[2]
                d9 = b9 + post[3]
                top_leftpost1 = (a9,b9)
                bottom_rightpost1 = (c9,d9)   
                # Generate a random x-coordinate within the box
                e9 = np.random.randint(top_leftpost1[0], bottom_rightpost1[0])
                # Generate a random y-coordinate within the box
                f9 = np.random.randint(top_leftpost1[1], bottom_rightpost1[1])
                # Move the mouse cursor to the random coordinates and click
                print(e9,f9)
                click(e9,f9)
                print('clicked on post')
                print(i)
                time.sleep(np.random.randint(3,10))
    else:
                print('not found post')
            

        
    
            




       
                 


              

      
  

            
        
