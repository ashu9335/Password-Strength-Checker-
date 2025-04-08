# 🔐 Password Strength Checker

A simple Python program that checks the strength of a password based on common security standards.

## 🚀 Features

- Minimum password length check
- Checks for at least:
  - One lowercase letter
  - One uppercase letter
  - One number
  - One special character (`@ $ ! % * ? &`)
- Provides real-time feedback to the user

## 📂 Project Structure

password-strength-checker/ ├── password_checker.py └── README.md

## 🧠 How It Works

The program uses **regular expressions** to verify if the password meets each of the following conditions:

1. At least 8 characters in length
2. Contains at least one **lowercase** letter
3. Contains at least one **uppercase** letter
4. Contains at least one **digit**
5. Contains at least one **special character**

It gives feedback on what's missing if the password is weak, or confirms it's strong if all checks pass.

## 🛠️ Requirements

- Python 3.x

No external libraries are needed beyond the built-in `re` module (for regex).

## 🧪 Usage

1. Clone the repository:

```bash
git clone https://github.com/your-username/password-strength-checker.git
cd password-strength-checker
python password_checker.py
```
## Example
```
Enter your password: P@ssw0rd
Password is strong!
```
```
Enter your password: password
Password should contain at least one uppercase letter.
```

Created with ❤️ by Ashutosh Singh Yadav
---

Would you like me to generate a `.zip` file with the code and this README for easy upload to GitHub?

