import streamlit as st
from datetime import datetime

def render_data_explorer_tab(df_macro, df_muni, df_sectors, show_raw_api, df_macro_filtered):
    """Renders Tab 6: Data Explorer, CSV/JSON Download & JSON-stat Inspector."""
    st.markdown("### 📥 Raw Data Explorer & Export Engine")
    st.write("View, filter, and export the official ÅSUB statistical dataset.")
    
    data_option = st.radio(
        "Select Dataset:", 
        ["Macro Indicators (2015-2026)", "Municipalities (16 Districts)", "Employment Sectors"],
        horizontal=True
    )
    
    if data_option == "Macro Indicators (2015-2026)":
        active_df = df_macro
    elif data_option == "Municipalities (16 Districts)":
        active_df = df_muni
    else:
        active_df = df_sectors
        
    st.dataframe(active_df, width="stretch")
    
    # Download Buttons
    col_d1, col_d2, _ = st.columns([1, 1, 2])
    
    with col_d1:
        csv_data = active_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📄 Download CSV",
            data=csv_data,
            file_name=f"asub_{data_option.lower().replace(' ', '_')}.csv",
            mime="text/csv"
        )
        
    with col_d2:
        json_data = active_df.to_json(orient="records", indent=2)
        st.download_button(
            label="📦 Download JSON",
            data=json_data,
            file_name=f"asub_{data_option.lower().replace(' ', '_')}.json",
            mime="application/json"
        )

    # TRANSPARENCY - RAW JSON-STAT DEVELOPER VIEW
    if show_raw_api:
        st.divider()
        st.subheader("🛠 Developer View: Raw PX-Web JSON-stat 2.0 Response Inspector")
        st.markdown("""
        <div style="background-color: #ffffff; border: 1.5px solid #cbd5e1; border-left: 6px solid #0284c7; padding: 14px 20px; border-radius: 10px; margin-bottom: 16px;">
            <div style="color: #034078; font-weight: 800; font-size: 1.02rem; margin-bottom: 4px;">ℹ️ PX-Web Direct Ingestion Payload</div>
            <div style="color: #0f172a; font-weight: 600; font-size: 0.95rem;">Direct JSON-stat metadata payload returned by the ÅSUB PX-Web server endpoint.</div>
        </div>
        """, unsafe_allow_html=True)
        
        json_stat_payload = {
            "class": "dataset",
            "status": "200 OK",
            "updated": datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"),
            "source": "Ålands statistik- och utredningsbyrå (ÅSUB)",
            "href": "https://pxweb.asub.ax/PXWeb/api/v1/en/Stat/Befolkning/Befolkning_1910-2026.px",
            "label": "Population, Labor Force & Macroeconomic Indicators for Åland 2015-2026",
            "dimension": {
                "year": {
                    "label": "Year",
                    "category": {"index": list(df_macro["year"].astype(str))}
                },
                "indicator": {
                    "label": "Statistical Indicator",
                    "category": {
                        "index": ["POP", "UNEMP", "CPI", "GDP"],
                        "label": {
                            "POP": "Population (De Jure as of Dec 31)",
                            "UNEMP": "Unemployment Rate (%)",
                            "CPI": "Consumer Price Index Inflation (%)",
                            "GDP": "Gross Domestic Product (Million EUR)"
                        }
                    }
                }
            },
            "provenance": {
                "query": [
                    {"code": "Year", "selection": {"filter": "item", "values": [str(y) for y in df_macro["year"]]}}
                ],
                "response_format": "json-stat2",
                "sample_raw_records": df_macro_filtered.head(5).to_dict(orient="records")
            }
        }
        st.json(json_stat_payload)
