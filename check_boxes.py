from PyQt5.QtWidgets import QApplication, QDialog, QWidget, QMainWindow, QPushButton, QHBoxLayout, QCheckBox
import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Subject import subject
import json
from PyQt5.QtCore import Qt
from Subject import subject
from time_spent_object import time_spent


class GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 800, 500)
        self.setWindowTitle("Time management app")
        self.setStyleSheet("background-color:white")
        self.layout = QGridLayout(self)
        self.childLayout = QVBoxLayout(self)
        self.layout.addLayout(self.childLayout, 2, 2)
        stop_watch_widget = QWidget(self.stop_watch())
        self.childLayout.addWidget(stop_watch_widget)
        course_list_widget = QWidget(self.subject_list())
        self.show_day_progress_button()
        self.childLayout.addWidget(course_list_widget)
        self.setLayout(self.layout)
        self.subject_object_dictionary = {}
        self.time_spent_object_dictionary = {}
        self.subject_count = 0
        #self.setLayout(layout)
        self.show()

    def show_day_progress_button(self):
        day_progress_button = QPushButton("Show day's progress", self)
        self.childLayout.addWidget(day_progress_button)
        day_progress_button.clicked.connect(self.connect_progress_button)

    def connect_progress_button(self):
        file_name = "day's progress file"
        with open(file_name, 'w') as convert_file:
            convert_file.write(json.dumps(self.time_spent_object_dictionary))

    def subject_list(self):
        self.nameLabel = QLabel(self)
        self.nameLabel.setText('Subject:')
        self.line = QLineEdit(self)
        self.line.move(80, 20)
        self.line.resize(200, 32)
        self.nameLabel.move(20, 20)
        self.childLayout.addWidget(self.nameLabel)
        self.childLayout.addWidget(self.line)
        pybutton = QPushButton('OK', self)
        #self.layout.addWidget(self.nameLabel, 1, 2)
        self.childLayout.addWidget(pybutton)
        pybutton.clicked.connect(self.clickMethod)
        pybutton.resize(200, 32)
        pybutton.move(80, 60)

    def clickMethod(self):
        courseinfo = self.line.text().split(',')
        course = subject(courseinfo[0], int(courseinfo[1]))
        self.subject_object_dictionary[course.name] = course.time_required
        self.create_checkbox_subject(course.name)
        self.subject_object_dictionary[course.name] = course
        file_name = "subjectobject.json"
        with open(file_name, 'a+') as file_object:
            # json.dump(subject_object_dictionary, file_object)
            json.dump(course.serialize(), file_object)
        print('Your name: ' + self.line.text())
        self.subject_count+=1

    def create_checkbox_subject(self, subject_name):
        self.subject_checkbox = QCheckBox(subject_name, self)
        self.childLayout.addWidget(self.subject_checkbox)
        self.subject_checkbox.stateChanged.connect(self.clickBox)
        self.subject_checkbox.move(20, 20)
        self.subject_checkbox.resize(320, 40)
    def clickBox(self, state):
        if state == QtCore.Qt.Checked:
            self.accessing_subject_file()
            return True
        else:
            print('Unsucessful in acessing file')
#accessing subejct file function only works when there is one subject dictionary in the json file
    def accessing_subject_file(self):
        file_name = "subjectobject.json"
        return subject

#updating the time spent on a subject
    def update_time_spent_on_subject(self, time):
        self.current_subject = self.accessing_subject_file()
        updated_time = self.current_subject["Hours"]*60*60*100-time
        self.current_subject["Hours"] = updated_time

    def stop_watch(self):
        self.count = 0
        self.flag = False
        self.label = QLabel(self)
        self.childLayout.addWidget(self.label)
        self.label.setGeometry(75, 100, 250, 70)
        self.label.setStyleSheet("border : 4px solid black;")
        self.label.setText(str(self.count))
        self.label.setFont(QFont('Arial', 25))
        self.label.setAlignment(Qt.AlignCenter)
        start = QPushButton("Start", self)
        self.childLayout.addWidget(start)
        start.setGeometry(125, 250, 150, 40)
        start.pressed.connect(self.Start)
        pause = QPushButton("Pause", self)
        self.childLayout.addWidget(pause)
        pause.setGeometry(125, 300, 150, 40)
        pause.pressed.connect(self.Pause)
        re_set = QPushButton("Re-set", self)
        self.childLayout.addWidget(re_set)
        re_set.setGeometry(125, 350, 150, 40)
        re_set.pressed.connect(self.Re_set)
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(100)

    def showTime(self):
        if self.flag:
            self.count += 1
        text = str(self.count / 10)
        self.label.setText(text)

    def Start(self):
        self.flag = True

    def Pause(self):
        self.flag = False

    def Re_set(self):
        self.flag = False
        # resetting the count and storing time spent in a json file
        self.create_time_object(self.count)
        self.count = 0
        self.label.setText(str(self.count))

    '''time object stores time in milliseconds'''
    def create_time_object(self, current_time):
        subject = "math"
        day = "day1"
        current_time_spent = time_spent(subject, day, int(current_time))
        self.time_spent_object_dictionary[current_time_spent.day]=current_time_spent.time_spent
        filename = "progress_file"
        with open(filename, 'a+') as file_object:
            # json.dump(subject_object_dictionary, file_object)
            json.dump(current_time_spent.serialize(), file_object)






app=QApplication(sys.argv)
window = GUI()
sys.exit(app.exec_())
