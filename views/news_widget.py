import streamlit as st
import streamlit.components.v1 as components
import plotly.express as px
import plotly.graph_objects as go
from utils.plotly_theme import get_plotly_preset

def render_news_widget_tab(df_macro, df_muni, df_sectors, df_tourism_monthly):
    """Renders the Embeddable News Widget Engine for Local Media (Ålandstidningen, Nya Åland)."""
    
    st.markdown("""
    <div class="section-theme-banner" style="background: linear-gradient(135deg, #0f172a 0%, #334155 100%);">
        📰 Section 7: Embeddable News Media Widget Generator
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background-color: #ffffff; border: 1.5px solid #cbd5e1; border-left: 6px solid #0f172a; padding: 16px 20px; border-radius: 10px; margin-bottom: 20px;">
        <div style="color: #0f172a; font-weight: 800; font-size: 1.05rem; margin-bottom: 6px;">
            🗞️ Live Interactive Embeds for Journalists & News Outlets
        </div>
        <div style="color: #334155; font-size: 0.95rem; line-height: 1.5;">
            Replace static screenshot tables in <strong>Ålandstidningen</strong>, <strong>Nya Åland</strong>, and <strong>Ålands Radio</strong> with live interactive ÅSUB charts. 
            Embedded charts update automatically when official statistical registries are revised.
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col_ctrl, col_prev = st.columns([1, 2])
    
    with col_ctrl:
        st.subheader("⚙️ Widget Configuration")
        
        selected_chart = st.selectbox(
            "Select Chart Dataset:",
            [
                "Macro Growth & GDP Trajectory",
                "Municipal Population Breakdown (16 Districts)",
                "Employment Share by Economic Sector",
                "Monthly Tourism Guest Nights Peak"
            ]
        )
        
        widget_theme = st.radio(
            "Color Theme Preset:",
            ["Official Blue (#004077)", "High-Contrast Slate", "Emerald Sustainable"],
            horizontal=False
        )
        
        widget_height = st.slider("Widget Height (px)", min_value=300, max_value=600, value=400, step=20)
        
        show_caption = st.checkbox("Include Official ÅSUB Attribution Caption", value=True)
        
        # Color mapping based on selected theme
        if "Official Blue" in widget_theme:
            primary_color = "#004077"
            accent_color = "#d97706"
        elif "High-Contrast" in widget_theme:
            primary_color = "#0f172a"
            accent_color = "#0284c7"
        else:
            primary_color = "#0f766e"
            accent_color = "#15803d"
            
        chart_key_map = {
            "Macro Growth & GDP Trajectory": "macro",
            "Municipal Population Breakdown (16 Districts)": "muni",
            "Employment Share by Economic Sector": "sectors",
            "Monthly Tourism Guest Nights Peak": "tourism"
        }
        chart_code = chart_key_map[selected_chart]
        
    with col_prev:
        st.subheader("👁️ Live News Article Preview")
        
        # Render mock newspaper article wrapper
        with st.container(border=True):
            st.markdown("""
            <div style="border-bottom: 2px solid #e2e8f0; padding-bottom: 8px; margin-bottom: 12px;">
                <span style="background-color: #e2e8f0; color: #334155; font-size: 0.75rem; font-weight: 800; padding: 3px 8px; border-radius: 4px;">LOCAL NEWS EMBED</span>
                <span style="color: #64748b; font-size: 0.8rem; margin-left: 8px;">Ålandstidningen • Live Data Stream</span>
            </div>
            """, unsafe_allow_html=True)
            
            # Generate the chart based on selection
            if chart_code == "macro":
                fig = px.line(df_macro, x="year", y="population", title="Åland Total Population Trajectory (2015-2026)")
                fig.update_traces(line_color=primary_color, line_width=4)
            elif chart_code == "muni":
                fig = px.bar(df_muni.sort_values("population", ascending=True), x="population", y="municipality", orientation="h", title="Inhabitants Across 16 Municipalities")
                fig.update_traces(marker_color=primary_color)
            elif chart_code == "sectors":
                fig = px.pie(df_sectors, values="employees", names="sector", title="Employment Distribution by Sector", hole=0.4)
                fig.update_traces(marker_colors=[primary_color, accent_color, "#0284c7", "#16a34a", "#9333ea", "#ea580c", "#475569"])
            else:
                fig = px.bar(df_tourism_monthly, x="month", y="guest_nights", title="Monthly Tourist Guest Nights Peak")
                fig.update_traces(marker_color=primary_color)
                
            layout = get_plotly_preset()
            layout.update(
                height=widget_height - 60,
                margin=dict(l=10, r=10, t=35, b=10)
            )
            fig.update_layout(layout)
            st.plotly_chart(fig, width="stretch", config={'displayModeBar': False})
            
            if show_caption:
                st.caption("Source: Ålands statistik- och utredningsbyrå (ÅSUB) Live PX-Web API • Verified Official Data")

    st.divider()
    
    # EMBED CODE GENERATION SECTION
    st.subheader("📋 Embed Code for News CMS (Wordpress, Drupal, Custom)")
    
    base_embed_url = f"https://asub-project-showcase.streamlit.app/?embed=1&chart={chart_code}&theme={urllib.parse.quote(widget_theme)}"
    iframe_code = f'<iframe src="{base_embed_url}" width="100%" height="{widget_height}" frameborder="0" style="border: 1.5px solid #cbd5e1; border-radius: 12px; box-shadow: 0 4px 12px rgba(15,23,42,0.06);" title="ÅSUB Live Data Widget"></iframe>'
    script_embed_code = f'<!-- ÅSUB Live Data Widget -->\n{iframe_code}\n<script src="https://asub-project-showcase.streamlit.app/widget.js" async></script>'

    st.code(iframe_code, language="html")
    
    if st.button("🔗 Copy Embed Code to Clipboard"):
        js_copy_embed = f"""
        <script>
            if (navigator.clipboard) {{
                navigator.clipboard.writeText({repr(iframe_code)});
            }}
        </script>
        """
        components.html(js_copy_embed, height=0, width=0)
        st.toast("📋 News Iframe embed code copied to clipboard!", icon="📰")
        st.success("Embed HTML code ready! Paste directly into your newspaper CMS or HTML body.")
