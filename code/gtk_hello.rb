require 'gtk2'

# 配置する部品-----------------------------
scrolled_window = Gtk::ScrolledWindow.new
label = Gtk::Label.new("hello, world!")

# window全体のアレ-------------------------
window = Gtk::Window.new 
window.signal_connect("destroy") do
	Gtk.main_quit
end

window.title = "Hello World"
window.set_default_size(260, 60)

# windowにscrolled_windowを追加する。
window.add(scrolled_window)

# -----------------------------------------
# こんな感じで入れ子に出来る
scrolled_window.add(label)


window.show_all
Gtk.main
