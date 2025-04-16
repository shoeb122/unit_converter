import streamlit as st

def convert_units(value, unit_from, unit_to):
    conversions = {
        # Length conversions
        "millimeter_centimeter": 0.1,
        "centimeter_millimeter": 10,
        "centimeter_meter": 0.01,
        "meter_centimeter": 100,
        "meter_kilometer": 0.001,
        "kilometer_meter": 1000,
        "millimeter_meter": 0.001,
        "meter_millimeter": 1000,
        "centimeter_kilometer": 0.00001,
        "kilometer_centimeter": 100000,
        "millimeter_kilometer": 0.000001,
        "kilometer_millimeter": 1000000,

        # Weight conversions
        "milligram_gram": 0.001,
        "gram_milligram": 1000,
        "gram_kilogram": 0.001,
        "kilogram_gram": 1000,
        "milligram_kilogram": 0.000001,
        "kilogram_milligram": 1000000,
    }

    key = f"{unit_from}_{unit_to}"
    if key in conversions:
        return value * conversions[key]
    elif unit_from == unit_to:
        return value  # Same unit conversion
    else:
        return "Conversion not found"

st.title("🔄 Smart Unit Converter")

value = st.number_input("Enter the value to convert:", min_value=0.0, step=1.0)

all_units = [
    "millimeter", "centimeter", "meter", "kilometer",
    "milligram", "gram", "kilogram"
]

unit_from = st.selectbox("Convert from:", all_units)
unit_to = st.selectbox("Convert to:", all_units)

if st.button("Convert"):
    result = convert_units(value, unit_from, unit_to)
    st.write(f"🔁 Converted Value: {result}")
