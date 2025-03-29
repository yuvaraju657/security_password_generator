# Secure Password Generator

This is a simple web application built with Streamlit that allows users to generate strong, cryptographically secure passwords based on their specified criteria.

## Features

* **Adjustable Password Length:** Users can select the desired length of the password using a slider (minimum 8, maximum 32 characters).
* **Character Set Options:** Users can choose to include:
    * Uppercase letters
    * Numbers (digits)
    * Special characters (punctuation)
* **Cryptographically Secure Generation:** The password generation utilizes the `secrets` module in Python, which is designed for generating cryptographically strong random numbers suitable for managing secrets like passwords.
* **Guaranteed Character Inclusion:** The generator ensures that if a character type (uppercase, digits, special characters) is selected, at least one character of that type will be present in the generated password.
* **Shuffled Output:** The generated password characters are shuffled to prevent any predictable patterns.
* **User-Friendly Interface:** Built with Streamlit, the application provides an easy-to-use web interface.
* **Minimum Length Enforcement:** Enforces a minimum password length of 8 characters for security reasons.

## How to Use

1.  **Clone the Repository (Optional):** If you have the code locally, skip this step. Otherwise, clone the repository from GitHub:
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2.  **Install Dependencies:** Make sure you have Streamlit installed. If not, you can install it using pip:
    ```bash
    pip install streamlit
    ```

3.  **Run the Application:** Navigate to the directory containing the Python script (`your_script_name.py`, likely the name you saved the provided code as) and run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

4.  **Interact with the Generator:** A new tab will open in your web browser displaying the Secure Password Generator.
    * Use the slider to select the desired password length.
    * Check the boxes to include uppercase letters, numbers, and special characters as needed.
    * Click the "Generate Password" button.
    * The generated secure password will be displayed on the screen.

## Security Considerations

* This tool uses the `secrets` module, which provides a cryptographically strong source of randomness. This is crucial for generating secure passwords.
* It is recommended to always use strong, unique passwords for your online accounts.
* Consider using a password manager to securely store and manage your generated passwords.
* The minimum password length is set to 8 characters as a basic security measure. It is generally recommended to use passwords longer than 12 characters for better security.

## Contributing

Contributions to this project are welcome. Feel free to submit bug reports, feature requests, or pull requests.

## License

MIT LICENSED PROJECT
