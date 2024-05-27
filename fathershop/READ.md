Certainly! Here's the information formatted to be added to a `README.md` file:

---

# Setting Up Selenium WebDriver Test Scripts with pytest

This guide outlines the steps required to set up and run Selenium WebDriver test scripts using the pytest framework on a local machine. 

## 1. Environment Setup:

### 1.1. **Python Installation**
Ensure Python is installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

```bash
pip --version
```

### 1.2. **PyCharm Installation**
Install PyCharm IDE or any other preferred IDE. PyCharm can be downloaded from the [JetBrains website](https://www.jetbrains.com/pycharm/download/).

## 2. Project Setup:

### 2.1. **Clone Repository**
Clone the project repository or download the project files and extract them to a local directory.

### 2.2. **Virtual Environment**
Navigate to the project directory in the terminal and set up a virtual environment. This isolates the project dependencies.

```bash
python3 -m venv venv
```

Activate the virtual environment:

- **Windows**:
    ```bash
    venv\Scripts\activate
    ```
- **macOS/Linux**:
    ```bash
    source venv/bin/activate
    ```

### 2.3. **Install Dependencies**
Install all the required packages from the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

## 3. WebDrivers:

### 3.1. **Chrome WebDriver**
Download the Chrome WebDriver that matches the Chrome browser version installed on your machine. Ensure the WebDriver executable is in the system PATH or specify its path in the test script.

### 3.2. **Firefox WebDriver**
If using Firefox, download the geckodriver and set its path similarly.

### 3.3. **Automated WebDriver Installation**
Install the `chromedriver-autoinstaller` to automatically manage Chrome WebDriver versions.

```bash
pip install chromedriver-autoinstaller
```

## 4. Install Required Packages:

```bash
pip install pytest selenium openpyxl
```

## 5. Additional pytest Plugins:

Install the following pytest plugins to enhance testing capabilities:

```bash
pip install pytest-xdist pytest-forked
```

---

By following this guide, you should have all the necessary tools and configurations to run Selenium WebDriver test scripts using the pytest framework on your local machine.

## 3. Execute scripts:

1. Set Python project directory
```bash
set PYTHONPATH=%PYTHONPATH%;pathtodirectory
```
2. Execute scripts using command
```bash
pytest footer_screen\footer_run.py
```
3. Results would be generated in Excel output