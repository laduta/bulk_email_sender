# 📧 Auto Email Sender – Bulk Email Sender with Python

A simple Python script to send personalized bulk emails using Gmail SMTP. Reads recipient names and emails from a CSV file, fills in a message template, and sends emails automatically.

---

## 🚀 Features

- ✅ Reads names and emails from a `.csv` file
- ✅ Uses an email message template with `{name}` placeholder
- ✅ Sends personalized emails to multiple recipients
- ✅ Secure login using Gmail App Password
- ✅ Simple and fast — send 100+ emails in minutes

---

## 🗂️ Project Structure

bulk_email_sender/

├── auto_emailer.py          
├── recipients.csv           
├── email_template.txt       
└── README.md                

---

## 📦 Requirements

- Python 3.6+
- Gmail account with [App Passwords enabled](https://support.google.com/accounts/answer/185833)

### 📚 Python Libraries Used

```bash
pip install pandas

---

## 🧪 How to Use
1. Clone This Repo
  git clone https://github.com/yourusername/auto-emailer.git
  cd auto-emailer

2. Update your credentials in auto_emailer.py
  EMAIL_ADDRESS = "your_email@gmail.com"
  EMAIL_PASSWORD = "your_app_password"  #Do not use your normal Gmail password, Use Gmail App Password

3. Run the script
  python auto_emailer.py

📌 Notes
- Gmail security: Use App Passwords instead of your real password if you use two-factor authentication (2FA).
- Daily Limits: Gmail has sending limits (about 500/day for free accounts).

✨ Future Improvements
- Add HTML email support
- Add GUI with tkinter
- Add attachment support (PDF, images)
- Save logs of sent emails
- Add CLI options (e.g., --file or --subject)

🤝 Contributing
Contributions are welcome! Feel free to submit pull requests for improvements.

📄 License
This project is licensed under the MIT License. See the LICENSE file for details.

🙋‍♂️ Author
Abubakar Jibrin – Python Developer
Feel free to connect on LinkedIn or follow for more projects.


---

### ✅ What to do next:
- Replace `yourusername` in the `git clone` URL with your GitHub username.
- Update your real **LinkedIn URL** and Gmail info if you're uploading publicly.
- You can copy this into your GitHub repo as the `README.md`.


