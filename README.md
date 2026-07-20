# Playwright Python Automation Framework

A Python-based UI Automation Testing Framework built with **Playwright** and **Pytest**. This framework is designed to automate web application testing with HTML reports, screenshots, and video recording.

## 🚀 Features

- Playwright with Python
- Pytest Test Runner
- HTML Test Reports
- Screenshot Capture
- Video Recording
- Page Object Model (POM) Ready
- Easy Test Execution

## 📁 Project Structure

```
playwright/
│
├── pages/
├── test/
├── reports/
├── screenshots/
├── videos/
├── utils/
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

## 🛠️ Installation

Clone the repository:

```bash
git clone https://github.com/kumkum555/playwright.git
```

Move into the project directory:

```bash
cd playwright
```

Create a virtual environment:

```bash
python -m venv venvpython
```

Activate the virtual environment:

### Windows

```bash
venvpython\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Install Playwright browsers

```bash
playwright install
```

## ▶️ Run Tests

Run all tests:

```bash
pytest
```

Run a specific test:

```bash
pytest test/test_login.py
```

## 📊 Generate HTML Report

```bash
pytest --html=reports/report.html --self-contained-html
```

Open the report:

```
reports/report.html
```

## 📸 Test Artifacts

- HTML Reports
- Screenshots
- Videos (if enabled)

## 🧰 Tech Stack

- Python
- Playwright
- Pytest
- pytest-html

## 👩‍💻 Author

**Kumkum Kapkoti**

GitHub: https://github.com/kumkum555

---

Happy Testing! 🚀
