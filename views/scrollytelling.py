import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from utils.plotly_theme import get_plotly_preset

def render_scrollytelling_tab(df_macro, df_muni, df_sectors):
    """Renders the 'Åland in Figures' Narrative Scrollytelling Interface."""
    
    st.markdown("""
    <div class="section-theme-banner" style="background: linear-gradient(135deg, #3b0764 0%, #6b21a8 100%);">
        📖 Section 8: 'Åland in Figures' Scrollytelling Story Mode
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background-color: #ffffff; border: 1.5px solid #cbd5e1; border-left: 6px solid #6b21a8; padding: 16px 20px; border-radius: 10px; margin-bottom: 20px;">
        <div style="color: #4c1d95; font-weight: 800; font-size: 1.05rem; margin-bottom: 6px;">
            📖 Interactive Narrative Storytelling ("Åland in Figures")
        </div>
        <div style="color: #334155; font-size: 0.95rem; line-height: 1.5;">
            Ditch static PDFs! Step through the interactive narrative of Åland's population, economy, green transition, and maritime identity. 
            The visual charts adapt dynamically as you progress through each chapter of the story.
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Story Chapter Navigation Stepper
    if "story_chapter" not in st.session_state:
        st.session_state["story_chapter"] = 1
        
    chap_col1, chap_col2, chap_col3, chap_col4 = st.columns(4)
    
    with chap_col1:
        if st.button("1️⃣ Chapter 1: Population", type="primary" if st.session_state["story_chapter"] == 1 else "secondary"):
            st.session_state["story_chapter"] = 1
            st.rerun()
            
    with chap_col2:
        if st.button("2️⃣ Chapter 2: Economy & GDP", type="primary" if st.session_state["story_chapter"] == 2 else "secondary"):
            st.session_state["story_chapter"] = 2
            st.rerun()
            
    with chap_col3:
        if st.button("3️⃣ Chapter 3: Green Transition", type="primary" if st.session_state["story_chapter"] == 3 else "story_chapter" == 3):
            st.session_state["story_chapter"] = 3
            st.rerun()
            
    with chap_col4:
        if st.button("4️⃣ Chapter 4: Maritime & Ferry", type="primary" if st.session_state["story_chapter"] == 4 else "secondary"):
            st.session_state["story_chapter"] = 4
            st.rerun()
            
    st.divider()
    
    curr_chapter = st.session_state["story_chapter"]
    col_text, col_visual = st.columns([1, 1])
    
    if curr_chapter == 1:
        with col_text:
            st.markdown("## 👥 Chapter 1: Reaching 30,952 Inhabitants")
            st.markdown("### *A Decade of Sustained Demographic Expansion*")
            
            st.markdown("""
            Over the past decade, the autonomous territory of **Åland** has achieved steady, resilient population expansion, growing from 28,983 residents in 2015 to an all-time high of **30,952 permanent residents** in 2026.
            
            Key regional drivers include:
            * **Jomala Suburban Boom:** Jomala recorded an average annual growth rate of **+1.8%**, expanding rapidly due to suburban residential development adjacent to Mariehamn.
            * **Capital Urban Hub:** Mariehamn remains the economic center, accommodating **38.3%** of all island inhabitants (11,850 residents).
            * **Archipelago Maritime Links:** Archipelago districts like Föglö and Brändö maintain essential ferry connections to sustain year-round community vitality.
            """)
            
            st.markdown("""
            <div style="background-color: #f0f9ff; border-left: 5px solid #0284c7; padding: 14px 18px; border-radius: 8px; font-weight: 700; color: #0369a1; margin-top: 16px;">
                💡 <strong>Key Takeaway:</strong> Net positive in-migration from Nordic neighbors continues to drive demographic resilience, compensating for natural population aging.
            </div>
            """, unsafe_allow_html=True)

        with col_visual:
            fig1 = px.area(df_macro, x="year", y="population", title="Demographic Growth Trajectory (2015-2026)", markers=True)
            fig1.update_traces(line_color="#004077", fillcolor="rgba(0, 64, 119, 0.15)")
            layout1 = get_plotly_preset()
            layout1.update(height=420)
            fig1.update_layout(layout1)
            st.plotly_chart(fig1, width="stretch")

    elif curr_chapter == 2:
        with col_text:
            st.markdown("## 💼 Chapter 2: The €1.62 Billion Economic Engine")
            st.markdown("### *High GDP per Capita & Robust Labor Market*")
            
            st.markdown("""
            Åland's economy displays extraordinary output relative to its population size, generating an annual Gross Domestic Product (GDP) of **€1.62 Billion** (€1,620M) in 2026.
            
            Economic pillars include:
            * **€52,330 GDP Per Capita:** Ranks among the highest living standards in the Nordic region.
            * **Maritime & Shipping Pillar:** Maritime logistics, passenger ferries, and shipping services generate over **22.4%** of total employment (3,250 direct jobs).
            * **Public Administration & Healthcare:** Accounting for **25.8%** of workforce employment, providing essential public services.
            """)
            
            st.markdown("""
            <div style="background-color: #fef3c7; border-left: 5px solid #d97706; padding: 14px 18px; border-radius: 8px; font-weight: 700; color: #92400e; margin-top: 16px;">
                ⚠️ <strong>Key Takeaway:</strong> Labor market unemployment has stabilized at 5.3% following post-pandemic recovery across international shipping channels.
            </div>
            """, unsafe_allow_html=True)

        with col_visual:
            fig2 = px.bar(df_sectors, x="employees", y="sector", orientation="h", color="share_pct", title="Employment Distribution Across Economic Sectors", color_continuous_scale="Blues")
            layout2 = get_plotly_preset()
            layout2.update(height=420)
            fig2.update_layout(layout2)
            st.plotly_chart(fig2, width="stretch")

    elif curr_chapter == 3:
        with col_text:
            st.markdown("## 🌱 Chapter 3: Leading the Nordic Green Transition")
            st.markdown("### *70.2% Renewable Energy Share Reached in 2026*")
            
            st.markdown("""
            Targeting climate neutrality, Åland has rapidly scaled up wind, solar, and bio-energy infrastructure over the last decade.
            
            Milestones achieved:
            * **70.2% Renewable Adoption:** Up from 38.2% in 2015, driven by offshore wind planning and solar micro-grids.
            * **Maritime Electrification:** Modernization of archipelago short-route ferries with electric and hybrid propulsion.
            * **Circular Economy:** Island-wide waste recycling initiatives achieving over 65% material recovery.
            """)
            
            st.markdown("""
            <div style="background-color: #dcfce7; border-left: 5px solid #16a34a; padding: 14px 18px; border-radius: 8px; font-weight: 700; color: #064e3b; margin-top: 16px;">
                ✅ <strong>Key Takeaway:</strong> Åland is positioned as a living laboratory for Nordic renewable energy adoption and maritime decarbonization.
            </div>
            """, unsafe_allow_html=True)

        with col_visual:
            fig3 = px.line(df_macro, x="year", y="renewable_energy_pct", title="Renewable Energy Share Growth (%)", markers=True)
            fig3.update_traces(line_color="#15803d", line_width=4)
            layout3 = get_plotly_preset()
            layout3.update(height=420)
            fig3.update_layout(layout3)
            st.plotly_chart(fig3, width="stretch")

    else: # Chapter 4
        with col_text:
            st.markdown("## 🚢 Chapter 4: Maritime Gateway & Archipelago Tourism")
            st.markdown("### *2.22 Million Ferry Passengers & Summer Peaks*")
            
            st.markdown("""
            As an island territory located in the Baltic Sea between Sweden and Finland, maritime transportation is Åland's lifethread.
            
            Key metrics:
            * **2.22 Million Ferry Passengers:** Annual passenger throughput across Stockholm, Mariehamn, Långnäs, and Turku routes.
            * **515,000 Tourist Guest Nights:** Tourism activity reaches its peak in July (145,000 guest nights), supporting local hospitality and commerce.
            * **Archipelago Lifelines:** Connecting 6 island municipalities via regional ferry networks.
            """)
            
            st.markdown("""
            <div style="background-color: #f3e8ff; border-left: 5px solid #9333ea; padding: 14px 18px; border-radius: 8px; font-weight: 700; color: #6b21a8; margin-top: 16px;">
                🌊 <strong>Key Takeaway:</strong> Maritime transit remains the lifeblood of the Åland economy, connecting culture, trade, and tourism.
            </div>
            """, unsafe_allow_html=True)

        with col_visual:
            fig4 = px.bar(df_macro, x="year", y="ferry_passengers_k", title="Annual Ferry Passengers (Thousands)", color="tourist_nights", color_continuous_scale="Viridis")
            layout4 = get_plotly_preset()
            layout4.update(height=420)
            fig4.update_layout(layout4)
            st.plotly_chart(fig4, width="stretch")

    # Stepper Control Footer
    st.divider()
    c_prev, c_space, c_next = st.columns([1, 2, 1])
    
    with c_prev:
        if curr_chapter > 1:
            if st.button("⬅️ Previous Chapter"):
                st.session_state["story_chapter"] -= 1
                st.rerun()
                
    with c_next:
        if curr_chapter < 4:
            if st.button("Next Chapter ➡️"):
                st.session_state["story_chapter"] += 1
                st.rerun()
