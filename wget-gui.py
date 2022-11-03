#!/usr/bin/python
# Importing libraries
import gi
import os
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk

#Defining a class. This looks like the main class in this program.
class AppWindow(Gtk.ApplicationWindow):
#Defining methods/functions. __init__ looks like the main one.
    def __init__(self, app):
        super(AppWindow, self).__init__(application=app)
#The following is the main window of the app.
        global mainWindow
        mainWindow = Gtk.Box.new(Gtk.Orientation.VERTICAL, 0)
#The elements inside the window.
        self.set_title('wget-gui')
        self.label()
        self.text_box()
        self.quit_button()
#Now each of the elements gets defined.
    def label(self):
        labelText = Gtk.Label(label="\nEnter the download URL:\n")
        mainWindow.append(labelText)
        self.set_child(mainWindow)
    def text_box(self):
        global textBoxInput
        textBoxInput = Gtk.Entry()
        textBoxInput.connect('activate', user_input)
        mainWindow.append(textBoxInput)
        self.set_child(mainWindow)
    def quit_button(self):
        quitButton = Gtk.Button(label="Quit")
        quitButton.connect('clicked', lambda _: self.close())
        quitButton.set_halign(Gtk.Align.CENTER)
        quitButton.set_valign(Gtk.Align.CENTER)
        quitButton.set_margin_top(20)
        mainWindow.append(quitButton)
        self.set_default_size(350, 195)
        self.set_child(mainWindow)
#Unclear what this means. Probably a way to keep the app running.
def on_activate(app):
    win = AppWindow(app)
    win.present()
#Defining my input method.
def user_input(self):
    inputUrl = textBoxInput.get_text()
    wget_this = "echo " + inputUrl
    os.system(wget_this)

app = Gtk.Application(application_id='com.markosoft.WgetGui')
app.connect('activate', on_activate)
app.run(None)
