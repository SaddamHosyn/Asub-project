import streamlit as st
import streamlit.components.v1 as components
import plotly.express as px
import urllib.parse

def render_social_share_preview(df):
    """Renders the Social Media Share Preview card expander component with real dynamic links."""
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

    # Base App URL for sharing
    base_url = "https://asub-project-showcase.streamlit.app"
    params = {
        "metric": "population",
        "pop": str(latest_pop),
        "growth": growth_rate,
        "year": str(latest_year)
    }
    encoded_params = urllib.parse.urlencode(params)
    dynamic_share_url = f"{base_url}/?{encoded_params}"

    # Auto expand if loaded via a share link
    is_shared = any(k in st.query_params for k in ["metric", "pop", "share"])

    with st.expander("🚀 Social Media Share Preview", expanded=is_shared):
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
                
        # Action button to copy real dynamic link
        if st.button("🔗 Copy Link with Dynamic Preview"):
            # Set Streamlit query params in URL
            st.query_params["metric"] = "population"
            st.query_params["pop"] = str(latest_pop)
            st.query_params["year"] = str(latest_year)
            
            # JS Clipboard write
            js_copy = f"""
            <script>
                if (navigator.clipboard) {{
                    navigator.clipboard.writeText("{dynamic_share_url}");
                }}
            </script>
            """
            components.html(js_copy, height=0, width=0)
            
            st.toast("🔗 Dynamic share link copied to clipboard!", icon="📋")
            st.markdown(f"""
            <div style="background-color: #dcfce7; border: 1.5px solid #16a34a; padding: 12px 18px; border-radius: 10px; font-size: 0.95rem; margin-top: 12px; margin-bottom: 12px;">
                <span style="color: #064e3b; font-weight: 800;">✅ Share Link Ready:</span> 
                <a href="{dynamic_share_url}" target="_blank" style="color: #004077 !important; font-weight: 800; text-decoration: underline !important; word-break: break-all; margin-left: 6px;">
                    {dynamic_share_url}
                </a>
            </div>
            """, unsafe_allow_html=True)
            st.code(dynamic_share_url, language="text")
