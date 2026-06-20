# 🚀 WhatsApp Bulk Message Bot using Python

> A powerful and simple **WhatsApp Automation Bot** built with **Python** and **PyWhatKit** to send images and captions to multiple contacts from a CSV file through **WhatsApp Web**.

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![WhatsApp](https://img.shields.io/badge/WhatsApp-Web-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

---

## 📌 Overview

This project is a **Python WhatsApp Bulk Messaging Bot** that automatically sends an image with a custom message to multiple phone numbers stored in a CSV file.

It is useful for:

- 📢 Marketing campaigns
- 🎓 Student notifications
- 🏫 Course announcements
- 📅 Event invitations
- 📣 Broadcast messages
- 🤖 WhatsApp automation tasks

The bot uses **WhatsApp Web** and **PyWhatKit** without requiring the WhatsApp Business API.

---

## ✨ Features

- ✅ Bulk WhatsApp messaging
- ✅ Send image with caption
- ✅ CSV-based contact management
- ✅ Automatic phone number cleaning
- ✅ Duplicate removal
- ✅ Random delay to avoid spam detection
- ✅ Retry mechanism for failed messages
- ✅ Logging system
- ✅ Modular project structure
- ✅ Easy configuration
- ✅ Supports Pakistani phone numbers (+92)
- ✅ WhatsApp Web integration

---

## 📂 Project Structure

```text
whatsApp-bot/
│
├── data/
│   ├── students.csv
│   └── logo.png
│
├── logs/
│   └── send_log.csv
│
├── src/
│   ├── config.py
│   ├── sender.py
│   ├── logger.py
│   ├── number_cleaner.py
│   └── __init__.py
│
├── main.py
├── requirements.txt
├── README.md
└── setup.md
```

---

## ⚙️ How It Works

```text
CSV Contacts
      ↓
Clean Phone Numbers
      ↓
Remove Duplicates
      ↓
User Confirmation
      ↓
Open WhatsApp Web
      ↓
Send Image + Caption
      ↓
Retry Failed Messages
      ↓
Save Logs
```

---

## 📦 Installation

### Clone Repository

```bash
git clone https://github.com/Waqas-Khan-CodeCanvas/whatsApp-bot.git

cd whatsApp-bot
```

---

### Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 📁 Prepare Contact List

Create:

```text
data/students.csv
```

Example:

| Number |
|----------|
| 03001234567 |
| 03111234567 |
| 03451234567 |

---

## 🖼 Add Image

Place your image inside:

```text
data/logo.png
```

---

## ⚙️ Configure Settings

Edit:

```python
src/config.py
```

Example:

```python
DEFAULT_COUNTRY_CODE = "92"

MIN_DELAY_SECONDS = 30
MAX_DELAY_SECONDS = 45

MAX_RETRIES = 2

PHONE_COLUMN_NAME = "Number"
```

---

## 🚀 Run the Bot

```bash
python main.py
```

The bot will:

1. Load contacts from CSV
2. Validate phone numbers
3. Remove duplicates
4. Ask for confirmation
5. Open WhatsApp Web
6. Send image + caption
7. Save logs

---

## 📊 Logs

All sending results are stored in:

```text
logs/send_log.csv
```

Example:

| Number | Status |
|----------|--------|
| +923001234567 | SUCCESS |
| +923111234567 | FAILED |

---

## 🛠 Tech Stack

- Python
- PyWhatKit
- Pandas
- WhatsApp Web
- CSV
- Automation

---

## Use Cases

### 📢 Marketing Campaigns

Send promotional messages to customers.

### 🎓 Educational Institutes

Notify students about admissions, classes, and events.

### 🏢 Organizations

Broadcast announcements to employees.

### 📅 Event Management

Send invitations and reminders.

---

## Advantages

- No WhatsApp Business API required
- Simple setup
- Modular architecture
- Easy customization
- Logging support
- Retry mechanism
- Contact cleaning and validation

---

## Limitations

- Requires WhatsApp Web login
- Browser must remain open
- Not suitable for massive campaigns
- Dependent on internet connection

---

## Future Improvements

- [ ] GUI Dashboard
- [ ] Excel Support
- [ ] Schedule Messages
- [ ] Resume Interrupted Campaigns
- [ ] Multiple Campaign Support
- [ ] Personalized Messages
- [ ] AI Message Generator
- [ ] WhatsApp Business API Integration

---

## 🤝 Contributing

Contributions are welcome.

Feel free to fork the repository and submit pull requests.

---

## ⭐ Support

If you found this project useful, please consider giving it a star ⭐.

---

## 🔑 Keywords

WhatsApp Bot Python, WhatsApp Automation, Bulk WhatsApp Sender, WhatsApp Message Bot, PyWhatKit WhatsApp Bot, WhatsApp Marketing Tool, WhatsApp Bulk Messaging Python, WhatsApp Web Automation, CSV WhatsApp Sender, Python WhatsApp Project, WhatsApp Notification Bot, Image Sender WhatsApp Bot, Python Automation Project.

---

## 📜 License

This project is licensed under the MIT License.
