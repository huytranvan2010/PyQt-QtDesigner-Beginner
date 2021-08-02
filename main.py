import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from calculator import Ui_MainWindow    # chính là file chuyển từ .ui

class MainWindow:   # tạo class nên thêm dấu ngoặc (), nếu super class có thể không cần
    def __init__(self):
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)

        # khi nút này được nhấn nó sẽ gọi đến method được gọi
        self.uic.Button_Add.clicked.connect(self.add)   # bên dưới method ko nhận tham số ngoài self thì ko cần dấu ngoặc ()
        self.uic.Button_Substract.clicked.connect(self.substract)
        self.uic.Button_Multiply.clicked.connect(self.multiply)
        self.uic.Button_Divide.clicked.connect(self.divide)

    def add(self):
        add_number = self.uic.textEdit.toPlainText() + "+" + self.uic.textEdit_2.toPlainText()  # lấy biểu thức cộng
        # print(number)
        # xử lý ngoại lệ tránh chương trình crash trong lúc chạy
        try:
            result = eval(add_number)   # đánh giá biểu thức và trả về dạng số
            self.uic.label.setText(str(result))     # cần chuyển về string mới hiển thị được
        except:
            self.uic.label.setText("error")

    def substract(self):
        add_number = self.uic.textEdit.toPlainText() + "-" + self.uic.textEdit_2.toPlainText()  # lấy biểu thức cộng
        # print(number)
        try:
            result = eval(add_number)   # đánh giá biểu thức và trả về dạng số
            self.uic.label.setText(str(result))     # cần chuyển về string mới hiển thị được
        except:
            self.uic.label.setText("error")

    def multiply(self):
        add_number = self.uic.textEdit.toPlainText() + "*" + self.uic.textEdit_2.toPlainText()  # lấy biểu thức cộng
        # print(number)
        try:
            result = eval(add_number)   # đánh giá biểu thức và trả về dạng số
            self.uic.label.setText(str(result))     # cần chuyển về string mới hiển thị được
        except:
            self.uic.label.setText("error")

    def divide(self):
        add_number = self.uic.textEdit.toPlainText() + "/" + self.uic.textEdit_2.toPlainText()  # lấy biểu thức cộng
        # print(number)
        try:
            result = eval(add_number)   # đánh giá biểu thức và trả về dạng số
            self.uic.label.setText(str(result))     # cần chuyển về string mới hiển thị được
        except:
            self.uic.label.setText("error")

    def show(self):
        self.main_win.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)    # trong này truyền list tham số
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())    # trong python 3 ko cần phải exec_()
    

