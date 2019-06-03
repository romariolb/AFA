import csv
import re
import os


class BuildFiles:

    def __init__(self):
        self.student = None
        self.listStudents = []

    def __str__(self):
        text = ''
        for i in self.listStudents:
            text += str(i) + ' '
        return text

    def create_list(self, file):
        with open(file, 'r') as log:
            reader = csv.reader(log, delimiter=";")

            for linha in reader:
                self.student = linha[6]
                if self.student not in self.listStudents:
                    self.listStudents.append(self.student)
                else:
                    pass
        log.close()

        print(self.listStudents)

    def create_files(self, file):
        for i in self.listStudents:
            student = './Support/Files/logs_teste/'+str(i)+'.csv'

            fin = open(file, 'r')
            fout = open(student, 'w')

            reader = csv.DictReader(fin, delimiter=';')
            writer = csv.DictWriter(fout, delimiter=';', quotchar='"', quoting=csv.QUOTE_ALL, fieldnames=reader.fieldnames)

            fin.close()
            fout.close()

            print('\nArquivo criado\n')

