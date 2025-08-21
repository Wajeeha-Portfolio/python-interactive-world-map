import streamlit as st
import plotly.express as px
import pandas as pd
import os
import data_collector as collector

# Set the title of the Streamlit app
st.title("Global Indicators Dashboard")

if "indicators_list" not in st.session_state:
    st.session_state.indicators_list = ["population","GDP-per-capita","literacy-rate","inflation-rate"]

if "last_selected_feature" not in st.session_state:
    st.session_state.last_selected_feature = None
    st.session_state.df = None  # To store the loaded DataFrame

# Streamlit dropdown
selected_feature = st.selectbox("Select an indicator", st.session_state.indicators_list)

st.markdown("### Add indicator to List")

if selected_feature != st.session_state.last_selected_feature:
    csv_path = f"{selected_feature}.csv"

    if os.path.exists(csv_path):
        print(f"CSV file found at {csv_path}. Loading data...")
        st.session_state.df = pd.read_csv(csv_path)
        print(f"Data loaded successfully for {st.session_state.indicators_list}.")
    else:
        print(f"CSV file not found at {csv_path}. Calling fetch_data()...")
        st.session_state.df = collector.fetch_data(selected_feature)  # Fetch and save in helper.py

    # Update session state with the new selection
    st.session_state.last_selected_feature = selected_feature

# Text input
new_item = st.text_input("Enter indicator:")

# Add to list when button is clicked
if st.button("Add"):
    if new_item.strip():
        if collector.validate_indicator(new_item.strip()) == "true" and new_item.strip().replace(" ", "-").lower() not in st.session_state.indicators_list:
            st.session_state.indicators_list.append(new_item.strip().replace(" ", "-").lower())
            st.session_state.last_selected_feature = new_item.strip().replace(" ", "-").lower()
            st.success(f"Added: {new_item}")
            print(f"updated value: {st.session_state.indicators_list}")
            st.rerun()
        else:
            st.warning("Invalid indicator.")
    else:
        st.warning("Please enter a non-empty value.")


# Create the choropleth map figure using Plotly Express
fig = px.choropleth(st.session_state.df,
                    locations="Country Code",
                    color=selected_feature,
                    hover_name="Country",
                    color_continuous_scale="Viridis",
                    projection="natural earth")

# Display the Plotly figure in the Streamlit app
st.plotly_chart(fig, use_container_width=True)

# You can add more Streamlit widgets and text here
st.markdown("### Data Source")
st.write("This map visualizes the data from the gpt-4.1-mini")