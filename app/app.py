import sys
import os
from configparser import ConfigParser
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit,
                             QPushButton, QFormLayout, QMessageBox, QDialog, QInputDialog,
                             QTableWidget, QTableWidgetItem, QComboBox, QHBoxLayout, QHeaderView)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from swiftlink import SwiftLink
# from qt_material import apply_stylesheet  


class Config:
    def __init__(self, file=os.path.join(os.path.expanduser('~'), '.swift_link.cfg')):
        self.config_file = file
        self.parser = ConfigParser()
        if not os.path.exists(self.config_file):
            self.parser['Setting'] = {'BaseURL': 'http://127.0.0.1:8000'}
            with open(self.config_file, 'w') as configfile:
                self.parser.write(configfile)
        else:
            self.parser.read(self.config_file)

    def get_base_url(self):
        return self.parser['Setting']['BaseURL']

    def set_base_url(self, url):
        self.parser['Setting']['BaseURL'] = url
        with open(self.config_file, 'w') as configfile:
            self.parser.write(configfile)


class LoginDialog(QDialog):
    def __init__(self, config):
        super().__init__()
        self.setWindowTitle('Login')
        self.setGeometry(100, 100, 400, 200)
        self.config = config

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.url_label = QLabel("Base URL:")
        self.url_input = QLineEdit(self.config.get_base_url())

        self.username_label = QLabel("Username:")
        self.username_input = QLineEdit()

        self.password_label = QLabel("Password:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)

        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.login)

        self.register_button = QPushButton("Register")
        self.register_button.clicked.connect(self.register)

        self.form_layout = QFormLayout()
        self.form_layout.addRow(self.url_label, self.url_input)
        self.form_layout.addRow(self.username_label, self.username_input)
        self.form_layout.addRow(self.password_label, self.password_input)

        self.layout.addLayout(self.form_layout)
        self.layout.addWidget(self.login_button)
        self.layout.addWidget(self.register_button)

        self.swiftlink = None

    def login(self):
        base_url = self.url_input.text()
        username = self.username_input.text()
        password = self.password_input.text()

        self.swiftlink = SwiftLink(username, password, base_url)

        if self.swiftlink.user_auth():
            self.config.set_base_url(base_url)
            QMessageBox.information(self, "Login Success", "Logged in successfully!")
            self.accept()
        else:
            QMessageBox.warning(self, "Login Failed", "Failed to log in. Please check your credentials.")

    def register(self):
        base_url = self.url_input.text()
        username = self.username_input.text()
        password = self.password_input.text()

        self.swiftlink = SwiftLink(username, password, base_url)

        if self.swiftlink.user_create():
            self.config.set_base_url(base_url)
            QMessageBox.information(self, "Registration Success", "Registered successfully!")
        else:
            QMessageBox.warning(self, "Registration Failed", "Failed to register. Please try again.")


class SwiftLinkApp(QMainWindow):
    def __init__(self, swiftlink):
        super().__init__()
        self.setWindowTitle('SwiftLink')
        self.setGeometry(100, 100, 800, 600)

        self.swiftlink = swiftlink

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(['Route', 'URL'])
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.table.setWindowTitle("Short Links")
        self.refresh_button = QPushButton("Refresh")
        self.refresh_button.clicked.connect(self.load_shortlinks)

        self.create_shortlink_button = QPushButton("Create Short Link")
        self.create_shortlink_button.clicked.connect(self.create_shortlink)

        self.update_shortlink_button = QPushButton("Update Short Link")
        self.update_shortlink_button.clicked.connect(self.update_shortlink)

        self.delete_shortlink_button = QPushButton("Delete Short Link")
        self.delete_shortlink_button.clicked.connect(self.delete_shortlink)

        self.change_password_button = QPushButton("Change Password")
        self.change_password_button.clicked.connect(self.change_password)

        self.link_combobox = QComboBox()

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.refresh_button)
        button_layout.addWidget(self.create_shortlink_button)
        button_layout.addWidget(self.update_shortlink_button)
        button_layout.addWidget(self.delete_shortlink_button)
        button_layout.addWidget(self.change_password_button)

        self.layout.addWidget(self.table)
        self.layout.addWidget(QLabel("Select Short Link:"))
        self.layout.addWidget(self.link_combobox)
        self.layout.addLayout(button_layout)

        self.load_shortlinks()

    def load_shortlinks(self):
        self.link_combobox.clear()
        shortlinks = self.swiftlink.get_shortlinks()
        if isinstance(shortlinks, Exception):
            QMessageBox.warning(self, "Failed", "Failed to retrieve short links.")
        else:
            self.table.setRowCount(len(shortlinks['short_links']))
            for i, link in enumerate(shortlinks['short_links']):
                self.table.setItem(i, 0, QTableWidgetItem(link['route']))
                self.table.setItem(i, 1, QTableWidgetItem(link['url']))
                self.link_combobox.addItem(link['route'])

    def create_shortlink(self):
        route, url = self.get_route_and_url()
        if route and url and self.swiftlink.create_short_link(route, url):
            QMessageBox.information(self, "Success", "Short link created successfully!")
            self.load_shortlinks()
        else:
            QMessageBox.warning(self, "Failed", "Failed to create short link.")

    def update_shortlink(self):
        route = self.link_combobox.currentText()
        new_route, new_url = self.get_new_route_and_url()
        if route and new_route and new_url and self.swiftlink.update_short_link(route, new_route, new_url):
            QMessageBox.information(self, "Success", "Short link updated successfully!")
            self.load_shortlinks()
        else:
            QMessageBox.warning(self, "Failed", "Failed to update short link.")

    def delete_shortlink(self):
        route = self.link_combobox.currentText()
        if route and self.swiftlink.delete_short_link(route):
            QMessageBox.information(self, "Success", "Short link deleted successfully!")
            self.load_shortlinks()
        else:
            QMessageBox.warning(self, "Failed", "Failed to delete short link.")

    def change_password(self):
        new_password, ok = QInputDialog.getText(self, "Change Password", "Enter new password:", QLineEdit.Password)
        if ok and new_password:
            result = self.swiftlink.change_password(new_password)
            if result:
                QMessageBox.information(self, "Success", "Password changed successfully!")
            else:
                QMessageBox.warning(self, "Failed", "Failed to change password.")

    def get_route_and_url(self):
        route, ok1 = QInputDialog.getText(self, "Input Route", "Enter the route:")
        url, ok2 = QInputDialog.getText(self, "Input URL", "Enter the URL:")
        if ok1 and ok2:
            return route, url
        return None, None

    def get_new_route_and_url(self):
        new_route, ok1 = QInputDialog.getText(self, "Input New Route", "Enter the new route:")
        new_url, ok2 = QInputDialog.getText(self, "Input New URL", "Enter the new URL:")
        if ok1 and ok2:
            return new_route, new_url
        return None, None


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # apply_stylesheet(app, theme='light_blue.xml')
    config = Config()
    login_dialog = LoginDialog(config)
    if login_dialog.exec_() == QDialog.Accepted:
        window = SwiftLinkApp(login_dialog.swiftlink)
        window.show()

    sys.exit(app.exec_())
