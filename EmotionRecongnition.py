# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EmotionRecongnition_UI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMovie
from real_time_video_me import Emotion_Rec
from os import getcwd
import numpy as np
import cv2
import time
from base64 import b64decode
from os import remove
from slice_png import img as bgImg
import image1_rc

class Ui_MainWindow(object):
    def __init__(self, MainWindow):
        self.path = getcwd()
        self.timer_camera = QtCore.QTimer()  # 定时器

        self.setupUi(MainWindow)
        self.retranslateUi(MainWindow)
        self.slot_init()  # 槽函数设置

        # 设置界面动画
        gif = QMovie(':/newPrefix/images_test/scan.gif')
        self.label_face.setMovie(gif)
        gif.start()

        self.cap = cv2.VideoCapture()  # 屏幕画面对象
        self.CAM_NUM = 0  # 摄像头标号
        self.model_path = None  # 模型路径
        # self.__flag_work = 0

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(765, 645)
        MainWindow.setMinimumSize(QtCore.QSize(765, 645))
        MainWindow.setMaximumSize(QtCore.QSize(765, 645))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/images_test/result.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolTip("")
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("#MainWindow{border-image: url(:/newPrefix/images_test/background.PNG);}\n"
                                "\n"
                                "#QInputDialog{border-image: url(:/newPrefix/images_test/light.png);}\n"
                                "\n"
                                "QMenuBar{border-color:transparent;}\n"
                                "QToolButton[objectName=pushButton_doIt]{\n"
                                "border:5px;}\n"
                                "\n"
                                "QToolButton[objectName=pushButton_doIt]:hover {\n"
                                "image:url(:/newPrefix/images_test/run_hover.png);}\n"
                                "\n"
                                "QToolButton[objectName=pushButton_doIt]:pressed {\n"
                                "image:url(:/newPrefix/images_test/run_pressed.png);}\n"
                                "\n"
                                "QScrollBar:vertical{\n"
                                "background:transparent;\n"
                                "padding:2px;\n"
                                "border-radius:8px;\n"
                                "max-width:14px;}\n"
                                "\n"
                                "QScrollBar::handle:vertical{\n"
                                "background:#9acd32;\n"
                                "min-height:50px;\n"
                                "border-radius:8px;\n"
                                "}\n"
                                "\n"
                                "QScrollBar::handle:vertical:hover{\n"
                                "background:#9eb764;}\n"
                                "\n"
                                "QScrollBar::handle:vertical:pressed{\n"
                                "background:#9eb764;\n"
                                "}\n"
                                "QScrollBar::add-page:vertical{\n"
                                "background:none;\n"
                                "}\n"
                                "                               \n"
                                "QScrollBar::sub-page:vertical{\n"
                                "background:none;\n"
                                "}\n"
                                "\n"
                                "QScrollBar::add-line:vertical{\n"
                                "background:none;}\n"
                                "                                 \n"
                                "QScrollBar::sub-line:vertical{\n"
                                "background:none;\n"
                                "}\n"
                                "QScrollArea{\n"
                                "border:0px;\n"
                                "}\n"
                                "\n"
                                "QScrollBar:horizontal{\n"
                                "background:transparent;\n"
                                "padding:0px;\n"
                                "border-radius:6px;\n"
                                "max-height:12px;\n"
                                "}\n"
                                "\n"
                                "QScrollBar::handle:horizontal{\n"
                                "background:#9acd32;\n"
                                "min-width:50px;\n"
                                "border-radius:6px;\n"
                                "}\n"
                                "\n"
                                "QScrollBar::handle:horizontal:hover{\n"
                                "background:#9eb764;\n"
                                "}\n"
                                "\n"
                                "QScrollBar::handle:horizontal:pressed{\n"
                                "background:#9eb764;\n"
                                "}\n"
                                "\n"
                                "QScrollBar::add-page:horizontal{\n"
                                "background:none;\n"
                                "}\n"
                                "\n"
                                "QScrollBar::sub-page:horizontal{\n"
                                "background:none;\n"
                                "}\n"
                                "QScrollBar::add-line:horizontal{\n"
                                "background:none;\n"
                                "}\n"
                                "\n"
                                "QScrollBar::sub-line:horizontal{\n"
                                "background:none;\n"
                                "}\n"
                                "QToolButton::hover{\n"
                                "border:0px;\n"
                                "} ")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(80, 40, 271, 30))
        self.label_title.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(22)
        font.setItalic(True)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_title.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_title.setObjectName("label_title")
        self.label_useTime = QtWidgets.QLabel(self.centralwidget)
        self.label_useTime.setGeometry(QtCore.QRect(530, 200, 91, 51))
        font = QtGui.QFont()
        font.setFamily("华文仿宋")
        font.setPointSize(18)
        self.label_useTime.setFont(font)
        self.label_useTime.setObjectName("label_useTime")
        self.label_scanResult = QtWidgets.QLabel(self.centralwidget)
        self.label_scanResult.setGeometry(QtCore.QRect(530, 280, 151, 31))
        font = QtGui.QFont()
        font.setFamily("华文仿宋")
        font.setPointSize(18)
        self.label_scanResult.setFont(font)
        self.label_scanResult.setObjectName("label_scanResult")
        self.label_picTime = QtWidgets.QLabel(self.centralwidget)
        self.label_picTime.setGeometry(QtCore.QRect(480, 200, 38, 38))
        self.label_picTime.setStyleSheet("border-image:url(:/newPrefix/images_test2/jishi.png);")
        self.label_picTime.setText("")
        self.label_picTime.setObjectName("label_picTime")
        self.label_picResult = QtWidgets.QLabel(self.centralwidget)
        self.label_picResult.setGeometry(QtCore.QRect(480, 270, 41, 41))
        self.label_picResult.setStyleSheet("border-image: url(:/newPrefix/images_test2/zhibiaojieguo.png)")
        self.label_picResult.setText("")
        self.label_picResult.setObjectName("label_picResult")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(440, 160, 321, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_face = QtWidgets.QLabel(self.centralwidget)
        self.label_face.setGeometry(QtCore.QRect(10, 360, 420, 280))
        self.label_face.setMinimumSize(QtCore.QSize(420, 280))
        self.label_face.setMaximumSize(QtCore.QSize(420, 280))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        self.label_face.setFont(font)
        self.label_face.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_face.setStyleSheet("border-image: url(:/newPrefix/images_test/scan.gif);")
        self.label_face.setAlignment(QtCore.Qt.AlignCenter)
        self.label_face.setObjectName("label_face")
        self.textEdit_model = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_model.setGeometry(QtCore.QRect(60, 180, 360, 30))
        self.textEdit_model.setMinimumSize(QtCore.QSize(360, 30))
        self.textEdit_model.setMaximumSize(QtCore.QSize(360, 30))
        font = QtGui.QFont()
        font.setFamily("华文仿宋")
        font.setPointSize(12)
        self.textEdit_model.setFont(font)
        self.textEdit_model.setStyleSheet("background-color: transparent;\n"
"border-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);")
        self.textEdit_model.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_model.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_model.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.textEdit_model.setReadOnly(True)
        self.textEdit_model.setObjectName("textEdit_model")
        self.toolButton_file = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_file.setGeometry(QtCore.QRect(10, 300, 50, 40))
        self.toolButton_file.setMinimumSize(QtCore.QSize(50, 39))
        self.toolButton_file.setMaximumSize(QtCore.QSize(50, 40))
        self.toolButton_file.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_file.setAutoFillBackground(False)
        self.toolButton_file.setStyleSheet("background-color: transparent;")
        self.toolButton_file.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/images_test2/wenjian.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_file.setIcon(icon1)
        self.toolButton_file.setIconSize(QtCore.QSize(40, 40))
        self.toolButton_file.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.toolButton_file.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_file.setAutoRaise(False)
        self.toolButton_file.setArrowType(QtCore.Qt.NoArrow)
        self.toolButton_file.setObjectName("toolButton_file")
        self.textEdit_camera = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_camera.setGeometry(QtCore.QRect(60, 250, 360, 30))
        self.textEdit_camera.setMinimumSize(QtCore.QSize(360, 30))
        self.textEdit_camera.setMaximumSize(QtCore.QSize(360, 30))
        font = QtGui.QFont()
        font.setFamily("华文仿宋")
        font.setPointSize(12)
        self.textEdit_camera.setFont(font)
        self.textEdit_camera.setStyleSheet("background-color: transparent;\n"
"border-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);")
        self.textEdit_camera.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_camera.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_camera.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.textEdit_camera.setReadOnly(True)
        self.textEdit_camera.setObjectName("textEdit_camera")
        self.textEdit_pic = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_pic.setGeometry(QtCore.QRect(60, 310, 360, 30))
        self.textEdit_pic.setMinimumSize(QtCore.QSize(360, 30))
        self.textEdit_pic.setMaximumSize(QtCore.QSize(360, 30))
        font = QtGui.QFont()
        font.setFamily("华文仿宋")
        font.setPointSize(12)
        self.textEdit_pic.setFont(font)
        self.textEdit_pic.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textEdit_pic.setStyleSheet("background-color: transparent;\n"
"border-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);")
        self.textEdit_pic.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_pic.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_pic.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.textEdit_pic.setReadOnly(True)
        self.textEdit_pic.setObjectName("textEdit_pic")
        self.toolButton_camera = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_camera.setGeometry(QtCore.QRect(10, 240, 50, 45))
        self.toolButton_camera.setMinimumSize(QtCore.QSize(50, 39))
        self.toolButton_camera.setMaximumSize(QtCore.QSize(50, 45))
        self.toolButton_camera.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_camera.setAutoFillBackground(False)
        self.toolButton_camera.setStyleSheet("background-color: transparent;")
        self.toolButton_camera.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/images_test2/shexiangtou.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_camera.setIcon(icon2)
        self.toolButton_camera.setIconSize(QtCore.QSize(50, 39))
        self.toolButton_camera.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.toolButton_camera.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_camera.setAutoRaise(False)
        self.toolButton_camera.setArrowType(QtCore.Qt.NoArrow)
        self.toolButton_camera.setObjectName("toolButton_camera")
        self.toolButton_model = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_model.setGeometry(QtCore.QRect(10, 170, 50, 40))
        self.toolButton_model.setMinimumSize(QtCore.QSize(0, 0))
        self.toolButton_model.setMaximumSize(QtCore.QSize(50, 40))
        self.toolButton_model.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_model.setAutoFillBackground(False)
        self.toolButton_model.setStyleSheet("background-color: transparent;")
        self.toolButton_model.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/newPrefix/images_test2/dakaiwenjian.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_model.setIcon(icon3)
        self.toolButton_model.setIconSize(QtCore.QSize(40, 40))
        self.toolButton_model.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.toolButton_model.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_model.setAutoRaise(False)
        self.toolButton_model.setArrowType(QtCore.Qt.NoArrow)
        self.toolButton_model.setObjectName("toolButton_model")
        self.label_time = QtWidgets.QLabel(self.centralwidget)
        self.label_time.setGeometry(QtCore.QRect(610, 206, 90, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_time.setFont(font)
        self.label_time.setObjectName("label_time")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(440, 340, 321, 21))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_result = QtWidgets.QLabel(self.centralwidget)
        self.label_result.setGeometry(QtCore.QRect(640, 278, 120, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_result.setFont(font)
        self.label_result.setStyleSheet("color: rgb(0, 189, 189);")
        self.label_result.setObjectName("label_result")
        self.label_outputResult = QtWidgets.QLabel(self.centralwidget)
        self.label_outputResult.setGeometry(QtCore.QRect(450, 380, 300, 250))
        self.label_outputResult.setMinimumSize(QtCore.QSize(300, 250))
        self.label_outputResult.setMaximumSize(QtCore.QSize(300, 250))
        self.label_outputResult.setStyleSheet("border-image: url(:/newPrefix/images_test2/ini.png)")
        self.label_outputResult.setText("")
        self.label_outputResult.setObjectName("label_outputResult")
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionGoogle_Translate = QtWidgets.QAction(MainWindow)
        self.actionGoogle_Translate.setObjectName("actionGoogle_Translate")
        self.actionHTML_type = QtWidgets.QAction(MainWindow)
        self.actionHTML_type.setObjectName("actionHTML_type")
        self.actionsoftware_version = QtWidgets.QAction(MainWindow)
        self.actionsoftware_version.setObjectName("actionsoftware_version")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Emotion recongnition"))
        self.label_title.setText(_translate("MainWindow", "表情识别系统 "))
        self.label_useTime.setText(_translate("MainWindow", "<html><head/><body><p>用时：</p></body></html>"))
        self.label_scanResult.setText(_translate("MainWindow", "<html><head/><body><p>识别结果：<br/></p></body></html>"))
        self.label_face.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.textEdit_model.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'华文仿宋\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Adobe Devanagari\';\">选择模型</span></p></body></html>"))
        self.textEdit_camera.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'华文仿宋\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Adobe Devanagari\';\">实时摄像未开启</span></p></body></html>"))
        self.textEdit_pic.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'华文仿宋\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Adobe Devanagari\';\">选择图片</span></p></body></html>"))
        self.label_time.setText(_translate("MainWindow", "0 s"))
        self.label_result.setText(_translate("MainWindow", "None"))
        self.actionGoogle_Translate.setText(_translate("MainWindow", "Google Translate"))
        self.actionHTML_type.setText(_translate("MainWindow", "HTML type"))
        self.actionsoftware_version.setText(_translate("MainWindow", "software version"))

    def slot_init(self):  # 定义槽函数
        self.toolButton_camera.clicked.connect(self.button_open_camera_click)
        self.toolButton_model.clicked.connect(self.choose_model)
        self.timer_camera.timeout.connect(self.show_camera)
        self.toolButton_file.clicked.connect(self.choose_pic)

    def button_open_camera_click(self):
        if self.timer_camera.isActive() == False:  # 检查定时状态
            flag = self.cap.open(self.CAM_NUM)  # 检查相机状态
            if flag == False:  # 相机打开失败提示
                msg = QtWidgets.QMessageBox.warning(self.centralwidget, u"Warning",
                                                    u"请检测相机与电脑是否连接正确！ ",
                                                    buttons=QtWidgets.QMessageBox.Ok,
                                                    defaultButton=QtWidgets.QMessageBox.Ok)

            else:
                # 准备运行识别程序
                self.textEdit_pic.setText('文件未选中')
                QtWidgets.QApplication.processEvents()
                self.textEdit_camera.setText('实时摄像已开启')
                self.label_face.setText('正在启动识别系统...\n\nleading')
                # 新建对象
                self.emotion_model = Emotion_Rec(self.model_path)
                QtWidgets.QApplication.processEvents()
                # 打开定时器
                self.timer_camera.start(30)
        else:
            # 定时器未开启，界面回复初始状态
            self.timer_camera.stop()
            self.cap.release()
            self.label_face.clear()
            self.textEdit_camera.setText('实时摄像已关闭')
            self.textEdit_pic.setText('文件未选中')
            gif = QMovie(':/newPrefix/images_test/scan.gif')
            self.label_face.setMovie(gif)
            gif.start()
            self.label_outputResult.clear()
            self.label_outputResult.setStyleSheet("border-image: url(:/newPrefix/images_test2/ini.png);")

            self.label_result.setText('None')
            self.label_time.setText('0 s')

    def show_camera(self):
        # 定时器槽函数，每隔一段时间执行
        flag, self.image = self.cap.read()  # 获取画面
        self.image = cv2.flip(self.image, 1)  # 左右翻转

        tmp = open('slice.png', 'wb')
        tmp.write(b64decode(bgImg))
        tmp.close()
        canvas = cv2.imread('slice.png')  # 用于数据显示的背景图片
        remove('slice.png')

        time_start = time.time()  # 计时
        # 使用模型预测
        result = self.emotion_model.run(self.image, canvas, self.label_face, self.label_outputResult)
        time_end = time.time()
        # 在界面显示结果
        self.label_result.setText(result)
        self.label_time.setText(str(round((time_end - time_start), 3)) + ' s')

    def choose_pic(self):
        # 界面处理
        self.timer_camera.stop()
        self.cap.release()
        self.label_face.clear()
        self.label_result.setText('None')
        self.label_time.setText('0 s')
        self.textEdit_camera.setText('实时摄像已关闭')
        self.label_outputResult.clear()
        self.label_outputResult.setStyleSheet("border-image: url(:/newPrefix/images_test2/ini.png);")

        # 使用文件选择对话框选择图片
        fileName_choose, filetype = QFileDialog.getOpenFileName(
            self.centralwidget, "选取图片文件",
            self.path,  # 起始路径
            "图片(*.jpg;*.jpeg;*.png)")  # 文件类型
        self.path = fileName_choose  # 保存路径
        if fileName_choose != '':
            self.textEdit_pic.setText(fileName_choose + '文件已选中')
            self.label_face.setText('正在启动识别系统...\n\nleading')
            QtWidgets.QApplication.processEvents()
            # 生成模型对象
            self.emotion_model = Emotion_Rec(self.model_path)
            # 读取背景图
            tmp = open('slice.png', 'wb')
            tmp.write(b64decode(bgImg))
            tmp.close()
            canvas = cv2.imread('slice.png')
            remove('slice.png')

            image = self.cv_imread(fileName_choose)  # 读取选择的图片
            # 计时并开始模型预测
            QtWidgets.QApplication.processEvents()
            time_start = time.time()
            result = self.emotion_model.run(image, canvas, self.label_face, self.label_outputResult)
            time_end = time.time()
            # 显示结果
            self.label_result.setText(result)
            self.label_time.setText(str(round((time_end - time_start), 3)) + ' s')

        else:
            # 选择取消，恢复界面状态
            self.textEdit_pic.setText('文件未选中')
            gif = QMovie(':/newPrefix/images_test/scan.gif')
            self.label_face.setMovie(gif)
            gif.start()
            self.label_outputResult.clear()  # 清除画面
            self.label_outputResult.setStyleSheet("border-image: url(:/newPrefix/images_test2/ini.png);")
            self.label_result.setText('None')
            self.label_time.setText('0 s')

    def cv_imread(self, filePath):
        # 读取图片
        cv_img = cv2.imdecode(np.fromfile(filePath, dtype=np.uint8), -1)
        ## imdecode读取的是rgb，如果后续需要opencv处理的话，需要转换成bgr，转换后图片颜色会变化
        ## cv_img=cv2.cvtColor(cv_img,cv2.COLOR_RGB2BGR)
        return cv_img

    def choose_model(self):
        # 选择训练好的模型文件
        self.timer_camera.stop()
        self.cap.release()
        self.label_face.clear()
        self.label_result.setText('None')
        self.label_time.setText('0 s')
        self.textEdit_camera.setText('实时摄像已关闭')
        self.label_outputResult.clear()
        self.label_outputResult.setStyleSheet("border-image: url(:/newPrefix/images_test2/ini.png);")

        # 调用文件选择对话框
        fileName_choose, filetype = QFileDialog.getOpenFileName(self.centralwidget,
                                                                "选取图片文件", getcwd(),  # 起始路径
                                                                "Model File (*.hdf5)")  # 文件类型
        # 显示提示信息
        if fileName_choose != '':
            self.model_path = fileName_choose
            self.textEdit_model.setText(fileName_choose + ' 已选中')
        else:
            self.textEdit_model.setText('使用默认模型')

        # 恢复界面
        gif = QMovie(':/newPrefix/images_test/scan.gif')
        self.label_face.setMovie(gif)
        gif.start()
