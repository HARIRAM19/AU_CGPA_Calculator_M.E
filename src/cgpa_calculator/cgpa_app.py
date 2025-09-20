
from PyQt5 import QtWidgets, QtCore

grade_points = {
    "O/S": 10,
    "A+": 9,
    "A": 8,
    "B+": 7,
    "B": 6,
    "C": 5,
    "RA/U": 0
}

subjects_reg2023 = {
    1: [
        ("MA3154", "Advanced Mathematics for Scientific Computing", 4),
        ("RM3151", "Research Methodology and IPR", 3),
        ("CP3153", "Multicore Architectures", 3),
        ("CP3154", "Networking Technologies", 4.5),
        ("CP3152", "Database Technologies", 3),
        ("CP3151", "Data Structures and Algorithms", 3),
        ("CP3161", "Data Structures and Algorithms Laboratory", 2)
    ],
    2: [
        ("CP3251", "Advanced Operating Systems", 3),
        ("CP3201", "Compiler Optimization Techniques", 4),
        ("CP3252", "Machine Learning", 4.5),
        ("CP3261", "Professional Practices", 2),
        ("PE1", "Professional Elective I", 3),
        ("PE2", "Professional Elective II", 3)
    ],
    3: [
        ("CP3351", "Cyber Security", 3),
        ("CP3311", "Project Work I", 6),
        ("PE3", "Professional Elective III", 3),
        ("PE4", "Professional Elective IV", 3),
        ("PE5", "Professional Elective V", 4)
    ],
    4: [
        ("CP3411", "Project Work II", 12)
    ]
}

class CGPACalculator(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Anna University M.E CGPA Calculator - Regulation 2023")
        self.setGeometry(100, 100, 1000, 750)

        self.grade_inputs = {}
        self.displayed_semesters = set()
        self.initUI()

    def initUI(self):
        layout = QtWidgets.QVBoxLayout(self)

        title = QtWidgets.QLabel("CGPA Calculator - Anna University (M.E, R2023)")
        title.setStyleSheet("font-size:22px; font-weight:bold; color:#2E86C1; margin:10px;")
        layout.addWidget(title, alignment=QtCore.Qt.AlignCenter)

        sem_select_layout = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel("Select number of semesters:")
        label.setStyleSheet("font-size:14px; font-weight:600;")
        sem_select_layout.addWidget(label)

        self.sem_combo = QtWidgets.QComboBox()
        self.sem_combo.addItems(["1", "2", "3", "4"])
        self.sem_combo.setStyleSheet("padding:5px; font-size:14px;")
        sem_select_layout.addWidget(self.sem_combo)

        show_btn = QtWidgets.QPushButton("Show Semesters")
        show_btn.setStyleSheet("QPushButton {background:#28B463; color:white; font-size:14px; padding:6px 12px; border-radius:6px;} QPushButton:hover {background:#239B56;}")
        show_btn.clicked.connect(self.show_semesters)
        sem_select_layout.addWidget(show_btn)

        reset_btn = QtWidgets.QPushButton("Reset")
        reset_btn.setStyleSheet("QPushButton {background:#E74C3C; color:white; font-size:14px; padding:6px 12px; border-radius:6px;} QPushButton:hover {background:#C0392B;}")
        reset_btn.clicked.connect(self.reset)
        sem_select_layout.addWidget(reset_btn)

        layout.addLayout(sem_select_layout)

        self.scroll_area = QtWidgets.QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.input_container = QtWidgets.QWidget()
        self.input_layout = QtWidgets.QVBoxLayout(self.input_container)
        self.scroll_area.setWidget(self.input_container)
        layout.addWidget(self.scroll_area)

        calc_btn = QtWidgets.QPushButton("Calculate SGPA/CGPA")
        calc_btn.setStyleSheet("QPushButton {background:#5DADE2; color:white; font-size:16px; padding:8px 16px; border-radius:6px;} QPushButton:hover {background:#3498DB;}")
        calc_btn.clicked.connect(self.calculate)
        layout.addWidget(calc_btn, alignment=QtCore.Qt.AlignCenter)

        self.output_box = QtWidgets.QTextEdit()
        self.output_box.setReadOnly(True)
        self.output_box.setStyleSheet("font-size:14px; background:#F4F6F7; border:1px solid #D5DBDB; padding:10px;")
        layout.addWidget(self.output_box)

    def show_semesters(self):
        num_semesters = int(self.sem_combo.currentText())

        for sem in range(1, num_semesters + 1):
            if sem in self.displayed_semesters:
                continue

            group = QtWidgets.QGroupBox(f"Semester {sem}")
            group.setStyleSheet("QGroupBox {font-size:16px; font-weight:bold; margin-top:10px;} QGroupBox::title {subcontrol-origin: margin; subcontrol-position: top left; padding:5px;}")
            vbox = QtWidgets.QVBoxLayout(group)

            grid = QtWidgets.QGridLayout()
            headers = ["Course Code", "Course Name", "Credits", "Grade"]
            for j, header in enumerate(headers):
                lbl = QtWidgets.QLabel(header)
                lbl.setStyleSheet("font-weight:bold; background:#D5DBDB; padding:4px; border:1px solid #AAB7B8;")
                grid.addWidget(lbl, 0, j)

            self.grade_inputs.setdefault(sem, [])

            for i, (code, name, credit) in enumerate(subjects_reg2023[sem]):
                lbl_code = QtWidgets.QLabel(code)
                lbl_name = QtWidgets.QLabel(name)
                lbl_credit = QtWidgets.QLabel(str(credit))
                for lbl in (lbl_code, lbl_name, lbl_credit):
                    lbl.setStyleSheet("padding:4px; border:1px solid #CCD1D1;")

                grade_combo = QtWidgets.QComboBox()
                grade_combo.addItems(list(grade_points.keys()))

                if len(self.grade_inputs[sem]) > i:
                    previous_combo = self.grade_inputs[sem][i][1]
                    grade_combo.setCurrentText(previous_combo.currentText())
                    self.grade_inputs[sem][i] = (credit, grade_combo)
                else:
                    self.grade_inputs[sem].append((credit, grade_combo))

                grid.addWidget(lbl_code, i+1, 0)
                grid.addWidget(lbl_name, i+1, 1)
                grid.addWidget(lbl_credit, i+1, 2)
                grid.addWidget(grade_combo, i+1, 3)

            vbox.addLayout(grid)
            self.input_layout.addWidget(group)
            self.displayed_semesters.add(sem)

    def reset(self):
        for i in reversed(range(self.input_layout.count())):
            widget = self.input_layout.itemAt(i).widget()
            if widget:
                widget.deleteLater()
        self.grade_inputs.clear()
        self.displayed_semesters.clear()
        self.output_box.clear()

    def calculate(self):
        self.output_box.clear()

        total_credits = 0
        total_points = 0

        for sem, subjects in self.grade_inputs.items():
            sem_credits = 0
            sem_points = 0

            for credit, grade_combo in subjects:
                grade = grade_combo.currentText()
                if grade not in grade_points:
                    QtWidgets.QMessageBox.warning(self, "Error", f"Invalid grade in Semester {sem}.")
                    return
                sem_credits += credit
                sem_points += grade_points[grade] * credit

            if sem_credits > 0:
                sgpa = sem_points / sem_credits
                self.output_box.append(f"Semester {sem} SGPA: {sgpa:.2f}")

                total_credits += sem_credits
                total_points += sem_points

        if total_credits > 0:
            cgpa = total_points / total_credits
            self.output_box.append("\nOverall CGPA: {:.2f}".format(cgpa))
        else:
            self.output_box.append("No grades entered.")