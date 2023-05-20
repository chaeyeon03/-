import startscreen_rc
import mainscreen_rc
import play_rc
import food_rc
import cafe_rc
import theater_rc
import itertools

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTextEdit, QSpacerItem, QSizePolicy, QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
## 전역 변수 선언 부분 ##
G1 = None
nameAry = ['혜화역', '페르시안 궁전', '이삭토스트', '나누미떡볶이', '머노까머나', '뎁짜이', '호호식당','메밀향그집','정돈','군자대한곱창','칸다소바',\
           '순대실록','핏제리아오','투파인드피터','고부기','코야코',\
           '이디야_성균관대점','삼원샏','학림','CONCRETE_PALETTE','스타벅스_혜화역점','스타벅스_마로니에공원점','스타벅스_동숭로아트점',\
           '링크아트센터', '서연아트홀','쿼드','예스24스테이지','컬쳐씨어터','자유극장','티오엠','드림씨어터',\
           '국립어린이과학관','짚풀박물관','아르코미술관','낙산공원']

#혜화역 변수
혜화역 = 0
#음식점 변수
페르시안궁전, 이삭토스트, 나누미떡볶이, 머노까머나, 뎁짜이, 호호식당, 메밀향그집, 정돈, 군자대한곱창, 칸다소바 =  1, 2, 3, 4, 5, 6, 7, 8, 9, 10
순대실록, 핏제리아오, 투파인드피터, 고부기, 코야코 = 11, 12, 13, 14, 15
#카페 변수
이디야_성균관대점, 삼원샏, 학림, CONCRETE_PALETTE, 스타벅스_혜화역점, 스타벅스_마로니에공원점, 스타벅스_동숭로아트점 = 16, 17, 18, 19, 20, 21, 22
#연극 변수
링크아트센터, 서연아트홀, 쿼드, 예스24스테이지, 컬쳐씨어터, 자유극장, 티오엠, 드림씨어터 = 23, 24, 25, 26, 27, 28, 29, 30
#놀거리 변수
국립어린이과학관, 짚풀박물관, 아르코미술관, 낙산공원 = 31, 32, 33, 34

## 그래프 구성 코드 부분 ##
gSize = 35
choose=[]
user_nodes=[]
class Graph():
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]



    def getMinCostAndPath(self, start, end):
        visited = [False] * self.SIZE
        dist = [float('inf')] * self.SIZE
        dist[start] = 0
        prev = [None] * self.SIZE

        for _ in range(self.SIZE):
            min_distance = float('inf')
            for i in range(self.SIZE):
                if not visited[i] and dist[i] < min_distance:
                    min_distance = dist[i]
                    current = i

            visited[current] = True
            for neighbor in range(self.SIZE):
                if not visited[neighbor] and self.graph[current][neighbor] != 0:
                    new_distance = dist[current] + self.graph[current][neighbor]
                    if new_distance < dist[neighbor]:
                        dist[neighbor] = new_distance
                        prev[neighbor] = current

        path = []
        current = end
        while current != start:
            path.append(current)
            current = prev[current]
        path.append(start)
        path.reverse()

        return dist[end], path
    def getMinCostTour(self, nodes):
        min_cost = float('inf')
        min_path = []

        for start in nodes:  # 각 노드를 시작점으로 해서 검사
            remaining_nodes = nodes.copy()
            remaining_nodes.remove(start)

            for permutation in itertools.permutations(remaining_nodes):
                path = [start] + list(permutation)
                valid_path = True
                for i in range(len(path) - 1):
                    if path[i] == path[i+1]:  # 같은 노드를 연달아 방문하면 경로를 무효화
                        valid_path = False
                        break

                if valid_path:
                    total_cost = 0
                    for i in range(len(path) - 1):
                        cost, _ = self.getMinCostAndPath(path[i], path[i+1])
                        total_cost += cost
                    if total_cost < min_cost:
                        min_cost = total_cost
                        min_path = path

        return min_cost, min_path
class UI_startscreen(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1600, 900)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 1600, 900))
        self.label.setStyleSheet("background-image: url(:/startscreen/startscreen.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.NEXT = QtWidgets.QPushButton(Dialog)
        self.NEXT.setGeometry(QtCore.QRect(760, 530, 91, 31))
        self.NEXT.setStyleSheet("background-image: url(:/startscreen/NEXT.png);")
        self.NEXT.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/NEXT/NEXT.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.NEXT.setIcon(icon)
        self.NEXT.setIconSize(QtCore.QSize(80, 30))
        self.NEXT.setObjectName("NEXT")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)



    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "혜화에서 뭐하지?"))

        self.NEXT.clicked.connect(Dialog.accept)
class UI_mainscreen(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1600, 897)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 1600, 897))
        self.label.setStyleSheet("background-image: url(:/mainscreen/mainscreen.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.food = QtWidgets.QPushButton(Dialog)
        self.food.setGeometry(QtCore.QRect(970, 30, 112, 34))
        font = QtGui.QFont()
        font.setFamily("HY동녘M")
        self.food.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/mainscreen/food.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.food.setIcon(icon)
        self.food.setIconSize(QtCore.QSize(30, 30))
        self.food.setObjectName("food")
        self.cafe = QtWidgets.QPushButton(Dialog)
        self.cafe.setGeometry(QtCore.QRect(1110, 30, 112, 34))
        font = QtGui.QFont()
        font.setFamily("HY동녘M")
        self.cafe.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/mainscreen/cafe.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cafe.setIcon(icon1)
        self.cafe.setIconSize(QtCore.QSize(30, 30))
        self.cafe.setObjectName("cafe")
        self.play = QtWidgets.QPushButton(Dialog)
        self.play.setGeometry(QtCore.QRect(1240, 30, 112, 34))
        font = QtGui.QFont()
        font.setFamily("HY동녘M")
        self.play.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/mainscreen/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.play.setIcon(icon2)
        self.play.setIconSize(QtCore.QSize(30, 30))
        self.play.setObjectName("play")
        self.theater = QtWidgets.QPushButton(Dialog)
        self.theater.setGeometry(QtCore.QRect(1380, 30, 112, 34))
        font = QtGui.QFont()
        font.setFamily("HY동녘M")
        self.theater.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/mainscreen/theater.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.theater.setIcon(icon3)
        self.theater.setIconSize(QtCore.QSize(30, 30))
        self.theater.setObjectName("theater")
        self.else_2 = QtWidgets.QPushButton(Dialog)
        self.else_2.setGeometry(QtCore.QRect(1540, 30, 41, 34))
        font = QtGui.QFont()
        font.setFamily("HY동녘M")
        self.else_2.setFont(font)
        self.else_2.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/mainscreen/else.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.else_2.setIcon(icon4)
        self.else_2.setIconSize(QtCore.QSize(30, 30))
        self.else_2.setObjectName("else_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "혜화동"))
        self.food.setText(_translate("Dialog", "음식점"))
        self.cafe.setText(_translate("Dialog", "카페"))
        self.play.setText(_translate("Dialog", "놀거리"))
        self.theater.setText(_translate("Dialog", "연극"))
        self.play.clicked.connect(self.open_play_screen)
        self.food.clicked.connect(self.open_food_screen)
        self.cafe.clicked.connect(self.open_cafe_screen)
        self.theater.clicked.connect(self.open_theater_screen)
        self.else_2.clicked.connect(self.open_finish_screen)

    def open_play_screen(self):
        play_dialog = QtWidgets.QDialog()
        play_ui = UI_play()
        play_ui.setupUi(play_dialog)
        play_dialog.exec_()
    def open_food_screen(self):
        food_dialog = QtWidgets.QDialog()
        food_ui = UI_food()
        food_ui.setupUi(food_dialog)
        food_dialog.exec_()
    def open_cafe_screen(self):
        cafe_dialog = QtWidgets.QDialog()
        cafe_ui = UI_cafe()
        cafe_ui.setupUi(cafe_dialog)
        cafe_dialog.exec_()
    def open_theater_screen(self):
        theater_dialog = QtWidgets.QDialog()
        theater_ui = UI_theater()
        theater_ui.setupUi(theater_dialog)
        theater_dialog.exec_()
    def open_finish_screen(self):
        for value in choose:
            user_nodes.append(value)
        if not user_nodes:
            popup_dialog = QtWidgets.QDialog()
            popup_ui = UI_popup()
            popup_ui.setupUi(popup_dialog)
            popup_dialog.exec_()
        else:
            finish_dialog = QtWidgets.QDialog()
            finish_ui = UI_finish()
            finish_ui.setupUi(finish_dialog)
            finish_dialog.exec_()
#########팝업 화면들
#메인화면 우측상단의 카페 버튼을 눌렀을 때 뜨는 화면
class UI_popup(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 160)
        Dialog.setStyleSheet("background-color: rgb(255, 189, 190);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 380, 140))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(50, 60, 131, 40))
        font = QtGui.QFont()
        font.setFamily("HY동녘M")
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(229, 60, 131, 40))
        font = QtGui.QFont()
        font.setFamily("HY동녘M")
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton_2.clicked.connect(exit)
        self.pushButton.clicked.connect(Dialog.accept)



    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "결과"))
        self.pushButton.setText(_translate("Dialog", "창 닫기"))
        self.pushButton_2.setText(_translate("Dialog", "종료"))

class UI_cafe(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 900)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(0, 0))
        Dialog.setStyleSheet("background-color: rgb(255, 189, 190);")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.finish_cafe = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("HY동녘M")
        self.finish_cafe.setFont(font)
        self.finish_cafe.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.finish_cafe.setObjectName("finish_cafe")
        self.verticalLayout.addWidget(self.finish_cafe)
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -1393, 746, 2222))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/cafe/concrete.png"))
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.concrete_add = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        self.concrete_add.setFont(font)
        self.concrete_add.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.concrete_add.setObjectName("concrete_add")
        self.verticalLayout_2.addWidget(self.concrete_add)
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_5.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(":/cafe/ediya.png"))
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.ediya_add = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        self.ediya_add.setFont(font)
        self.ediya_add.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ediya_add.setObjectName("ediya_add")
        self.verticalLayout_2.addWidget(self.ediya_add)
        self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_6.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap(":/cafe/hakrym.png"))
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.hakrim_add = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        self.hakrim_add.setFont(font)
        self.hakrim_add.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.hakrim_add.setObjectName("hakrim_add")
        self.verticalLayout_2.addWidget(self.hakrim_add)
        self.label_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_7.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap(":/cafe/samone.png"))
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.sam_add = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        self.sam_add.setFont(font)
        self.sam_add.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.sam_add.setObjectName("sam_add")
        self.verticalLayout_2.addWidget(self.sam_add)
        self.label_9 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_9.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap(":/cafe/sb_donsung.png"))
        self.label_9.setObjectName("label_9")
        self.verticalLayout_2.addWidget(self.label_9)
        self.sbdong_add = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        self.sbdong_add.setFont(font)
        self.sbdong_add.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.sbdong_add.setObjectName("sbdong_add")
        self.verticalLayout_2.addWidget(self.sbdong_add)
        self.label_10 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_10.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap(":/cafe/sb_heyhwa.png"))
        self.label_10.setObjectName("label_10")
        self.verticalLayout_2.addWidget(self.label_10)
        self.sbhehwa_add = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        self.sbhehwa_add.setFont(font)
        self.sbhehwa_add.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.sbhehwa_add.setObjectName("sbhehwa_add")
        self.verticalLayout_2.addWidget(self.sbhehwa_add)
        self.label_11 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_11.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap(":/cafe/sb_maro.png"))
        self.label_11.setObjectName("label_11")
        self.verticalLayout_2.addWidget(self.label_11)
        self.sbmaro_add = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        self.sbmaro_add.setFont(font)
        self.sbmaro_add.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.sbmaro_add.setObjectName("sbmaro_add")
        self.verticalLayout_2.addWidget(self.sbmaro_add)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.finish_cafe.clicked.connect(Dialog.accept)
        self.concrete_add.clicked.connect(self.add_concrete)
        self.ediya_add.clicked.connect(self.add_ediya)
        self.hakrim_add.clicked.connect(self.add_hakrim)
        self.sam_add.clicked.connect(self.add_sam)
        self.sbdong_add.clicked.connect(self.add_sbdong)
        self.sbhehwa_add.clicked.connect(self.add_sbhehwa)
        self.sbmaro_add.clicked.connect(self.add_sbmaro)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "카페"))
        self.finish_cafe.setText(_translate("Dialog", "완료"))
        self.concrete_add.setText(_translate("Dialog", "추가✔"))
        self.ediya_add.setText(_translate("Dialog", "추가✔"))
        self.hakrim_add.setText(_translate("Dialog", "추가✔"))
        self.sam_add.setText(_translate("Dialog", "추가✔"))
        self.sbdong_add.setText(_translate("Dialog", "추가✔"))
        self.sbhehwa_add.setText(_translate("Dialog", "추가✔"))
        self.sbmaro_add.setText(_translate("Dialog", "추가✔"))
    def add_concrete(self):
        choose.append(19)
    def add_ediya(self):
        choose.append(16)
    def add_hakrim(self):
        choose.append(18)
    def add_sam(self):
        choose.append(17)
    def add_sbdong(self):
        choose.append(22)
    def add_sbhehwa(self):
        choose.append(20)
    def add_sbmaro(self):
        choose.append(21)
class UI_play(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 900)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(0, 0))
        Dialog.setStyleSheet("background-color: rgb(255, 189, 190);")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.finish_play = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("HY동녘M")
        self.finish_play.setFont(font)
        self.finish_play.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.finish_play.setObjectName("finish_play")
        self.verticalLayout.addWidget(self.finish_play)
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -340, 746, 1172))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/play/arco.png"))
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.arco_add = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        self.arco_add.setFont(font)
        self.arco_add.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.arco_add.setObjectName("arco_add")
        self.verticalLayout_2.addWidget(self.arco_add)
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_5.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(":/play/kid.png"))
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.kid_add = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        self.kid_add.setFont(font)
        self.kid_add.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.kid_add.setObjectName("kid_add")
        self.verticalLayout_2.addWidget(self.kid_add)
        self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_6.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap(":/play/naksan.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.naksan_add = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        self.naksan_add.setFont(font)
        self.naksan_add.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.naksan_add.setObjectName("naksan_add")
        self.verticalLayout_2.addWidget(self.naksan_add)
        self.label_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_7.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap(":/play/sanghwal.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.sanghwal_add = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        self.sanghwal_add.setFont(font)
        self.sanghwal_add.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.sanghwal_add.setObjectName("sanghwal_add")
        self.verticalLayout_2.addWidget(self.sanghwal_add)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.finish_play.clicked.connect(Dialog.accept)
        self.arco_add.clicked.connect(self.add_arco)
        self.kid_add.clicked.connect(self.add_kid)
        self.naksan_add.clicked.connect(self.add_naksan)
        self.sanghwal_add.clicked.connect(self.add_sanghwal)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "놀거리"))
        self.finish_play.setText(_translate("Dialog", "완료"))
        self.arco_add.setText(_translate("Dialog", "추가✔"))
        self.kid_add.setText(_translate("Dialog", "추가✔"))
        self.naksan_add.setText(_translate("Dialog", "추가✔"))
        self.sanghwal_add.setText(_translate("Dialog", "추가✔"))
    def add_arco(self):
        choose.append(33)
    def add_kid(self):
        choose.append(31)
    def add_naksan(self):
        choose.append(34)
    def add_sanghwal(self):
        choose.append(32)
class UI_food(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 900)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(0, 0))
        Dialog.setStyleSheet("background-color: rgb(255, 189, 190);")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.finish_food = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("HY동녘M")
        self.finish_food.setFont(font)
        self.finish_food.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.finish_food.setObjectName("finish_food")
        self.verticalLayout.addWidget(self.finish_food)
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -1400, 746, 5782))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/food/coyaco.png"))
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.coyaco_add = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        self.coyaco_add.setFont(font)
        self.coyaco_add.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.coyaco_add.setObjectName("coyaco_add")
        self.verticalLayout_2.addWidget(self.coyaco_add)
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_5.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(":/food/depzzai.png"))
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.depzzai_add = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        self.depzzai_add.setFont(font)
        self.depzzai_add.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.depzzai_add.setObjectName("depzzai_add")
        self.verticalLayout_2.addWidget(self.depzzai_add)
        self.label_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_7.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap(":/food/gobugi.png"))
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.gobugi_add = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        self.gobugi_add.setFont(font)
        self.gobugi_add.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.gobugi_add.setObjectName("gobugi_add")
        self.verticalLayout_2.addWidget(self.gobugi_add)
        self.label_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_8.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap(":/food/gunja.png"))
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.gunja_add = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        self.gunja_add.setFont(font)
        self.gunja_add.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.gunja_add.setObjectName("gunja_add")
        self.verticalLayout_2.addWidget(self.gunja_add)
        self.label_9 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_9.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap(":/food/hoho.png"))
        self.label_9.setObjectName("label_9")
        self.verticalLayout_2.addWidget(self.label_9)
        self.hoho_add = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        self.hoho_add.setFont(font)
        self.hoho_add.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.hoho_add.setObjectName("hoho_add")
        self.verticalLayout_2.addWidget(self.hoho_add)
        self.label_10 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_10.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap(":/food/issac.png"))
        self.label_10.setObjectName("label_10")
        self.verticalLayout_2.addWidget(self.label_10)
        self.issac_add = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        self.issac_add.setFont(font)
        self.issac_add.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.issac_add.setObjectName("issac_add")
        self.verticalLayout_2.addWidget(self.issac_add)
        self.label_11 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_11.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap(":/food/jungdon.png"))
        self.label_11.setObjectName("label_11")
        self.verticalLayout_2.addWidget(self.label_11)
        self.jungdon_add = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        self.jungdon_add.setFont(font)
        self.jungdon_add.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.jungdon_add.setObjectName("jungdon_add")
        self.verticalLayout_2.addWidget(self.jungdon_add)
        self.label_12 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_12.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap(":/food/kanda.png"))
        self.label_12.setObjectName("label_12")
        self.verticalLayout_2.addWidget(self.label_12)
        self.kanda_add = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        self.kanda_add.setFont(font)
        self.kanda_add.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.kanda_add.setObjectName("kanda_add")
        self.verticalLayout_2.addWidget(self.kanda_add)
        self.label_13 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_13.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap(":/food/memil.png"))
        self.label_13.setObjectName("label_13")
        self.verticalLayout_2.addWidget(self.label_13)
        self.memil_add = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        self.memil_add.setFont(font)
        self.memil_add.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.memil_add.setObjectName("memil_add")
        self.verticalLayout_2.addWidget(self.memil_add)
        self.label_14 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_14.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_14.setText("")
        self.label_14.setPixmap(QtGui.QPixmap(":/food/muno.png"))
        self.label_14.setObjectName("label_14")
        self.verticalLayout_2.addWidget(self.label_14)
        self.muno_add = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        self.muno_add.setFont(font)
        self.muno_add.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.muno_add.setObjectName("muno_add")
        self.verticalLayout_2.addWidget(self.muno_add)
        self.label_15 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_15.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_15.setText("")
        self.label_15.setPixmap(QtGui.QPixmap(":/food/nanumi.png"))
        self.label_15.setObjectName("label_15")
        self.verticalLayout_2.addWidget(self.label_15)
        self.nanumi_add = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        self.nanumi_add.setFont(font)
        self.nanumi_add.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.nanumi_add.setObjectName("nanumi_add")
        self.verticalLayout_2.addWidget(self.nanumi_add)
        self.label_16 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_16.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_16.setText("")
        self.label_16.setPixmap(QtGui.QPixmap(":/food/persian.png"))
        self.label_16.setObjectName("label_16")
        self.verticalLayout_2.addWidget(self.label_16)
        self.persian_add = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        self.persian_add.setFont(font)
        self.persian_add.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.persian_add.setObjectName("persian_add")
        self.verticalLayout_2.addWidget(self.persian_add)
        self.label_18 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_18.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_18.setText("")
        self.label_18.setPixmap(QtGui.QPixmap(":/food/pitze.png"))
        self.label_18.setObjectName("label_18")
        self.verticalLayout_2.addWidget(self.label_18)
        self.pitzeriao_add = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        self.pitzeriao_add.setFont(font)
        self.pitzeriao_add.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pitzeriao_add.setObjectName("pitzeriao_add")
        self.verticalLayout_2.addWidget(self.pitzeriao_add)
        self.label_19 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_19.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_19.setText("")
        self.label_19.setPixmap(QtGui.QPixmap(":/food/soondae.png"))
        self.label_19.setObjectName("label_19")
        self.verticalLayout_2.addWidget(self.label_19)
        self.soondae_add = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        self.soondae_add.setFont(font)
        self.soondae_add.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.soondae_add.setObjectName("soondae_add")
        self.verticalLayout_2.addWidget(self.soondae_add)
        self.label_21 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_21.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_21.setText("")
        self.label_21.setPixmap(QtGui.QPixmap(":/food/twofind.png"))
        self.label_21.setObjectName("label_21")
        self.verticalLayout_2.addWidget(self.label_21)
        self.twofind_add = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        self.twofind_add.setFont(font)
        self.twofind_add.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.twofind_add.setObjectName("twofind_add")
        self.verticalLayout_2.addWidget(self.twofind_add)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.finish_food.clicked.connect(Dialog.accept)
        self.coyaco_add.clicked.connect(self.add_coyaco)
        self.depzzai_add.clicked.connect(self.add_depzzai)
        self.gobugi_add.clicked.connect(self.add_gobugi)
        self.gunja_add.clicked.connect(self.add_gunja)
        self.hoho_add.clicked.connect(self.add_hoho)
        self.issac_add.clicked.connect(self.add_issac)
        self.jungdon_add.clicked.connect(self.add_jungdon)
        self.kanda_add.clicked.connect(self.add_kanda)
        self.memil_add.clicked.connect(self.add_memil)
        self.muno_add.clicked.connect(self.add_muno)
        self.nanumi_add.clicked.connect(self.add_nanumi)
        self.persian_add.clicked.connect(self.add_persian)
        self.pitzeriao_add.clicked.connect(self.add_pitzeriao)
        self.soondae_add.clicked.connect(self.add_soondae)
        self.twofind_add.clicked.connect(self.add_twofind)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "음식점"))
        self.finish_food.setText(_translate("Dialog", "완료"))
        self.coyaco_add.setText(_translate("Dialog", "추가✔"))
        self.depzzai_add.setText(_translate("Dialog", "추가✔"))
        self.gobugi_add.setText(_translate("Dialog", "추가✔"))
        self.gunja_add.setText(_translate("Dialog", "추가✔"))
        self.hoho_add.setText(_translate("Dialog", "추가✔"))
        self.issac_add.setText(_translate("Dialog", "추가✔"))
        self.jungdon_add.setText(_translate("Dialog", "추가✔"))
        self.kanda_add.setText(_translate("Dialog", "추가✔"))
        self.memil_add.setText(_translate("Dialog", "추가✔"))
        self.muno_add.setText(_translate("Dialog", "추가✔"))
        self.nanumi_add.setText(_translate("Dialog", "추가✔"))
        self.persian_add.setText(_translate("Dialog", "추가✔"))
        self.pitzeriao_add.setText(_translate("Dialog", "추가✔"))
        self.soondae_add.setText(_translate("Dialog", "추가✔"))
        self.twofind_add.setText(_translate("Dialog", "추가✔"))
    def add_coyaco(self):
        choose.append(15)
    def add_depzzai(self):
        choose.append(5)
    def add_gobugi(self):
        choose.append(14)
    def add_gunja(self):
        choose.append(9)
    def add_hoho(self):
        choose.append(6)
    def add_issac(self):
        choose.append(2)
    def add_jungdon(self):
        choose.append(8)
    def add_kanda(self):
        choose.append(10)
    def add_memil(self):
        choose.append(7)
    def add_muno(self):
        choose.append(4)
    def add_nanumi(self):
        choose.append(3)
    def add_persian(self):
        choose.append(1)
    def add_pitzeriao(self):
        choose.append(12)
    def add_soondae(self):
        choose.append(11)
    def add_twofind(self):
        choose.append(13)
class UI_theater(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 900)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(0, 0))
        Dialog.setStyleSheet("background-color: rgb(255, 189, 190);")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.finish_theater = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("HY동녘M")
        self.finish_theater.setFont(font)
        self.finish_theater.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.finish_theater.setObjectName("finish_theater")
        self.verticalLayout.addWidget(self.finish_theater)
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -1048, 746, 1877))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/theater/culture.png"))
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.culture_add = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        self.culture_add.setFont(font)
        self.culture_add.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.culture_add.setObjectName("culture_add")
        self.verticalLayout_2.addWidget(self.culture_add)
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_5.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(":/theater/dream.png"))
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.dream_add = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        self.dream_add.setFont(font)
        self.dream_add.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dream_add.setObjectName("dream_add")
        self.verticalLayout_2.addWidget(self.dream_add)
        self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_6.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap(":/theater/free.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.free_add = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        self.free_add.setFont(font)
        self.free_add.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.free_add.setObjectName("free_add")
        self.verticalLayout_2.addWidget(self.free_add)
        self.label_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_7.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap(":/theater/link.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.link_add = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        self.link_add.setFont(font)
        self.link_add.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.link_add.setObjectName("link_add")
        self.verticalLayout_2.addWidget(self.link_add)
        self.label_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_8.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap(":/theater/quad.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.quad_add = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        self.quad_add.setFont(font)
        self.quad_add.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.quad_add.setObjectName("quad_add")
        self.verticalLayout_2.addWidget(self.quad_add)
        self.label_9 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_9.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap(":/theater/seoyeon.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_2.addWidget(self.label_9)
        self.seoyeon_add = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        self.seoyeon_add.setFont(font)
        self.seoyeon_add.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.seoyeon_add.setObjectName("seoyeon_add")
        self.verticalLayout_2.addWidget(self.seoyeon_add)
        self.label_10 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_10.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap(":/theater/tom.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_2.addWidget(self.label_10)
        self.tom_add = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        self.tom_add.setFont(font)
        self.tom_add.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tom_add.setObjectName("tom_add")
        self.verticalLayout_2.addWidget(self.tom_add)
        self.label_11 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_11.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap(":/theater/yes24.png"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_2.addWidget(self.label_11)
        self.yes_add = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("HY견고딕")
        self.yes_add.setFont(font)
        self.yes_add.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.yes_add.setObjectName("yes_add")
        self.verticalLayout_2.addWidget(self.yes_add)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.finish_theater.clicked.connect(Dialog.accept)
        self.culture_add.clicked.connect(self.add_culture)
        self.dream_add.clicked.connect(self.add_dream)
        self.free_add.clicked.connect(self.add_free)
        self.link_add.clicked.connect(self.add_link)
        self.quad_add.clicked.connect(self.add_quad)
        self.seoyeon_add.clicked.connect(self.add_seoyeon)
        self.tom_add.clicked.connect(self.add_tom)
        self.yes_add.clicked.connect(self.add_yes)
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "극장"))
        self.finish_theater.setText(_translate("Dialog", "완료"))
        self.culture_add.setText(_translate("Dialog", "추가✔"))
        self.dream_add.setText(_translate("Dialog", "추가✔"))
        self.free_add.setText(_translate("Dialog", "추가✔"))
        self.link_add.setText(_translate("Dialog", "추가✔"))
        self.quad_add.setText(_translate("Dialog", "추가✔"))
        self.seoyeon_add.setText(_translate("Dialog", "추가✔"))
        self.tom_add.setText(_translate("Dialog", "추가✔"))
        self.yes_add.setText(_translate("Dialog", "추가✔"))
    def add_culture(self):
        choose.append(27)
    def add_dream(self):
        choose.append(30)
    def add_free(self):
        choose.append(28)
    def add_link(self):
        choose.append(23)
    def add_quad(self):
        choose.append(25)
    def add_seoyeon(self):
        choose.append(24)
    def add_tom(self):
        choose.append(29)
    def add_yes(self):
        choose.append(26)
class UI_finish(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 200)
        self.reset = QtWidgets.QPushButton(Dialog)
        self.reset.setGeometry(QtCore.QRect(180, 80, 100, 40))
        font = QtGui.QFont()
        font.setFamily("HY동녘M")
        self.reset.setFont(font)
        self.reset.setObjectName("reset")
        self.program_finish = QtWidgets.QPushButton(Dialog)
        self.program_finish.setGeometry(QtCore.QRect(460, 80, 100, 40))
        font = QtGui.QFont()
        font.setFamily("HY동녘M")
        self.program_finish.setFont(font)
        self.program_finish.setObjectName("program_finish")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 600, 200))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 189, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 222, 222))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 94, 95))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 126, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 189, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 189, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 222, 222))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 189, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 222, 222))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 94, 95))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 126, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 189, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 189, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 222, 222))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 94, 95))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 189, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 222, 222))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 94, 95))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 126, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 94, 95))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 94, 95))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 189, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 189, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 189, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.label_2.setPalette(palette)
        self.label_2.setStyleSheet("background-color: rgb(255, 189, 190);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 580, 180))
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.clse_finish = QtWidgets.QPushButton(Dialog)
        self.clse_finish.setGeometry(QtCore.QRect(320, 80, 100, 40))
        font = QtGui.QFont()
        font.setFamily("HY동녘M")
        self.clse_finish.setFont(font)
        self.clse_finish.setObjectName("clse_finish")
        self.result = QtWidgets.QPushButton(Dialog)
        self.result.setGeometry(QtCore.QRect(40, 80, 100, 40))
        font = QtGui.QFont()
        font.setFamily("HY동녘M")
        self.result.setFont(font)
        self.result.setObjectName("result")
        self.label_2.raise_()
        self.label_3.raise_()
        self.reset.raise_()
        self.program_finish.raise_()
        self.clse_finish.raise_()
        self.result.raise_()
        self.retranslateUi(Dialog)
        self.result.clicked.connect(self.show_result)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.clse_finish.clicked.connect(Dialog.accept)
        self.program_finish.clicked.connect(exit)
        self.reset.clicked.connect(self.re_set)

        def findVertex(g, findVtx):  # 정점이 그래프에 연결되어 있는지 확인하는 함수
            stack = []
            visitedAry = []  # 방문한 정점

            current = 0  # 시작 정점
            stack.append(current)
            visitedAry.append(current)

            while (len(stack) != 0):
                next = None
                for vertex in range(gSize):
                    if g.graph[current][vertex] != 0:
                        if vertex in visitedAry:  # 방문한 적이 있는 정점이면 탈락
                            pass
                        else:  # 방문한 적이 없으면 다음 정점으로 지정
                            next = vertex
                            break

                if next != None:  # 다음에 방문할 정점이 있는 경우
                    current = next
                    stack.append(current)
                    visitedAry.append(current)
                else:  # 다음에 방문할 정점이 없는 경우
                    current = stack.pop()

            if findVtx in visitedAry:
                return True
            else:
                return False

        G1 = Graph(gSize)

        # 혜화역 -> 음식점
        G1.graph[혜화역][페르시안궁전] = 9
        G1.graph[혜화역][이삭토스트] = 8
        G1.graph[혜화역][나누미떡볶이] = 7
        G1.graph[혜화역][머노까머나] = 4
        G1.graph[혜화역][뎁짜이] = 4
        G1.graph[혜화역][호호식당] = 5
        G1.graph[혜화역][메밀향그집] = 3
        G1.graph[혜화역][정돈] = 1
        G1.graph[혜화역][군자대한곱창] = 1
        G1.graph[혜화역][칸다소바] = 2
        G1.graph[혜화역][순대실록] = 2
        G1.graph[혜화역][핏제리아오] = 5
        G1.graph[혜화역][투파인드피터] = 2
        G1.graph[혜화역][고부기] = 4
        G1.graph[혜화역][코야코] = 4

        # 음식점 -> 혜화역
        G1.graph[페르시안궁전][혜화역] = 9
        G1.graph[이삭토스트][혜화역] = 8
        G1.graph[나누미떡볶이][혜화역] = 7
        G1.graph[머노까머나][혜화역] = 4
        G1.graph[뎁짜이][혜화역] = 4
        G1.graph[호호식당][혜화역] = 3
        G1.graph[메밀향그집][혜화역] = 3
        G1.graph[정돈][혜화역] = 1
        G1.graph[군자대한곱창][혜화역] = 1
        G1.graph[칸다소바][혜화역] = 2
        G1.graph[순대실록][혜화역] = 2
        G1.graph[핏제리아오][혜화역] = 5
        G1.graph[투파인드피터][혜화역] = 2
        G1.graph[고부기][혜화역] = 4
        G1.graph[코야코][혜화역] = 4

        # 혜화역 -> 카페
        G1.graph[혜화역][이디야_성균관대점] = 6
        G1.graph[혜화역][삼원샏] = 5
        G1.graph[혜화역][학림] = 3
        G1.graph[혜화역][CONCRETE_PALETTE] = 4
        G1.graph[혜화역][스타벅스_혜화역점] = 3
        G1.graph[혜화역][스타벅스_마로니에공원점] = 2
        G1.graph[혜화역][스타벅스_동숭로아트점] = 6

        ## 카페 -> 혜화역
        G1.graph[이디야_성균관대점][혜화역] = 6
        G1.graph[삼원샏][혜화역] = 5
        G1.graph[학림][혜화역] = 3
        G1.graph[CONCRETE_PALETTE][혜화역] = 4
        G1.graph[스타벅스_혜화역점][혜화역] = 3
        G1.graph[스타벅스_마로니에공원점][혜화역] = 2
        G1.graph[스타벅스_동숭로아트점][혜화역] = 6

        ## 혜화역 -> 극장
        G1.graph[혜화역][링크아트센터] = 5
        G1.graph[혜화역][서연아트홀] = 5
        G1.graph[혜화역][쿼드] = 5
        G1.graph[혜화역][예스24스테이지] = 4
        G1.graph[혜화역][컬쳐씨어터] = 5
        G1.graph[혜화역][자유극장] = 5
        G1.graph[혜화역][티오엠] = 5
        G1.graph[혜화역][드림씨어터] = 4

        ## 극장 -> 혜화역
        G1.graph[링크아트센터][혜화역] = 5
        G1.graph[서연아트홀][혜화역] = 5
        G1.graph[쿼드][혜화역] = 5
        G1.graph[예스24스테이지][혜화역] = 4
        G1.graph[컬쳐씨어터][혜화역] = 5
        G1.graph[자유극장][혜화역] = 5
        G1.graph[티오엠][혜화역] = 5
        G1.graph[드림씨어터][혜화역] = 4

        ##혜화역 -> 놀거리
        G1.graph[혜화역][국립어린이과학관] = 13
        G1.graph[혜화역][짚풀박물관] = 9
        G1.graph[혜화역][아르코미술관] = 4
        G1.graph[혜화역][낙산공원] = 11

        ##놀거리 -> 혜화역
        G1.graph[국립어린이과학관][혜화역] = 13
        G1.graph[짚풀박물관][혜화역] = 9
        G1.graph[아르코미술관][혜화역] = 4
        G1.graph[낙산공원][혜화역] = 11

        ## 카페 -> 놀거리
        G1.graph[이디야_성균관대점][국립어린이과학관] = 3
        G1.graph[이디야_성균관대점][짚풀박물관] = 5
        G1.graph[이디야_성균관대점][아르코미술관] = 12
        G1.graph[이디야_성균관대점][낙산공원] = 19

        G1.graph[삼원샏][국립어린이과학관] = 10
        G1.graph[삼원샏][짚풀박물관] = 9
        G1.graph[삼원샏][아르코미술관] = 7
        G1.graph[삼원샏][낙산공원] = 13

        G1.graph[학림][국립어린이과학관] = 16
        G1.graph[학림][짚풀박물관] = 8
        G1.graph[학림][아르코미술관] = 5
        G1.graph[학림][낙산공원] = 12

        G1.graph[CONCRETE_PALETTE][국립어린이과학관] = 15
        G1.graph[CONCRETE_PALETTE][짚풀박물관] = 7
        G1.graph[CONCRETE_PALETTE][아르코미술관] = 6
        G1.graph[CONCRETE_PALETTE][낙산공원] = 13

        G1.graph[스타벅스_혜화역점][국립어린이과학관] = 16
        G1.graph[스타벅스_혜화역점][짚풀박물관] = 8
        G1.graph[스타벅스_혜화역점][아르코미술관] = 5
        G1.graph[스타벅스_혜화역점][낙산공원] = 12

        G1.graph[스타벅스_마로니에공원점][국립어린이과학관] = 17
        G1.graph[스타벅스_마로니에공원점][짚풀박물관] = 10
        G1.graph[스타벅스_마로니에공원점][아르코미술관] = 3
        G1.graph[스타벅스_마로니에공원점][낙산공원] = 10

        G1.graph[스타벅스_동숭로아트점][국립어린이과학관] = 18
        G1.graph[스타벅스_동숭로아트점][짚풀박물관] = 10
        G1.graph[스타벅스_동숭로아트점][아르코미술관] = 5
        G1.graph[스타벅스_동숭로아트점][낙산공원] = 10

        ## 놀거리 -> 카페
        G1.graph[국립어린이과학관][이디야_성균관대점] = 2
        G1.graph[짚풀박물관][이디야_성균관대점] = 5
        G1.graph[아르코미술관][이디야_성균관대점] = 12
        G1.graph[낙산공원][이디야_성균관대점] = 19

        G1.graph[국립어린이과학관][삼원샏] = 10
        G1.graph[짚풀박물관][삼원샏] = 9
        G1.graph[아르코미술관][삼원샏] = 7
        G1.graph[낙산공원][삼원샏] = 13

        G1.graph[국립어린이과학관][학림] = 16
        G1.graph[짚풀박물관][학림] = 8
        G1.graph[아르코미술관][학림] = 5
        G1.graph[낙산공원][학림] = 12

        G1.graph[국립어린이과학관][CONCRETE_PALETTE] = 15
        G1.graph[짚풀박물관][CONCRETE_PALETTE] = 7
        G1.graph[아르코미술관][CONCRETE_PALETTE] = 6
        G1.graph[낙산공원][CONCRETE_PALETTE] = 13

        G1.graph[국립어린이과학관][스타벅스_혜화역점] = 16
        G1.graph[짚풀박물관][스타벅스_혜화역점] = 8
        G1.graph[아르코미술관][스타벅스_혜화역점] = 5
        G1.graph[낙산공원][스타벅스_혜화역점] = 12

        G1.graph[국립어린이과학관][스타벅스_마로니에공원점] = 17
        G1.graph[짚풀박물관][스타벅스_마로니에공원점] = 10
        G1.graph[아르코미술관][스타벅스_마로니에공원점] = 3
        G1.graph[낙산공원][스타벅스_마로니에공원점] = 9

        G1.graph[국립어린이과학관][스타벅스_동숭로아트점] = 18
        G1.graph[짚풀박물관][스타벅스_동숭로아트점] = 10
        G1.graph[아르코미술관][스타벅스_동숭로아트점] = 5
        G1.graph[낙산공원][스타벅스_동숭로아트점] = 10

        # 연극 -> 카페
        G1.graph[링크아트센터][이디야_성균관대점] = 11
        G1.graph[서연아트홀][이디야_성균관대점] = 6
        G1.graph[쿼드][이디야_성균관대점] = 8
        G1.graph[예스24스테이지][이디야_성균관대점] = 14
        G1.graph[컬쳐씨어터][이디야_성균관대점] = 9
        G1.graph[자유극장][이디야_성균관대점] = 10
        G1.graph[티오엠][이디야_성균관대점] = 12
        G1.graph[드림씨어터][이디야_성균관대점] = 13

        G1.graph[링크아트센터][삼원샏] = 7
        G1.graph[서연아트홀][삼원샏] = 5
        G1.graph[쿼드][삼원샏] = 7
        G1.graph[예스24스테이지][삼원샏] = 6
        G1.graph[컬쳐씨어터][삼원샏] = 6
        G1.graph[자유극장][삼원샏] = 6
        G1.graph[티오엠][삼원샏] = 6
        G1.graph[드림씨어터][삼원샏] = 6

        G1.graph[링크아트센터][학림] = 7
        G1.graph[서연아트홀][학림] = 4
        G1.graph[쿼드][학림] = 6
        G1.graph[예스24스테이지][학림] = 4
        G1.graph[컬쳐씨어터][학림] = 4
        G1.graph[자유극장][학림] = 5
        G1.graph[티오엠][학림] = 4
        G1.graph[드림씨어터][학림] = 3

        G1.graph[링크아트센터][CONCRETE_PALETTE] = 6
        G1.graph[서연아트홀][CONCRETE_PALETTE] = 4
        G1.graph[쿼드][CONCRETE_PALETTE] = 5
        G1.graph[예스24스테이지][CONCRETE_PALETTE] = 4
        G1.graph[컬쳐씨어터][CONCRETE_PALETTE] = 4
        G1.graph[자유극장][CONCRETE_PALETTE] = 5
        G1.graph[티오엠][CONCRETE_PALETTE] = 5
        G1.graph[드림씨어터][CONCRETE_PALETTE] = 4

        G1.graph[링크아트센터][스타벅스_혜화역점] = 6
        G1.graph[서연아트홀][스타벅스_혜화역점] = 9
        G1.graph[쿼드][스타벅스_혜화역점] = 5
        G1.graph[예스24스테이지][스타벅스_혜화역점] = 3
        G1.graph[컬쳐씨어터][스타벅스_혜화역점] = 4
        G1.graph[자유극장][스타벅스_혜화역점] = 4
        G1.graph[티오엠][스타벅스_혜화역점] = 4
        G1.graph[드림씨어터][스타벅스_혜화역점] = 4

        G1.graph[링크아트센터][스타벅스_마로니에공원점] = 7
        G1.graph[서연아트홀][스타벅스_마로니에공원점] = 7
        G1.graph[쿼드][스타벅스_마로니에공원점] = 6
        G1.graph[예스24스테이지][스타벅스_마로니에공원점] = 4
        G1.graph[컬쳐씨어터][스타벅스_마로니에공원점] = 4
        G1.graph[자유극장][스타벅스_마로니에공원점] = 5
        G1.graph[티오엠][스타벅스_마로니에공원점] = 3
        G1.graph[드림씨어터][스타벅스_마로니에공원점] = 3

        G1.graph[링크아트센터][스타벅스_동숭로아트점] = 5
        G1.graph[서연아트홀][스타벅스_동숭로아트점] = 8
        G1.graph[쿼드][스타벅스_동숭로아트점] = 2
        G1.graph[예스24스테이지][스타벅스_동숭로아트점] = 2
        G1.graph[컬쳐씨어터][스타벅스_동숭로아트점] = 2
        G1.graph[자유극장][스타벅스_동숭로아트점] = 1
        G1.graph[티오엠][스타벅스_동숭로아트점] = 2
        G1.graph[드림씨어터][스타벅스_동숭로아트점] = 2

        ## 카페 -> 연극
        G1.graph[이디야_성균관대점][링크아트센터] = 11
        G1.graph[이디야_성균관대점][서연아트홀] = 6
        G1.graph[이디야_성균관대점][쿼드] = 8
        G1.graph[이디야_성균관대점][예스24스테이지] = 14
        G1.graph[이디야_성균관대점][컬쳐씨어터] = 9
        G1.graph[이디야_성균관대점][자유극장] = 10
        G1.graph[이디야_성균관대점][티오엠] = 12
        G1.graph[이디야_성균관대점][드림씨어터] = 13

        G1.graph[삼원샏][링크아트센터] = 7
        G1.graph[삼원샏][서연아트홀] = 5
        G1.graph[삼원샏][쿼드] = 7
        G1.graph[삼원샏][예스24스테이지] = 6
        G1.graph[삼원샏][컬쳐씨어터] = 6
        G1.graph[삼원샏][자유극장] = 6
        G1.graph[삼원샏][티오엠] = 6
        G1.graph[삼원샏][드림씨어터] = 6

        G1.graph[학림][링크아트센터] = 7
        G1.graph[학림][서연아트홀] = 4
        G1.graph[학림][쿼드] = 6
        G1.graph[학림][예스24스테이지] = 4
        G1.graph[학림][컬쳐씨어터] = 4
        G1.graph[학림][자유극장] = 5
        G1.graph[학림][티오엠] = 4
        G1.graph[학림][드림씨어터] = 3

        G1.graph[CONCRETE_PALETTE][링크아트센터] = 6
        G1.graph[CONCRETE_PALETTE][서연아트홀] = 4
        G1.graph[CONCRETE_PALETTE][쿼드] = 5
        G1.graph[CONCRETE_PALETTE][예스24스테이지] = 4
        G1.graph[CONCRETE_PALETTE][컬쳐씨어터] = 4
        G1.graph[CONCRETE_PALETTE][자유극장] = 5
        G1.graph[CONCRETE_PALETTE][티오엠] = 5
        G1.graph[CONCRETE_PALETTE][드림씨어터] = 4

        G1.graph[스타벅스_혜화역점][링크아트센터] = 6
        G1.graph[스타벅스_혜화역점][서연아트홀] = 9
        G1.graph[스타벅스_혜화역점][쿼드] = 5
        G1.graph[스타벅스_혜화역점][예스24스테이지] = 3
        G1.graph[스타벅스_혜화역점][컬쳐씨어터] = 4
        G1.graph[스타벅스_혜화역점][자유극장] = 4
        G1.graph[스타벅스_혜화역점][티오엠] = 4
        G1.graph[스타벅스_혜화역점][드림씨어터] = 4

        G1.graph[스타벅스_마로니에공원점][링크아트센터] = 7
        G1.graph[스타벅스_마로니에공원점][서연아트홀] = 7
        G1.graph[스타벅스_마로니에공원점][쿼드] = 6
        G1.graph[스타벅스_마로니에공원점][예스24스테이지] = 4
        G1.graph[스타벅스_마로니에공원점][컬쳐씨어터] = 4
        G1.graph[스타벅스_마로니에공원점][자유극장] = 5
        G1.graph[스타벅스_마로니에공원점][티오엠] = 3
        G1.graph[스타벅스_마로니에공원점][드림씨어터] = 3

        G1.graph[스타벅스_동숭로아트점][링크아트센터] = 5
        G1.graph[스타벅스_동숭로아트점][서연아트홀] = 8
        G1.graph[스타벅스_동숭로아트점][쿼드] = 2
        G1.graph[스타벅스_동숭로아트점][예스24스테이지] = 2
        G1.graph[스타벅스_동숭로아트점][컬쳐씨어터] = 2
        G1.graph[스타벅스_동숭로아트점][자유극장] = 1
        G1.graph[스타벅스_동숭로아트점][티오엠] = 2
        G1.graph[스타벅스_동숭로아트점][드림씨어터] = 2

        # 음식점 -> 카페
        G1.graph[페르시안궁전][이디야_성균관대점] = 3
        G1.graph[페르시안궁전][삼원샏] = 9
        G1.graph[페르시안궁전][학림] = 10
        G1.graph[페르시안궁전][CONCRETE_PALETTE] = 9
        G1.graph[페르시안궁전][스타벅스_혜화역점] = 12
        G1.graph[페르시안궁전][스타벅스_마로니에공원점] = 12
        G1.graph[페르시안궁전][스타벅스_동숭로아트점] = 13

        G1.graph[이삭토스트][이디야_성균관대점] = 2
        G1.graph[이삭토스트][삼원샏] = 8
        G1.graph[이삭토스트][학림] = 9
        G1.graph[이삭토스트][CONCRETE_PALETTE] = 8
        G1.graph[이삭토스트][스타벅스_혜화역점] = 10
        G1.graph[이삭토스트][스타벅스_마로니에공원점] = 11
        G1.graph[이삭토스트][스타벅스_동숭로아트점] = 12

        G1.graph[나누미떡볶이][이디야_성균관대점] = 1
        G1.graph[나누미떡볶이][삼원샏] = 7
        G1.graph[나누미떡볶이][학림] = 8
        G1.graph[나누미떡볶이][CONCRETE_PALETTE] = 7
        G1.graph[나누미떡볶이][스타벅스_혜화역점] = 9
        G1.graph[나누미떡볶이][스타벅스_마로니에공원점] = 10
        G1.graph[나누미떡볶이][스타벅스_동숭로아트점] = 11

        G1.graph[머노까머나][이디야_성균관대점] = 3
        G1.graph[머노까머나][삼원샏] = 4
        G1.graph[머노까머나][학림] = 5
        G1.graph[머노까머나][CONCRETE_PALETTE] = 5
        G1.graph[머노까머나][스타벅스_혜화역점] = 7
        G1.graph[머노까머나][스타벅스_마로니에공원점] = 7
        G1.graph[머노까머나][스타벅스_동숭로아트점] = 9

        G1.graph[뎁짜이][이디야_성균관대점] = 4
        G1.graph[뎁짜이][삼원샏] = 3
        G1.graph[뎁짜이][학림] = 4
        G1.graph[뎁짜이][CONCRETE_PALETTE] = 3
        G1.graph[뎁짜이][스타벅스_혜화역점] = 6
        G1.graph[뎁짜이][스타벅스_마로니에공원점] = 6
        G1.graph[뎁짜이][스타벅스_동숭로아트점] = 8

        G1.graph[호호식당][이디야_성균관대점] = 5
        G1.graph[호호식당][삼원샏] = 2
        G1.graph[호호식당][학림] = 3
        G1.graph[호호식당][CONCRETE_PALETTE] = 3
        G1.graph[호호식당][스타벅스_혜화역점] = 5
        G1.graph[호호식당][스타벅스_마로니에공원점] = 5
        G1.graph[호호식당][스타벅스_동숭로아트점] = 8

        G1.graph[메밀향그집][이디야_성균관대점] = 6
        G1.graph[메밀향그집][삼원샏] = 1
        G1.graph[메밀향그집][학림] = 2
        G1.graph[메밀향그집][CONCRETE_PALETTE] = 2
        G1.graph[메밀향그집][스타벅스_혜화역점] = 4
        G1.graph[메밀향그집][스타벅스_마로니에공원점] = 4
        G1.graph[메밀향그집][스타벅스_동숭로아트점] = 7

        G1.graph[정돈][이디야_성균관대점] = 7
        G1.graph[정돈][삼원샏] = 3
        G1.graph[정돈][학림] = 1
        G1.graph[정돈][CONCRETE_PALETTE] = 2
        G1.graph[정돈][스타벅스_혜화역점] = 3
        G1.graph[정돈][스타벅스_마로니에공원점] = 3
        G1.graph[정돈][스타벅스_동숭로아트점] = 6

        G1.graph[군자대한곱창][이디야_성균관대점] = 6
        G1.graph[군자대한곱창][삼원샏] = 2
        G1.graph[군자대한곱창][학림] = 3
        G1.graph[군자대한곱창][CONCRETE_PALETTE] = 2
        G1.graph[군자대한곱창][스타벅스_혜화역점] = 3
        G1.graph[군자대한곱창][스타벅스_마로니에공원점] = 5
        G1.graph[군자대한곱창][스타벅스_동숭로아트점] = 6

        G1.graph[칸다소바][이디야_성균관대점] = 8
        G1.graph[칸다소바][삼원샏] = 2
        G1.graph[칸다소바][학림] = 2
        G1.graph[칸다소바][CONCRETE_PALETTE] = 1
        G1.graph[칸다소바][스타벅스_혜화역점] = 2
        G1.graph[칸다소바][스타벅스_마로니에공원점] = 3
        G1.graph[칸다소바][스타벅스_동숭로아트점] = 5

        G1.graph[순대실록][이디야_성균관대점] = 11
        G1.graph[순대실록][삼원샏] = 5
        G1.graph[순대실록][학림] = 5
        G1.graph[순대실록][CONCRETE_PALETTE] = 4
        G1.graph[순대실록][스타벅스_혜화역점] = 3
        G1.graph[순대실록][스타벅스_마로니에공원점] = 5
        G1.graph[순대실록][스타벅스_동숭로아트점] = 4

        G1.graph[핏제리아오][이디야_성균관대점] = 14
        G1.graph[핏제리아오][삼원샏] = 8
        G1.graph[핏제리아오][학림] = 6
        G1.graph[핏제리아오][CONCRETE_PALETTE] = 7
        G1.graph[핏제리아오][스타벅스_혜화역점] = 4
        G1.graph[핏제리아오][스타벅스_마로니에공원점] = 6
        G1.graph[핏제리아오][스타벅스_동숭로아트점] = 2

        G1.graph[투파인드피터][이디야_성균관대점] = 11
        G1.graph[투파인드피터][삼원샏] = 5
        G1.graph[투파인드피터][학림] = 3
        G1.graph[투파인드피터][CONCRETE_PALETTE] = 4
        G1.graph[투파인드피터][스타벅스_혜화역점] = 3
        G1.graph[투파인드피터][스타벅스_마로니에공원점] = 2
        G1.graph[투파인드피터][스타벅스_동숭로아트점] = 2

        G1.graph[고부기][이디야_성균관대점] = 15
        G1.graph[고부기][삼원샏] = 8
        G1.graph[고부기][학림] = 6
        G1.graph[고부기][CONCRETE_PALETTE] = 7
        G1.graph[고부기][스타벅스_혜화역점] = 5
        G1.graph[고부기][스타벅스_마로니에공원점] = 4
        G1.graph[고부기][스타벅스_동숭로아트점] = 3

        G1.graph[코야코][이디야_성균관대점] = 14
        G1.graph[코야코][삼원샏] = 8
        G1.graph[코야코][학림] = 6
        G1.graph[코야코][CONCRETE_PALETTE] = 7
        G1.graph[코야코][스타벅스_혜화역점] = 5
        G1.graph[코야코][스타벅스_마로니에공원점] = 4
        G1.graph[코야코][스타벅스_동숭로아트점] = 3

        # 연극->음식점
        G1.graph[링크아트센터][페르시안궁전] = 13
        G1.graph[링크아트센터][이삭토스트] = 12
        G1.graph[링크아트센터][나누미떡볶이] = 11
        G1.graph[링크아트센터][머노까머나] = 8
        G1.graph[링크아트센터][뎁짜이] = 8
        G1.graph[링크아트센터][호호식당] = 8
        G1.graph[링크아트센터][메밀향그집] = 7
        G1.graph[링크아트센터][정돈] = 8
        G1.graph[링크아트센터][군자대한곱창] = 5
        G1.graph[링크아트센터][칸다소바] = 5
        G1.graph[링크아트센터][순대실록] = 3
        G1.graph[링크아트센터][핏제리아오] = 7
        G1.graph[링크아트센터][투파인드피터] = 6
        G1.graph[링크아트센터][고부기] = 7
        G1.graph[링크아트센터][코야코] = 7

        G1.graph[서연아트홀][페르시안궁전] = 7
        G1.graph[서연아트홀][이삭토스트] = 7
        G1.graph[서연아트홀][나누미떡볶이] = 6
        G1.graph[서연아트홀][머노까머나] = 4
        G1.graph[서연아트홀][뎁짜이] = 4
        G1.graph[서연아트홀][호호식당] = 4
        G1.graph[서연아트홀][메밀향그집] = 3
        G1.graph[서연아트홀][정돈] = 6
        G1.graph[서연아트홀][군자대한곱창] = 1
        G1.graph[서연아트홀][칸다소바] = 3
        G1.graph[서연아트홀][순대실록] = 6
        G1.graph[서연아트홀][핏제리아오] = 9
        G1.graph[서연아트홀][투파인드피터] = 8
        G1.graph[서연아트홀][고부기] = 10
        G1.graph[서연아트홀][코야코] = 10

        G1.graph[쿼드][페르시안궁전] = 14
        G1.graph[쿼드][이삭토스트] = 13
        G1.graph[쿼드][나누미떡볶이] = 12
        G1.graph[쿼드][머노까머나] = 8
        G1.graph[쿼드][뎁짜이] = 8
        G1.graph[쿼드][호호식당] = 8
        G1.graph[쿼드][메밀향그집] = 6
        G1.graph[쿼드][정돈] = 7
        G1.graph[쿼드][군자대한곱창] = 6
        G1.graph[쿼드][칸다소바] = 4
        G1.graph[쿼드][순대실록] = 1
        G1.graph[쿼드][핏제리아오] = 3
        G1.graph[쿼드][투파인드피터] = 3
        G1.graph[쿼드][고부기] = 4
        G1.graph[쿼드][코야코] = 4

        G1.graph[예스24스테이지][페르시안궁전] = 14
        G1.graph[예스24스테이지][이삭토스트] = 13
        G1.graph[예스24스테이지][나누미떡볶이] = 12
        G1.graph[예스24스테이지][머노까머나] = 9
        G1.graph[예스24스테이지][뎁짜이] = 7
        G1.graph[예스24스테이지][호호식당] = 7
        G1.graph[예스24스테이지][메밀향그집] = 6
        G1.graph[예스24스테이지][정돈] = 6
        G1.graph[예스24스테이지][군자대한곱창] = 5
        G1.graph[예스24스테이지][칸다소바] = 4
        G1.graph[예스24스테이지][순대실록] = 1
        G1.graph[예스24스테이지][핏제리아오] = 3
        G1.graph[예스24스테이지][투파인드피터] = 2
        G1.graph[예스24스테이지][고부기] = 4
        G1.graph[예스24스테이지][코야코] = 4

        G1.graph[컬쳐씨어터][페르시안궁전] = 14
        G1.graph[컬쳐씨어터][이삭토스트] = 13
        G1.graph[컬쳐씨어터][나누미떡볶이] = 12
        G1.graph[컬쳐씨어터][머노까머나] = 9
        G1.graph[컬쳐씨어터][뎁짜이] = 8
        G1.graph[컬쳐씨어터][호호식당] = 7
        G1.graph[컬쳐씨어터][메밀향그집] = 6
        G1.graph[컬쳐씨어터][정돈] = 6
        G1.graph[컬쳐씨어터][군자대한곱창] = 5
        G1.graph[컬쳐씨어터][칸다소바] = 4
        G1.graph[컬쳐씨어터][순대실록] = 2
        G1.graph[컬쳐씨어터][핏제리아오] = 3
        G1.graph[컬쳐씨어터][투파인드피터] = 2
        G1.graph[컬쳐씨어터][고부기] = 4
        G1.graph[컬쳐씨어터][코야코] = 4

        G1.graph[자유극장][페르시안궁전] = 15
        G1.graph[자유극장][이삭토스트] = 14
        G1.graph[자유극장][나누미떡볶이] = 13
        G1.graph[자유극장][머노까머나] = 9
        G1.graph[자유극장][뎁짜이] = 8
        G1.graph[자유극장][호호식당] = 8
        G1.graph[자유극장][메밀향그집] = 6
        G1.graph[자유극장][정돈] = 6
        G1.graph[자유극장][군자대한곱창] = 6
        G1.graph[자유극장][칸다소바] = 5
        G1.graph[자유극장][순대실록] = 2
        G1.graph[자유극장][핏제리아오] = 2
        G1.graph[자유극장][투파인드피터] = 2
        G1.graph[자유극장][고부기] = 3
        G1.graph[자유극장][코야코] = 3

        G1.graph[티오엠][페르시안궁전] = 15
        G1.graph[티오엠][이삭토스트] = 14
        G1.graph[티오엠][나누미떡볶이] = 13
        G1.graph[티오엠][머노까머나] = 10
        G1.graph[티오엠][뎁짜이] = 8
        G1.graph[티오엠][호호식당] = 7
        G1.graph[티오엠][메밀향그집] = 6
        G1.graph[티오엠][정돈] = 6
        G1.graph[티오엠][군자대한곱창] = 6
        G1.graph[티오엠][칸다소바] = 5
        G1.graph[티오엠][순대실록] = 2
        G1.graph[티오엠][핏제리아오] = 3
        G1.graph[티오엠][투파인드피터] = 1
        G1.graph[티오엠][고부기] = 4
        G1.graph[티오엠][코야코] = 4

        G1.graph[드림씨어터][페르시안궁전] = 14
        G1.graph[드림씨어터][이삭토스트] = 13
        G1.graph[드림씨어터][나누미떡볶이] = 12
        G1.graph[드림씨어터][머노까머나] = 9
        G1.graph[드림씨어터][뎁짜이] = 8
        G1.graph[드림씨어터][호호식당] = 7
        G1.graph[드림씨어터][메밀향그집] = 6
        G1.graph[드림씨어터][정돈] = 5
        G1.graph[드림씨어터][군자대한곱창] = 5
        G1.graph[드림씨어터][칸다소바] = 4
        G1.graph[드림씨어터][순대실록] = 3
        G1.graph[드림씨어터][핏제리아오] = 4
        G1.graph[드림씨어터][투파인드피터] = 2
        G1.graph[드림씨어터][고부기] = 5
        G1.graph[드림씨어터][코야코] = 5

        # 음식점->연극
        G1.graph[페르시안궁전][링크아트센터] = 13
        G1.graph[이삭토스트][링크아트센터] = 12
        G1.graph[나누미떡볶이][링크아트센터] = 11
        G1.graph[머노까머나][링크아트센터] = 8
        G1.graph[뎁짜이][링크아트센터] = 8
        G1.graph[호호식당][링크아트센터] = 8
        G1.graph[메밀향그집][링크아트센터] = 7
        G1.graph[정돈][링크아트센터] = 8
        G1.graph[군자대한곱창][링크아트센터] = 5
        G1.graph[칸다소바][링크아트센터] = 5
        G1.graph[순대실록][링크아트센터] = 3
        G1.graph[핏제리아오][링크아트센터] = 7
        G1.graph[투파인드피터][링크아트센터] = 6
        G1.graph[고부기][링크아트센터] = 7
        G1.graph[코야코][링크아트센터] = 7

        G1.graph[페르시안궁전][서연아트홀] = 7
        G1.graph[이삭토스트][서연아트홀] = 7
        G1.graph[나누미떡볶이][서연아트홀] = 6
        G1.graph[머노까머나][서연아트홀] = 4
        G1.graph[뎁짜이][서연아트홀] = 4
        G1.graph[호호식당][서연아트홀] = 4
        G1.graph[메밀향그집][서연아트홀] = 3
        G1.graph[정돈][서연아트홀] = 6
        G1.graph[군자대한곱창][서연아트홀] = 1
        G1.graph[칸다소바][서연아트홀] = 3
        G1.graph[순대실록][서연아트홀] = 6
        G1.graph[핏제리아오][서연아트홀] = 9
        G1.graph[투파인드피터][서연아트홀] = 8
        G1.graph[고부기][서연아트홀] = 10
        G1.graph[코야코][서연아트홀] = 10

        G1.graph[페르시안궁전][쿼드] = 14
        G1.graph[이삭토스트][쿼드] = 13
        G1.graph[나누미떡볶이][쿼드] = 12
        G1.graph[머노까머나][쿼드] = 8
        G1.graph[뎁짜이][쿼드] = 8
        G1.graph[호호식당][쿼드] = 8
        G1.graph[메밀향그집][쿼드] = 6
        G1.graph[정돈][쿼드] = 7
        G1.graph[군자대한곱창][쿼드] = 6
        G1.graph[칸다소바][쿼드] = 4
        G1.graph[순대실록][쿼드] = 1
        G1.graph[핏제리아오][쿼드] = 3
        G1.graph[투파인드피터][쿼드] = 3
        G1.graph[고부기][쿼드] = 4
        G1.graph[코야코][쿼드] = 4

        G1.graph[페르시안궁전][예스24스테이지] = 14
        G1.graph[이삭토스트][예스24스테이지] = 13
        G1.graph[나누미떡볶이][예스24스테이지] = 12
        G1.graph[머노까머나][예스24스테이지] = 9
        G1.graph[뎁짜이][예스24스테이지] = 7
        G1.graph[호호식당][예스24스테이지] = 7
        G1.graph[메밀향그집][예스24스테이지] = 6
        G1.graph[정돈][예스24스테이지] = 6
        G1.graph[군자대한곱창][예스24스테이지] = 5
        G1.graph[칸다소바][예스24스테이지] = 4
        G1.graph[순대실록][예스24스테이지] = 1
        G1.graph[핏제리아오][예스24스테이지] = 3
        G1.graph[투파인드피터][예스24스테이지] = 2
        G1.graph[고부기][예스24스테이지] = 4
        G1.graph[코야코][예스24스테이지] = 4

        G1.graph[페르시안궁전][컬쳐씨어터] = 14
        G1.graph[이삭토스트][컬쳐씨어터] = 13
        G1.graph[나누미떡볶이][컬쳐씨어터] = 12
        G1.graph[머노까머나][컬쳐씨어터] = 9
        G1.graph[뎁짜이][컬쳐씨어터] = 8
        G1.graph[호호식당][컬쳐씨어터] = 7
        G1.graph[메밀향그집][컬쳐씨어터] = 6
        G1.graph[정돈][컬쳐씨어터] = 6
        G1.graph[군자대한곱창][컬쳐씨어터] = 5
        G1.graph[칸다소바][컬쳐씨어터] = 4
        G1.graph[순대실록][컬쳐씨어터] = 2
        G1.graph[핏제리아오][컬쳐씨어터] = 3
        G1.graph[투파인드피터][컬쳐씨어터] = 2
        G1.graph[고부기][컬쳐씨어터] = 4
        G1.graph[코야코][컬쳐씨어터] = 4

        G1.graph[페르시안궁전][자유극장] = 15
        G1.graph[이삭토스트][자유극장] = 14
        G1.graph[나누미떡볶이][자유극장] = 13
        G1.graph[머노까머나][자유극장] = 9
        G1.graph[뎁짜이][자유극장] = 8
        G1.graph[호호식당][자유극장] = 8
        G1.graph[메밀향그집][자유극장] = 6
        G1.graph[정돈][자유극장] = 6
        G1.graph[군자대한곱창][자유극장] = 6
        G1.graph[칸다소바][자유극장] = 5
        G1.graph[순대실록][자유극장] = 2
        G1.graph[핏제리아오][자유극장] = 2
        G1.graph[투파인드피터][자유극장] = 2
        G1.graph[고부기][자유극장] = 3
        G1.graph[코야코][자유극장] = 3

        G1.graph[페르시안궁전][티오엠] = 15
        G1.graph[이삭토스트][티오엠] = 14
        G1.graph[나누미떡볶이][티오엠] = 13
        G1.graph[머노까머나][티오엠] = 10
        G1.graph[뎁짜이][티오엠] = 8
        G1.graph[호호식당][티오엠] = 7
        G1.graph[메밀향그집][티오엠] = 6
        G1.graph[정돈][티오엠] = 6
        G1.graph[군자대한곱창][티오엠] = 6
        G1.graph[칸다소바][티오엠] = 5
        G1.graph[순대실록][티오엠] = 2
        G1.graph[핏제리아오][티오엠] = 3
        G1.graph[투파인드피터][티오엠] = 1
        G1.graph[고부기][티오엠] = 4
        G1.graph[코야코][티오엠] = 4

        G1.graph[페르시안궁전][드림씨어터] = 14
        G1.graph[이삭토스트][드림씨어터] = 13
        G1.graph[나누미떡볶이][드림씨어터] = 12
        G1.graph[머노까머나][드림씨어터] = 9
        G1.graph[뎁짜이][드림씨어터] = 8
        G1.graph[호호식당][드림씨어터] = 7
        G1.graph[메밀향그집][드림씨어터] = 6
        G1.graph[정돈][드림씨어터] = 5
        G1.graph[군자대한곱창][드림씨어터] = 5
        G1.graph[칸다소바][드림씨어터] = 4
        G1.graph[순대실록][드림씨어터] = 3
        G1.graph[핏제리아오][드림씨어터] = 4
        G1.graph[투파인드피터][드림씨어터] = 2
        G1.graph[고부기][드림씨어터] = 5
        G1.graph[코야코][드림씨어터] = 5

        # 놀거리->음식점
        G1.graph[국립어린이과학관][페르시안궁전] = 6
        G1.graph[국립어린이과학관][이삭토스트] = 5
        G1.graph[국립어린이과학관][나누미떡볶이] = 4
        G1.graph[국립어린이과학관][머노까머나] = 3
        G1.graph[국립어린이과학관][뎁짜이] = 4
        G1.graph[국립어린이과학관][호호식당] = 6
        G1.graph[국립어린이과학관][메밀향그집] = 6
        G1.graph[국립어린이과학관][정돈] = 7
        G1.graph[국립어린이과학관][군자대한곱창] = 7
        G1.graph[국립어린이과학관][칸다소바] = 8
        G1.graph[국립어린이과학관][순대실록] = 11
        G1.graph[국립어린이과학관][핏제리아오] = 14
        G1.graph[국립어린이과학관][투파인드피터] = 12
        G1.graph[국립어린이과학관][고부기] = 15
        G1.graph[국립어린이과학관][코야코] = 15

        G1.graph[짚풀박물관][페르시안궁전] = 5
        G1.graph[짚풀박물관][이삭토스트] = 4
        G1.graph[짚풀박물관][나누미떡볶이] = 6
        G1.graph[짚풀박물관][머노까머나] = 6
        G1.graph[짚풀박물관][뎁짜이] = 6
        G1.graph[짚풀박물관][호호식당] = 8
        G1.graph[짚풀박물관][메밀향그집] = 6
        G1.graph[짚풀박물관][정돈] = 10
        G1.graph[짚풀박물관][군자대한곱창] = 5
        G1.graph[짚풀박물관][칸다소바] = 7
        G1.graph[짚풀박물관][순대실록] = 10
        G1.graph[짚풀박물관][핏제리아오] = 13
        G1.graph[짚풀박물관][투파인드피터] = 12
        G1.graph[짚풀박물관][고부기] = 13
        G1.graph[짚풀박물관][코야코] = 14

        G1.graph[아르코미술관][페르시안궁전] = 15
        G1.graph[아르코미술관][이삭토스트] = 14
        G1.graph[아르코미술관][나누미떡볶이] = 13
        G1.graph[아르코미술관][머노까머나] = 10
        G1.graph[아르코미술관][뎁짜이] = 9
        G1.graph[아르코미술관][호호식당] = 7
        G1.graph[아르코미술관][메밀향그집] = 7
        G1.graph[아르코미술관][정돈] = 6
        G1.graph[아르코미술관][군자대한곱창] = 8
        G1.graph[아르코미술관][칸다소바] = 7
        G1.graph[아르코미술관][순대실록] = 5
        G1.graph[아르코미술관][핏제리아오] = 4
        G1.graph[아르코미술관][투파인드피터] = 2
        G1.graph[아르코미술관][고부기] = 3
        G1.graph[아르코미술관][코야코] = 2

        G1.graph[낙산공원][페르시안궁전] = 20
        G1.graph[낙산공원][이삭토스트] = 19
        G1.graph[낙산공원][나누미떡볶이] = 18
        G1.graph[낙산공원][머노까머나] = 14
        G1.graph[낙산공원][뎁짜이] = 14
        G1.graph[낙산공원][호호식당] = 13
        G1.graph[낙산공원][메밀향그집] = 12
        G1.graph[낙산공원][정돈] = 12
        G1.graph[낙산공원][군자대한곱창] = 12
        G1.graph[낙산공원][칸다소바] = 11
        G1.graph[낙산공원][순대실록] = 6
        G1.graph[낙산공원][핏제리아오] = 6
        G1.graph[낙산공원][투파인드피터] = 7
        G1.graph[낙산공원][고부기] = 6
        G1.graph[낙산공원][코야코] = 6

        # 음식점->놀거리
        G1.graph[페르시안궁전][국립어린이과학관] = 6
        G1.graph[이삭토스트][국립어린이과학관] = 5
        G1.graph[나누미떡볶이][국립어린이과학관] = 4
        G1.graph[머노까머나][국립어린이과학관] = 3
        G1.graph[뎁짜이][국립어린이과학관] = 4
        G1.graph[호호식당][국립어린이과학관] = 6
        G1.graph[메밀향그집][국립어린이과학관] = 6
        G1.graph[정돈][국립어린이과학관] = 7
        G1.graph[군자대한곱창][국립어린이과학관] = 7
        G1.graph[칸다소바][국립어린이과학관] = 8
        G1.graph[순대실록][국립어린이과학관] = 11
        G1.graph[핏제리아오][국립어린이과학관] = 14
        G1.graph[투파인드피터][국립어린이과학관] = 12
        G1.graph[고부기][국립어린이과학관] = 15
        G1.graph[코야코][국립어린이과학관] = 15

        G1.graph[페르시안궁전][짚풀박물관] = 5
        G1.graph[이삭토스트][짚풀박물관] = 4
        G1.graph[나누미떡볶이][짚풀박물관] = 6
        G1.graph[머노까머나][짚풀박물관] = 6
        G1.graph[뎁짜이][짚풀박물관] = 6
        G1.graph[호호식당][짚풀박물관] = 8
        G1.graph[메밀향그집][짚풀박물관] = 6
        G1.graph[정돈][짚풀박물관] = 10
        G1.graph[군자대한곱창][짚풀박물관] = 5
        G1.graph[칸다소바][짚풀박물관] = 7
        G1.graph[순대실록][짚풀박물관] = 10
        G1.graph[핏제리아오][짚풀박물관] = 13
        G1.graph[투파인드피터][짚풀박물관] = 12
        G1.graph[고부기][짚풀박물관] = 13
        G1.graph[코야코][짚풀박물관] = 14

        G1.graph[페르시안궁전][아르코미술관] = 15
        G1.graph[이삭토스트][아르코미술관] = 14
        G1.graph[나누미떡볶이][아르코미술관] = 13
        G1.graph[머노까머나][아르코미술관] = 10
        G1.graph[뎁짜이][아르코미술관] = 9
        G1.graph[호호식당][아르코미술관] = 7
        G1.graph[메밀향그집][아르코미술관] = 7
        G1.graph[정돈][아르코미술관] = 6
        G1.graph[군자대한곱창][아르코미술관] = 8
        G1.graph[칸다소바][아르코미술관] = 7
        G1.graph[순대실록][아르코미술관] = 5
        G1.graph[핏제리아오][아르코미술관] = 4
        G1.graph[투파인드피터][아르코미술관] = 2
        G1.graph[고부기][아르코미술관] = 3
        G1.graph[코야코][아르코미술관] = 2

        G1.graph[페르시안궁전][낙산공원] = 20
        G1.graph[이삭토스트][낙산공원] = 19
        G1.graph[나누미떡볶이][낙산공원] = 18
        G1.graph[머노까머나][낙산공원] = 14
        G1.graph[뎁짜이][낙산공원] = 14
        G1.graph[호호식당][낙산공원] = 13
        G1.graph[메밀향그집][낙산공원] = 12
        G1.graph[정돈][낙산공원] = 12
        G1.graph[군자대한곱창][낙산공원] = 12
        G1.graph[칸다소바][낙산공원] = 11
        G1.graph[순대실록][낙산공원] = 6
        G1.graph[핏제리아오][낙산공원] = 6
        G1.graph[투파인드피터][낙산공원] = 7
        G1.graph[고부기][낙산공원] = 6
        G1.graph[코야코][낙산공원] = 6

        # 놀거리->연극
        G1.graph[국립어린이과학관][링크아트센터] = 11
        G1.graph[국립어린이과학관][서연아트홀] = 6
        G1.graph[국립어린이과학관][쿼드] = 12
        G1.graph[국립어린이과학관][예스24스테이지] = 11
        G1.graph[국립어린이과학관][컬쳐씨어터] = 12
        G1.graph[국립어린이과학관][자유극장] = 12
        G1.graph[국립어린이과학관][티오엠] = 12
        G1.graph[국립어린이과학관][드림씨어터] = 12

        G1.graph[짚풀박물관][링크아트센터] = 9
        G1.graph[짚풀박물관][서연아트홀] = 3
        G1.graph[짚풀박물관][쿼드] = 10
        G1.graph[짚풀박물관][예스24스테이지] = 10
        G1.graph[짚풀박물관][컬쳐씨어터] = 11
        G1.graph[짚풀박물관][자유극장] = 11
        G1.graph[짚풀박물관][티오엠] = 11
        G1.graph[짚풀박물관][드림씨어터] = 11

        G1.graph[아르코미술관][링크아트센터] = 9
        G1.graph[아르코미술관][서연아트홀] = 9
        G1.graph[아르코미술관][쿼드] = 5
        G1.graph[아르코미술관][예스24스테이지] = 4
        G1.graph[아르코미술관][컬쳐씨어터] = 3
        G1.graph[아르코미술관][자유극장] = 4
        G1.graph[아르코미술관][티오엠] = 3
        G1.graph[아르코미술관][드림씨어터] = 3

        G1.graph[낙산공원][링크아트센터] = 9
        G1.graph[낙산공원][서연아트홀] = 12
        G1.graph[낙산공원][쿼드] = 6
        G1.graph[낙산공원][예스24스테이지] = 7
        G1.graph[낙산공원][컬쳐씨어터] = 6
        G1.graph[낙산공원][자유극장] = 6
        G1.graph[낙산공원][티오엠] = 7
        G1.graph[낙산공원][드림씨어터] = 7

        # 연극->놀거리
        G1.graph[링크아트센터][국립어린이과학관] = 11
        G1.graph[서연아트홀][국립어린이과학관] = 6
        G1.graph[쿼드][국립어린이과학관] = 12
        G1.graph[예스24스테이지][국립어린이과학관] = 11
        G1.graph[컬쳐씨어터][국립어린이과학관] = 12
        G1.graph[자유극장][국립어린이과학관] = 12
        G1.graph[티오엠][국립어린이과학관] = 12
        G1.graph[드림씨어터][국립어린이과학관] = 12

        G1.graph[링크아트센터][짚풀박물관] = 9
        G1.graph[서연아트홀][짚풀박물관] = 3
        G1.graph[쿼드][짚풀박물관] = 10
        G1.graph[예스24스테이지][짚풀박물관] = 10
        G1.graph[컬쳐씨어터][짚풀박물관] = 11
        G1.graph[자유극장][짚풀박물관] = 11
        G1.graph[티오엠][짚풀박물관] = 11
        G1.graph[드림씨어터][짚풀박물관] = 11

        G1.graph[링크아트센터][아르코미술관] = 9
        G1.graph[서연아트홀][아르코미술관] = 9
        G1.graph[쿼드][아르코미술관] = 5
        G1.graph[예스24스테이지][아르코미술관] = 4
        G1.graph[컬쳐씨어터][아르코미술관] = 3
        G1.graph[자유극장][아르코미술관] = 4
        G1.graph[티오엠][아르코미술관] = 3
        G1.graph[드림씨어터][아르코미술관] = 3

        G1.graph[링크아트센터][낙산공원] = 9
        G1.graph[서연아트홀][낙산공원] = 12
        G1.graph[쿼드][낙산공원] = 6
        G1.graph[예스24스테이지][낙산공원] = 7
        G1.graph[컬쳐씨어터][낙산공원] = 6
        G1.graph[자유극장][낙산공원] = 6
        G1.graph[티오엠][낙산공원] = 7
        G1.graph[드림씨어터][낙산공원] = 7
        min_cost, path = G1.getMinCostTour(user_nodes)
        path_name = ' - '.join(nameAry[i] for i in path)
        self.state1=f"  추천 데이트 코스는 다음과 같습니다."
        self.state2=f"  {path_name}"
        self.state3=f"  예상 이동 시간은 {min_cost}분 입니다."

    def show_result(self):
        msg = QMessageBox()
        msg.setWindowTitle("추천 코스")
        msg.setStandardButtons(QMessageBox.NoButton)
        ok_button = QPushButton("확인", msg)  # create OK button
        ok_button.setStyleSheet("QPushButton { min-width: 70px; min-height: 30px; }")
        ok_button.setFont(QFont("HY동녘M", 10))
        ok_button.clicked.connect(msg.accept)
        msg.setStyleSheet("QMessageBox {background-color: rgb(255, 189, 190); margin: 10px;}}")

        text_edit = QTextEdit()

        # set font
        font = QFont("HY동녘M", 9)  # replace "Arial" with your preferred font and 14 with your preferred font size
        text_edit.setFont(font)

        text_edit.setText(self.state1 +  "\n" +"\n" +self.state2+"\n"+"\n"+self.state3)
        text_edit.setReadOnly(True)

        layout = msg.layout()
        layout.addWidget(text_edit, 0, 1)  # Move the text_edit to the top
        layout.addWidget(ok_button, 1, 0, 1, 2, Qt.AlignCenter)  # Move the OK button to the bottom center
        layout.addItem(QSpacerItem(800, 0, QSizePolicy.Minimum, QSizePolicy.Expanding), layout.rowCount(), 0, 1, layout.columnCount())  # 500 here is the width you want
        msg.exec()
 # Set the size of the QMessageBox

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "결과"))
        self.reset.setText(_translate("Dialog", "초기화"))
        self.program_finish.setText(_translate("Dialog", "종료"))
        self.clse_finish.setText(_translate("Dialog", "창 닫기"))
        self.result.setText(_translate("Dialog", "결과 보기"))


    def re_set(self):
        choose.clear()
        user_nodes.clear()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    startscreen = QtWidgets.QDialog()
    start_ui = UI_startscreen()
    start_ui.setupUi(startscreen)

    mainscreen = QtWidgets.QDialog()
    main_ui = UI_mainscreen()
    main_ui.setupUi(mainscreen)

    start_ui.NEXT.clicked.connect(startscreen.close)  # Close the start screen dialog
    start_ui.NEXT.clicked.connect(mainscreen.show)  # Open the main screen dialog

    startscreen.show()
    sys.exit(app.exec_())

