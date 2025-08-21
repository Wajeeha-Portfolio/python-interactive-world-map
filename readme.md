# 🌍 Python Interactive World Map

An interactive Streamlit dashboard for visualizing global development indicators on a world map.  
Easily add new indicators, fetch real-time data using OpenAI, and explore country-level statistics with beautiful Plotly choropleth maps.

---

## 🚀 Features

- **Dynamic Indicator List:**  
  Add new global indicators and instantly visualize them.

- **AI-Powered Data Fetching:**  
  Uses OpenAI to validate indicators and generate up-to-date datasets.

- **Interactive Visualization:**  
  Explore data on a world map with Plotly Express.

- **Easy to Use:**  
  Simple Streamlit UI for both data exploration and indicator management.

---

## 🖥️ Demo

![Demo Screenshot]()  
*Visualize any global indicator with a single click!*

---

## 📦 Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Wajeeha-Portfolio/python-interactive-world-map.git
    cd python-interactive-world-map-repo/python-interactive-world-map
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Set your OpenAI API key:**  
   Edit `data_collector.py` and replace `"your-api-key"` with your actual OpenAI API key.

---

## 🏃 Usage

```bash
streamlit run app.py
```

- Select an indicator from the dropdown to view its world map.
- Add a new indicator using the text input and "Add" button.
- The map and dropdown update automatically with new data.

---

## 🛠️ Project Structure

```
python-interactive-world-map/
│
├── app.py                # Main Streamlit app
├── data_collector.py     # OpenAI-powered data fetching & validation
├── requirements.txt      # Python dependencies
└── README.md             # This file
```

---

## 🤖 How It Works

- **Indicator Validation:**  
  Uses OpenAI to check if your input is a recognized global indicator.

- **Data Fetching:**  
  If data for an indicator is missing, OpenAI generates a CSV-style dataset for all countries.

- **Visualization:**  
  Plotly Express renders the data as a choropleth map.

---

## 📊 Example Indicators

- `population`
- `GDP-per-capita`
- `literacy-rate`
- `inflation-rate`
- *(Add your own!)*

---

## 💡 Customization

- Add more default indicators in `app.py`.
- Adjust the OpenAI prompt in `data_collector.py` for different data needs.

---

## 🙏 Acknowledgements

- [Streamlit](https://streamlit.io/)
- [Plotly](https://plotly.com/python/)
