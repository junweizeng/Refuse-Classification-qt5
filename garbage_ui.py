import sys
from PyQt5.QtWidgets import QMessageBox
from main import *
from kid import *
import requests


class MainShow(QtWidgets.QWidget, Ui_Main_Dialog):
    def __init__(self):
        super(MainShow, self).__init__()
        self.setupUi(self)
        # 上传图片
        self.pushButton_2.clicked.connect(self.ChoosePath)
        # 开始识别
        self.pushButton.clicked.connect(self.Recognition)
        self.test_path = ''

    def ChoosePath(self):
        file_name = QtWidgets.QFileDialog.getOpenFileName(self, "打开图片", self.test_path, "图片(*.jpg)")
        print(file_name[0])
        self.test_path = file_name[0]
        # 显示路径
        self.lineEdit_2.setText(self.test_path)
        # 显示待测图片
        self.label_4.setPixmap(QtGui.QPixmap(self.test_path))

        # 清空不相关内容
        self.lineEdit.clear()

    def Recognition(self):
        # 存获取的地址
        input = self.lineEdit_2.text()
        if input == "":
            print(QMessageBox.warning(self, "警告", "未插入图片！\n无法进行垃圾识别！", QMessageBox.Yes, QMessageBox.Yes))
            return
        else:
            url = "http://127.0.0.1:5000/upload"
            files = {'file': open(input, 'rb')}
            r = requests.post(url, files=files)
            str = bytes.decode(r.content)
            print(str)
            garbage_type = str.split(" ")

            self.lineEdit.setText(garbage_type[1])
            print(QMessageBox.information(self, "成功识别垃圾类型！", "垃圾识别结果为：" + garbage_type[0], QMessageBox.Yes, QMessageBox.Yes))


class KidShow(QtWidgets.QWidget, Ui_Dialog):
    def __init__(self):
        super(KidShow, self).__init__()
        self.setupUi(self)
        # 上传图片
        self.pushButton.clicked.connect(self.ShowOtherTrash)
        # 开始识别
        self.pushButton_2.clicked.connect(self.ShowRecyclableTrash)

    def ShowRecyclableTrash(self):
        self.label.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; "
                           "color:#428663;\">可回收垃圾介绍</span></p></body></html>")
        self.label_2.setText("<html><head/><body><p><span style=\" font-size:12pt; "
                             "font-weight:600;\">可回收物主要包括废纸、塑料、玻璃、金属和布料五大类。</span></p><p><span style=\" "
                             "font-size:12pt; font-weight:600;\">1. 废纸：主要包括报纸、期刊、图书、各种包装纸等。但是，要注意</span></p><p><span "
                             "style=\" font-size:12pt; font-weight:600;\">纸巾和厕所纸由于水溶性太强不可回收。</span></p><p><span "
                             "style=\" font-size:12pt; font-weight:600;\">2. "
                             "塑料：各种塑料袋、塑料泡沫、塑料包装（快递包装纸是其他垃圾/</span></p><p><span style=\" font-size:12pt; "
                             "font-weight:600;\">干垃圾）、一次性塑料餐盒餐具、硬塑料、塑料牙刷、塑料杯子、矿</span></p><p><span style=\" "
                             "font-size:12pt; font-weight:600;\">泉水瓶等。</span></p><p><span style=\" font-size:12pt; "
                             "font-weight:600;\">3. 玻璃：主要包括各种玻璃瓶、碎玻璃片、暖瓶等。（镜子是其他垃</span></p><p><span style=\" "
                             "font-size:12pt; font-weight:600;\">圾/干垃圾）</span></p><p><span style=\" font-size:12pt; "
                             "font-weight:600;\">4. 金属物：主要包括易拉罐、罐头盒等。</span></p><p><span style=\" font-size:12pt; "
                             "font-weight:600;\">5. 布料：主要包括废弃衣服、桌布、洗脸巾、书包、鞋等。</span></p><p><span style=\" "
                             "font-size:12pt;\"><br/></span></p><p><span style=\" font-size:12pt; "
                             "font-weight:600;\">这些垃圾通过综合处理回收利用，可以减少污染，节省资源。如每回</span></p><p><span style=\" "
                             "font-size:12pt; font-weight:600;\">收1吨废纸可造好纸850公斤，节省木材300公斤，比等量生产减少污</span></p><p><span "
                             "style=\" font-size:12pt; "
                             "font-weight:600;\">染74%；每回收1吨塑料饮料瓶可获得0.7吨二级原料；每回收1吨废钢</span></p><p><span style=\" "
                             "font-size:12pt; "
                             "font-weight:600;\">铁可炼好钢0.9吨，比用矿石冶炼节约成本47%，减少空气污染75%，</span></p><p><span style=\" "
                             "font-size:12pt; font-weight:600;\">减少97%的水污染和固体废物。</span></p></body></html>")
        pixmap = QPixmap("img/可回收垃圾.jpg")
        self.label_3.setScaledContents(True)
        self.label_3.setPixmap(pixmap)

    def ShowOtherTrash(self):
        self.label.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; "
                           "color:#428663;\">干垃圾介绍</span></p></body></html>")
        self.label_2.setText("<html><head/><body><p><span style=\" font-size:12pt; "
                             "font-weight:600;\">其他垃圾（上海称干垃圾）包括除上述几类垃圾之外的砖瓦陶瓷、渣</span></p><p><span style=\" "
                             "font-size:12pt; font-weight:600;\">土、卫生间废纸、纸巾等难以回收的废弃物及尘土、食品袋（盒）。</span></p><p><span "
                             "style=\" font-size:12pt; "
                             "font-weight:600;\">采取卫生填埋可有效减少对地下水、地表水、土壤及空气的污染。<br"
                             "/>大棒骨因为“难腐蚀”被列入“其它垃圾”。玉米核、坚果壳、果</span></p><p><span style=\" font-size:12pt; "
                             "font-weight:600;\">核、鸡骨等则是餐厨垃圾。</span></p><p><span style=\" font-size:12pt; "
                             "font-weight:600;\"><br/>1. 卫生纸：厕纸、卫生纸遇水即溶，不算可回收的“纸张”，类似的</span></p><p><span style=\" "
                             "font-size:12pt; font-weight:600;\">还有烟盒等。</span></p><p><span style=\" font-size:12pt; "
                             "font-weight:600;\"><br/>2. 餐厨垃圾装袋：常用的塑料袋，即使是可以降解的也远比餐厨垃圾</span></p><p><span style=\" "
                             "font-size:12pt; font-weight:600;\">更难腐蚀。此外塑料袋本身是可回收垃圾。正确做法应该是将餐厨垃</span></p><p><span "
                             "style=\" font-size:12pt; font-weight:600;\">圾倒入垃圾桶，塑料袋另扔进“可回收垃圾”桶。</span></p><p><span "
                             "style=\" font-size:12pt; font-weight:600;\"><br/>3. "
                             "果壳：在垃圾分类中，“果壳瓜皮”的标识就是花生壳，的确属于</span></p><p><br/></p><p><span style=\" font-size:12pt; "
                             "font-weight:600;\">厨余垃圾。家里用剩的废弃食用油，也归类在“厨余垃圾”。<br/>4. "
                             "尘土：在垃圾分类中，尘土属于“其它垃圾”，但残枝落叶属于</span></p><p><span style=\" font-size:12pt; "
                             "font-weight:600;\">“厨余垃圾”，包括家里开败的鲜花等。</span></p></body></html>")
        pixmap = QPixmap("img/干垃圾.jpg")
        self.label_3.setScaledContents(True)
        self.label_3.setPixmap(pixmap)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # 实例化主窗口
    main = QMainWindow()
    main_ui = Ui_Main_Dialog()
    main_ui.setupUi(main)
    main = MainShow()
    main.setWindowTitle("垃垃队识垃圾")

    # 实例化子窗口
    child = QDialog()
    child.setWindowTitle("垃垃队识垃圾")
    child_ui = Ui_Dialog()
    child_ui.setupUi(child)
    child1 = KidShow()
    # 按钮绑定事件
    btn = main.pushButton_3
    btn.clicked.connect(child1.show)

    # 显示主窗口
    main.show()
    sys.exit(app.exec_())
