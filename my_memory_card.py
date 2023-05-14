from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget,  QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton, QGroupBox, QButtonGroup
from random import shuffle


class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

def next_question():

    shuffle(q_list)#случайный вопрос

    main_win.cur_question = main_win.cur_question + 1 #переход к другому вопросу

    if main_win.cur_question >= len(q_list):
        main_win.cur_question = 0 #при окончании списка вопросов начинаем сначала
        
    q = q_list[main_win.cur_question]
    ask(q)



def click_OK():
    if ans_but.text() == 'Ответить':
        check_answer()
    else:
        next_question()




def ask(q: Question):
    #сначала все спрячем
    RGB.hide()
    grup_ans.hide()
	


	#заполняем неотображаемые радиокнопки значениями
    rbut_1.setText(q.right_answer)
    rbut_2.setText(q.wrong1)
    rbut_3.setText(q.wrong2)
    rbut_4.setText(q.wrong3)
	
	

    #перемешиваем значения
    shuffle(answers)                
    layout_ver1.addWidget(answers[0]) 
    layout_ver1.addWidget(answers[1])
    layout_ver2.addWidget(answers[2]) 
    layout_ver2.addWidget(answers[3])

	

    #сброс флагов
    RadioGroup.setExclusive(False)    
    rbut_1.setChecked(False)
    rbut_2.setChecked(False)
    rbut_3.setChecked(False)
    rbut_4.setChecked(False)
    RadioGroup.setExclusive(True)
	

	
	

    question.setText(q.question)
    answear.setText(q.right_answer)

    RGB.show()
    ans_but.setText('Ответить')



#функция проверки
def check_answer():    
    ans_correct = 'У кого правда тот и сильней'
    ans_wrong = 'Отказать'
    ans_miss = 'Друже, чтобы ответить, ответ надо выбрать'

    if rbut_1.isChecked():
        show_correct(ans_correct)
        main_win.number_right_question += 1
        main_win.number_of_question += 1

    elif rbut_2.isChecked() or rbut_3.isChecked() or rbut_4.isChecked():
        show_correct(ans_wrong)
        main_win.number_of_question += 1

    else:
        show_correct(ans_miss)
        main_win.number_of_question += 1


def show_correct(res):
    #прячим фцнкции
    RGB.hide()
    grup_ans.hide()
    
    #заполняем переменные
    rez_ans.setText(res)
    
    #проявляем обратно
    grup_ans.show()
    ans_but.setText('Следующий вопрос')

      

def show_question():
    RGB.show()
    grup_ans.hide()
    question.setText('Какой национальности не существует?')
    ans_but.setText('Ответить')
    RadioGroup.setExclusive(False)    
    rbut_1.setChecked(False)
    rbut_2.setChecked(False)
    rbut_3.setChecked(False)
    rbut_4.setChecked(False)
    RadioGroup.setExclusive(True)


def show_result():
    RGB.hide()
    grup_ans.show()
    question.setText('Самый слож вопрос')
    ans_but.setText('Следующий вопрос')



def start_test():
    if ans_but.text() == 'Ответить':
        show_result()
    else:
        show_question()



#настройка окна
app = QApplication([])
main_win = QWidget()
main_win.resize(350,250)

main_win.setWindowTitle('Memory Card')

question = QLabel('Какой национальности не существует?')

#статистика
main_win.number_of_question = 0
main_win.number_right_question = 0


#группа
RGB = QGroupBox('Варианты')  
rbut_1 = QRadioButton('Энцы')
rbut_2 = QRadioButton('Смурфы')
rbut_3 = QRadioButton('Чулымцы')
rbut_4 = QRadioButton('Алеуты')



#список с кнопками
answers = [rbut_1, rbut_2, rbut_3, rbut_4]     
layout_gor1 = QHBoxLayout()   
layout_ver1 = QVBoxLayout() 
layout_ver2 = QVBoxLayout()




#групп по функц
RadioGroup = QButtonGroup() 
RadioGroup.addButton(rbut_1)
RadioGroup.addButton(rbut_2)
RadioGroup.addButton(rbut_3)
RadioGroup.addButton(rbut_4)


layout_ver1.addWidget(rbut_1) 
layout_ver1.addWidget(rbut_2)
layout_ver2.addWidget(rbut_3) 
layout_ver2.addWidget(rbut_4)
layout_gor1.addLayout(layout_ver1)
layout_gor1.addLayout(layout_ver2)
layout_ver1.setSpacing(35)
layout_ver2.setSpacing(35)
layout_gor1.setSpacing(35)
RGB.setLayout(layout_gor1)




#кнопка ответа
ans_but = QPushButton('Ответить')     
maim_lin_vert = QVBoxLayout()
maim_lin_gor1 = QHBoxLayout()
maim_lin_gor3 = QHBoxLayout()





#сбор виджетов и группы
maim_lin_gor1.addWidget(question, alignment=Qt.AlignHCenter)   
maim_lin_gor3.addStretch(2)
maim_lin_gor3.addWidget(ans_but, stretch=5)
maim_lin_gor3.addStretch(2)
maim_lin_vert.addLayout(maim_lin_gor1)
maim_lin_vert.addWidget(RGB, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))




#ФОРМА окна результата
grup_ans = QGroupBox('Результат ответа')
rez_ans = QLabel('Прав/неправ')
answear = QLabel('Правильный ответ')
boxline_vert = QVBoxLayout()

boxline_vert.addWidget(rez_ans)
boxline_vert.setSpacing(50)
boxline_vert.addWidget(answear, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))

grup_ans.setLayout(boxline_vert)


#сбор виджетов и двух групп
maim_lin_vert.addWidget(grup_ans, alignment=(Qt.AlignHCenter | Qt.AlignVCenter)) 


#сбор виджетов и двух групп
maim_lin_vert.addLayout(maim_lin_gor3)  


#сбор виджетов и двух групп
main_win.setLayout(maim_lin_vert)       


main_win.cur_question = -1
q_list = list()


q1 = Question('В чём сила брат?',
 'В правде', 'В деньгах', 'В силе', 'В слабости')

q2 = Question('2+2=?',
 '4', '5', '2', '0')

q3 = Question('H2O - это?',
 'вода', 'воздух', 'земля', 'огонь')

q_list.append(q1)
q_list.append(q2)
q_list.append(q3)


#ask(q)

ans_but.clicked.connect(click_OK)
next_question()

#RGB.show()
#grup_ans.hide()



main_win.show()
app.exec_()
wix = main_win.number_right_question/main_win.number_of_question*100
wix = round(wix)
print('Количество всех вопросов',main_win.number_of_question)
print('Количество правильных вопросов',main_win.number_right_question)
print('Рейтинг',wix,'%')