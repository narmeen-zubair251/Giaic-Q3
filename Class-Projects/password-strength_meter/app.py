import streamlit as st
import re

st.set_page_config(page_title="Password Strength Meter🔐")

st.title("Password Strength Meter🔓")
st.markdown("""
## welcome to the ultimate password strength meter!👏.
Assess the security of your passwords with our intuitive strength meter, providing instant feedback to help you create unbreakable passwords!🔐.
""")

password = st.text_input("Enter your password here", type="password")

feedback = []
score = 0 

if password:
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌Password should be at least 8 characters long.")
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌Password should contain at least one uppercase and one lowercase letter.")
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("❌Password should contain at least one digit.")
    if re.search(r"[!@#$%&*]", password):
        score += 1
    else:
        feedback.append("❌Password should contain at least one special character (!@#$%&*).")
    if score == 4 :
        st.info("✅ Your Password is strong!🚀.")
    elif score == 3 :
        st.info("🟡 Your Password is moderately strong.It can be more stronger!")
    else:
        st.info("🔴 Your Password is weak. Please make it stronger.")
    
    if feedback:
       st.markdown("## Recommendations!")
       for suggesstion in feedback:
           st.write(suggesstion)

else:
    st.info("Enter your password to get started.")
