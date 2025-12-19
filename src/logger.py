'''
Purpose:
---------
This module is responsible for configuring application-wide logging.

What this code does:
--------------------
1. Generates a unique log file name using the current date and time.
2. Creates a 'logs' directory (if it does not already exist).
3. Stores log files inside the 'logs' folder with timestamped names.
4. Configures the Python logging module to:
   - Write logs to a file instead of the console
   - Include timestamp, line number, logger name, log level, and message
   - Capture logs with INFO level and above

Why this is useful:
-------------------
- Helps in debugging and monitoring application behavior.
- Prevents log overwriting by creating a new log file for each run.
- Centralizes logging configuration for consistent logging across the project.
'''

import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format= "[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,


)

