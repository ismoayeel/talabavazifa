from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QHBoxLayout, QVBoxLayout, QMessageBox, QCheckBox, QRadioButton, QComboBox
class myclass(QWidget):
    def __init__(self):
        super().__init__()

        self.setStyleSheet("font-size:20px")

        self.h_lay=QHBoxLayout()
        self.h1_lay=QHBoxLayout()
        self.h2_lay=QHBoxLayout()
        self.h3_lay=QHBoxLayout()
        self.h4_lay=QHBoxLayout()
        self.h5_lay=QHBoxLayout()
        self.h6_lay=QHBoxLayout()
        self.h7_lay=QHBoxLayout()
        self.h8_lay=QHBoxLayout()

        self.v1_lay=QVBoxLayout()
        self.v2_lay=QVBoxLayout()
        self.v3_lay=QVBoxLayout()
        self.v4_lay=QVBoxLayout()
        self.v5_lay=QVBoxLayout()
        self.v6_lay=QVBoxLayout()

        self.v_main_lay=QVBoxLayout()

        self.ism_lbl=QLabel("Ism:")
        self.sharif_lbl=QLabel("Sharif:")
        self.yosh_lbl=QLabel("Yosh:")
        self.jins_lbl=QLabel("Jins:")
        self.viloyat_lbl=QLabel("viloyat:")
        self.telefon_lbl=QLabel("Telefon:")
        self.fakultet_lbl=QLabel("Fakultet:")
        self.kurs_lbl=QLabel("Kurs:")

        self.erkak_radio_btn=QRadioButton("Erkak")
        self.ayol_radio_btn=QRadioButton("Ayol")

        self.saqlash_btn=QPushButton("Saqlash")
        self.saqlash_btn.clicked.connect(self.Saqlash)

        self.ism_edit=QLineEdit()
        self.sharif_edit=QLineEdit()
        self.yosh_edit=QLineEdit()
        self.telefon_edit=QLineEdit()
        self.fakultet_edit=QLineEdit()

        self.viloyat_cmb=QComboBox()
        self.viloyat_cmb.addItems(["", "Toshkent viloyati", "Andijon viloyati", "Farg'ona viloyati", "Namangan viloyati", "Samarqand viloyati", 
                                   "Buxoro viloyati", "Navoiy viloyati", "Qashqadaryo viloyati", "Surhondaryo viloyati", "Jizzax viloyati", 
                                   "Sirdaryo viloyati", "Xorazm viloyati"])
        

        self.kurs_cmb=QComboBox()
        self.kurs_cmb.addItems(["", "1-kurs", "2-kurs", "3-kurs", "4-kurs"])

        self.v1_lay.addWidget(self.ism_lbl)
        self.v2_lay.addWidget(self.ism_edit)

        self.v1_lay.addWidget(self.sharif_lbl)
        self.v2_lay.addWidget(self.sharif_edit)

        self.v1_lay.addWidget(self.yosh_lbl)
        self.v2_lay.addWidget(self.yosh_edit)

        self.v2_lay.addWidget(self.erkak_radio_btn)
        self.v2_lay.addWidget(self.ayol_radio_btn)
        self.v1_lay.addWidget(self.jins_lbl)
        self.v1_lay.addStretch()

        self.h1_lay.addLayout(self.v1_lay)
        self.h1_lay.addLayout(self.v2_lay)

        self.v3_lay.addWidget(self.viloyat_lbl)
        self.v4_lay.addWidget(self.viloyat_cmb)

        self.v3_lay.addWidget(self.telefon_lbl)
        self.v4_lay.addWidget(self.telefon_edit)

        self.v3_lay.addWidget(self.fakultet_lbl)
        self.v4_lay.addWidget(self.fakultet_edit)
        
        self.v3_lay.addWidget(self.kurs_lbl)
        self.v4_lay.addWidget(self.kurs_cmb)

        self.h2_lay.addLayout(self.v3_lay)
        self.h2_lay.addLayout(self.v4_lay)


        self.v_main_lay.addLayout(self.h1_lay)
        self.v_main_lay.addLayout(self.h2_lay)
        self.v_main_lay.addWidget(self.saqlash_btn)

        self.setLayout(self.v_main_lay)


    def Saqlash(self):
        f=open("malumotlar.txt", "w+")

        if self.ism_edit.text() != "" and list(self.ism_edit.text())[0].isupper():
            if self.sharif_edit.text() != "" and list(self.sharif_edit.text())[0].isupper():
                if self.yosh_edit.text() != "" and int(self.yosh_edit.text()) > 10 and int(self.yosh_edit.text()) < 100:
                    if self.telefon_edit.text() != "" and list(self.telefon_edit.text())[0] == "+" and len(self.telefon_edit.text()) == 13:
                        if self.erkak_radio_btn.isChecked() or self.ayol_radio_btn.isChecked():
                            if self.viloyat_cmb.currentText() != "":
                                if self.kurs_cmb.currentText() != "":
                                    if self.fakultet_edit.text() !="":
                                        if self.erkak_radio_btn.isChecked():
                                            jins=self.erkak_radio_btn.text()
                                        else:
                                            jins=self.ayol_radio_btn.text()
                                        f.write(f"{self.ism_edit.text()},{self.sharif_edit.text()},{self.yosh_edit.text()},"
                                                f"{self.telefon_edit.text()},{jins},{self.viloyat_cmb.currentText()},"
                                                f"{self.kurs_cmb.currentText()},{self.fakultet_edit.text()}\n")

                                        self.msg=QMessageBox()
                                        self.msg.setWindowTitle("Muvaffaqiyatli")
                                        self.msg.setIcon(QMessageBox.Information)
                                        self.msg.setText("Ma'lumotlar muvaffaqiyatli saqlandi")
                                        self.msg.exec_()
                                        self.ism_edit.clear()
                                        self.sharif_edit.clear()
                                        self.yosh_edit.clear()
                                        self.erkak_radio_btn.setChecked(False)
                                        self.ayol_radio_btn.setChecked(False)
                                        self.viloyat_cmb.setCurrentIndex(-1)
                                        self.kurs_cmb.setCurrentIndex(-1),
                                        self.fakultet_edit.clear()
                                        self.telefon_edit.clear()
                                    else:
                                        self.msg=QMessageBox()
                                        self.msg.setIcon(QMessageBox.Warning)
                                        self.msg.setText("Fakultetni kiriting!!!")
                                        self.msg.exec_()
                                else:
                                    self.msg=QMessageBox()
                                    self.msg.setIcon(QMessageBox.Warning)
                                    self.msg.setText("Kursni tanlang!!!")
                                    self.msg.exec_()
                            else:
                                self.msg=QMessageBox()
                                self.msg.setIcon(QMessageBox.Warning)
                                self.msg.setText("Viloyatni tanlang!!!")
                                self.msg.exec_()
                        else:
                            self.msg=QMessageBox()
                            self.msg.setIcon(QMessageBox.Warning)
                            self.msg.setText("Jinsni tanlang!!!")
                            self.msg.exec_()
                    else:
                        self.msg=QMessageBox()
                        self.msg.setIcon(QMessageBox.Warning)
                        self.msg.setText("Telefonni togri kiriting birinchi + bolsin va 12ta raqam")
                        self.msg.exec_()
                else:
                    self.msg=QMessageBox()
                    self.msg.setIcon(QMessageBox.Warning)
                    self.msg.setText("Yoshni to'gri kiriting musbat butun 10 va 100 orasida bolsin!!!")
                    self.msg.exec_()
            else:
                self.msg=QMessageBox()
                self.msg.setIcon(QMessageBox.Warning)
                self.msg.setText("Sharfni togri kiriting!!! \n1-harfi katta qolganlari kichik bolsin!!!")
                self.msg.exec_()
        else:
            self.msg=QMessageBox()
            self.msg.setIcon(QMessageBox.Warning)
            self.msg.setText("Ismni togri kiriting!!! \n1-harfi katta qolganlari kichik bolsin!!!")
            self.msg.exec_()


        f.close()



        
app=QApplication([])
win=myclass()
win.show()
app.exec_()
