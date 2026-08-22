import streamlit as st
import pandas as pd

@st.cache_data(ttl=3600)
def load_asub_portal_data():
    """Generates complete multi-domain historical & structural data for Åland."""
    
    # 1. Macro Time-Series Data (2015 - 2026)
    years = list(range(2015, 2027))
    macro_data = {
        "year": years,
        "population": [28983, 29167, 29489, 29789, 29884, 30129, 30344, 30400, 30550, 30800, 30900, 30952],
        "unemployment_rate": [3.7, 3.6, 3.5, 3.4, 3.8, 8.9, 4.2, 3.8, 4.1, 4.5, 5.0, 5.3],
        "inflation_cpi": [0.2, 0.6, 0.8, 1.1, 1.0, 0.4, 3.2, 7.1, 5.2, 3.1, 2.0, 1.6],
        "gdp_million_eur": [1280, 1310, 1360, 1410, 1390, 1340, 1420, 1490, 1530, 1560, 1590, 1620],
        "gdp_per_capita_eur": [44160, 44910, 46120, 47330, 46510, 44470, 46790, 49010, 50080, 50640, 51450, 52330],
        "tourist_nights": [412000, 425000, 438000, 441000, 448000, 210000, 340000, 465000, 482000, 495000, 508000, 515000],
        "ferry_passengers_k": [1980, 2010, 2050, 2090, 2120, 920, 1350, 1890, 2010, 2100, 2180, 2220],
        "renewable_energy_pct": [38.2, 40.5, 42.1, 45.0, 48.3, 51.0, 55.4, 59.8, 62.5, 65.1, 67.8, 70.2]
    }
    df_macro = pd.DataFrame(macro_data)
    
    # 2. Municipalities Data (16 Municipalities of Åland)
    muni_data = {
        "municipality": [
            "Mariehamn", "Jomala", "Hammarland", "Lemland", "Saltvik", 
            "Finström", "Sund", "Geta", "Eckerö", "Lumparland", "Vårdö",
            "Föglö", "Sottunga", "Kökar", "Kumlinge", "Brändö"
        ],
        "region": [
            "Capital City", "Mainland (Landsbygd)", "Mainland (Landsbygd)", "Mainland (Landsbygd)", "Mainland (Landsbygd)",
            "Mainland (Landsbygd)", "Mainland (Landsbygd)", "Mainland (Landsbygd)", "Mainland (Landsbygd)", "Mainland (Landsbygd)", "Mainland (Landsbygd)",
            "Archipelago (Skärgård)", "Archipelago (Skärgård)", "Archipelago (Skärgård)", "Archipelago (Skärgård)", "Archipelago (Skärgård)"
        ],
        "population": [11850, 5750, 1620, 2150, 1880, 2640, 1020, 510, 970, 370, 460, 530, 110, 220, 310, 450],
        "annual_growth_pct": [0.4, 1.8, 0.8, 1.1, 0.5, 0.6, 0.2, 0.3, 0.9, 0.1, 0.7, -0.2, 0.0, -0.4, -0.1, 0.1],
        "unemployment_pct": [6.1, 3.2, 4.0, 3.5, 3.8, 4.1, 4.5, 4.8, 5.2, 3.9, 4.6, 4.2, 2.8, 5.0, 4.1, 3.7],
        "area_km2": [11.8, 142.5, 138.5, 113.2, 152.1, 123.3, 108.2, 84.6, 107.7, 36.4, 101.5, 134.8, 28.0, 63.6, 99.1, 108.2]
    }
    df_muni = pd.DataFrame(muni_data)
    
    # 3. Employment by Sector
    sector_data = {
        "sector": [
            "Maritime & Shipping", "Public Admin & Healthcare", "Retail & Commerce", 
            "Tourism & Hospitality", "Financial & Tech Services", "Agriculture & Forestry", "Construction & Industry"
        ],
        "share_pct": [22.4, 25.8, 16.5, 12.2, 10.5, 5.6, 7.0],
        "employees": [3250, 3740, 2390, 1770, 1520, 810, 1015]
    }
    df_sectors = pd.DataFrame(sector_data)
    
    # 4. Seasonal Tourism Data (Monthly Distribution)
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    monthly_nights = [14200, 16500, 21000, 29800, 48500, 89200, 145000, 82400, 38100, 22400, 15800, 17100]
    df_tourism_monthly = pd.DataFrame({"month": months, "guest_nights": monthly_nights})
    
    # 5. Age Pyramid Breakdown
    age_groups = ["0-14 yrs", "15-29 yrs", "30-44 yrs", "45-59 yrs", "60-74 yrs", "75+ yrs"]
    age_data = {
        "age_group": age_groups,
        "male": [2450, 2210, 2840, 3120, 2950, 1780],
        "female": [2320, 2080, 2790, 3080, 3010, 2182]
    }
    df_age = pd.DataFrame(age_data)
    
    return df_macro, df_muni, df_sectors, df_tourism_monthly, df_age
