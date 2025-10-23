import sys
import ipaddress
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QGridLayout
)
from PyQt5.QtGui import QFont

class LanCalc(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🌐 Network Calculator")
        self.setGeometry(300, 200, 450, 300)
        self.initUI()

    def initUI(self):
        layout = QGridLayout()
        font = QFont("Segoe UI", 10)

        # Input Fields
        self.ip_label = QLabel("IP Address / Subnet (e.g., 192.168.1.10/24):")
        self.ip_label.setFont(font)
        self.ip_input = QLineEdit()
        self.ip_input.setFont(font)

        self.calc_btn = QPushButton("Calculate")
        self.calc_btn.setFont(QFont("Segoe UI", 10, QFont.Bold))
        self.calc_btn.clicked.connect(self.calculate)

        # Result labels
        self.result_labels = {
            "Network": QLabel(),
            "Broadcast": QLabel(),
            "Netmask": QLabel(),
            "Host Range": QLabel(),
            "Usable Hosts": QLabel()
        }
        for lbl in self.result_labels.values():
            lbl.setFont(font)

        # Layout structure
        layout.addWidget(self.ip_label, 0, 0, 1, 2)
        layout.addWidget(self.ip_input, 1, 0, 1, 2)
        layout.addWidget(self.calc_btn, 2, 0, 1, 2)

        row = 3
        for key, lbl in self.result_labels.items():
            layout.addWidget(QLabel(f"{key}:"), row, 0)
            layout.addWidget(lbl, row, 1)
            row += 1

        self.setLayout(layout)

    def calculate(self):
        try:
            net = ipaddress.ip_network(self.ip_input.text(), strict=False)
            self.result_labels["Network"].setText(str(net.network_address))
            self.result_labels["Broadcast"].setText(str(net.broadcast_address))
            self.result_labels["Netmask"].setText(str(net.netmask))
            self.result_labels["Host Range"].setText(f"{net.network_address + 1} - {net.broadcast_address - 1}")
            self.result_labels["Usable Hosts"].setText(str(net.num_addresses - 2))
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Invalid input: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LanCalc()
    window.show()
    sys.exit(app.exec_())
