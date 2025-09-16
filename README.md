# python-password-cracker
A simple Python script to perform a dictionary-based brute-force attack on a local web server.
# Brute-Force Password Cracker (Ethical Hacking Project)

## Project Description
This project is a hands-on exercise in ethical hacking, demonstrating how a simple brute-force dictionary attack works. The project consists of two Python scripts:
- `app.py`: A basic Flask web server with a vulnerable login page.
- `cracker.py`: A client script that automates password guessing against the server.

**Note:** This project is for educational purposes only and should only be run in a controlled, local environment.

## Key Concepts Demonstrated
- **Ethical Hacking:** Understanding and simulating a common attack vector.
- **Web Requests:** Using Python's `requests` library to send POST requests.
- **File I/O:** Reading a wordlist from a file.
- **Security Principles:** Highlighting the importance of strong passwords and account lockout policies.

## How to Run the Project
1.  **Clone the repository:** `git clone [Your Repository URL]`
2.  **Install dependencies:** `pip install requests Flask`
3.  **Start the server:** In the first terminal, run `python app.py`.
4.  **Run the cracker:** In a second terminal, run `python cracker.py`.

## Files
- `cracker.py`: The password cracking script.
- `app.py`: The vulnerable web application.
- `passwords.txt`: The wordlist used for the attack.
