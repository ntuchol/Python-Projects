Import pakage
from multiclipboard import multiclipboard

bd_file = "c:\\user\\my_files"

my_multiclipboard = multiclipboard.Multiclipboard(bd_file)


my_multiclipboard.save_text ("key4")

my_multiclipboard.save_text ("key2", text="Example text to save")

text = my_multiclipboard.get_text ("key2")
print (text)

my_multiclipboard.copy_text ("key4")

my_multiclipboard.delete_keyword (1)

my_multiclipboard.delete_all()

my_multiclipboard.list_keywords()

