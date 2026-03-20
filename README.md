# Basic Keylogger ⌨️

A professional yet simple keylogger written in Python that monitors and records keystrokes. It captures real-time keyboard inputs and saves them into both **Raw Text (.log)** and **JSON** formats for easier data analysis.



<img width="449" height="136" alt="image" src="https://github.com/user-attachments/assets/ab4e1afb-b299-462a-8df5-67adb9636bc8" />
---

<img width="466" height="381" alt="image" src="https://github.com/user-attachments/assets/07bde9eb-7bfc-4617-a5e1-2a642e811833" />



## ✨ Features
* **Real-time Logging:** Captures every keystroke instantly.
* **Format Support:** Stores data in a human-readable `.log` file and a structured `.json` file.
* **Special Key Detection:** Recognizes keys like `Space`, `Enter`, `Ctrl`, and `Esc`.
* **Clean Termination:** Safely stops logging when the `ESC` key is pressed or `Ctrl+C` is triggered.

---

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Rafiuzzaman-sourov/Basic_Keylogger.git](https://github.com/Rafiuzzaman-sourov/Basic_Keylogger.git)
   cd Basic_Keylogger






Create a Virtual Environment (Optional but recommended):
Bash

python3 -m venv venv
source venv/bin/activate

Install Dependencies:
(Make sure you have pynput installed)
Bash

    pip install pynput

🚀 Usage

To start the keylogger, simply run the Python script:
Bash

python3 keylogger.py

    The script will start capturing keystrokes.

    Press ESC to stop logging.

    Check keystrokes.log to see the captured data.

📊 Output Example

The log file will look something like this:
Plaintext

2026-03-20 22:15:15 - Key pressed: h
2026-03-20 22:15:15 - Key pressed: i
2026-03-20 22:15:15 - Special key pressed: space

⚠️ Disclaimer

Educational Purposes Only. This tool is created for educational and ethical cybersecurity research purposes only. Using this software to monitor devices without explicit permission is illegal and unethical. The developer is not responsible for any misuse of this tool.
👨‍💻 Author

Md. Rafiuzzaman Sowrov (i_am_iron_man)








