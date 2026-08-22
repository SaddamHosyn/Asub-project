# 🏛️ Åland Official Statistics Portal (ÅSUB)

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://asub-project-showcase.streamlit.app/)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/streamlit-v1.30+-ff4b4b.svg)](https://streamlit.io/)
[![Plotly](https://img.shields.io/badge/plotly-v5.18+-3f4f75.svg)](https://plotly.com/)

An interactive, high-contrast, multi-domain statistical portal for **Åland (Ålands statistik- och utredningsbyrå)**. Designed for statisticians, policy analysts, journalists, and decision-makers requiring accurate demographic, macroeconomic, labor market, and tourism intelligence.

---

## 🌐 Live Interactive Portal

Experience the live deployed application on Streamlit Community Cloud:  
👉 **[https://asub-project-showcase.streamlit.app/](https://asub-project-showcase.streamlit.app/)**

---

## 🌟 Key Features & Sections

### ⚡ 1. Smart Defaults & Permalinks Bar
* **1-Click Quick Presets**: Bypass multi-click matrix filtering with instant analytical presets:
  * 📊 **Last 5 Yrs Trend**: Pre-loads 2021–2026 macro data across all regions.
  * 📍 **Capital Spotlight**: Filters regional metrics specifically to Mariehamn.
  * 💼 **Post-2020 Recovery**: Analyzes post-pandemic labor & GDP normalization (2020–2026).
  * 🚢 **Tourism & Green**: Highlights renewable energy adoption & maritime tourism peaks (2018–2026).
  * 🔄 **Reset Defaults**: Instantly restores default portal scope.

### 📊 2. Executive Overview
* **Macro Trajectory**: Dual-axis visualization comparing total population growth (2015–2026) against annual GDP (€ Millions).
* **Regional Pulse**: Donut chart detailing population distribution across Capital, Mainland, and Archipelago regions.
* **Strategic Observation Cards**: High-contrast insight summaries highlighting mainland growth leaders, labor market trends, and green energy adoption.

### 👥 3. Demographics & Municipalities
* **16 Municipal Districts**: Detailed population ranking across all 16 Åland municipalities (Mariehamn, Jomala, Hammarland, Lemland, Saltvik, Finström, etc.).
* **Population Pyramid**: Gender & age distribution breakdown across 6 primary age brackets.
* **Growth vs. Unemployment Matrix**: Interactive scatter matrix evaluating municipal growth rate against regional unemployment percentages.

### 💼 4. Economy & Labor Market
* **Macro Trends**: Inflation (CPI) vs. Unemployment Rate trajectory timeline.
* **Employment Share**: Industry sector breakdown encompassing Maritime, Public Administration, Retail, Tourism, Tech/Finance, and Agriculture.
* **GDP per Capita**: Economic productivity trajectory per capita (€52,330 in 2026).

### 🚢 5. Tourism & Transport
* **Seasonality Breakdown**: Monthly guest overnight stay distribution across commercial accommodations.
* **Maritime Logistics**: Ferry passenger traffic volume timeline across major Åland ports (2.22M annual passengers).

### 🔮 6. Scenario Forecaster
* **Demographic & GDP Projections**: Interactive slider controls allowing users to adjust forecast horizon (up to 15 years), population growth rates, and GDP annual expansion.
* **Baseline vs. Model Plot**: Comparative model line chart illustrating historical baseline vs. projected future outcomes.

### 📖 7. 'Åland in Figures' Scrollytelling Story Mode
* **Narrative Storytelling**: Ditch static PDFs for an interactive 4-chapter narrative:
  * **Chapter 1: Demographic Expansion** (30,952 residents & Jomala +1.8% boom).
  * **Chapter 2: Economic Resilience** (€1.62B GDP engine & shipping jobs).
  * **Chapter 3: Nordic Green Transition** (70.2% renewable energy adoption milestone).
  * **Chapter 4: Maritime Gateway & Tourism** (2.22M ferry passengers & summer peaks).
* **Interactive Stepper**: Step-by-step chapter navigation with key insight callout cards and dynamic morphing Plotly figures.

### 📰 8. Embeddable News Media Widget Generator
* **Live Embeds for Local Media**: Purpose-built tool for journalists at *Ålandstidningen*, *Nya Åland*, and *Ålands Radio*.
* **Customization**: Select chart dataset, color theme preset (Official Blue, High Contrast, Emerald), and height.
* **1-Click Iframe Generator**: Generates clean `<iframe src="...">` embed HTML snippets with 1-click clipboard copy.
* **Headless Embed Mode**: Supports `?embed=1` query parameters for borderless iframe embedding on news portals.

### 🚀 9. Social Media Share Preview
* **OpenGraph Card Preview**: Preview dynamic cards for Twitter/LinkedIn sharing.
* **Deep Share Links**: Generates share links with query parameters (`?metric=population&pop=30952...`) with automatic clipboard copying.

---

## 🏗️ Project Architecture

```
d:\Projects\Asub\
├── app.py                     # Main Streamlit entrypoint, query router & tab navigation
├── requirements.txt           # Python dependencies
├── README.md                  # Comprehensive project documentation
├── utils/
│   ├── __init__.py
│   ├── styles.py              # High-contrast CSS design system & component polish
│   ├── data_loader.py         # Data caching engine & PX-Web synthetic dataset generator
│   └── plotly_theme.py        # Unified high-contrast Plotly layout preset helper
└── views/
    ├── __init__.py
    ├── smart_defaults.py      # 1-Click Smart Permalinks & quick presets bar
    ├── overview.py            # Section 1: Executive Overview view
    ├── demographics.py        # Section 2: Demographics & Municipalities view
    ├── economy.py             # Section 3: Economy & Labor Market view
    ├── tourism.py             # Section 4: Tourism & Transport view
    ├── forecaster.py          # Section 5: Scenario Forecaster view
    ├── scrollytelling.py      # Section 6: 'Åland in Figures' Scrollytelling story mode
    ├── news_widget.py         # Section 7: Embeddable News Media Widget generator
    ├── data_explorer.py       # Section 8: Data Explorer & JSON-stat 2.0 inspector
    └── social_share.py        # Social Media Share Preview component
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
