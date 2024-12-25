import customtkinter as ctk
import os

def create_icon(master: object):
    path = os.path.abspath(os.path.join(__file__, "..", "..", "..", "static", "icon", "app.ico"))
    master.iconbitmap(path)

