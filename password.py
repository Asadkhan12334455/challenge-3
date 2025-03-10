import streamlit as st
import re
import random
import string

def check_password_strength(password):
    score = 0
    suggestions = []
    
    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("❌ Password should be at least 8 characters long.")
    
    # Uppercase Check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("❌ Include at least one uppercase letter (A-Z).")
    
    # Lowercase Check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("❌ Include at least one lowercase letter (a-z).")
    
    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("❌ Add at least one number (0-9).")
    
    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        suggestions.append("❌ Include at least one special character (!@#$%^&*).")
    
    return score, suggestions

def generate_random_password(length=12):
    """Generate a random password of a given length"""
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    st.title("Password Strength Meter")
    st.write("Enter your password below to check its strength and get suggestions for improvement.")
    
    # Input for password
    password = st.text_input("Enter Password", type="password")
    
    # Button to check password strength
    if st.button("Check Strength"):
        if not password:
            st.error("Please enter a password.")
        else:
            score, suggestions = check_password_strength(password)
            
            # Display strength based on the score
            if score == 5:
                st.success("✅ Strong Password! All security criteria are met.")
            elif 3 <= score <= 4:
                st.warning("⚠️ Moderate Password: Consider adding more security features.")
            else:
                st.error("❌ Weak Password: Please follow the suggestions below to improve.")
            
            # Show suggestions if any
            if suggestions:
                st.markdown("### Suggestions:")
                for suggestion in suggestions:
                    st.write("- " + suggestion)

    # Button to generate a random password
    if st.button("Generate Random Password"):
        random_password = generate_random_password()
        st.text_input("Generated Password", value=random_password, disabled=True)
        st.success("Password Generated! You can use this for your account.")

if __name__ == "__main__":
    main()
