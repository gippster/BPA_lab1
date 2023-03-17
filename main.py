import Parser

if __name__ == '__main__':
    f = open("departments.txt", "w")
    departments = Parser.parse()
    f.write(departments.replace('  ', ' ')) #Замена nonBreakSpace на обычные пробелы