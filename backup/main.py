# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sd_reader.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import serial
import serial.tools.list_ports


conn_status = "Chưa kết nối"
dir_stack = []


class hexType(QtWidgets.QSpinBox):
    def __init__(self, *args, **kwargs):
        self.var = tk.StringVar()
        self.bytenum = kwargs.pop('bytenum')
        max_val = 0x1<<(self.bytenum*8)
        super().__init__(*args, **kwargs, textvariable=self.var, from_=0,to=max_val,
                         increment=1, command=self.cange )

    def set(self, val):
        s = "0x{:0%dx}" % (self.bytenum*2)
        self.var.set(s.format(int(val)))
        
    def get(self):
        hstr = super().get()
        return int(hstr, 16)

    def cange(self):
        val = super().get()
        self.set(val)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(528, 442)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/micro-sd-xxl.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        self.tab1_wr_btn = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.tab1_wr_btn.setFont(font)
        self.tab1_wr_btn.setObjectName("tab1_wr_btn")
        self.gridLayout_3.addWidget(self.tab1_wr_btn, 11, 3, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 9, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 4, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 0, 3, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 9, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 11, 1, 1, 1)
        self.tab1_rd_btn = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tab1_rd_btn.setFont(font)
        self.tab1_rd_btn.setObjectName("tab1_rd_btn")
        self.gridLayout_3.addWidget(self.tab1_rd_btn, 11, 2, 1, 1)
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
        self.com_sel_box = QtWidgets.QComboBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.com_sel_box.setFont(font)
        self.com_sel_box.setEditable(True)
        self.com_sel_box.setObjectName("com_sel_box")
        self.com_sel_box.addItem("")
        self.com_sel_box.addItem("")
        self.com_sel_box.addItem("")
        self.com_sel_box.addItem("")
        self.com_sel_box.addItem("")
        self.com_sel_box.addItem("")
        self.com_sel_box.addItem("")
        self.com_sel_box.addItem("")
        self.com_sel_box.addItem("")
        self.com_sel_box.addItem("")
        self.com_sel_box.addItem("")
        self.com_sel_box.addItem("")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.com_sel_box)
        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 2, 4)
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
        self.tab1_text1 = QtWidgets.QLineEdit(self.tab)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab1_text1.setFont(font)
        self.tab1_text1.setObjectName("tab1_text1")
        self.tab1_text1.setText("0x")
        self.gridLayout_2.addWidget(self.tab1_text1, 1, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 1, 1, 1)
        self.tab1_text2 = QtWidgets.QLineEdit(self.tab)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab1_text2.setFont(font)
        self.tab1_text2.setObjectName("tab1_text2")
        self.tab1_text2.setMaxLength(1)
        self.gridLayout_2.addWidget(self.tab1_text2, 2, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 1, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tab_2.setFont(font)
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout_4.addWidget(self.label_10, 0, 1, 1, 2)
        self.tab2_text1 = QtWidgets.QLineEdit(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab2_text1.setFont(font)
        self.tab2_text1.setText("")
        self.tab2_text1.setObjectName("tab2_text1")
        self.tab2_text1.setText("0x")
        self.gridLayout_4.addWidget(self.tab2_text1, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 0, 0, 1, 1)
        self.tab2_text3 = QtWidgets.QTextEdit(self.tab_2)
        self.tab2_text3.setObjectName("tab2_text3")
        self.tab2_text3.textChanged.connect(self.content_validate)
        self.gridLayout_4.addWidget(self.tab2_text3, 3, 0, 1, 4)
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_4.addWidget(self.label_9, 2, 0, 1, 1)
        self.tab2_text2 = QtWidgets.QSpinBox(self.tab_2)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.tab2_text2.setFont(font)
        self.tab2_text2.setMaximum(999)
        self.tab2_text2.setObjectName("tab2_text2")
        self.gridLayout_4.addWidget(self.tab2_text2, 1, 1, 1, 2)
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
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.tab3_selector = QtWidgets.QToolButton(self.tab_5)
        self.tab3_selector.clicked.connect(self.file_browse_handler)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab3_selector.setFont(font)
        self.tab3_selector.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.tab3_selector.setAutoFillBackground(True)
        self.tab3_selector.setObjectName("tab3_selector")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.tab3_selector)
        self.tab3_text1 = QtWidgets.QLineEdit(self.tab_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab3_text1.setFont(font)
        self.tab3_text1.setText("")
        self.tab3_text1.setObjectName("tab3_text1")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.tab3_text1)
        self.tabWidget.addTab(self.tab_5, "")
        self.gridLayout_3.addWidget(self.tabWidget, 3, 0, 5, 4)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 528, 22))
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
        self.actionAboutUs = QtWidgets.QAction(MainWindow)
        self.actionAboutUs.setObjectName("actionAboutUs")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuAbout_2.addAction(self.actionAboutUs)
        self.menubar.addAction(self.menuAbout_2.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.statusbar.showMessage("Chưa kết nối")
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Đọc ghi nội dung SD Card - Nhóm 7"))
        self.tab1_wr_btn.setText(_translate("MainWindow", "Ghi"))
        self.tab1_wr_btn.clicked.connect(self.write_callback)
        self.tab1_rd_btn.setText(_translate("MainWindow", "Đọc"))
        self.tab1_rd_btn.clicked.connect(self.read_callback)
        self.groupBox.setTitle(_translate("MainWindow", "Kết nối"))
        self.label.setText(_translate("MainWindow", "Kết nối bộ đọc/ghi"))
        self.conn_btn.setText(_translate("MainWindow", "Kết nối"))
        self.conn_btn.clicked.connect(self.serial_conn)

        ports = [p.name for p in serial.tools.list_ports.comports()]
        if len(ports) != 0:
            for i in range(len(ports)):
                self.com_sel_box.setItemText(i, _translate("MainWindow", str(ports[i])))
        else:
            self.com_sel_box.setCurrentText(_translate("MainWindow", "Không phát hiện COM Port"))
        
        self.com_sel_box.currentIndexChanged.connect(self.refresh_com_list)
        # self.com_sel_box.setItemText(0, _translate("MainWindow", "COM1"))
        # self.com_sel_box.setItemText(1, _translate("MainWindow", "COM2"))
        # self.com_sel_box.setItemText(2, _translate("MainWindow", "COM3"))
        # self.com_sel_box.setItemText(3, _translate("MainWindow", "COM4"))
        # self.com_sel_box.setItemText(4, _translate("MainWindow", "COM5"))
        # self.com_sel_box.setItemText(5, _translate("MainWindow", "COM6"))
        # self.com_sel_box.setItemText(6, _translate("MainWindow", "COM7"))
        # self.com_sel_box.setItemText(7, _translate("MainWindow", "COM8"))
        # self.com_sel_box.setItemText(8, _translate("MainWindow", "COM9"))
        # self.com_sel_box.setItemText(9, _translate("MainWindow", "COM10"))
        # self.com_sel_box.setItemText(10, _translate("MainWindow", "COM11"))
        # self.com_sel_box.setItemText(11, _translate("MainWindow", "COM12"))
        self.label_2.setText(_translate("MainWindow", "Địa chỉ byte"))
        self.label_3.setText(_translate("MainWindow", "Nội dung byte"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Đọc ghi từng byte"))
        self.label_10.setText(_translate("MainWindow", "Kích thước block (byte)"))
        self.label_5.setText(_translate("MainWindow", "Địa chỉ bắt đầu block"))
        self.label_9.setText(_translate("MainWindow", "Nội dung ghi"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Đọc ghi từng Block"))
        self.label_8.setText(_translate("MainWindow", "Đường dẫn file"))
        self.tab3_selector.setText(_translate("MainWindow", "..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Đọc ghi file"))
        self.menuAbout_2.setTitle(_translate("MainWindow", "About"))
        self.actionOpen_file.setText(_translate("MainWindow", "Mở file"))
        self.actionAboutUs.setText(_translate("MainWindow", "Về chúng tôi"))
        self.actionExit.setText(_translate("MainWindow", "Thoát"))

    def write_callback(self):
        current_tab = self.tabWidget.currentIndex()

        if (current_tab == 0):
            byte_addr = self.tab1_text1.text()
            if (byte_addr[:2] != "0x"):
                self.statusbar.showMessage("Địa chỉ không hợp lệ!!!")
                return -1
            byte_content = self.tab1_text2.text()
            #TODO: Send write command to serial
            try:
                status = "Gửi ký tự '" +str(byte_content)+"' tới địa chỉ "+ byte_addr
                self.statusbar.showMessage(status)
            except Exception as e:
                self.statusbar.showMessage("Lỗi ghi: "+ str(e))

        elif (current_tab == 1):
            block_addr = self.tab2_text1.text()
            if (block_addr[:2] != "0x"):
                self.statusbar.showMessage("Địa chỉ không hợp lệ!!!")
                return -1
            block_size = self.tab2_text2.value()
            block_content = self.tab2_text3.toPlainText()
            print(block_size)
            print(block_content)
            self.statusbar.showMessage("Tab2")

        elif (current_tab == 2):
            self.statusbar.showMessage("Tab3")

    def read_callback(self):
        current_tab = self.tabWidget.currentIndex()

        if (current_tab == 0):
            byte_addr = self.tab1_text1.text()
            if (byte_addr[:2] != "0x"):
                self.statusbar.showMessage("Địa chỉ không hợp lệ!!!")
                return -1

            #TODO: Read byte content to byte_content
            try:
                byte_content = 'O'
                self.tab1_text2.setText(byte_content)
                status = "Nội dung ở ô nhớ "+ byte_addr+ " là: "+str(byte_content)
                self.statusbar.showMessage(status)
            except Exception as e:
                self.statusbar.showMessage("Lỗi khi đọc ô nhớ "+ byte_addr+": "+str(e))

    def serial_conn(self):
        port = str(self.com_sel_box.currentText())
        status = str("Đang kết nối "+port+" nè...")
        self.statusbar.showMessage(status)

        try:
            handler = serial.Serial(port = port, baudrate=115200,
                            bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
            
            self.statusbar.showMessage("Đã kết nối")

        except Exception as e:
            self.statusbar.showMessage("Lỗi khi kết nối: "+ str(e))
    
    def refresh_com_list(self):
        ports = [p.name for p in serial.tools.list_ports.comports()]
        if len(ports) != 0:
            self.com_sel_box.setCurrentText(_translate("MainWindow", str(ports[0])))
            for i in range(1,len(ports)):
                self.com_sel_box.setItemText(i, _translate("MainWindow", str(ports[i])))


    def content_validate(self):
        txt = self.tab2_text3.toPlainText()
        max_len = self.tab2_text2.value()
        if (len(txt) > max_len):
            txt = txt[0:max_len]
            self.tab2_text3.setText("")
            self.tab2_text3.append(str(txt))
            self.statusbar.showMessage("Nội dung ghi vượt quá kích thước block!!!")
        self.tab2_text3.update()
        return 0


    def file_browse_handler(self):
        global dir_stack
        #### Lưu ý trường hợp trùng tên file
        try:
            file_names = ""
            dirs = QFileDialog.getOpenFileNames()[0]
            for dir in dirs:
                fields = dir.split('/')
                print(fields)
                if str(self.tab3_text1.text()).find(str(fields[-1])) == -1:
                    dir_stack.append(dir)
                    file_names += str(fields[-1])+";"
                else:
                    self.statusbar.showMessage("Trùng file "+ fields[-1])
            for dir in dir_stack:
                print(dir)
            files = self.tab3_text1.text() + file_names
            self.tab3_text1.setText(files)
            return 0
        except Exception as e:
            self.statusbar.showMessage("Lỗi khi mở duyệt file: "+ str(e))
            return -1


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
