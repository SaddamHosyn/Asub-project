import streamlit as st

def _preset_last_5(max_year):
    st.session_state["year_range_slider"] = (max_year - 5, max_year)
    st.session_state["region_selectbox"] = "All Regions"

def _preset_capital():
    st.session_state["region_selectbox"] = "Capital City"

def _preset_post_2020(max_year):
    st.session_state["year_range_slider"] = (2020, max_year)
    st.session_state["region_selectbox"] = "All Regions"

def _preset_tourism_green(max_year):
    st.session_state["year_range_slider"] = (2018, max_year)
    st.session_state["region_selectbox"] = "All Regions"

def _preset_reset(max_year):
    st.session_state["year_range_slider"] = (2017, max_year)
    st.session_state["region_selectbox"] = "All Regions"

def render_smart_defaults_bar(min_year, max_year, region_options):
    """Renders 1-Click Smart Permalinks Bar using on_click callbacks to prevent Streamlit state mutation exceptions."""
    
    st.markdown("""
    <div style="background-color: #ffffff; border: 1.5px solid #cbd5e1; border-left: 6px solid #004077; padding: 12px 18px; border-radius: 10px; margin-bottom: 16px; box-shadow: 0 2px 8px rgba(15,23,42,0.04);">
        <div style="color: #004077; font-weight: 800; font-size: 0.98rem; margin-bottom: 4px;">
            ⚡ Smart Permalinks & Quick Presets
        </div>
        <div style="color: #475569; font-size: 0.88rem; font-weight: 600;">
            1-Click pre-configured views to bypass manual matrix filtering:
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    c1, c2, c3, c4, c5 = st.columns(5)
    
    with c1:
        st.button(
            "📊 Last 5 Yrs Trend", 
            help="Pre-load 2021-2026 Macro Data across all regions",
            on_click=_preset_last_5,
            args=(max_year,)
        )
            
    with c2:
        st.button(
            "📍 Capital Spotlight", 
            help="Focus metrics specifically on Mariehamn",
            on_click=_preset_capital
        )
            
    with c3:
        st.button(
            "💼 Post-2020 Recovery", 
            help="Analyze post-pandemic economic and labor normalization (2020-2026)",
            on_click=_preset_post_2020,
            args=(max_year,)
        )

    with c4:
        st.button(
            "🚢 Tourism & Green", 
            help="Highlight seasonal tourism & renewable energy progress (2018-2026)",
            on_click=_preset_tourism_green,
            args=(max_year,)
        )

    with c5:
        st.button(
            "🔄 Reset Defaults", 
            help="Restore default portal time horizon and regional scope",
            on_click=_preset_reset,
            args=(max_year,)
        )
    
    st.markdown("<div style='margin-bottom: 12px;'></div>", unsafe_allow_html=True)
