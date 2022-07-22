# QT Designer 연동 소스
from PySide2.QtWidgets import (QApplication, QWidget, QMainWindow, QAbstractItemView, 
                               QTableWidgetItem, QMessageBox)
from PySide2.QtCore import Qt
import sys
from naverSearch import *
import webbrowser

from naverSearch_ui import Ui_MainWindow

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # uic.loadUi('./ui/naverSearch.ui', self)

        #ui에 있는 위젯하고 시그널 처리(컨트롤 이벤트처리)
        self.ui.btnSearch.clicked.connect(self.btnSearch_Clicked)
        self.ui.tblResult.itemSelectionChanged.connect(self.tblResult_Selected)
        self.ui.txtSearchWord.returnPressed.connect(self.btnSearch_Clicked)

    def tblResult_Selected(self):
        selected = self.ui.tblResult.currentRow() # 현재 선택된 열의 인덱스
        url = self.ui.tblResult.item(selected, 1).text()
        # QMessageBox.about(self, 'URL', url)
        webbrowser.open(url)

    def makeTable(self, result):
        self.ui.tblResult.setSelectionMode(QAbstractItemView.SingleSelection)
        self.ui.tblResult.setColumnCount(2)
        self.ui.tblResult.setRowCount(len(result))

        self.ui.tblResult.setHorizontalHeaderLabels(['기사제목', '뉴스링크'])

        n = 0
        for post in result:
            title = post['title'].replace('&lt;', '<').replace('&gt;', '>').replace('<b>', '').replace('</b>', '').replace('&quot;', "'")
            self.ui.tblResult.setItem(n, 0, QTableWidgetItem(title))
            self.ui.tblResult.setItem(n, 1, QTableWidgetItem(post['originallink']))
            n += 1

        self.ui.tblResult.setColumnWidth(0, 400)
        self.ui.tblResult.setColumnWidth(1, 300)
        self.ui.tblResult.setEditTriggers(QAbstractItemView.NoEditTriggers) # 컬럼데이터 수정 금지


    def btnSearch_Clicked(self):       
        api = naverSearch()
        jsonResult = []
        sNode = 'news'
        search_word = self.ui.txtSearchWord.text()
        display = 100

        if len(search_word) == 0:
            QMessageBox.about(self, 'popup', '검색어를 입력하세요')
            return

        # naver api search
        jsonSearch = api.getNaverSearchResult(sNode, search_word, 1, display)
        jsonResult = jsonSearch['items'] # items 리스트 분리
        print(len(jsonResult))
        self.ui.stsResult.showMessage('검색결과 : {0}개'.format(len(jsonResult)))
        #print(jsonSearch)
        # model = QtGui.QStandardItemModel()
        # self.lsvResult.setModel(model)
        
        # for post in jsonResult:
        #     item = QtGui.QStandardItem(post['title'])
        #     model.appendRow(item)
        self.makeTable(jsonResult)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())