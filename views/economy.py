import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from utils.plotly_theme import get_plotly_preset

def render_economy_tab(df_macro_filtered, df_sectors):
    """Renders Tab 3: Economy, Employment Sectors & CPI Inflation."""
    st.markdown("""
    <div class="section-theme-banner theme-econ">
        💼 Section 3: Economy, Employment Sectors & Inflation Trends
    </div>
    """, unsafe_allow_html=True)
    
    e1, e2 = st.columns(2)
    
    with e1:
        st.subheader("Inflation (CPI) vs Unemployment Rate (%)")
        fig_econ_trend = go.Figure()
        
        fig_econ_trend.add_trace(go.Scatter(
            x=df_macro_filtered["year"],
            y=df_macro_filtered["inflation_cpi"],
            name="CPI Inflation (%)",
            line=dict(color="#dc2626", width=3.5),
            mode="lines+markers"
        ))
        
        fig_econ_trend.add_trace(go.Scatter(
            x=df_macro_filtered["year"],
            y=df_macro_filtered["unemployment_rate"],
            name="Unemployment Rate (%)",
            line=dict(color="#1e3a8a", width=3.5),
            mode="lines+markers"
        ))
        
        layout_econ = get_plotly_preset()
        layout_econ.update(
            height=380,
            margin=dict(l=10, r=10, t=20, b=20),
            legend=dict(orientation="h", y=1.12, bordercolor="#cbd5e1", borderwidth=1, bgcolor="#ffffff", font=dict(color="#0f172a")),
            xaxis=dict(
                title=dict(text="Year", font=dict(color="#0f172a", size=13)),
                tickfont=dict(color="#0f172a", size=12)
            ),
            yaxis=dict(
                title=dict(text="Percentage (%)", font=dict(color="#0f172a", size=13)),
                tickfont=dict(color="#0f172a", size=12)
            )
        )
        fig_econ_trend.update_layout(layout_econ)
        st.plotly_chart(fig_econ_trend, width="stretch")
        
    with e2:
        st.subheader("Employment Share by Industry Sector")
        fig_sector_donut = px.pie(
            df_sectors,
            values="share_pct",
            names="sector",
            hole=0.42,
            color_discrete_sequence=px.colors.qualitative.Bold
        )
        layout_sector = get_plotly_preset()
        layout_sector.update(
            height=380,
            margin=dict(l=10, r=10, t=20, b=20),
            legend=dict(orientation="v", x=1.02, bordercolor="#cbd5e1", borderwidth=1, bgcolor="#ffffff", font=dict(color="#0f172a"))
        )
        fig_sector_donut.update_layout(layout_sector)
        st.plotly_chart(fig_sector_donut, width="stretch")

    st.divider()
    st.subheader("GDP per Capita Growth Trajectory (€)")
    fig_gdp_cap = px.area(
        df_macro_filtered,
        x="year",
        y="gdp_per_capita_eur",
        markers=True,
        color_discrete_sequence=["#15803d"]
    )
    layout_gdp = get_plotly_preset()
    layout_gdp.update(
        height=340,
        xaxis=dict(
            title=dict(text="Year", font=dict(color="#0f172a", size=13)),
            tickfont=dict(color="#0f172a", size=12)
        ),
        yaxis=dict(
            title=dict(text="EUR (€)", font=dict(color="#0f172a", size=13)),
            tickfont=dict(color="#0f172a", size=12)
        )
    )
    fig_gdp_cap.update_layout(layout_gdp)
    st.plotly_chart(fig_gdp_cap, width="stretch")
    
    # METADATA & DOWNLOAD FOR ECONOMY
    col_meta3, col_dl3 = st.columns([3, 1])
    with col_meta3:
        with st.expander("ℹ️ Economic Standards & Sector Definitions"):
            st.markdown("""
            **Economic Provenance Notes:**
            * **Industrial Classification:** Grouped according to NACE Rev. 2 / TOL 2008 standard.
            * **CPI Base:** Consumer Price Index indexed to base year 2020 = 100.
            * **Maritime Sector:** Encompasses passenger ferries, cargo operations, and port infrastructure services.
            """)
    with col_dl3:
        csv_econ = df_sectors.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Export Sector Data (CSV)",
            data=csv_econ,
            file_name='asub_economic_sectors_2026.csv',
            mime='text/csv',
            help="Export employment sector share dataset"
        )
