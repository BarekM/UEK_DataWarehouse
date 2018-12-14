import sys


from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QComboBox


from modules.extract import data_scrape
from modules.transform import data_transform
from modules.load import load_files, output_db, output_files, clear_db
from modules.helpers import clear_directory, clear_temp_directories
import config


class MyException(Exception):
    pass


class ETL():
    def __init__(self):
        pass

    def extract(self, city_name):
        city_name = city_name
        output_method = data_scrape(city_name)
        return output_method

    def transform(self):
        output_method = data_transform()
        return output_method

    def load(self):
        output_method = load_files()
        return output_method

    def print(self):
        output_method = output_db()
        return output_method

    def print_files(self):
        output_method = output_files()
        return output_method

    def clear(self):
        output_method = clear_db()
        return output_method


class GuiWebScraper(QWidget):

    def __init__(self, app):
        super().__init__()

        clear_temp_directories()
        self.app = app
        self.initUI()
        self.etl = ETL()

    def initUI(self):

        # tytul pojawiajacy sie w oknie
        self.setWindowTitle('WebScraper')

        # element do wyboru miasta
        self.combobox_city = QComboBox()
        self.combobox_city.addItem("Warszawa")
        self.combobox_city.addItem("Gdansk")
        self.combobox_city.addItem("Wroclaw")
        self.combobox_city.addItem("Katowice")
        self.combobox_city.addItem("Rzeszow")
        self.combobox_city.addItem("Lublin")
        self.combobox_city.addItem("Lodz")
        self.combobox_city.addItem("Krakow")
        self.combobox_city.addItem("Poznan")
        self.combobox_city.addItem("Szczecin")

        # tworzenie przyciskow
        self.button_etl = QPushButton('ETL')
        self.button_etl.clicked.connect(self.etl)

        self.button_extract = QPushButton('Extract')
        self.button_extract.clicked.connect(self.extract)

        self.button_load = QPushButton('Load')
        self.button_load.clicked.connect(self.load)

        self.button_transform = QPushButton('Transform')
        self.button_transform.clicked.connect(self.transform)

        self.button_print = QPushButton('Print')
        self.button_print.clicked.connect(self.print)

        self.button_print_files = QPushButton('Print files')
        self.button_print_files.clicked.connect(self.print_files)

        self.button_clear = QPushButton('Clear')
        self.button_clear.clicked.connect(self.clear)

        # przestrzen do wyswietlenia danych
        self.label_text = QLabel()
        self.label_text.setText("wyprintowanie informacji statystycznych")

        # vbox - segreguje wszystkie elementy w pionie
        vbox = QVBoxLayout(self)
        vbox.addWidget(self.combobox_city)
        vbox.addWidget(self.button_etl)
        vbox.addWidget(self.button_extract)
        vbox.addWidget(self.button_transform)
        vbox.addWidget(self.button_load)
        vbox.addWidget(self.button_print)
        vbox.addWidget(self.button_print_files)
        vbox.addWidget(self.button_clear)
        vbox.addWidget(self.label_text)

        # buduj slownik ze statusami przyciskow
        self.dict_buttons_status = {
            self.button_load.text(): False,
            self.button_clear.text(): True,
            self.button_etl.text(): True,
            self.button_extract.text(): True,
            self.button_transform.text(): False,
            self.button_print.text(): True,
            self.button_print_files.text(): True,
        }

        # buduj liste przyciskow
        self.lst_buttons = [
            self.button_print,
            self.button_transform,
            self.button_extract,
            self.button_etl,
            self.button_clear,
            self.button_load,
            self.button_print_files,
        ]

        # wyswietlenie obiektu vbox w oknie
        self.show()

        self.refresh_buttons(False)

    def etl(self):
        self.extract()
        self.transform()
        self.load()

    def handle_f_output(self, function_output):
        exit_code = function_output[0]
        message = function_output[1]
        self.label_text.setText(message)
        if exit_code != 0:
            raise MyException

    # ustaw state przyciskow
    def refresh_buttons(self, flag_disable):
        if flag_disable:
            for button in self.lst_buttons:
                button.setEnabled(False)
            pass
        else:
            for button in self.lst_buttons:
                button.setEnabled(self.dict_buttons_status[button.text()])
        app.processEvents()

    def extract(self):
        try:
            self.label_text.setText("Extraction started.")
            clear_temp_directories()
            self.refresh_buttons(True)
            f_output = self.etl.extract(self.combobox_city.currentText())
            self.handle_f_output(f_output)
            self.dict_buttons_status['Transform'] = True
        except Exception as e:
            self.label_text.setText(str(e))
        self.refresh_buttons(False)

    def transform(self):
        try:
            self.label_text.setText("Transformation started.")
            self.refresh_buttons(True)
            f_output = self.etl.transform()
            self.handle_f_output(f_output)
            self.dict_buttons_status['Load'] = True
            self.dict_buttons_status['Transform'] = False
            clear_directory(config.path_scraped)
        except Exception as e:
            self.label_text.setText(str(e))
        self.refresh_buttons(False)

    def load(self):
        try:
            self.label_text.setText("Loading started")
            self.refresh_buttons(True)
            f_output = self.etl.load()
            self.handle_f_output(f_output)
            self.dict_buttons_status['Load'] = False
            clear_directory(config.path_transformed)
        except Exception as e:
            self.label_text.setText(str(e))
        self.refresh_buttons(False)

    def print(self):
        try:
            self.label_text.setText("Printing...")
            self.refresh_buttons(True)
            f_output = self.etl.print()
            self.handle_f_output(f_output)
        except Exception as e:
            self.label_text.setText(str(e))
        self.refresh_buttons(False)

    def print_files(self):
        try:
            self.label_text.setText("Printing files...")
            self.refresh_buttons(True)
            f_output = self.etl.print_files()
            self.handle_f_output(f_output)
        except Exception as e:
            self.label_text.setText(str(e))
        self.refresh_buttons(False)

    def clear(self):
        try:
            self.label_text.setText("Clearing started")
            self.refresh_buttons(True)
            f_output = self.etl.clear()
            self.handle_f_output(f_output)
            clear_temp_directories()
        except Exception as e:
            self.label_text.setText(str(e))
        self.refresh_buttons(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GuiWebScraper(app)
    sys.exit(app.exec_())
