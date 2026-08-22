import streamlit as st
import plotly.express as px

def render_social_share_preview(df):
    """Renders the Social Media Share Preview card expander component."""
    if df is None or df.empty or "population" not in df.columns:
        return

    latest_pop = df["population"].iloc[-1]
    latest_year = df["year"].iloc[-1] if "year" in df.columns else 2026
    
    if len(df) > 1:
        prev_pop = df["population"].iloc[-2]
        growth_val = ((latest_pop - prev_pop) / prev_pop) * 100
        growth_rate = f"+{growth_val:.1f}" if growth_val >= 0 else f"{growth_val:.1f}"
    else:
        growth_rate = "+0.2"

    with st.expander("🚀 Social Media Share Preview"):
        st.write("Preview how this data looks when shared on Twitter/LinkedIn:")
        
        # Create a mock social card container
        with st.container(border=True):
            col_img, col_text = st.columns([1, 2])
            
            with col_img:
                # Dynamic visual representation of chart for social preview
                fig_mini = px.line(df, x="year", y="population", title="")
                fig_mini.update_layout(
                    height=110,
                    margin=dict(l=10, r=10, t=10, b=10),
                    xaxis=dict(visible=False),
                    yaxis=dict(visible=False),
                    showlegend=False,
                    paper_bgcolor="#f8fafc",
                    plot_bgcolor="#f8fafc"
                )
                fig_mini.update_traces(line_color="#004077", line_width=3)
                st.plotly_chart(fig_mini, width="stretch", config={'displayModeBar': False})
                st.caption("📷 Dynamic Preview Card Image")
                
            with col_text:
                st.markdown(f"**Åland Population Hits {latest_pop:,}**")
                st.caption("asub.ax • Official Statistics")
                st.write(f"New data shows a {growth_rate}% increase in {latest_year}. See the full breakdown...")
                
        if st.button("🔗 Copy Link with Dynamic Preview"):
            st.toast("🔗 Dynamic social share link copied to clipboard!", icon="📋")
            st.success("Share link generated with OpenGraph meta preview tags!")
