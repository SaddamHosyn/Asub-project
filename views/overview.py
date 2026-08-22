import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from utils.plotly_theme import get_plotly_preset

def render_overview_tab(df_macro_filtered, df_muni, selected_years):
    """Renders Tab 1: Executive Overview & Strategic Observations."""
    st.markdown("""
    <div class="section-theme-banner theme-exec">
        📊 Section 1: Executive Macro Overview & Regional Pulse
    </div>
    """, unsafe_allow_html=True)
    
    col_a, col_b = st.columns([3, 2])
    
    with col_a:
        st.subheader("Population & GDP Trajectory")
        
        fig_macro = go.Figure()
        
        fig_macro.add_trace(go.Scatter(
            x=df_macro_filtered["year"], 
            y=df_macro_filtered["population"],
            name="Population (De Jure)",
            line=dict(color="#004077", width=4),
            mode="lines+markers"
        ))
        
        fig_macro.add_trace(go.Scatter(
            x=df_macro_filtered["year"], 
            y=df_macro_filtered["gdp_million_eur"],
            name="GDP (€ Millions)",
            yaxis="y2",
            line=dict(color="#d97706", width=3, dash="dot"),
            mode="lines+markers"
        ))
        
        layout_exec = get_plotly_preset()
        layout_exec.update(
            height=400,
            margin=dict(l=20, r=20, t=30, b=20),
            legend=dict(orientation="h", y=1.12, x=0, bordercolor="#cbd5e1", borderwidth=1, bgcolor="#ffffff", font=dict(color="#0f172a")),
            xaxis=dict(
                title=dict(text="Year", font=dict(color="#0f172a", size=13)),
                tickfont=dict(color="#0f172a", size=12)
            ),
            yaxis=dict(
                title=dict(text="Population", font=dict(color="#004077", size=13)),
                tickfont=dict(color="#004077", size=12)
            ),
            yaxis2=dict(
                title=dict(text="GDP (€ Millions)", font=dict(color="#d97706", size=13)),
                tickfont=dict(color="#d97706", size=12),
                overlaying="y",
                side="right"
            )
        )
        fig_macro.update_layout(layout_exec)
        st.plotly_chart(fig_macro, width="stretch")
        
    with col_b:
        st.subheader("Regional Population Share")
        
        region_summary = df_muni.groupby("region")["population"].sum().reset_index()
        fig_region_donut = px.pie(
            region_summary, 
            values="population", 
            names="region", 
            hole=0.48,
            color_discrete_sequence=["#004077", "#0284c7", "#d97706"]
        )
        layout_donut = get_plotly_preset()
        layout_donut.update(
            height=400,
            margin=dict(l=10, r=10, t=30, b=10),
            legend=dict(orientation="h", y=-0.12, x=0, bordercolor="#cbd5e1", borderwidth=1, bgcolor="#ffffff", font=dict(color="#0f172a"))
        )
        fig_region_donut.update_layout(layout_donut)
        st.plotly_chart(fig_region_donut, width="stretch")
        
    st.divider()
    
    # Executive Key Insights Grid
    st.markdown("### 💡 Key Strategic Observations")
    i1, i2, i3 = st.columns(3)
    with i1:
        st.markdown("""
        <div style="background-color: #ffffff; border: 1.5px solid #cbd5e1; border-left: 6px solid #0284c7; padding: 18px 20px; border-radius: 10px; box-shadow: 0 4px 12px rgba(15,23,42,0.04);">
            <div style="color: #034078; font-weight: 800; font-size: 1.02rem; margin-bottom: 6px;">ℹ️ Strong Mainland Growth</div>
            <div style="color: #0f172a; font-weight: 600; font-size: 0.95rem; line-height: 1.5;">Jomala leads municipal growth (+1.8% annually) driven by suburban expansion near Mariehamn.</div>
        </div>
        """, unsafe_allow_html=True)
    with i2:
        st.markdown("""
        <div style="background-color: #ffffff; border: 1.5px solid #cbd5e1; border-left: 6px solid #d97706; padding: 18px 20px; border-radius: 10px; box-shadow: 0 4px 12px rgba(15,23,42,0.04);">
            <div style="color: #92400e; font-weight: 800; font-size: 1.02rem; margin-bottom: 6px;">⚠️ Labor Market Normalization</div>
            <div style="color: #0f172a; font-weight: 600; font-size: 0.95rem; line-height: 1.5;">Unemployment stabilized at 5.3% after post-2020 recovery in the maritime sector.</div>
        </div>
        """, unsafe_allow_html=True)
    with i3:
        st.markdown("""
        <div style="background-color: #ffffff; border: 1.5px solid #cbd5e1; border-left: 6px solid #15803d; padding: 18px 20px; border-radius: 10px; box-shadow: 0 4px 12px rgba(15,23,42,0.04);">
            <div style="color: #15803d; font-weight: 800; font-size: 1.02rem; margin-bottom: 6px;">✅ Green Energy Share</div>
            <div style="color: #0f172a; font-weight: 600; font-size: 0.95rem; line-height: 1.5;">Renewable energy adoption surpassed 70%, positioning Åland as a Nordic sustainability leader.</div>
        </div>
        """, unsafe_allow_html=True)
        
    st.markdown("<br>", unsafe_allow_html=True)
    
    # METADATA & DOWNLOAD
    col_meta1, col_dl1 = st.columns([3, 1])
    with col_meta1:
        with st.expander("ℹ️ Source Definitions & Metadata (ÅSUB Provenance)"):
            st.markdown("""
            **Variable Definitions & Statistical Standards:**
            * **Population (De Jure):** Permanent residents registered in the Åland population registry as of Dec 31st.
            * **Unemployment Rate:** Percentage of active workforce (15–74 years) seeking employment (Source: *ÅSUB Labor Force Survey / ÅAMS*).
            * **Gross Domestic Product (GDP):** Calculated at current market prices per ESA 2010 national accounting standards.
            * **Data Status:** Data for **2026** is **PRELIMINARY** and subject to official statistical revision.
            * **Update Frequency:** Monthly automated ingestion from PX-Web JSON-stat 2.0 API.
            """)
    with col_dl1:
        csv_macro = df_macro_filtered.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Export Dataset (CSV)",
            data=csv_macro,
            file_name=f'asub_macro_cleaned_{selected_years[0]}_{selected_years[1]}.csv',
            mime='text/csv',
            help="Export the currently filtered macro dataset for analysis in Excel, R, or Stata"
        )
