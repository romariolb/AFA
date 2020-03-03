class Confusion:
    def __init__(self):
        """

        :param corrects: List
        :param incorrect: List
        """
        self.class_corrects = []
        self.class_questions = []
        # self.orderedCorrect = []
        # self.orderedIncorrect = []
        #self.qtd = qtd
        self.sum = 0
        self.score = 0

    def __str__(self):
        text = 'Seu NIVEL DE CONFUSAO e de {}%, com base na quantidade de marcacoes' \
               ' e questoes corretas da sua avaliacao.\n'.format(round(self.score, 2))

        return text

    def num_corrects(self, student_corrects):
        check = 0
        if self.class_corrects == []:
            for item in student_corrects:
                self.class_corrects.append([item[0], item[1].count])
                self.class_questions.append([item[0], item[1].count])
        else:
            for i in student_corrects:
                for j in self.class_corrects:
                    if i[0] == j[0]:
                        j[1] += i[1].count
                        check = 1
                    else:
                        pass
                if check == 0:
                    self.class_corrects.append([i[0], i[1].count])
                    self.class_questions.append([i[0], i[1].count])
                else:
                    check = 0

    def count_marks_questions(self, student_incorrects):
        check = 0
        for i in student_incorrects:
            for j in self.class_questions:
                if i[0] == j[0]:
                        j[1] += i[1].count
                        check = 1
                else:
                    pass
            if check == 0:
                self.class_questions.append([i[0], i[1].count])
            else:
                check = 0
    
    def total_marks_corrects(self):
        for i in self.class_questions:
            self.sum += int(i[1])
    
    def confusionLevel(self):
        if self.sum != 0:
            self.score = float(1.0 - (float(len(self.class_corrects)) / float(self.sum))) * 100
        else:
            pass
        # print(str(self.incorrect))
        """for i in range(len(self.corrects)):
            self.corrects[i].append(self.corrects[i][1].count)
            # print("1 lugar correto")
        for j in range(len(self.incorrect)):
            if self.incorrect[j] is not None:
                self.incorrect[j].append(self.incorrect[j][1].count)
                # print("1 lugar incorreto")
            else:
                self.incorrect[j] = [0, 0, 0]
                # print("1 lugar vazio")
        for item in self.corrects:
            self.sum += item[2]
        for item in self.incorrect:
            self.sum += item[2]

    def calculus(self):
        if self.sum != 0:
            self.score = float(1.0 - (float(len(self.corrects)) / float(self.sum)))
        else:
            pass"""
        

"""
o aluno benjamin fica com esse coeficiente negativo. pq? tem problema?
verificar numero de marcacao do denominador da metrica.
"""