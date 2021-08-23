# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from v1 import *
import copy

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(798, 593)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.btnRod = QtWidgets.QPushButton(self.centralwidget)
        self.btnRod.setGeometry(QtCore.QRect(20, 10, 121, 23))
        self.btnRod.setObjectName("btnRod")
        self.btnF = QtWidgets.QPushButton(self.centralwidget)
        self.btnF.setGeometry(QtCore.QRect(170, 10, 121, 23))
        self.btnF.setObjectName("btnF")

        self.btnOne = QtWidgets.QPushButton(self.centralwidget)
        self.btnOne.setGeometry(QtCore.QRect(320, 10, 121, 23))
        self.btnOne.setObjectName("btnOne")
        self.btnFull = QtWidgets.QPushButton(self.centralwidget)
        self.btnFull.setGeometry(QtCore.QRect(470, 10, 121, 23))
        self.btnFull.setObjectName("btnFull")

        self.txtRules = QtWidgets.QTextEdit(self.centralwidget)
        self.txtRules.setGeometry(QtCore.QRect(310, 70, 471, 191))
        self.txtRules.setObjectName("txtRules")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(310, 50, 47, 13))
        self.label.setObjectName("label")

        self.txtActions = QtWidgets.QTextEdit(self.centralwidget)
        self.txtActions.setGeometry(QtCore.QRect(310, 290, 471, 201))
        self.txtActions.setObjectName("txtActions")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(310, 270, 47, 13))
        self.label_4.setObjectName("label_4")

        self.txtSpravy = QtWidgets.QTextEdit(self.centralwidget)
        self.txtSpravy.setGeometry(QtCore.QRect(10, 440, 281, 141))
        self.txtSpravy.setObjectName("txtSpravy")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 420, 47, 13))
        self.label_2.setObjectName("label_2")

        self.txtruleAdd = QtWidgets.QTextEdit(self.centralwidget)
        self.txtruleAdd.setGeometry(QtCore.QRect(310, 520, 471, 31))
        self.txtruleAdd.setObjectName("txtruleAdd")
        self.btnAddF = QtWidgets.QPushButton(self.centralwidget)
        self.btnAddF.setGeometry(QtCore.QRect(310, 560, 131, 21))
        self.btnAddF.setObjectName("btnAddF")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(310, 500, 81, 16))
        self.label_5.setObjectName("label_5")

        self.listFacts = QtWidgets.QTextEdit(self.centralwidget)
        self.listFacts.setGeometry(QtCore.QRect(10, 70, 281, 341))
        self.listFacts.setObjectName("listFacts")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 50, 47, 13))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.btnRod.clicked.connect(self.fill)
        self.btnF.clicked.connect(self.fillP)
        self.btnOne.clicked.connect(self.one_step)
        self.btnFull.clicked.connect(self.to_the_end)
        self.btnAddF.clicked.connect(self.add_new_fact)
        self.facts = []
        self.rules = []
        self.actions = []
        self.spravy = []

    # Start for my base
    def fillP(self):
        self.spravy.clear()
        self.txtSpravy.clear()
        self.txtActions.clear()
        self.listFacts.clear()
        file1 = open('Work_facts.txt', 'r') 
        self.facts = file1.readlines() 
        txt = ""
        for line in self.facts:
            txt += line
        self.listFacts.setText(txt)

        self.txtRules.clear()
        txt = ""
        file2 = open('Work_rules.txt', 'r')
        Rules = file2.readlines()
        for line in Rules:
            txt += line
            if "Meno:" in line:
                self.rules.append(Rule(line[6:-1]))
            if "AK" in line:
                self.rules[len(self.rules)-1].condition = line[6:-1]
            if "POTOM" in line:
                self.rules[len(self.rules)-1].outcome = line[6:-1]
        self.txtRules.setText(txt)
        for r in self.rules:
            r.m()
        self.go()

    # Start for "Rodinne vztahy"
    def fill(self):
        self.spravy.clear()
        self.txtSpravy.clear()
        self.txtActions.clear()
        self.listFacts.clear()
        file1 = open('Rodina_facts.txt', 'r') 
        self.facts = file1.readlines() 
        txt = ""
        for line in self.facts:
            txt += line
        self.listFacts.setText(txt)

        self.txtRules.clear()
        txt = ""
        file2 = open('Rodina_rules.txt', 'r')
        Rules = file2.readlines()
        for line in Rules:
            txt += line
            if "Meno:" in line:
                self.rules.append(Rule(line[6:-1]))
            if "AK" in line:
                self.rules[len(self.rules)-1].condition = line[6:-1]
            if "POTOM" in line:
                self.rules[len(self.rules)-1].outcome = line[6:-1]
        self.txtRules.setText(txt)
        for r in self.rules:
            r.m()
        self.go()

    # Finding all propreate facts for rules
    def go(self):
        self.actions.clear()
        executable = []
        for rule in range(len(self.rules)):
            all_t = []
            all_t.append(self.rules[rule].name)
            all_t.append(rule)
            for con in self.rules[rule].listC:
                truth = []
                for fact in self.facts:
                    t = True
                    for c in con:
                        if c not in str(fact)[:-1]:
                            t = False
                            break
                    if t: truth.append(fact[:-1])
                all_t.append(truth)
            executable.append(all_t)
        t = copy.deepcopy(len(executable))
        # If not all conditions are fulfilled, remove possible executable rule
        while True:
            for i in executable:
                if len(i[2]) == 0 or len(i[3]) == 0:
                    executable.remove(i)
            if t == len(executable):
                break
            else:
                t = copy.deepcopy(len(executable))
        self.actions.clear()
        # Take all instans of actions
        for j in executable:
            res = self.rules[j[1]].exec(j)
            if res != None:
                for r in res:
                    self.actions.append(r)
        self.actions = list(dict.fromkeys(self.actions))
        self.rewrite_actions()

    # Checking wether it's doing something what already exists
    def rewrite_actions(self):
        t = copy.deepcopy(len(self.actions))
        n = 0
        while n<t:
            source = self.actions[n].split(',')
            for i in source:
                akcia = i.split(' ')[0]
                if "pridaj" in akcia:
                    if i[7:]+"\n" in self.facts:
                        self.actions.remove(self.actions[n])
                        n-=1
                        t = copy.deepcopy(len(self.actions))
                        break
                if "vymaz" in akcia:
                    if i[6:]+"\n" not in self.facts:
                        self.actions.remove(self.actions[n])
                        n-=1
                        t = copy.deepcopy(len(self.actions))
                        break
                if "sprava" in akcia:
                    if i[7:] in self.spravy:
                        self.actions.remove(self.actions[n])
                        n-=1
                        t = copy.deepcopy(len(self.actions))
                        break
            n+=1
        self.full_facts_actions()
        print(self.actions) 

    # Execute one action
    def one_step(self):
        if len(self.actions) > 0:
            t = self.actions[0].split(',')
            for txt in t:
                if "pridaj" in txt:
                    self.facts.append(txt[7:]+"\n")
                    if len(self.actions) > 0:self.actions.remove(self.actions[0])
                    self.full_facts_actions()
                elif "vymaz" in txt:
                    self.facts.remove(txt[6:]+"\n")
                    if len(self.actions) > 0:self.actions.remove(self.actions[0])
                    self.full_facts_actions()
                elif "sprava" in txt:
                    self.spravy.append(txt[7:])
                    if len(self.actions) > 0:self.actions.remove(self.actions[0])
                    self.full_facts_actions()
            self.go()

    # Adding new fact in list
    def add_new_fact(self):
        txt = self.txtruleAdd.toPlainText()
        if(txt != ""):
            text = txt.split('\n')
            for i in text:
                if i+'\n' not in self.facts:
                    self.facts.append(i+"\n")
            self.full_facts_actions()
        self.txtruleAdd.clear()
        self.rewrite_actions()

    # Goes to the end 
    def to_the_end(self):
        while(len(self.actions)>0):
            self.one_step()

    # Rewriting all lists
    def full_facts_actions(self):
        self.listFacts.clear()
        txt = ""
        for t in self.facts:
            txt += t
        self.listFacts.setText(txt)
        self.txtActions.clear()
        txt = ""
        for t in self.actions:
            txt += t + "\n"
        self.txtActions.setText(txt)
        txt = ""
        for t in self.spravy:
            txt += t + "\n"
        self.txtSpravy.setText(txt)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnRod.setText(_translate("MainWindow", "Rodinne vztahy"))
        self.btnF.setText(_translate("MainWindow", "Work"))
        self.btnFull.setText(_translate("MainWindow", "To the end"))
        self.btnOne.setText(_translate("MainWindow", "One step"))
        self.label.setText(_translate("MainWindow", "Rules"))
        self.label_2.setText(_translate("MainWindow", "Spravy"))
        self.label_3.setText(_translate("MainWindow", "Facts"))
        self.label_4.setText(_translate("MainWindow", "Actions"))
        self.btnAddF.setText(_translate("MainWindow", "Add"))
        self.label_5.setText(_translate("MainWindow", "Add new fact"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
