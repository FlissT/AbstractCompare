#!/usr/bin/env python3

import webbrowser
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Pango

class AbsBox(Gtk.Bin):
    def __init__(self):
        Gtk.Bin.__init__(self)

        self.builder = Gtk.Builder()
        self.builder.add_from_file("abs_comp.glade")
        self.abs_box = self.builder.get_object("GtkBox")
        self.add(self.abs_box)
        self.absbox1 = self.builder.get_object("GtkEntry1")
        self.absbox2 = self.builder.get_object("GtkEntry2")
        self.label = self.builder.get_object("GtkLabel")
        self.button = self.builder.get_object("GtkButton")
        self.button.connect("clicked", self.clicked_callback)

    def abs_comp(self): #compares abstracts
        abs1 = self.absbox1.get_text()
        abs2 = self.absbox2.get_text()
        abs_result = (abs1) == (abs2)
        if abs_result == True:
            self.label.set_text(str(abs_result) + ", these abstracts match")
        elif abs_result == False:
            self.label.set_text(str(abs_result) + ", these abstracts do not match")

        
    def clicked_callback(self, button): #runs function when button is clicked
        self.abs_comp()
        

class MyWindow(Gtk.Window): #makes the overall display window

    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_size_request(300, 300)
        
        vbox = Gtk.VBox()
        abs_box = AbsBox()
        vbox.add(abs_box)
        self.add(vbox)
        
        self.show_all()
        self.connect("delete-event", self.on_quit)

    def on_quit(self, widget, event):
        Gtk.main_quit()

       
window = MyWindow()

Gtk.main()
