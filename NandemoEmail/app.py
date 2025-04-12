import sys, argparse, json, os
from PySide6.QtWidgets import QApplication
from src.Forms.MainWindow import MainWindow

def setting(data_address):
    app = QApplication(sys.argv)
    window = MainWindow(data_address)
    window.show()

    app.exec_()

def create(Address):
    data = {
        "EmailType": "",
        "AccRec":[],
        "AttSet":"",
        "AttAddress":"",
        "Compressed":False,
        "MailContent":"" # Text File Address
    }

    if getattr(sys, 'frozen', False):
        account_json_path = os.path.join(sys._MEIPASS, f"{Address}/data.json")
        with open(account_json_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent="\t")
    else:
        account_json_path = f"{Address}/data.json"
        with open(account_json_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent="\t")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', "--setting", dest="s_data_address", type=str)
    parser.add_argument('-c', '--create', dest="c_data_address", type=str)
    parser.add_argument('-r', '--run', dest="r_data_address", type=str)
    args = parser.parse_args()

    if args.s_data_address:
        data_address = args.s_data_address
        setting(data_address)
        
    if args.c_data_address:
        address = args.c_data_address
        create(address)
