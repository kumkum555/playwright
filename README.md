# 🚀 Playwright Python Automation Framework

A Python-based UI Automation Testing Framework built using **Playwright**, **Pytest**, and **Python**.

This framework supports:
- UI Automation Testing
- HTML Reports
- Screenshots on Failure
- Video Recording
- Cross Browser Testing
- Easy Setup

---

# 📋 Prerequisites

Before running the project, make sure the following software is installed:

- Python 3.10 or above
- Visual Studio Code
- Git
- Playwright

Check Python version:

```bash
python --version
```

---

# 📥 Clone Repository

```bash
git clone https://github.com/kumkum555/playwright.git
```

Move into the project directory:

```bash
cd playwright
```

---

# 📁 Project Structure

```
playwright/
│
├── test/
│   └── test_login.py
│
├── utils/
│
├── reports/
│
├── screenshots/
│
├── videos/
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```

---

# 🐍 Create Virtual Environment

Windows

```bash
python -m venv venvpython
```

---

# ▶️ Activate Virtual Environment

Windows

```bash
venvpython\Scripts\activate
```

After activation you should see:

```
(venvpython)
```

---

# 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🎭 Install Playwright Browsers

Run this command only once after installing dependencies.

```bash
playwright install
```

---

# ▶️ Run All Test Cases

```bash
pytest
```

---

# ▶️ Run Specific Test File

```bash
pytest test/test_login.py
```

---

# 📊 Generate HTML Report

```bash
pytest --html=reports/report.html --self-contained-html
```

Open the generated report:

```
reports/report.html
```

---

# 📸 Screenshots

Failure screenshots are automatically saved in:

```
screenshots/
```

---

# 🎥 Video Recording

Execution videos are automatically saved in:

```
videos/
```

---

# 📄 requirements.txt

If you install any new package, update the requirements file.

```bash
pip freeze > requirements.txt
```

---

# 🔄 Pull Latest Changes

```bash
git pull origin main
```

---

# ⬆️ Push Your Changes

```bash
git add .

git commit -m "Your Commit Message"

git push origin main
```

---

# 🧹 Deactivate Virtual Environment

```bash
deactivate
```

---

# 📝 Common Commands

| Task | Command |
|------|---------|
| Create Virtual Environment | `python -m venv venvpython` |
| Activate Virtual Environment | `venvpython\Scripts\activate` |
| Install Dependencies | `pip install -r requirements.txt` |
| Install Playwright Browsers | `playwright install` |
| Run Tests | `pytest` |
| Generate HTML Report | `pytest --html=reports/report.html --self-contained-html` |
| Update Requirements | `pip freeze > requirements.txt` |
| Deactivate Environment | `deactivate` |

---

# 📌 Notes

- Activate the virtual environment before running the project.
- Install dependencies using `requirements.txt`.
- Run `playwright install` only once after setup.
- HTML reports are generated inside the `reports` folder.
- Failure screenshots are stored inside the `screenshots` folder.
- Test execution videos are stored inside the `videos` folder.

---

# 👩‍💻 Author

**Kumkum Kapkoti**

Playwright Python Automation Framework
