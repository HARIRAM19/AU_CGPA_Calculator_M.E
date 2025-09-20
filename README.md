# Anna University M.E CGPA Calculator - Regulation 2023

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A **PyQt5 GUI Application** to calculate **SGPA and CGPA** for M.E students of **Anna University**, Regulation 2023.

---

## Features

* Calculate **Semester GPA (SGPA)** and **Overall CGPA**.
* Works for **1 to 4 semesters**.
* Supports all subjects for Regulation 2023 with credits preloaded.
* Maintains grades when switching between semesters.
* User-friendly GUI built with **PyQt5**.

---


## Installation

### Windows (Using Installer)

1. Go to [Releases](https://github.com/HARIRAM19/AU_CGPA_Calculator_M.E/releases/tag/v1.0) on GitHub.
2. Download the Install for Windows (`.msi`).
3. Run the installer and follow the instructions.

### From Source (Requires Python 3.8+)

```bash
git clone https://github.com/HARIRAM19/AU_CGPA_Calculator_M.E
cd cgpa-calculator
python -m cgpa_calculator.__main__
```

> Make sure `PyQt5` is installed. You can also use `pip install PyQt5` if not included.

---

## Usage

1. Launch the app.
2. Select the **number of semesters**.
3. Enter grades for each subject.
4. Click **Calculate SGPA/CGPA**.
5. View the results in the output box.

> Grades are preserved when switching between semesters.

---

## Project Structure

```
cgpa_calculator_briefcase/
├── pyproject.toml       # Briefcase configuration
├── LICENSE              # MIT license
├── README.md
└── src/
    └── cgpa_calculator/
        ├── __init__.py
        ├── __main__.py
        └── cgpa_app.py
```

---

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a Pull Request.

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## Contact

* Author: HARIRAM S
* GitHub: [https://github.com/HARIRAM19](https://github.com/HARIRAM19)

* Email: [itsme6341@gmail.com](itsme6341@gmail.com)

