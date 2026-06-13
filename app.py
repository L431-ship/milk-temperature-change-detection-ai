import streamlit as st

import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Dairy Product Temperature Recommendation System",
    page_icon="🌡️",
    layout="centered"
)

# Function to calculate recommended temperature
def get_required_temperature(product, external_temp, insulation_quality):

    product_temp_map = {
        'Milk': {'target': 3, 'min': 1, 'max': 4},
        'Curd': {'target': 4, 'min': 2, 'max': 6},
        'Ice-cream': {'target': -15, 'min': -18, 'max': -12},
        'Cheese': {'target': 4, 'min': 1, 'max': 7},
        'Flavored Milk': {'target': 5, 'min': 2, 'max': 8}
    }

    insulation_factor = {
        "Poor": 1.50,
        "Medium": 1.00,
        "Good": 0.60
    }

    if product not in product_temp_map:
        return None, None

    data = product_temp_map[product]
    base_temp = data['target']

    # Calculate heat load
    heat_load = max(
        0,
        external_temp - 25
    ) * insulation_factor[insulation_quality]

    # Adjust storage temperature
    recommended_temp = base_temp - (heat_load * 0.05)

    # Keep within safe range
    recommended_temp = max(
        data['min'],
        min(recommended_temp, data['max'])
    )

    return round(recommended_temp, 1), round(heat_load, 2)


# Title
st.title("🌡️ Dairy Product Temperature Recommendation System")

st.write(
    "This system recommends an optimal storage temperature "
    "based on product type, external temperature, and insulation quality."
)

# Product selection
product = st.selectbox(
    "Select Product",
    [
        "Milk",
        "Curd",
        "Ice-cream",
        "Cheese",
        "Flavored Milk"
    ]
)

# External temperature input
external_temp = st.number_input(
    "Enter External Temperature (°C)",
    min_value=-10.0,
    max_value=60.0,
    value=30.0,
    step=1.0
)

# Insulation selection
insulation_quality = st.selectbox(
    "Select Insulation Quality",
    [
        "Poor",
        "Medium",
        "Good"
    ]
)

# Button
if st.button("Calculate Recommendation"):

    recommended_temp, heat_load = get_required_temperature(
        product,
        external_temp,
        insulation_quality
    )

    st.success(
        f"Recommended Storage Temperature: {recommended_temp} °C"
    )

    st.info(
        f"Estimated Heat Load Index: {heat_load}"
    )

    # Additional remarks
    if insulation_quality == "Poor":
        st.warning(
            "Poor insulation detected. Energy consumption may increase."
        )

    elif insulation_quality == "Good":
        st.success(
            "Good insulation helps reduce cooling energy requirements."
        )

# Footer
st.markdown("---")
st.caption(
    "Developed as an AI-based Environmental Temperature Control System for Dairy Products."
)
