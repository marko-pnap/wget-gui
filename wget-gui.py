#!/usr/bin/python

import gi
import os
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk


class AppWindow(Gtk.ApplicationWindow):

    def __init__(self, app):

        super(AppWindow, self).__init__(application=app)
        self.set_title('wget-gui')
        self.label()

    def label(self):
        box1 = Gtk.Box.new(Gtk.Orientation.VERTICAL, 0)
        text = Gtk.Label(label="\nEnter the download URL:\n")
        box1.append(text)

        self.set_child(box1)

        global dia
        dia = Gtk.Entry()
        dia.connect('activate', user_input)
        box1.append(dia)
        self.set_default_size(350, 150)
        self.set_child(box1)


def on_activate(app):

    win = AppWindow(app)
    win.present()

def user_input(self):
    this = dia.get_text()
    wget_this = "wget " + this
    os.system(wget_this)

app = Gtk.Application(application_id='com.zetcode.QuitButton')
app.connect('activate', on_activate)
app.run(None)
