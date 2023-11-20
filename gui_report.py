from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QHBoxLayout, QWidget, QTableWidget,QTableWidgetItem
from PyQt6 import QtCore
from control import cont
import pandas as pd


class AnotherWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self):
        super().__init__()
        self.data = pd.DataFrame(columns=['Minerals','Number','Size'])
        self.setWindowTitle('Report')
        layout = QHBoxLayout()
        #self.label = QLabel("Another Window")
       
        self.setLayout(layout)
        self.count_table = QTableWidget(self)

        self.count_table.setColumnCount(3)
        self.count_table.setHorizontalHeaderLabels(['Minerals','Number','Size'])
        self.count_table.setStyleSheet("background-color: rgb(105, 105, 105);")
        
        layout.addWidget(self.count_table)
        self.resize(self.count_table.width()*4,int(self.count_table.height())*5)

        


    def show_table(self):

        mineralCntDict = cont.CountShot()
        mineralSize = cont.CountSquareDetailed(mineralCntDict)

        if mineralCntDict != None:

            cnt = 0
            for key in mineralCntDict.items():


                for x in mineralSize[key[0]]:
                    self.count_table.insertRow( self.count_table.rowCount())
                    #print(cnt)
                    item = QTableWidgetItem(str(key[0]))
                    self.count_table.setItem(cnt, 0, item)
                    #print(key[0],end = ' ')
                    item = QTableWidgetItem(str(x))
                    self.count_table.setItem(cnt, 1, item)
                    #print(x,end = ' ')
                    size = mineralSize[key[0]][x]
                    item = QTableWidgetItem(str(round(size,3)))
                    self.count_table.setItem(cnt, 2, item) 
                    #print(size)
                    #rowpd = pd.DataFrame([str(key[0]),x,round(size,3)]) 
                    #print(rowpd)
                    self.data.loc[len(self.data)] = [str(key[0]),x,round(size,3)]
                    cnt+=1

        print(self.data)
        self.data.to_excel("Report.xlsx")