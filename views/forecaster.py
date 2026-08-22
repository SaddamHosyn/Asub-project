import streamlit as st
import pandas as pd
import plotly.express as px
from utils.plotly_theme import get_plotly_preset

def render_forecaster_tab(df_macro, latest_year):
    """Renders Tab 5: Scenario Forecaster Projections Engine."""
    st.markdown("""
    <div class="section-theme-banner theme-fore">
        🔮 Section 5: Demographic & Macroeconomic Projection Engine
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background-color: #ffffff; border: 1.5px solid #cbd5e1; border-left: 6px solid #7c3aed; padding: 14px 20px; border-radius: 10px; box-shadow: 0 4px 12px rgba(15,23,42,0.04); margin-bottom: 20px;">
        <div style="color: #581c87; font-weight: 800; font-size: 1.02rem; margin-bottom: 4px;">💡 Projection Instructions</div>
        <div style="color: #0f172a; font-weight: 600; font-size: 0.95rem;">Adjust scenario sliders to simulate future Åland population and GDP trajectories.</div>
    </div>
    """, unsafe_allow_html=True)
    
    f_col1, f_col2 = st.columns([1, 2])
    
    with f_col1:
        st.markdown("#### Scenario Controls")
        horizon_years = st.slider("Forecast Horizon (Years)", 1, 15, 8)
        growth_rate = st.slider("Est. Annual Population Growth (%)", -0.5, 3.0, 0.8, step=0.1)
        gdp_growth_rate = st.slider("Est. Annual GDP Growth (%)", -1.0, 4.0, 1.5, step=0.1)
        
        base_pop = df_macro["population"].iloc[-1]
        base_gdp = df_macro["gdp_million_eur"].iloc[-1]
        
        future_years = [latest_year + i for i in range(1, horizon_years + 1)]
        projected_pop = [int(base_pop * ((1 + growth_rate / 100) ** i)) for i in range(1, horizon_years + 1)]
        projected_gdp = [round(base_gdp * ((1 + gdp_growth_rate / 100) ** i), 1) for i in range(1, horizon_years + 1)]
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.metric("Projected Population in " + str(future_years[-1]), f"{projected_pop[-1]:,}", delta=f"+{projected_pop[-1] - base_pop:,}")
        st.metric("Projected GDP in " + str(future_years[-1]), f"€{projected_gdp[-1]}M", delta=f"+€{round(projected_gdp[-1] - base_gdp, 1)}M")
        
    with f_col2:
        st.markdown("#### Baseline vs. Model Projection")
        
        df_proj = pd.DataFrame({
            "year": list(df_macro["year"]) + future_years,
            "population": list(df_macro["population"]) + projected_pop,
            "type": ["Historical Baseline"] * len(df_macro) + ["Model Forecast"] * len(future_years)
        })
        
        fig_proj = px.line(
            df_proj,
            x="year",
            y="population",
            color="type",
            markers=True,
            color_discrete_map={"Historical Baseline": "#004077", "Model Forecast": "#dc2626"}
        )
        layout_proj = get_plotly_preset()
        layout_proj.update(
            height=380,
            xaxis=dict(
                title=dict(text="Year", font=dict(color="#0f172a", size=13)),
                tickfont=dict(color="#0f172a", size=12)
            ),
            yaxis=dict(
                title=dict(text="Population", font=dict(color="#0f172a", size=13)),
                tickfont=dict(color="#0f172a", size=12)
            ),
            legend=dict(bordercolor="#cbd5e1", borderwidth=1, bgcolor="#ffffff", font=dict(color="#0f172a"))
        )
        fig_proj.update_layout(layout_proj)
        st.plotly_chart(fig_proj, width="stretch")
