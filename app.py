import secrets
import string
import streamlit as st

def generate_secure_password(length=16, use_uppercase=True, use_digits=True, use_special_chars=True):
    """
    Generates a cryptographically secure password based on user preferences.
    :param length: Length of the password (default: 16)
    :param use_uppercase: Include uppercase letters (default: True)
    :param use_digits: Include digits (default: True)
    :param use_special_chars: Include special characters (default: True)
    :return: Securely generated password
    """
    if length < 8:
        raise ValueError("Password length must be at least 8 characters for security reasons.")
    
    character_pool = string.ascii_lowercase  # Always include lowercase letters
    
    if use_uppercase:
        character_pool += string.ascii_uppercase
    if use_digits:
        character_pool += string.digits
    if use_special_chars:
        character_pool += string.punctuation
    
    # Ensure password includes at least one of each selected character type
    password = [
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.ascii_uppercase) if use_uppercase else '',
        secrets.choice(string.digits) if use_digits else '',
        secrets.choice(string.punctuation) if use_special_chars else ''
    ]
    
    # Fill the remaining length with random selections from the pool
    password += [secrets.choice(character_pool) for _ in range(length - len(password))]
    
    # Shuffle to avoid predictable patterns
    secrets.SystemRandom().shuffle(password)
    
    return ''.join(password)

# Streamlit UI
st.title("Secure Password Generator")

length = st.slider("Select password length", min_value=8, max_value=32, value=16)
use_uppercase = st.checkbox("Include Uppercase Letters", value=True)
use_digits = st.checkbox("Include Numbers", value=True)
use_special_chars = st.checkbox("Include Special Characters", value=True)

if st.button("Generate Password"):
    try:
        password = generate_secure_password(length, use_uppercase, use_digits, use_special_chars)
        st.success(f"Generated Password: {password}")
    except ValueError as e:
        st.error(str(e))
