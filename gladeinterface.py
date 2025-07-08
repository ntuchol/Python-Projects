import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="My Glade App")

        builder = Gtk.Builder()
        builder.add_from_file("example.glade")
        builder.connect_signals(self)

        self.window = builder.get_object("window1")
        self.label = builder.get_object("label1")
        self.button = builder.get_object("button1")

        self.window.add(self.label)
        self.window.add(self.button)

    def on_button1_clicked(self, button):
        self.label.set_text("Button clicked!")

    def on_window1_destroy(self, window):
        Gtk.main_quit()

window = MyWindow()
window.window.show_all()
Gtk.main()