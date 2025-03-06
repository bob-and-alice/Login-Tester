# LoginTester

**LoginTester** is a Python-based tool that automates the process of testing login credentials across various websites. It allows you to verify whether given username-password pairs work with specific URLs, and logs the results in CSV or TXT format. The program can be customized to check for valid and invalid login attempts and even store the results in a Firebase database for future reference.

## Features

- **Automated Login Testing**: Verifies username-password pairs for a list of URLs.
- **Flexible Output**: Saves valid and invalid login attempts in CSV or TXT formats.
- **Error Handling**: Catches connection errors and failed login attempts.
- **Firebase Integration**: Sends login attempt results to Firebase in real-time for further analysis.
- **User-Friendly Interface**: Console-based with colorful outputs for easy understanding of the results.

## Requirements

Before running the program, make sure you have the following dependencies installed:

- **Python 3.x**
- **ChromeDriver** (for Selenium WebDriver)
- Required Python packages:
  - `selenium`
  - `chardet`
  - `requests`
  - `colorama`
  - `csv`
  - `json`

You can install these dependencies using `pip` by running the following command:

```bash
pip install -r requirements.txt
