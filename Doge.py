from tkinter import *
import random
import winsound
import threading
import pyautogui
import os

pyautogui.FAILSAFE = False
def mouse_mover(x,y):
    pyautogui.moveTo(x, y, 10)



def R_run(ind, target_x, target_y, speed_factor, reserved_move=False, to_action=True):
    dx = (target_x - win.winfo_x()) // 200 * speed_factor
    dy = (target_y - win.winfo_y()) // 200 * speed_factor
    if (dx != 0) or (dy != 0):
        win.geometry(window_width + "x" + window_height + "+{}+{}".format(win.winfo_x() + dx, win.winfo_y()+dy))
        if ind == len(R_run_image):
            global Doge_direction
            Doge_direction = 'R'
            win.after(20, R_run, 0, target_x, target_y, speed_factor, reserved_move, to_action)
        else:
            frame = R_run_image[ind]
            ind += 1
            Doge.configure(image=frame)
            win.after(20, R_run, ind, target_x, target_y, speed_factor, reserved_move, to_action)
    else:
        if reserved_move:
            win.after(20, action, reserved_move)
        elif to_action:
            action()
        else:
            pass

def L_run(ind, target_x, target_y, speed_factor, reserved_move=False, to_action=True):
    dx = (target_x - win.winfo_x()) // 200 * speed_factor
    dy = (target_y - win.winfo_y()) // 200 * speed_factor
    if (dx != 0) or (dy != 0):
        win.geometry(window_width + "x" + window_height + "+{}+{}".format(win.winfo_x() + dx, win.winfo_y()+dy))
        if ind == len(L_run_image):
            global Doge_direction
            Doge_direction = 'L'
            win.after(20, L_run, 0, target_x, target_y, speed_factor, reserved_move, to_action)
        else:
            frame = L_run_image[ind]
            ind += 1
            Doge.configure(image=frame)
            win.after(20, L_run, ind, target_x, target_y, speed_factor, reserved_move, to_action)
    else:
        if reserved_move:
            win.after(20, action, reserved_move)
        elif to_action:
            action()
        else:
            pass



def R_wow(ind):
    if ind == len(R_wow_image): #end of wow, choose next action
        Doge.configure(image=R_idle_image)
        win.after(200, action)
    else:
        if ind == 0 :
            wow_window = Toplevel(win)
            wow_window.title('Wow!')
            wow_window.wm_attributes('-topmost', 1)
            wow_window.geometry(
                "288x175+{}+{}".format(win.winfo_x() + random.randint(-2, 2)*70, win.winfo_y() + random.randint(-2, 2)*70))
            wow_label = Label(wow_window, image=Wow_image_1)
            wow_label.pack()

            winsound.PlaySound('asset/sound/wow.wav', winsound.SND_ASYNC)
        win.lift()
        frame = R_wow_image[ind]
        ind += 1
        Doge.configure(image=frame)
        win.after(50, R_wow, ind)

def L_wow(ind):
    if ind == len(L_wow_image): #end of wow, choose next action
        Doge.configure(image=L_idle_image)
        win.after(200, action)
    else:
        if ind == 0 :
            wow_window = Toplevel(win)
            wow_window.title('Wow!')
            wow_window.wm_attributes('-topmost', 1)
            wow_window.geometry(
                "308x232+{}+{}".format(win.winfo_x() + random.randint(-3, 3)*70, win.winfo_y() + random.randint(-3, 3)*70))
            wow_label = Label(wow_window, image=Wow_image_2)
            wow_label.pack()

            winsound.PlaySound('asset/sound/wow.wav', winsound.SND_ASYNC)
        win.lift()
        frame = L_wow_image[ind]
        ind += 1
        Doge.configure(image=frame)
        win.after(50, L_wow, ind)

def R_lick(ind):
    if ind == len(R_lick_image):  # end of wow, choose next action
        action()
    else:
        if ind == 0 :
            pass
        frame = R_lick_image[ind]
        ind += 1
        Doge.configure(image=frame)
        win.after(50, R_lick, ind)

def L_lick(ind):
    if ind == len(L_lick_image):  # end of wow, choose next action
        action()
    else:
        if ind == 0:
            pass
        win.lift()
        frame = L_lick_image[ind]
        ind += 1
        Doge.configure(image=frame)
        win.after(50, L_lick, ind)

def R_bomb(ind, count=0):
    if ind == len(R_bomb_image):  # end of wow, choose next action
        if count == 80:
            action()
        else:
            count += 1
            win.after(50, R_bomb, 0, count)
    else:
        if ind == 0 and count == 0:
            tor_window = Toplevel(win)
            tor_window.overrideredirect(True)
            tor_window.wm_attributes('-transparentcolor', 'white')
            tor_window.title('Torando')
            tor_window.wm_attributes('-topmost', 1)
            tor_window.lift()
            tor_window.geometry(
                "180x232+{}+{}".format(win.winfo_x()-50,win.winfo_y()-32))
            tor_label = Label(tor_window, image=Tor_image)
            tor_label.pack()

            winsound.PlaySound('asset/sound/wind.wav', winsound.SND_ASYNC)
            move_thread = threading.Thread(target=mouse_mover, args=(win.winfo_x()+40, win.winfo_y()+40,))
            move_thread.start()
        win.lift()
        frame = R_bomb_image[ind]
        ind += 1
        Doge.configure(image=frame)
        win.after(20, R_bomb, ind, count)

def L_bomb(ind, count=0):
    if ind == len(L_bomb_image):  # end of wow, choose next action
        if count == 80:
            action()
        else:
            count += 1
            win.after(30, L_bomb, 0, count)
    else:
        if ind == 0 and count == 0:
            tor_window = Toplevel(win)
            tor_window.overrideredirect(True)
            tor_window.wm_attributes('-transparentcolor', 'white')
            tor_window.title('Torando')
            tor_window.wm_attributes('-topmost', 1)
            tor_window.geometry(
                "180x232+{}+{}".format(win.winfo_x()-50, win.winfo_y()-32))
            tor_label = Label(tor_window, image=Tor_image)
            tor_label.pack()
            winsound.PlaySound('asset/sound/wind.wav', winsound.SND_ASYNC)
            move_thread = threading.Thread(target=mouse_mover, args=(win.winfo_x() + 40, win.winfo_y() + 40,))
            move_thread.start()
        win.lift()
        frame = L_bomb_image[ind]
        ind += 1
        Doge.configure(image=frame)
        win.after(20, L_bomb, ind, count)

def R_idle():
    Doge.configure(image=R_idle_image)
    win.after(800, action)


def L_idle():
    Doge.configure(image=L_idle_image)
    win.after(800, action)


def text_popup():
    if Doge_direction == 'R':
        Doge.configure(image=R_idle_image)
    else:
        Doge.configure(image=L_idle_image)
    txt_choice = random.choice(Txts)
    os.startfile(txt_choice)
    win.after(200, action)

def image_popup(count = 0, image_window = None, pos=0):
    if count == 301 and pos==0 :
        win.after(600, action)
    elif count == 171 and pos == 1:
        win.after(600, action)
    elif count == 0:
        if Doge_direction == 'R':
            Doge.configure(image=R_idle_image)
        else:
            Doge.configure(image=L_idle_image)
        positions = [(-300, win.winfo_y()), (win.winfo_x(), -170)]
        pos = random.randint(0,1)
        position = positions[pos]
        im_window = Toplevel(win)
        im_window.overrideredirect(True)
        im_window.title('ㅋㅋ루ㅋㅋ')
        im_window.geometry(
            "300x170+{}+{}".format(position[0], position[1]))
        im_label = Label(im_window, image=random.choice(Pop_imgs))
        im_label.pack()
        count += 1
        win.after(1,image_popup, count, im_window, pos)
    else:
        image_window.lift()
        if pos == 0:
            image_window.geometry("300x170+{}+{}".format(image_window.winfo_x()+1, image_window.winfo_y()))
        else:
            image_window.geometry("300x170+{}+{}".format(image_window.winfo_x(), image_window.winfo_y()+1))
        count +=1
        win.after(1,image_popup, count, image_window, pos)



def action(action=None):
    if not action:
        next_action = random.choice(actions)
    else :
        next_action = action
    print(next_action)
    if Doge_direction == 'R':
        Doge.configure(image=R_idle_image)
    else:
        Doge.configure(image=L_idle_image)

    if next_action == 'run':
        target_x = random.randint(0,width-int(window_width))
        target_y = random.randint(0,height-int(window_height))
        if target_x > win.winfo_x():
            win.after(1, R_run, 0, target_x, target_y, 2)
        else:
            win.after(1, L_run, 0, target_x, target_y, 2)
    elif next_action == 'wow':
        if Doge_direction == 'R':
            win.after(1, R_wow, 0)
        else:
            win.after(1, L_wow, 0)

    elif next_action == 'lick':
        if Doge_direction == 'R':
            win.after(1, R_lick, 0)
        else:
            win.after(1, L_lick, 0)

    elif next_action == 'dodge':
        if Doge_direction == 'R':
            win.after(1, R_bomb, 0)
        else:
            win.after(1, L_bomb, 0)
    elif next_action == 'image_popup':
        win.after(1, image_popup)
    elif next_action == 'idle':
        if Doge_direction == 'R':
            win.after(1, R_idle)
        else:
            win.after(1, L_idle)
    else:
        win.after(1, text_popup)

#define actions
'''
actions = []
for i in range(30):
    actions.append('run')
for i in range(10):
    actions.append('wow')
for i in range(10):
    actions.append('lick')
for i in range(5):
    actions.append('image_popup')
for i in range(5):
    actions.append('text_popup')
for i in range(15):
    actions.append('idle')
for i in range(3):
    actions.append('dodge')
'''
actions = ['run', 'wow', 'lick', 'image_popup', 'text_popup', 'idle', 'dodge']
#actions = ['wow']

#Create Tk instance
win = Tk()

#Parameter for screen_width&height, window_width&height
width = win.winfo_screenwidth()
height = win.winfo_screenheight()
window_width = "76"
window_height = "78"

#for invisible titlebar
win.overrideredirect(True)

#always on top
win.wm_attributes('-topmost',1)

#for transparent background
win.wm_attributes('-transparentcolor','white')

#move to default starting point
win.geometry(window_width+"x"+window_height+"+500+500")

#Create Components====================================================================================

#Get text
Txts = [os.path.join(os.getcwd(), 'asset/TXT/TXT_1.txt'), os.path.join(os.getcwd(), 'asset/TXT/TXT_2.txt'),  os.path.join(os.getcwd(), 'asset/TXT/TXT_3.txt')]
#Get images of Doge
R_idle_image = PhotoImage(file='asset/sprite_sheet/Idle/R_idle.png')
R_run_image = [PhotoImage(file='asset/sprite_sheet/R_run/{}.png'.format(i)) for i in range(2,10)]
R_wow_image = [PhotoImage(file='asset/sprite_sheet/R_wow/{}.png'.format(i)) for i in range(1,13)]
R_lick_image = [PhotoImage(file='asset/sprite_sheet/R_lick/{}.png'.format(i)) for i in range(1,13)]
R_bomb_image = [PhotoImage(file='asset/sprite_sheet/R_bomb/{}.png'.format(i)) for i in range(1,5)]

L_idle_image = PhotoImage(file='asset/sprite_sheet/Idle/L_idle.png')
L_run_image = [PhotoImage(file='asset/sprite_sheet/L_run/{}.png'.format(i)) for i in range(2,10)]
L_wow_image = [PhotoImage(file='asset/sprite_sheet/L_wow/{}.png'.format(i)) for i in range(1,13)]
L_lick_image = [PhotoImage(file='asset/sprite_sheet/L_lick/{}.png'.format(i)) for i in range(1,13)]
L_bomb_image = [PhotoImage(file='asset/sprite_sheet/L_bomb/{}.png'.format(i)) for i in range(1,5)]

Wow_image_1 = PhotoImage(file='asset/static_image/wow.png')
Wow_image_2 = PhotoImage(file='asset/static_image/wow_2.png')
Tor_image = PhotoImage(file='asset/static_image/tornado.png')

Pop_img_1 = PhotoImage(file='asset/static_image/Doge.png')
Pop_img_2 = PhotoImage(file='asset/static_image/Muscle_doge.png')
Pop_img_3 = PhotoImage(file='asset/static_image/Rainboe_doge.png')
Pop_img_4 = PhotoImage(file='asset/static_image/Thug_doge.png')
Pop_imgs = [Pop_img_1, Pop_img_2, Pop_img_3, Pop_img_4]

#Create Label for Doge
Doge = Label(win, image=R_idle_image)

Doge_direction = 'R' #initial direction of Doge
Doge.pack()

win.after(1500, action)

#Start loop===============================================================================================
win.mainloop()