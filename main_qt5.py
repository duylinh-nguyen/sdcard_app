# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog,QMessageBox, QMainWindow, QDialog
from PyQt5.QtCore import pyqtSignal, QObject, QThread
import serial
from serial import Serial
import serial.tools.list_ports
import time
import threading
import queue
import sys
import glob


conn_status = "Chưa kết nối"
dir_stack = []
dataframe_q = queue.Queue()

class Ui_MainWindow(object):
    def __init__(self, connection_handler):
        self.com_handler = connection_handler
        self.conn_status = False
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(580, 505)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 14, 2, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 11, 4, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setObjectName("groupBox")
        self.formLayout_2 = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setEnabled(True)
        self.label.setMinimumSize(QtCore.QSize(0, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.conn_btn = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.conn_btn.setFont(font)
        self.conn_btn.setFlat(False)
        self.conn_btn.setObjectName("conn_btn")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.conn_btn)
        self.com_sel_box = customComboBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.com_sel_box.setFont(font)
        self.com_sel_box.setEditable(True)
        self.com_sel_box.setObjectName("com_sel_box")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.com_sel_box)
        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 2, 5)
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 5, 3, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 0, 4, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 11, 0, 1, 1)
        self.tab1_rd_btn = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tab1_rd_btn.setFont(font)
        self.tab1_rd_btn.setObjectName("tab1_rd_btn")
        self.gridLayout_3.addWidget(self.tab1_rd_btn, 14, 3, 1, 1)
        self.tab1_wr_btn = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.tab1_wr_btn.setFont(font)
        self.tab1_wr_btn.setObjectName("tab1_wr_btn")
        self.gridLayout_3.addWidget(self.tab1_wr_btn, 14, 4, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.frame)
        self.tabWidget.setMaximumSize(QtCore.QSize(751, 16777215))
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.tab.setFont(font)
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 1, 1, 1)
        self.tab1_text2 = QtWidgets.QLineEdit(self.tab)
        self.tab1_text2.setMaxLength(8)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab1_text2.setFont(font)
        self.tab1_text2.setObjectName("tab1_text2")
        self.gridLayout_2.addWidget(self.tab1_text2, 2, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 1, 1, 1)
        self.tab1_text1 = QtWidgets.QLineEdit(self.tab)
        self.tab1_text1.setMaxLength(10)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab1_text1.setText("0x00000000")
        self.tab1_text1.setFont(font)
        self.tab1_text1.setObjectName("tab1_text2")
        self.gridLayout_2.addWidget(self.tab1_text1,  1, 3, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tab_2.setFont(font)
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_4.addWidget(self.label_9, 2, 0, 1, 1)
        self.tab2_text3 = QtWidgets.QTextEdit(self.tab_2)
        self.tab2_text3.textChanged.connect(self.content_validate)
        self.tab2_text3.setObjectName("tab2_text3")
        self.gridLayout_4.addWidget(self.tab2_text3, 3, 0, 1, 4)
        self.tab2_text2 = QtWidgets.QSpinBox(self.tab_2)
        self.tab2_text2.valueChanged.connect(self.resize_text3)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.tab2_text2.setFont(font)
        self.tab2_text2.setMaximum(999)
        self.tab2_text2.setObjectName("tab2_text2")
        self.gridLayout_4.addWidget(self.tab2_text2, 1, 1, 1, 2)
        self.tab2_text1 = QtWidgets.QLineEdit(self.tab_2)
        self.tab2_text1.setMaxLength(10)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab2_text2.setValue(512)
        self.tab2_text2.setEnabled(False)
        self.tab2_text1.setFont(font)
        self.tab2_text1.setText("0x00000000")
        self.tab2_text1.setObjectName("tab2_text1")
        self.gridLayout_4.addWidget(self.tab2_text1, 1, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout_4.addWidget(self.label_10, 0, 1, 1, 2)
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.formLayout = QtWidgets.QFormLayout(self.tab_5)
        self.formLayout.setObjectName("formLayout")
        self.label_13 = QtWidgets.QLabel(self.tab_5)
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.label_8 = QtWidgets.QLabel(self.tab_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_8)
        self.tab3_text1 = QtWidgets.QLineEdit(self.tab_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab3_text1.setFont(font)
        self.tab3_text1.setText("")
        self.tab3_text1.setObjectName("tab3_text1")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.tab3_text1)
        # self.tab3_selector = QtWidgets.QToolButton(self.tab_5)
        # self.tab3_selector.clicked.connect(self.file_browse_handler)
        # font = QtGui.QFont()
        # font.setPointSize(12)
        # self.tab3_selector.setFont(font)
        # self.tab3_selector.setLayoutDirection(QtCore.Qt.RightToLeft)
        # self.tab3_selector.setAutoFillBackground(True)
        # self.tab3_selector.setObjectName("tab3_selector")
        # self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.tab3_selector)
        self.label_14 = QtWidgets.QLabel(self.tab_5)
        self.label_14.setObjectName("label_14")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.label_14)
        self.tab3_text2 = QtWidgets.QPlainTextEdit(self.tab_5)
        self.tab3_text2.setObjectName("tab3_text2")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.tab3_text2)
        self.tabWidget.addTab(self.tab_5, "")
        self.gridLayout_3.addWidget(self.tabWidget, 4, 0, 7, 5)
        self.gridLayout.addWidget(self.frame, 0, 0, 2, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 580, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        self.menuAbout_2 = QtWidgets.QMenu(self.menubar)
        self.menuAbout_2.setObjectName("menuAbout_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_file = QtWidgets.QAction(MainWindow)
        self.actionOpen_file.setObjectName("actionOpen_file")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionRefresh = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionRefresh.setObjectName("actionRefresh")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuAbout_2.addAction(self.actionAbout)
        self.menuAbout_2.addAction(self.actionRefresh)
        self.menuAbout_2.addAction(self.actionExit)
        self.actionExit.triggered.connect(self.exit)
        self.actionRefresh.triggered.connect(self.refresh)
        self.actionAbout.triggered.connect(self.about)
        self.menubar.addAction(self.menuAbout_2.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Đọc ghi nội dung SD Card - Nhóm 7"))
        self.groupBox.setTitle(_translate("MainWindow", "Kết nối"))
        self.label.setText(_translate("MainWindow", "Kết nối bộ đọc/ghi"))

        self.ports = self.com_handler.list_ports()

        if len(self.ports) != 0:
            for i in range(len(self.ports)):
                self.com_sel_box.addItem("")
                self.com_sel_box.setItemText(i, _translate("MainWindow", str(self.ports[i])))
        else:
            self.com_sel_box.setCurrentText(_translate("MainWindow", "Không phát hiện COM Port"))
        self.tab1_rd_btn.setText(_translate("MainWindow", "Đọc"))
        self.tab1_wr_btn.setText(_translate("MainWindow", "Ghi"))
        self.label_3.setText(_translate("MainWindow", "Nội dung byte"))
        self.label_2.setText(_translate("MainWindow", "Địa chỉ byte"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Đọc/ghi từng byte"))
        self.label_9.setText(_translate("MainWindow", "Nội dung đọc ghi"))
        self.label_10.setText(_translate("MainWindow", "Kích thước block (byte)"))
        self.label_5.setText(_translate("MainWindow", "Địa chỉ bắt đầu block"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Đọc ghi từng Block"))
        self.label_8.setText(_translate("MainWindow", "Đường dẫn file"))
        # self.tab3_selector.setText(_translate("MainWindow", "..."))
        self.label_14.setText(_translate("MainWindow", "Nội dung đọc/ghi"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Đọc ghi file"))
        self.menuAbout_2.setTitle(_translate("MainWindow", "Menu"))
        self.actionOpen_file.setText(_translate("MainWindow", "Mở file"))
        self.actionAbout.setText(_translate("MainWindow", "Về chúng tôi"))
        self.actionRefresh.setText(_translate("MainWindow", "Refresh COM Ports"))
        self.actionExit.setText(_translate("MainWindow", "Thoát"))
        self.conn_btn.setText(_translate("MainWindow", "Kết nối"))
        self.tab1_wr_btn.clicked.connect(self.write_callback)
        self.tab1_rd_btn.clicked.connect(self.read_callback)
        self.conn_btn.clicked.connect(self.serial_conn)

    def write_callback(self):
        if (self.conn_status == False):
            self.statusbar.showMessage("Chưa kết nối")
            return -1

        current_tab = self.tabWidget.currentIndex()

        if (current_tab == 0):
            byte_addr = self.tab1_text1.text()
            byte_content = self.tab1_text2.text()
            if (byte_addr[:2] != "0x" and len(byte_addr)!=10):
                self.statusbar.showMessage("Địa chỉ không hợp lệ!!!")
                return -1

            if len(byte_content) == 8:
                p = set(byte_content)
                s = {'0', '1'} 
                if s == p or p == {'0'} or p == {'1'}: 
                    byte_content = chr(int(byte_content,2))
                    print("Nội dung dạng binary")
                else:
                    self.statusbar.showMessage("Nội dung không đúng định dạng binary")
                    return -1

            elif len(byte_content) == 4:
                if byte_content[0:2] == '0x': 
                    byte_content =  bytearray.fromhex(byte_content[2:]).decode()
                    print("Nội dung dạng hex")
                else:
                    self.statusbar.showMessage("Nội dung không đúng định dạng")
                    return -1

            elif len(byte_content) == 1:
                print("Nội dung dạng ký tự ASCII")

            else:
                self.statusbar.showMessage("Nội dung phải ở dạng hex, binary hoặc kí tự ASCII")
                return -1

            #TODO: Send write command to serial
            # self.com_handler.handler.write("Hello world".encode())
            self.com_handler.write_byte(byte_addr[2:], byte_content, self)
            try:
                status = "Gửi ký tự '" +str(byte_content)+"' tới địa chỉ "+ byte_addr
                self.statusbar.showMessage(status)
            except Exception as e:
                self.statusbar.showMessage("Lỗi ghi: "+ str(e))

        elif (current_tab == 1):
            block_addr = self.tab2_text1.text()
            block_len = self.tab2_text2.value()
            if (block_addr[:2] != "0x"):
                self.statusbar.showMessage("Địa chỉ không hợp lệ!!!")
                return -1
            # block_size = self.tab2_text2.value()
            block_content = self.tab2_text3.toPlainText()
            stt = self.com_handler.write_block(block_addr[2:], block_content, block_len, self)
            if stt:
                self.statusbar.showMessage("Gửi lệnh thành công")
            else:
                self.statusbar.showMessage("Gửi lệnh  thất bại")

        if (current_tab == 2):
            file_addr = self.tab3_text1.text()
            file_content = self.tab3_text2.toPlainText()

            stt = self.com_handler.write_file(file_addr, file_content, self)

            if stt:
                self.statusbar.showMessage("Gửi lệnh thành công")
            else:
                self.statusbar.showMessage("Gửi lệnh thất bại")


    def read_callback(self):
        if (self.conn_status == False):
            self.statusbar.showMessage("Chưa kết nối")
            return -1
            
        current_tab = self.tabWidget.currentIndex()

        if (current_tab == 0):
            byte_addr = self.tab1_text1.text()
            
            if (byte_addr[:2] != "0x"):
                self.statusbar.showMessage("Địa chỉ không hợp lệ!!!")
                return -1

            #TODO: Read byte content to byte_content
            try:
                self.com_handler.read_byte(byte_addr[2:], self)
                # status = "Nội dung ở ô nhớ "+ byte_addr+ " là: "+str(byte_content)
                # self.statusbar.showMessage(status)
            except Exception as e:
                self.statusbar.showMessage("Lỗi khi đọc ô nhớ "+ byte_addr+": "+str(e))
        
        elif (current_tab == 1):
            byte_addr = self.tab2_text1.text()
            data_len = self.tab2_text2.value()

            if (byte_addr[:2] != "0x"):
                self.statusbar.showMessage("Địa chỉ không hợp lệ!!!")
                return -1

            #TODO: Read byte content to byte_content
            try:
                self.com_handler.read_block(byte_addr[2:], data_len, self)
            except Exception as e:
                self.statusbar.showMessage("Lỗi khi đọc Block "+ byte_addr+": "+str(e))

        if (current_tab == 2):
            file_addr = self.tab3_text1.text()

            try:
                stt = self.com_handler.read_file(file_addr, self)
            except Exception as e:
                self.statusbar.showMessage("Lỗi khi đọc file "+ file_addr+": "+str(e))

    def serial_conn(self):
        if not self.conn_status:
            port = str(self.com_sel_box.currentText())
            status = str("Đang kết nối "+port+" nè...")
            self.statusbar.showMessage(status)
            self.conn_status = self.com_handler.connect(port)
            if self.conn_status:
                self.statusbar.showMessage("Kết nối thành công")
                return 0
            else:
                self.statusbar.showMessage("Kết nối thất bại")
                return -1
        else:
            self.statusbar.showMessage("Đã kết nối")
            return -1
    
    def refresh_com_list(self):
        ports = self.com_handler.list_ports()
        print("Hello world")
        print(ports)
        if len(ports) != 0:
            self.com_sel_box.setCurrentText(_translate("MainWindow", str(ports[0])))
            for i in range(1,len(ports)):
                self.com_sel_box.setItemText(i, _translate("MainWindow", str(ports[i])))


    def content_validate(self):
        txt = self.tab2_text3.toPlainText()
        max_len = self.tab2_text2.value()
        if (len(txt.encode('utf-8')) > max_len):
            txt = txt[0:max_len]
            self.tab2_text3.setText('')
            self.tab2_text3.append(txt)
            self.statusbar.showMessage("Nội dung ghi vượt quá kích thước block!!!")
        # return 0

    def file_browse_handler(self):
        global dir_stack
        #### Lưu ý trường hợp trùng tên file
        try:
            path = QFileDialog.getOpenFileName()[0]
            self.tab3_text1.setText(path)
            return 0
        except Exception as e:
            self.statusbar.showMessage("Lỗi khi mở duyệt file: "+ str(e))
            return -1

    def resize_text3(self):
        # self.tab2_text3.setMaximumSize(self.tab2_text2.value 
        # self.statusbar.showMessage("Độ dài tối đa nội dung sẽ là "+self.tab2_text2.value()+" bytes")
        return 0

    def updateContent(self, buff, readtype, thread_obj):
        self.com_handler.serialThread.quit()
        if (readtype==0):
            b = str(format(ord(buff[0]), 'b'))
            self.tab1_text2.setMaxLength(50)
            self.tab1_text2.setText(str(b+" ("+buff[0]+")"))
        elif (readtype==1):
            self.tab2_text2.setValue(len(buff))
            self.tab2_text3.setText(str(buff))
        elif (readtype==2):
            self.tab3_text2.setPlainText(str(buff))

    def raise_write_status(self):
        self.com_handler.serialThread.quit()
        self.statusbar.showMessage("Ghi thành công")

    def exit(self):
        sys.exit()

    def refresh(self):
        _translate = QtCore.QCoreApplication.translate
        self.ports = self.com_handler.list_ports()
        self.com_sel_box.clear()
        if len(self.ports) != 0:
            for i in range(0,len(self.ports)):
                self.com_sel_box.addItem("")
                self.com_sel_box.setItemText(i, _translate("MainWindow", str(self.ports[i])))
        else:
            self.com_sel_box.setCurrentText(_translate("MainWindow", "Không phát hiện COM Port"))

    def about(self):
        dlg  =QMessageBox.about(self.MainWindow, "Thông tin về chúng tôi", "SẢN PHẨM CỦA NHÓM 7\n\nPhần mềm thao tác đọc/ghi thẻ nhớ.\n\nAuthor: Linh Nguyen")
    

class SerialCOM(object):
    def list_ports(self):
        if sys.platform.startswith('win'):
            ports = ['COM%s' % (i + 1) for i in range(256)]
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            # this excludes your current terminal "/dev/tty"
            ports = glob.glob('/dev/tty[A-Za-z]*')
        elif sys.platform.startswith('darwin'):
            ports = glob.glob('/dev/tty.*')
        else:
            raise EnvironmentError('Unsupported platform')

        result = []
        for port in ports:
            try:
                s = serial.Serial(port)
                s.close()
                result.append(port)
            except (OSError, serial.SerialException):
                pass
        return result

    def connect(self, port):
        try:
            self.handler = serial.Serial(port = port, baudrate=57600 ,
                            bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
            
            status = "Đã kết nối"
            return  True
        except Exception as e:
            status = "Lỗi khi kết nối: "+ str(e)
            return False
            pass

    def read_byte(self, addr, ui_obj):
        try:
            # Serial send read byte command
            cmd = ""
            for i in range(512):
                cmd += str(0x00)
            cmd = '##rb'+addr+cmd+"\r\n"
            print("Block len :", len(cmd))
            self.handler.write(cmd.encode())
            print("Start read byte...")
            self.serialThread = serialReadThread(self.handler, 0)
            self.serialThread.trigger.connect(ui_obj.updateContent)
            self.serialThread.start()
            return True
        except Exception as e:
            print("Read byte err: ", str(e))
            return False
            pass
        return 0
    
    def write_byte(self, addr, content, ui_obj):
        try:
            #Serial send write byte command
            cmd = content
            for i in range(512-len(cmd)):
                cmd += str(0x00)
            cmd ='##wb'+addr+cmd+ "\r\n"
            print("Block len :", len(cmd))
            print("--> Frame lenght: ", len(cmd))
            self.handler.write(cmd.encode())
            self.serialThread = serialWriteThread(self.handler)
            self.serialThread.trigger.connect(ui_obj.raise_write_status)
            self.serialThread.start()
            return True
        except:
            print("Lỗi write byte")
            return False
            pass

    def write_block(self, addr, content, data_len, ui_obj):
        try:
            #Serial send write byte command
            cmd = content
            for i in range(512-(len(cmd))):
                cmd += str(0x00)
            cmd = '##wl'+addr+cmd+"\r\n"
            print("Block len :", len(cmd))
            self.handler.write(cmd.encode())
            self.serialThread = serialWriteThread(self.handler)
            self.serialThread.trigger.connect(ui_obj.raise_write_status)
            self.serialThread.start()
            return True
        except Exception as e:
            print("Lỗi write block:", str(e))
            return False
            pass
    
    def write_file(self, path, content, ui_obj):
        try:
            cmd = chr(25)+content
            for i in range(512-(len(cmd))):
                cmd+= str(0x00)
            cmd = '##wf'+path+cmd+"\r\n"
            print("--> Length: ", len(cmd))
            print("--> Content: ", cmd)
            self.handler.write(cmd.encode())
            self.serialThread = serialWriteThread(self.handler)
            self.serialThread.trigger.connect(ui_obj.raise_write_status)
            self.serialThread.start()
            return True
        except Exception as e:
            print("Lỗi write file:", str(e))
            return False
            pass

    def read_block(self, addr, data_len, ui_obj):
        try:
            # Serial send read byte command
            cmd = ""
            for i in range(512):
                cmd += str(0x00)
            cmd = '##rl'+addr+cmd+"\r\n"
            print("--> Length: ", len(cmd))
            print("--> Content: ", cmd)
            self.handler.write(cmd.encode())
            print("Start read block...")
            self.serialThread = serialReadThread(self.handler, 1)
            self.serialThread.trigger.connect(ui_obj.updateContent)
            self.serialThread.start()
            return True
        except Exception as e:
            print("Read block err: ", str(e))
            return False
            pass
        return 0

    def read_file(self, path, ui_obj):
        try:
            # Serial send read byte command
            cmd = path
            for i in range(512-(len(cmd))):
                cmd += str(0x00)
            cmd = '##rf'+cmd+"\r\n"
            print("--> Length: ", len(cmd))
            print("--> Content: ", cmd)
            self.handler.write(cmd.encode())
            print("Start read file...")
            self.serialThread = serialReadThread(self.handler, 2)
            self.serialThread.trigger.connect(ui_obj.updateContent)
            self.serialThread.start()
            return True
        except Exception as e:
            print("Read file err: ", str(e))
            return False
            pass
        return 0


class customComboBox(QtWidgets.QComboBox):
    pass

## Function for serial read thread 
def serial_read(serial_obj, ui_obj, readtype):
    aux_buff = ""
    buff = ""
    is_start = False
    while True:
        for line in serial_obj.read():
            try:
                line = chr(line)
                aux_buff = aux_buff + line 
                if (is_start):
                    buff = buff + line 
                if ("##rb" == aux_buff[len(aux_buff)-4:]) and (readtype == 0):
                    # print("start frame")
                    aux_buff = ""
                    is_start= True
                if ("##rl" == aux_buff[len(aux_buff)-4:]) and (readtype == 1):
                    print("start frame")
                    aux_buff = ""
                    is_start= True
                if ("##rf" == aux_buff[len(aux_buff)-4:]) and (readtype == 2):
                    # print("start frame")
                    aux_buff = ""
                    is_start= True
                #### Sửa end frame thành \r\n
                if (aux_buff[len(aux_buff)-1:].encode() == b'\r') and is_start:
                    print("End frame, thread stoped")
                    # print("Send: ", buff)
                    if (readtype==0):
                        ui_obj.tab1_text2.setText(str(buff))
                    elif (readtype==1):
                        print(buff)
                        ui_obj.tab2_text3.setText(str(buff))
                    elif (readtype==2):
                        ui_obj.tab3_text2.setText(str(buff))
                    serial_obj.flush()
                    sys.exit()
            except (Exception) as e:
                print("Serial read err: ", str(e))
            # print("Encode:", aux_buff[len(aux_buff)-1:].encode())
            serial_obj.write(line.encode())

    return data_buffer

class serialReadThread(QThread):
    trigger = pyqtSignal(str, int, object)
    thread_exit = False
    def __init__(self, serial_obj=None, readtype = 0):
        QThread.__init__(self)
        self.serial_obj = serial_obj
        self.readtype = readtype

    def run(self):
        # global dataframe_q
        aux_buff = ""
        buff = ""
        is_start = False
        while (not self.thread_exit):
            for line in self.serial_obj.read():
                try:
                    line = chr(line)
                    print(line.encode())
                    aux_buff = aux_buff + line 
                    if (is_start):
                        buff = buff + line 
                    if ("##rb" == aux_buff[len(aux_buff)-4:]) and (self.readtype == 0):
                        # print("start frame")
                        aux_buff = ""
                        is_start= True
                    if ("##rl" == aux_buff[len(aux_buff)-4:]) and (self.readtype == 1):
                        # print("start Sframe")
                        aux_buff = ""
                        is_start= True
                    if ("##rf" == aux_buff[len(aux_buff)-4:]) and (self.readtype == 2):
                        # print("start frame")
                        aux_buff = ""
                        is_start= True
                    #### Sửa end frame thành \r\n
                    if (aux_buff[len(aux_buff)-1:].encode() == b'\r') and is_start:
                        print("End frame, thread stoped")
                        # print("Send: ", buff)
                        # dataframe_q.put(buff)
                        self.trigger.emit(buff, self.readtype, self)
                        self.serial_obj.flush()
                        print('Exittting...')
                        self.thread_exit = True
                        return 
                except (Exception) as e:
                    print("Serial read err: ", str(e))
                # print("Encode:", aux_buff[len(aux_buff)-1:].encode())
                self.serial_obj.write(line.encode())
                
 
class serialWriteThread(QThread):
    trigger = pyqtSignal()
    thread_exit = False
    def __init__(self, serial_obj=None):
        QThread.__init__(self)
        self.serial_obj = serial_obj

    def run(self):
        # global dataframe_q
        aux_buff = ""
        while (not self.thread_exit):
            for line in self.serial_obj.read():
                try:
                    line = chr(line)
                    print(line.encode())
                    #### Sửa end frame thành \r\n
                    if (aux_buff[len(aux_buff)-4:].encode() == b'ET##'):
                        print("Write successful, thread stopped")
                        self.trigger.emit()
                        self.serial_obj.flush()
                        print('Exittting...')
                        self.thread_exit = True
                        return 
                except (Exception) as e:
                    print("Serial wait for response err: ", str(e))
                # print("Encode:", aux_buff[len(aux_buff)-1:].encode())
                self.serial_obj.write(line.encode())


def main():
    global dir_stack, conn_status, dataframe_q
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    MainWindow = QtWidgets.QMainWindow()
    connection_handler = SerialCOM()
    ui = Ui_MainWindow(connection_handler)   
    ui.setupUi(MainWindow)
    ui.com_sel_box.installEventFilter(ui.com_sel_box)
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()