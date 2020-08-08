#!/usr/bin/python3
# -*- coding:utf-8-*-
import tkinter
from tkinter import Frame, LEFT, E, S, W, N, FLAT, SUNKEN, END, BOTH
from tkinter.filedialog import askopenfilename

from utils.logUtil import Log
from gui.context import GuiContext
from storyrunner import StoryRunner
from tkinter import messagebox
import asyncio
import threading

root = tkinter.Tk()

STORY = []


def restart():
    Log.log("Restart")


def quit():
    Log.log("Quit")


async def _do_run():

    await StoryRunner("../story/auto_war.txt", GuiContext(root, text)).read()


def _asyncio_thread(async_loop):
    try:
        async_loop.run_until_complete(_do_run())
    except Exception as e:
        Log.log(e)


def run(async_loop):
    threading.Thread(target=_asyncio_thread, args=(async_loop,)).start()


def pause():
    Log.log("pause ")


def load_story():

    pass

def add_scripts():
    Log.log("Opening file and add script to system ")
    filename = askopenfilename()
    if filename not in STORY:
        STORY.append(filename)
    Log.log("Load new file {}".format(filename))


if __name__ == '__main__':
    root.title("My Game Tool V1.0 @xxlv")
    root.geometry("600x800+610+100")
    async_loop = asyncio.get_event_loop()


    #  Status 200
    #  Task  400
    #  text 200
    #
    info_frame = Frame(root)

    status_frame = Frame(root, height=200, width=800, relief=SUNKEN, takefocus=True, highlightbackground="red")

    task_frame = Frame(root, height=400, width=800)

    # 文本输出绑定滚动条
    text = tkinter.Text(root, bg="black", fg="green", height=200)

    # Set log
    Log.root = root
    Log.text = text

    # 滚动
    scroll = tkinter.Scrollbar(orient="vertical")
    scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)
    scroll.config(command=text.yview)
    text.config(yscrollcommand=scroll.set)

    add_script_btn = tkinter.Button(status_frame, text="Add Scripts", command=add_scripts)

    pause_btn = tkinter.Button(status_frame, text="Pause", command=pause)

    restart_btn = tkinter.Button(status_frame, text="Restart", command=restart)

    quit_btn = tkinter.Button(status_frame, text="quit", command=quit)

    run_btn = tkinter.Button(status_frame, text="run", command=lambda: run(async_loop), bg="Red")

    add_script_btn.pack(padx=5, pady=10, side=LEFT)

    pause_btn.pack(padx=5, pady=20, side=LEFT)

    restart_btn.pack(padx=5, pady=30, side=LEFT)

    run_btn.pack(padx=5, pady=50, side=LEFT)

    quit_btn.pack(padx=5, pady=40, side=LEFT)

    status_frame.pack(padx=0, pady=0)

    task_frame.pack()

    info_frame.pack()

    text.pack(fill=BOTH)

    root.mainloop()
