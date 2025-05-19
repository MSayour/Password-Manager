# 🔐 Password Manager with Encryption

A simple yet secure password manager built using **Python** and **Tkinter**, with password encryption powered by the `cryptography` library. This desktop app allows you to generate, save, retrieve, and encrypt passwords locally in a JSON file.

---

## 🚀 Features

- 🧠 **Generate Strong Passwords** (random letters, numbers, symbols)
- 🔒 **Encrypt Passwords** using Fernet symmetric encryption
- 🔍 **Search Stored Entries** by website name
- 📋 **Copy Passwords** to clipboard instantly
- 📝 **Auto-fill Gmail** domain in the email field
- 💾 **Save and Load Data** from a local JSON file

---

## 📦 Requirements

- Python 3.x
- Libraries:
  - `tkinter` *(comes pre-installed with Python)*
  - `pyperclip`
  - `cryptography`

---

## 🛠 Installation

1. Clone the repository or download the project folder.

```bash
git clone https://github.com/MSayour/password-manager-encrypted.git
cd password-manager-encrypted
```

2. Install the dependencies:

```bash
pip install cryptography pyperclip
```

3. Run the app:

```bash
python main.py
```

---

## 🧪 How It Works

- The first time you run the app, it generates a unique `key.key` file used for encrypting/decrypting passwords.
- Passwords are encrypted using the Fernet algorithm and saved in `data file.json`.
- When retrieving passwords, the app securely decrypts and shows them.
- All operations (save/search) are done locally. No internet connection is required.

---

## 🖼 UI Preview

> ![App Screenshot](/app_prev.png)  

---

## 📁 File Structure

```
password-manager-encrypted/
│
├── main.py             # Main application file
├── key.key             # Encryption key (auto-generated)
├── data file.json      # Encrypted password data
├── logo.png            # Lock image for UI
└── README.md           # Project documentation
```

---

## 🧯 Security Note

> Keep your `key.key` file safe!  
> If you lose it, you will not be able to decrypt previously saved passwords.

---

## 🤝 Contributing

Pull requests are welcome! Feel free to open issues or suggest new features.

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 🙋‍♂️ Author

Developed by Mohamad Sayour (aka `SHOGUN`)  
Feel free to fork, improve, and share!
