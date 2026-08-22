# 🏛️ Åland Official Statistics Portal (ÅSUB)

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/streamlit-v1.30+-ff4b4b.svg)](https://streamlit.io/)
[![Plotly](https://img.shields.io/badge/plotly-v5.18+-3f4f75.svg)](https://plotly.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

An interactive, high-contrast, multi-domain statistical portal for **Åland (Ålands statistik- och utredningsbyrå)**. Designed for statisticians, policy analysts, and decision-makers requiring accurate demographic, macroeconomic, labor market, and tourism intelligence.

---

## 🌟 Key Features & Sections

### 1. 📊 Executive Overview
* **Macro Trajectory**: Dual-axis visualization comparing total population growth (2015–2026) against annual GDP (€ Millions).
* **Regional Pulse**: Donut chart detailing population distribution across Capital, Mainland, and Archipelago regions.
* **Strategic Observation Cards**: High-contrast insight summaries highlighting mainland growth leaders, labor market trends, and green energy adoption.

### 2. 👥 Demographics & Municipalities
* **16 Municipal Districts**: Detailed population ranking across all 16 Åland municipalities (Mariehamn, Jomala, Hammarland, Lemland, Saltvik, Finström, etc.).
* **Population Pyramid**: Gender & age distribution breakdown across 6 primary age brackets.
* **Growth vs. Unemployment Matrix**: Interactive scatter matrix evaluating municipal growth rate against regional unemployment percentages.

### 3. 💼 Economy & Labor Market
* **Macro Trends**: Inflation (CPI) vs. Unemployment Rate trajectory timeline.
* **Employment Share**: Industry sector breakdown encompassing Maritime, Public Administration, Retail, Tourism, Tech/Finance, and Agriculture.
* **GDP per Capita**: Economic productivity trajectory per capita in Euros.

### 4. 🚢 Tourism & Transport
* **Seasonality Breakdown**: Monthly guest overnight stay distribution across commercial accommodations.
* **Maritime Logistics**: Ferry passenger traffic volume timeline across major Åland ports.

### 5. 🔮 Scenario Forecaster
* **Demographic & GDP Projections**: Interactive slider controls allowing users to adjust forecast horizon (up to 15 years), population growth rates, and GDP annual expansion.
* **Baseline vs. Model Plot**: Comparative model line chart illustrating historical baseline vs. projected future outcomes.

### 6. 📥 Data Explorer & Export Engine
* **1-Click Export**: Download filtered datasets in **CSV** or **JSON** formats.
* **JSON-stat 2.0 API Inspector**: Raw PX-Web JSON-stat response payload inspector for software developers and data engineers.

---

## 🏗️ Project Architecture

```
d:\Projects\Asub\
├── app.py                     # Main Streamlit entrypoint & router (~130 lines)
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
├── utils/
│   ├── __init__.py
│   ├── styles.py              # Modern high-contrast CSS design system
│   ├── data_loader.py         # Data caching engine & PX-Web synthetic dataset generator
│   └── plotly_theme.py        # Unified high-contrast Plotly layout preset helper
└── views/
    ├── __init__.py
    ├── overview.py            # Section 1: Executive Overview view
    ├── demographics.py        # Section 2: Demographics & Municipalities view
    ├── economy.py             # Section 3: Economy & Labor Market view
    ├── tourism.py             # Section 4: Tourism & Transport view
    ├── forecaster.py          # Section 5: Scenario Forecaster view
    └── data_explorer.py       # Section 6: Data Explorer & JSON-stat view
```

---

## 🚀 Quick Start

### Prerequisites
* **Python 3.10+**
* `pip` package manager

### Installation & Execution

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/SaddamHosyn/Asub-project.git
   cd Asub-project
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Launch the Dashboard**:
   ```bash
   python -m streamlit run app.py
   ```

4. **Access in Browser**:
   Open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 🛠️ Built With

* [Streamlit](https://streamlit.io/) - Web Application Framework
* [Pandas](https://pandas.pydata.org/) - Data Manipulation & Analysis
* [Plotly](https://plotly.com/python/) - Interactive Graphing Library
* [NumPy](https://numpy.org/) - Numerical Data Processing

---
