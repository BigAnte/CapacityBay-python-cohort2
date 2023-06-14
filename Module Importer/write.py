# when this programm is ran, it write the content here into db.py
def write(main):
    read = open(main, "r")
    result = read.read()
    read.close()
    write = open("db.py", "w")
    write.write(result)
    write.close()


write("main.py")
