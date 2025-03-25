import streamlit as st

st.title("🌏🔄 Unit Converter")
st.markdown("### Converts Length, Weight, Time and Temperature Instantly")
st.write("Quickly switch between units with our powerful converter tool.")

category = st.selectbox("Select Category", ["Length", "Weight", "Time","Temperature"])

def convert_units(category, value, unit):
    unit_label = ""

    if category == "Length":
        if unit == "Kilometers to Miles":
            result = value * 0.631371
            unit_label = "miles"
        elif unit == "Miles to Kilometers":
            result = value / 0.631371
            unit_label = "kilometers"
        else:
            return None

    elif category == "Weight":
        if unit == "Kilograms to Pounds":
            result = value * 2.20462
            unit_label = "pounds"
        elif unit == "Pounds to Kilograms":
            result = value / 2.20462
            unit_label = "kilograms"
        else:
            return None

    elif category == "Time":
        if unit == "Seconds to Minutes":
            result = value / 60
            unit_label = "minutes"
        elif unit == "Minutes to Seconds":
            result = value * 60
            unit_label = "seconds"
        elif unit == "Minutes to Hours":
            result = value / 60
            unit_label = "hours"
        elif unit == "Hours to Minutes":
            result = value * 60
            unit_label = "minutes"
        elif unit == "Hours to Days":
            result = value / 24
            unit_label = "days"
        elif unit == "Days to Hours":
            result = value * 24
            unit_label = "hours"
        else:
            return None
    elif category == "Temperature":
        if unit == "Celsius to Fahrenheit":
            result = (value * 9/5) + 32
            unit_label = "Fahrenheit"
        elif unit == "Fahrenheit to Celsius":
            result = (value - 32) * 5/9
            unit_label = "Celsius"
        else:
         return None

    return f"{result:.2f} {unit_label}"

if category == "Length":
    unit = st.selectbox("📏 Select Conversion Unit", ["Kilometers to Miles", "Miles to Kilometers"])
elif category == "Weight":
    unit = st.selectbox("⚖ Select Conversion Unit", ["Kilograms to Pounds", "Pounds to Kilograms"])
elif category == "Time":
    unit = st.selectbox("🕰 Select Conversion Unit", ["Seconds to Minutes", "Minutes to Seconds", "Minutes to Hours", "Hours to Minutes", "Hours to Days", "Days to Hours"])
elif category == "Temperature":
    unit = st.selectbox("��️ Select Conversion Unit", ["Celsius to Fahrenheit", "Fahrenheit to Celsius"])
value = st.number_input("Enter a value to convert", min_value=0.0)

# Convert Button Styles
st.markdown("""
    <style>
    .stButton > button {
        background-color: #4c648c;
        color: white;
        border: none;
        padding: 10px 325px;
        font-size: 18px;
        cursor: pointer;
        border-radius: 10px;
        margin: 20px 0;
        box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.2), 0 3px 10px 0 rgba(0, 0, 0, 0.19);
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        background-color: #1798a8 ;
        color: black;
    }
    </style>
""",unsafe_allow_html= True)

if st.button("Convert"):
    result = convert_units(category, value, unit)
    
    if result is not None:
        st.success(f"The result is: {result}")
    else:
        st.error("Invalid Input")


