from tkinter import *
import random
import winsound
import threading
import pyautogui


def mouse_mover(x,y):
    pyautogui.moveTo(x, y, 0.1)
    '''
    move_thread = threading.Thread(target=mouse_mover, args=(win.winfo_x(), win.winfo_y(),))
    move_thread.start()
    '''

def mover():
    x = random.randint(0, width-int(window_width))
    y = random.randint(0, height-int(window_height))
    loc = window_width+"x"+window_height+"+{}+{}".format(x, y)

    print(win.winfo_x())
    if x!=win.winfo_x() and y != win.winfo_y():
        dx = (x - win.winfo_x()) // abs(x - win.winfo_x())
        dy = (y - win.winfo_y()) // abs(y - win.winfo_y())
        win.geometry(window_width+"x"+window_height+"+{}+{}".format(win.winfo_x()+dx, win.winfo_y()+dy))
    win.after(60, mover)


def R_run(ind, target_x, target_y, speed_factor, reserved_move=False):
    dx = (target_x - win.winfo_x()) // 200 * speed_factor
    dy = (target_y - win.winfo_y()) // 200 * speed_factor
    if (dx != 0) or (dy != 0):
        win.geometry(window_width + "x" + window_height + "+{}+{}".format(win.winfo_x() + dx, win.winfo_y()+dy))
        if ind == len(R_run_image):
            global Doge_direction
            Doge_direction = 'R'
            win.after(20, R_run, 0, target_x, target_y, speed_factor, reserved_move)
        else:
            frame = R_run_image[ind]
            ind += 1
            Doge.configure(image=frame)
            win.after(20, R_run, ind, target_x, target_y, speed_factor, reserved_move)
    else:
        if reserved_move:
            win.after(20, action, reserved_move)
        else:
            action()

def L_run(ind, target_x, target_y, speed_factor, reserved_move=False):
    dx = (target_x - win.winfo_x()) // 200 * speed_factor
    dy = (target_y - win.winfo_y()) // 200 * speed_factor
    if (dx != 0) or (dy != 0):
        win.geometry(window_width + "x" + window_height + "+{}+{}".format(win.winfo_x() + dx, win.winfo_y()+dy))
        if ind == len(L_run_image):
            global Doge_direction
            Doge_direction = 'L'
            win.after(20, L_run, 0, target_x, target_y, speed_factor)
        else:
            frame = L_run_image[ind]
            ind += 1
            Doge.configure(image=frame)
            win.after(20, L_run, ind, target_x, target_y, speed_factor)
    else:
        if reserved_move:
            win.after(20, action, reserved_move)
        else:
            action()

def R_wow(ind):
    if ind == len(R_wow_image): #end of wow, choose next action
        action()
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
        action()
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

def R_bomb(ind):
    if ind == len(R_bomb_image):  # end of wow, choose next action
        action()
    else:
        if ind == 0:
            pass
        win.lift()
        frame = R_bomb_image[ind]
        ind += 1
        Doge.configure(image=frame)
        win.after(50, R_bomb, ind)

def L_bomb(ind):
    if ind == len(L_bomb_image):  # end of wow, choose next action
        action()
    else:
        if ind == 0:
            pass
        win.lift()
        frame = L_bomb_image[ind]
        ind += 1
        Doge.configure(image=frame)
        win.after(50, L_bomb, ind)

def R_idle():
    Doge.configure(image=R_idle_image)
    win.after(100, action)


def L_idle():
    Doge.configure(image=L_idle_image)
    win.after(100, action)


def text_popup():
    action()

def image_popup():
    action()



def action(action=None):
    actions = ['run', 'wow', 'lick', 'dodge', 'image_popup', 'text_popup', 'idle']
    #actions = ['run', 'lick']
    if not action:
        next_action = random.choice(actions)
    else :
        next_action = action
    print(next_action)
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
#Create Label for Doge
Doge = Label(win, image=R_idle_image)

Doge_direction = 'R' #initial direction of Doge
Doge.pack()

win.after(60, action)

#Start loop===============================================================================================
win.mainloop()
