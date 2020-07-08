class TextFileHandling:

    def __init__(self, file_path, text_storage=None):
        self.file_path = file_path
        self.text_storage = text_storage

    # going to read in two ways and write in two ways

    # creating some methods

    # opening file
    # reading the file
    # closing the file
    def read_text(self):
        # read file
        # self.text_storage = file.read()
    #   self.text_storage = file.read(3) - #will print 3 first characters
    #     self.text_storage = file.readline() # will read first line from current position
        #self.text_storage = file.readline()
        # self.file.seek(0)
       #  self.file.seek(0)
    #     self.text_storage = file.readlines() # will read the rest of the lines from current position
        #file.seek(0)
        #file.seek(3,2)
       #  self.text_storage = file.readline()
        # print(file.tell()) # the pointer is at the current position and will start reading from there
        # close file
        #file.close()
        return self.text_storage

    def write_text_file(self):
        # it will create or override file
        file = open("writer.txt", "w")
        file.write("My first python created file")
        file.close()
        # file = open("writer.txt", "a") #append mode a+ means append and read
        file = open("writer.txt", "a+") # append and read
        file.write("\n I am overriding the file")
        file.seek(0)
        self.text_storage = file.read() # storing what I read from the file to the instance variable
        file.close()
        print(file.closed) # gives me the status of closure, # true because its closed
        print(file.name) # which file were working on currently
        print(file.mode)
        return self.text_storage

    def read_text_file_using_with(self):
        # to reduce the overhead of closing files
        # open the file and read it. No overhead of closing
        # automatically closes the file and also closes it during times of exception being raised
        with open("order.txt", "r") as file:
            self.text_storage = file.read()
            return self.text_storage

    def write_text_file_using(self):
        with open("writer.txt", "w+") as file: # w+ means write and read mode
            file.write("Using writer with functionality")
            print(file.tell()) # just to see where we are at - tells current position of your pointer
            file.seek(0) # repositioning the pointer to the beginning
            self.text_storage = file.read()
            return self.text_storage

    def playing_with_python_OS_module(self):
        import os
        print(os.getcwd()) # current working directory
        # os.remove("writer.txt") # this will remove the file
        # os.rmdir() # this will remove the folder
        # print(os.listdir()) # listening files and directories
        # os.rename('order.txt','modified.txt') #renaming
        #os.chdir("C:/Users/Ugne/Desktop/Holiday pictures")
        #print((os.getcwd()))
        # os.mkdir("Ugne") # adding directory
        # os.rmdir("Ugne") # removing directory
        os.chdir("C:/Users/Ugne/PycharmProjects/FileHandling_ClassDemo/")
        print((os.getcwd()))

    def playing_with_exception(self):
        try:
            file = open(self.file_path, 'r')
        except Exception as e:
            print(e)
            print("File is not present")
        else:
            self.text_storage = file.read()
            file.close()
        finally:
            print("Will run for sure")
            return self.text_storage


