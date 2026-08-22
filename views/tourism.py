import streamlit as st
import plotly.express as px
from utils.plotly_theme import get_plotly_preset

def render_tourism_tab(df_macro_filtered, df_tourism_monthly):
    """Renders Tab 4: Tourism Guest Nights & Maritime Transport Logistics."""
    st.markdown("""
    <div class="section-theme-banner theme-tour">
        🚢 Section 4: Tourism Guest Nights & Maritime Passenger Logistics
    </div>
    """, unsafe_allow_html=True)
    
    t1, t2 = st.columns(2)
    
    with t1:
        st.subheader("Monthly Seasonality (Guest Nights)")
        fig_monthly = px.bar(
            df_tourism_monthly,
            x="month",
            y="guest_nights",
            text="guest_nights",
            color="guest_nights",
            color_continuous_scale="Teal"
        )
        layout_month = get_plotly_preset()
        layout_month.update(
            height=380,
            xaxis=dict(
                title=dict(text="Month", font=dict(color="#0f172a", size=13)),
                tickfont=dict(color="#0f172a", size=12)
            ),
            yaxis=dict(
                title=dict(text="Overnight Stays", font=dict(color="#0f172a", size=13)),
                tickfont=dict(color="#0f172a", size=12)
            ),
            coloraxis_showscale=False
        )
        fig_monthly.update_layout(layout_month)
        st.plotly_chart(fig_monthly, width="stretch")
        
    with t2:
        st.subheader("Ferry Passenger Traffic Volume (Thousands)")
        fig_ferry = px.line(
            df_macro_filtered,
            x="year",
            y="ferry_passengers_k",
            markers=True,
            color_discrete_sequence=["#0f766e"]
        )
        layout_ferry = get_plotly_preset()
        layout_ferry.update(
            height=380,
            xaxis=dict(
                title=dict(text="Year", font=dict(color="#0f172a", size=13)),
                tickfont=dict(color="#0f172a", size=12)
            ),
            yaxis=dict(
                title=dict(text="Passengers (Thousands)", font=dict(color="#0f172a", size=13)),
                tickfont=dict(color="#0f172a", size=12)
            )
        )
        fig_ferry.update_layout(layout_ferry)
        st.plotly_chart(fig_ferry, width="stretch")
        
    # METADATA & DOWNLOAD FOR TOURISM
    col_meta4, col_dl4 = st.columns([3, 1])
    with col_meta4:
        with st.expander("ℹ️ Accommodation & Transport Provenance"):
            st.markdown("""
            **Tourism Survey Scope:**
            * **Overnight Stays:** Commercial accommodations (hotels, guest harbors, holiday villages) with capacity ≥ 10 beds.
            * **Ferry Passengers:** Disembarking/embarking passenger totals at Åland ports (Mariehamn, Långnäs, Eckerö).
            """)
    with col_dl4:
        csv_tourism = df_tourism_monthly.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Export Tourism Data (CSV)",
            data=csv_tourism,
            file_name='asub_tourism_seasonality.csv',
            mime='text/csv',
            help="Export monthly tourism dataset"
        )
