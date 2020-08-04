#!/usr/bin/python3
# -*- coding:utf-8-*-
import tkinter
from tkinter import Frame, LEFT, E, S, W, N
from utils.logUtil import Log

from storyrunner import StoryRunner

def restart():
    Log.log("Restart")

def quit():
    Log.log("Quit")

def run():

    StoryRunner("auto_war.txt").read()
    Log.log("Running ")


def pause():
    Log.log("pause ")

def add_scripts():
    Log.log("Opening file and add script to system  ")


if __name__=='__main__':
    root = tkinter.Tk()
    root.title("My Game Tool V1.0 @xxlv")
    root.geometry("600x800+610+100")
    info_frame =Frame(root)
    status_frame = Frame(root,height=200,width=800,bd=0)
    task_frame = Frame(root,height=600,width=800)




    add_script = tkinter.Button(status_frame, text="Add Scripts", command=add_scripts)

    pause = tkinter.Button(status_frame, text="Pause", command=pause)

    restart = tkinter.Button(status_frame, text="Restart", command=restart)

    quit = tkinter.Button(status_frame, text="quit", command=quit)

    run = tkinter.Button(status_frame, text="run", command=run,bg="Red")

    task_list=tkinter.Label(root,text="--------------------------------------------TASK LIST--------------------------------------------")

    add_script.pack()
    pause.pack()
    restart.pack()
    quit.pack()
    run.pack()
    task_list.pack()

    status_frame.pack(padx=100, pady=100)

    task_list.pack()

    task_frame.pack(padx=10, pady=10)

    info_frame.pack(padx=10, pady=10)
    root.mainloop()

