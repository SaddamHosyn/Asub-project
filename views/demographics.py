import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from utils.plotly_theme import get_plotly_preset

def render_demographics_tab(df_muni_filtered, df_muni, df_age):
    """Renders Tab 2: Demographics, Age Pyramids & 16 Municipal Districts."""
    st.markdown("""
    <div class="section-theme-banner theme-demo">
        👥 Section 2: Demographics, Age Pyramids & 16 Municipal Districts
    </div>
    """, unsafe_allow_html=True)
    
    c_m1, c_m2 = st.columns([3, 2])
    
    with c_m1:
        st.subheader("Population Across Municipalities")
        fig_muni_bar = px.bar(
            df_muni_filtered.sort_values("population", ascending=True),
            x="population",
            y="municipality",
            color="region",
            orientation="h",
            text="population",
            color_discrete_map={
                "Capital City": "#004077",
                "Mainland (Landsbygd)": "#0284c7",
                "Archipelago (Skärgård)": "#d97706"
            }
        )
        layout_muni = get_plotly_preset()
        layout_muni.update(
            height=460,
            margin=dict(l=10, r=10, t=20, b=20),
            xaxis=dict(
                title=dict(text="Inhabitants", font=dict(color="#0f172a", size=13)),
                tickfont=dict(color="#0f172a", size=12)
            ),
            yaxis=dict(
                title="",
                tickfont=dict(color="#0f172a", size=12)
            ),
            legend=dict(bordercolor="#cbd5e1", borderwidth=1, bgcolor="#ffffff", font=dict(color="#0f172a"))
        )
        fig_muni_bar.update_layout(layout_muni)
        st.plotly_chart(fig_muni_bar, width="stretch")
        
    with c_m2:
        st.subheader("Population Pyramid (Gender & Age)")
        fig_pyramid = go.Figure()
        
        fig_pyramid.add_trace(go.Bar(
            y=df_age["age_group"],
            x=-df_age["male"],
            name="Male Residents",
            orientation="h",
            marker_color="#004077"
        ))
        
        fig_pyramid.add_trace(go.Bar(
            y=df_age["age_group"],
            x=df_age["female"],
            name="Female Residents",
            orientation="h",
            marker_color="#d97706"
        ))
        
        layout_pyr = get_plotly_preset()
        layout_pyr.update(
            barmode="relative",
            bargap=0.12,
            height=460,
            margin=dict(l=10, r=10, t=20, b=20),
            legend=dict(bordercolor="#cbd5e1", borderwidth=1, bgcolor="#ffffff", orientation="h", y=1.12, font=dict(color="#0f172a")),
            xaxis=dict(
                tickvals=[-3000, -2000, -1000, 0, 1000, 2000, 3000],
                ticktext=["3k", "2k", "1k", "0", "1k", "2k", "3k"],
                tickfont=dict(color="#0f172a", size=12),
                title=dict(text="Population Count", font=dict(color="#0f172a", size=13))
            ),
            yaxis=dict(
                tickfont=dict(color="#0f172a", size=12)
            )
        )
        fig_pyramid.update_layout(layout_pyr)
        st.plotly_chart(fig_pyramid, width="stretch")
        
    st.divider()
    
    # Growth vs Unemployment Matrix
    st.subheader("Municipal Growth vs. Unemployment Rate Matrix")
    fig_scatter = px.scatter(
        df_muni,
        x="unemployment_pct",
        y="annual_growth_pct",
        size="population",
        color="region",
        hover_name="municipality",
        text="municipality",
        size_max=45,
        color_discrete_map={
            "Capital City": "#004077",
            "Mainland (Landsbygd)": "#0284c7",
            "Archipelago (Skärgård)": "#d97706"
        }
    )
    fig_scatter.update_traces(textposition="top center")
    layout_scat = get_plotly_preset()
    layout_scat.update(
        height=400,
        xaxis=dict(
            title=dict(text="Unemployment Rate (%)", font=dict(color="#0f172a", size=13)),
            tickfont=dict(color="#0f172a", size=12)
        ),
        yaxis=dict(
            title=dict(text="Annual Population Growth Rate (%)", font=dict(color="#0f172a", size=13)),
            tickfont=dict(color="#0f172a", size=12)
        ),
        legend=dict(bordercolor="#cbd5e1", borderwidth=1, bgcolor="#ffffff", font=dict(color="#0f172a"))
    )
    fig_scatter.update_layout(layout_scat)
    st.plotly_chart(fig_scatter, width="stretch")
    
    # METADATA & DOWNLOAD FOR DEMOGRAPHICS
    col_meta2, col_dl2 = st.columns([3, 1])
    with col_meta2:
        with st.expander("ℹ️ Municipal Definitions & Regional Classifications"):
            st.markdown("""
            **Municipal Provenance & Boundary Classifications:**
            * **Capital City:** Mariehamn urban district.
            * **Mainland (Landsbygd):** 9 contiguous municipalities on main island Åland.
            * **Archipelago (Skärgård):** 6 island districts accessible via maritime ferry connections (Brändö, Föglö, Kumlinge, Kökar, Sottunga, Vårdö).
            * **Growth Calculation:** Compound Annual Population Growth Rate over 5 consecutive registry reporting cycles.
            """)
    with col_dl2:
        csv_muni = df_muni_filtered.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Export Municipal Data (CSV)",
            data=csv_muni,
            file_name='asub_municipalities_2026.csv',
            mime='text/csv',
            help="Export municipal breakdown dataset for R/Excel"
        )
