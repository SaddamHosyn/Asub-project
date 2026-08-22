import streamlit as st

def apply_custom_styles():
    """Injects modern high-contrast CSS overrides into the Streamlit app."""
    st.markdown("""
    <style>
        /* Global Typography & High-Contrast Colors */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
        
        html, body, [class*="css"], .stMarkdown, p, span, label, div {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        }
        
        .stApp {
            background-color: #f1f5f9 !important;
            color: #0f172a !important;
        }

        /* Force crisp dark text across all headers and markdown elements */
        h1, h2, h3, h4, h5, h6, .stMarkdown p, .stMarkdown span {
            color: #0f172a !important;
        }

        /* Sidebar Styling */
        section[data-testid="stSidebar"] {
            background-color: #ffffff !important;
            border-right: 1.5px solid #cbd5e1 !important;
        }
        
        section[data-testid="stSidebar"] label, 
        section[data-testid="stSidebar"] span, 
        section[data-testid="stSidebar"] p,
        section[data-testid="stSidebar"] div {
            color: #0f172a !important;
            font-weight: 700 !important;
        }

        /* Input Controls (Selectbox, Dropdowns, Radio, Checkbox, Slider) */
        div[data-baseweb="select"] > div, 
        div[data-baseweb="base-input"] input {
            background-color: #ffffff !important;
            color: #0f172a !important;
            border: 1.5px solid #94a3b8 !important;
            font-weight: 700 !important;
            border-radius: 8px !important;
        }

        /* Dropdown Menu Popover Options Contrast */
        div[data-baseweb="popover"] {
            background-color: #ffffff !important;
            border: 2px solid #64748b !important;
            box-shadow: 0 10px 30px rgba(15, 23, 42, 0.18) !important;
        }
        
        div[data-baseweb="popover"] ul li {
            color: #0f172a !important;
            font-weight: 700 !important;
            background-color: #ffffff !important;
        }

        div[data-baseweb="popover"] ul li:hover {
            background-color: #e2e8f0 !important;
            color: #004077 !important;
        }

        div[role="radiogroup"] label p, 
        div[data-testid="stCheckbox"] label p,
        div[data-testid="stCheckbox"] label span {
            color: #0f172a !important;
            font-weight: 700 !important;
        }

        /* Checkbox Box Styling Fix (Force dark black rgb(43, 44, 54) box -> Light Grey #cbd5e1) */
        div[data-testid="stCheckbox"] [data-baseweb="checkbox"] div,
        div[data-testid="stCheckbox"] [data-baseweb="checkbox"] span,
        div[data-testid="stCheckbox"] label > div:first-child,
        div[data-testid="stCheckbox"] label > div:first-child *,
        div[data-testid="stCheckbox"] div[class*="st-emotion-cache"],
        div[data-baseweb="checkbox"] > div {
            background-color: #cbd5e1 !important;
            background: #cbd5e1 !important;
            border: 2px solid #475569 !important;
            border-radius: 4px !important;
        }

        div[data-testid="stCheckbox"] input:checked ~ div,
        div[data-testid="stCheckbox"] input:checked + div,
        div[data-testid="stCheckbox"] [aria-checked="true"] div,
        div[data-testid="stCheckbox"] [aria-checked="true"] span {
            background-color: #005293 !important;
            background: #005293 !important;
            border-color: #00284d !important;
        }

        /* Main Header Banner */
        .main-header-banner {
            background: linear-gradient(135deg, #001f3f 0%, #003366 50%, #004077 100%);
            color: #ffffff !important;
            padding: 28px 36px;
            border-radius: 16px;
            box-shadow: 0 10px 25px rgba(0, 31, 63, 0.25);
            margin-bottom: 24px;
            position: relative;
            overflow: hidden;
        }

        .main-header-title {
            font-size: 2.2rem;
            font-weight: 800;
            margin: 0;
            letter-spacing: -0.5px;
            color: #ffffff !important;
        }

        .main-header-subtitle {
            font-size: 1.1rem;
            color: #e2e8f0 !important;
            margin-top: 6px;
            margin-bottom: 0;
            font-weight: 500;
        }

        /* Distinct Section Accent Banners */
        .section-theme-banner {
            padding: 14px 22px;
            border-radius: 12px;
            color: #ffffff !important;
            font-weight: 800;
            font-size: 1.3rem;
            margin-bottom: 20px;
            display: flex;
            align-items: center;
            gap: 12px;
            box-shadow: 0 4px 12px rgba(15, 23, 42, 0.08);
        }
        
        .theme-exec { background: linear-gradient(135deg, #00284d 0%, #004077 100%); }
        .theme-demo { background: linear-gradient(135deg, #0284c7 0%, #0369a1 100%); }
        .theme-econ { background: linear-gradient(135deg, #1e3a8a 0%, #2563eb 100%); }
        .theme-tour { background: linear-gradient(135deg, #0f766e 0%, #0d9488 100%); }
        .theme-fore { background: linear-gradient(135deg, #581c87 0%, #7c3aed 100%); }

        /* Custom Metric Cards & Rich Green Delta Indicators */
        [data-testid="stMetric"] {
            background-color: #ffffff !important;
            border: 1.5px solid #cbd5e1 !important;
            border-radius: 12px !important;
            padding: 16px 20px !important;
            box-shadow: 0 4px 12px rgba(15, 23, 42, 0.05) !important;
        }

        [data-testid="stMetricLabel"] {
            color: #334155 !important;
            font-size: 0.95rem !important;
            font-weight: 700 !important;
        }

        [data-testid="stMetricValue"] {
            color: #0f172a !important;
            font-size: 2.1rem !important;
            font-weight: 800 !important;
        }

        /* Metric Delta Base Typography */
        [data-testid="stMetricDelta"] {
            font-weight: 800 !important;
            font-size: 0.95rem !important;
        }

        /* Streamlit Green Metric Deltas (data-test-color="green") -> Forest Green #15803d */
        div[data-testid="stMetricDelta"][data-test-color="green"],
        div[data-testid="stMetricDelta"][data-test-color="green"] *,
        div[data-testid="stMetricDelta"]:has(svg[data-testid="stMetricDeltaIcon-Up"]) *,
        svg[data-testid="stMetricDeltaIcon-Up"],
        svg[data-testid="stMetricDeltaIcon-Up"] path {
            color: #15803d !important;
            fill: #15803d !important;
            border-color: transparent !important;
            font-weight: 800 !important;
        }

        /* Streamlit Red Metric Deltas (data-test-color="red") -> Crimson Red #dc2626 */
        div[data-testid="stMetricDelta"][data-test-color="red"],
        div[data-testid="stMetricDelta"][data-test-color="red"] *,
        div[data-testid="stMetricDelta"]:has(svg[data-testid="stMetricDeltaIcon-Down"]) *,
        svg[data-testid="stMetricDeltaIcon-Down"],
        svg[data-testid="stMetricDeltaIcon-Down"] path {
            color: #dc2626 !important;
            fill: #dc2626 !important;
            border-color: transparent !important;
            font-weight: 800 !important;
        }

        /* Data Integrity Warning Box */
        .integrity-alert {
            background-color: #fff3cd !important;
            border: 1.5px solid #ffe69c !important;
            color: #664d03 !important;
            padding: 14px 20px;
            border-radius: 10px;
            font-weight: 600;
            font-size: 0.95rem;
            margin-bottom: 24px;
            box-shadow: 0 2px 8px rgba(102, 77, 3, 0.05);
        }

        /* Streamlit Alert Boxes High-Contrast Overrides (st.info, st.warning, st.success, st.error) */
        div[data-testid="stAlert"] {
            border-radius: 10px !important;
            padding: 16px 20px !important;
        }

        div[data-testid="stAlert"] p,
        div[data-testid="stAlert"] span,
        div[data-testid="stAlert"] div,
        div[data-testid="stAlert"] strong {
            font-weight: 700 !important;
            font-size: 0.95rem !important;
            opacity: 1 !important;
        }

        /* Info Box (st.info) */
        div[data-testid="stAlert"][kind="info"],
        div[data-baseweb="notification"][kind="info"] {
            background-color: #e0f2fe !important;
            border: 1.5px solid #0284c7 !important;
        }
        div[data-testid="stAlert"][kind="info"] *,
        div[data-baseweb="notification"][kind="info"] * {
            color: #034078 !important;
        }

        /* Warning Box (st.warning) */
        div[data-testid="stAlert"][kind="warning"],
        div[data-baseweb="notification"][kind="warning"] {
            background-color: #fff3cd !important;
            border: 1.5px solid #d97706 !important;
        }
        div[data-testid="stAlert"][kind="warning"] *,
        div[data-baseweb="notification"][kind="warning"] * {
            color: #664d03 !important;
        }

        /* Success Box (st.success) */
        div[data-testid="stAlert"][kind="success"],
        div[data-baseweb="notification"][kind="success"] {
            background-color: #dcfce7 !important;
            border: 1.5px solid #16a34a !important;
        }
        div[data-testid="stAlert"][kind="success"] *,
        div[data-baseweb="notification"][kind="success"] * {
            color: #064e3b !important;
        }

        /* Error Box (st.error) */
        div[data-testid="stAlert"][kind="error"],
        div[data-baseweb="notification"][kind="error"] {
            background-color: #fee2e2 !important;
            border: 1.5px solid #dc2626 !important;
        }
        div[data-testid="stAlert"][kind="error"] *,
        div[data-baseweb="notification"][kind="error"] * {
            color: #7f1d1d !important;
        }

        /* Slider Label & Value High-Contrast Text Fix (Photo 1 Fix) */
        div[data-testid="stSlider"] label,
        div[data-testid="stSlider"] label p,
        div[data-testid="stSlider"] label span,
        div[data-testid="stWidgetLabel"] p,
        div[data-testid="stWidgetLabel"] span,
        div[data-testid="stSlider"] [data-testid="stMarkdownContainer"] p {
            color: #0f172a !important;
            font-weight: 800 !important;
            font-size: 1rem !important;
            opacity: 1 !important;
        }

        /* Download CSV/JSON Buttons & Action Button Polish (Photo 2 Fix) */
        div.stDownloadButton > button,
        div.stButton > button,
        button[kind="primary"],
        button[kind="secondary"] {
            background: #004077 !important;
            background-color: #004077 !important;
            color: #ffffff !important;
            border: 1.5px solid #00284d !important;
            border-radius: 8px !important;
            font-weight: 800 !important;
            font-size: 0.95rem !important;
            padding: 10px 22px !important;
            box-shadow: 0 4px 12px rgba(0, 64, 119, 0.2) !important;
        }

        div.stDownloadButton > button:hover,
        div.stButton > button:hover,
        button[kind="primary"]:hover,
        button[kind="secondary"]:hover {
            background: #00284d !important;
            background-color: #00284d !important;
            color: #ffffff !important;
            border-color: #001f3f !important;
        }

        div.stDownloadButton > button *,
        div.stButton > button * {
            color: #ffffff !important;
            font-weight: 800 !important;
        }

        /* Tab Navigation Styling (Photo 3 Fix: Light Blue & Pitch-Black Text Theme) */
        .stTabs [data-baseweb="tab-list"] {
            gap: 8px !important;
            background-color: #e2e8f0 !important;
            padding: 10px 14px !important;
            border-radius: 12px !important;
            border: 1.5px solid #cbd5e1 !important;
        }

        /* Unselected Tabs (Default State) */
        .stTabs [data-baseweb="tab"] {
            height: 48px !important;
            background-color: #e0f2fe !important;
            border-radius: 8px !important;
            border: 1.5px solid #93c5fd !important;
            padding: 0px 20px !important;
        }

        /* Fix color: inherit on div.st-emotion-cache-6urfhe for the 6 Tab options (Photo DevTools Fix) */
        .st-emotion-cache-6urfhe,
        div.st-emotion-cache-6urfhe,
        [class*="st-emotion-cache-6urfhe"],
        .stTabs [data-baseweb="tab"] [class*="st-emotion-cache-6urfhe"],
        .stTabs button[role="tab"] [class*="st-emotion-cache"],
        .stTabs [data-baseweb="tab"] *,
        .stTabs [data-baseweb="tab"] p, 
        .stTabs [data-baseweb="tab"] span,
        .stTabs [data-baseweb="tab"] div,
        .stTabs [data-baseweb="tab"] [data-testid="stMarkdownContainer"] p {
            color: #0f172a !important;
            font-weight: 800 !important;
            font-size: 0.95rem !important;
            opacity: 1 !important;
        }

        /* Active Selected Tab State */
        .stTabs [aria-selected="true"],
        .stTabs [aria-selected="true"] .st-emotion-cache-6urfhe,
        .stTabs [aria-selected="true"] div.st-emotion-cache-6urfhe,
        .stTabs [aria-selected="true"] [class*="st-emotion-cache-6urfhe"],
        .stTabs button[role="tab"][aria-selected="true"] [class*="st-emotion-cache"] {
            background-color: #005293 !important;
            border: 2px solid #00284d !important;
            box-shadow: 0 4px 14px rgba(0, 82, 147, 0.35) !important;
        }

        .stTabs [aria-selected="true"] *,
        .stTabs [aria-selected="true"] p, 
        .stTabs [aria-selected="true"] span,
        .stTabs [aria-selected="true"] div,
        .stTabs [aria-selected="true"] [data-testid="stMarkdownContainer"] p,
        .stTabs [aria-selected="true"] .st-emotion-cache-6urfhe {
            color: #ffffff !important;
            font-weight: 800 !important;
            opacity: 1 !important;
        }

        /* Remove Streamlit default red highlight bar */
        .stTabs [data-baseweb="tab-highlight"] {
            background-color: transparent !important;
            display: none !important;
        }

        /* Force ALL Plotly SVG chart text (axis labels, tick marks, legend titles, annotations) to crisp dark slate (#0f172a) */
        .js-plotly-plot .plotly text,
        .js-plotly-plot .plotly .g-gtitle text,
        .js-plotly-plot .plotly .g-xtitle text,
        .js-plotly-plot .plotly .g-ytitle text,
        .js-plotly-plot .plotly .g-y2title text,
        .js-plotly-plot .plotly .xtick text,
        .js-plotly-plot .plotly .ytick text,
        .js-plotly-plot .plotly .y2tick text,
        .js-plotly-plot .plotly .legend text,
        .js-plotly-plot .plotly .legendtitle text,
        .js-plotly-plot .plotly .annotation text {
            fill: #0f172a !important;
            color: #0f172a !important;
            font-weight: 700 !important;
            opacity: 1 !important;
        }

        /* Hide Streamlit Menu Polish */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)
