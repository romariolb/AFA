import csv
import sys
import re
import os
import time


class BuildFiles:

    def __init__(self, file, day):
        self.log = file
        self.day = day
        self.student = None
        self.listStudents = []

    def __str__(self):
        text = ''
        for i in self.listStudents:
            text += str(i) + ' '
        return text

    def progress_bar(self, value, max, barsize):
        chars = int(value * barsize / float(max))
        percent = int((value / float(max)) * 100)
        sys.stdout.write("" * chars)
        sys.stdout.write("" * (barsize - chars + 2))
        if value >= max:
            sys.stdout.write("done. \n\n")
        else:
            sys.stdout.write("[%3i%%]\r" % (percent))
            sys.stdout.flush()

    def create_list(self):
        with open(self.log, 'r') as log:
            reader = csv.reader(log, delimiter=";")

            for linha in reader:
                self.student = linha[6]
                if self.student not in self.listStudents:
                    self.listStudents.append(self.student)
                else:
                    pass
        log.close()

        return self.listStudents
        # print(self.listStudents)

    def verify_file(self, student):
        dir = './logs/' + self.day + '/' +student
        if not os.path.exists(dir):
            os.makedirs(dir)
        elif not os.path.isdir(dir):
            raise IOError(dir + " isn't a path!")

        for file in dir:
            if file == str(student) + '.csv':
                os.remove(file)

        file_log = dir + '/' + str(student) + '.csv'

        if not os.path.exists(file_log):
            with open(file_log, 'w') as file:
                pass
            file.close()

        return file_log

    def create_files(self):
        print('Creating the log files')
        tam_progress = len(self.listStudents)
        for i in self.listStudents:
            self.progress_bar(self.listStudents.index(i), tam_progress, 30)
            file_log = self.verify_file(str(i))
            time.sleep(0.2)
            # print('File ' + file_log + ' was created.\n')

    def fill_files(self):
        print('Filling the individual\'s log')
        tam_progress = len(self.listStudents)
        for i in self.listStudents:
            # print('.')
            self.progress_bar(self.listStudents.index(i), tam_progress, 30)
            name_file_w = './logs/' + self.day + '/' +str(i) + '/' + str(i) + '.csv'
            file_w = open(name_file_w, 'w')
            file_r = open(self.log, 'r')

            reader1 = csv.DictReader(file_r, delimiter=';')
            writer = csv.DictWriter(file_w, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL,
                                    fieldnames=reader1.fieldnames)

            with open(os.path.join(name_file_w), 'w') as csvfile_w:
                writer = csv.DictWriter(csvfile_w, fieldnames=[
                    'field00', 'field01', 'field02', 'field03', 'field04', 'field05', 'field06',
                    'field07', 'field08', 'field09', 'field10', 'field11', 'field12',
                    'field13'
                ], delimiter=';')
                with open(self.log, 'r') as csvfile_r:
                    reader = csv.reader(csvfile_r, delimiter=";")

                    for row in reader:
                        if row[6] == str(i) and row[11] == 'input':
                            dh = dict(
                                field00=row[0], field01=row[1], field02=row[2], field03=row[3],
                                field04=row[4], field05=row[5], field06=row[6], field07=row[7],
                                field08=row[8], field09=row[9], field10=row[10], field11=row[11],
                                field12=row[12], field13=row[13]
                            )
                            writer.writerow(dh)
                        else:
                            pass
            time.sleep(0.2)
            file_w.close()
            file_r.close()

    def findFiles(self, folder, type):
        files = []
        pathAbs = os.path.abspath(folder)
        for actualFolder, subFolder, files_s in os.walk(pathAbs):
            files.extend([os.path.join(actualFolder, file) for file in files_s if file.endswith(type)])
        return files

