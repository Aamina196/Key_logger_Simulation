Keylogger Simulation 🔑

📌 Overview
This project is a simple keylogger simulation using Python and the pynput library. It captures user keystrokes and logs them into a text file while handling backspaces correctly. The project is intended for educational and security awareness purposes only.

🚀 Features

✔️ Captures and logs keystrokes in a clean format

✔️ Handles backspaces properly

✔️ Writes logs to a text file

✔️ Starts a new session with timestamps

✔️ Stops recording on pressing Esc

✔️ Provides a visualization of keystroke frequency

🛠️ Installation & Setup

Step 1: Clone the Repository

git clone https://github.com/Aamina196/Key_logger_Simulation.git

cd Key_logger_simulation


Step 2: Create a Virtual Environment (Optional but Recommended)

python -m venv .venv
Activate the environment:

Windows: .\.venv\Scripts\activate

Mac/Linux: source .venv/bin/activate

Step 3: Install Dependencies

pip install -r requirements.txt

📜 Usage

Run the Keylogger

python keylogger.py

Stopping the Keylogger :
Press Esc to stop logging.

📂 File Structure

Key_logger_simulation/        
│── src/                      
│   │── keylogger.py         
│   │── barchart.py.py      
│── logs/                     
│   └── keylog.txt                          
│── requirements.txt          
│── README.md                      

⚠️ Disclaimer

🔴 This project is for educational purposes only. Unauthorized keylogging is illegal and unethical. Do not use this script for malicious activities. The author is not responsible for any misuse.
