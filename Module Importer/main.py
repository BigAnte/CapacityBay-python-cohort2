def myfunction(filename):
    f = open(filename, "r")
    result = f.read()
    print(result)


myfunction('./Module Importer/data.txt')
