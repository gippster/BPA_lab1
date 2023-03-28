def file(departments):
    f = open("departments.txt", "w")
    for i in departments:
        f.write(i)  # Замена nonBreakSpace на обычные пробелы
        f.write('\n')