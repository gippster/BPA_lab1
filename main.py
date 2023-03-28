import Parser
import addtofile

if __name__ == '__main__':
    departments = Parser.parse()
    addtofile.file(departments)