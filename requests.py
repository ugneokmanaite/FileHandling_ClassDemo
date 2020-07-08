from text_file import TextFileHandling

file_path = "order.txt"
# by putting the file path here and importing the class we only need to change the file path once if we need to
text_file = TextFileHandling(file_path)

# print(text_file.read_text())
#
# text_file.write_text_file()

# print(text_file.write_text_file())

# print(text_file.read_text_file_using_with())

print(text_file.write_text_file_using())

