def get_plotly_preset():
    """Returns common high-contrast layout dictionary for Plotly figures."""
    return dict(
        template="plotly_white",
        font=dict(family="Inter", color="#0f172a", size=13),
        paper_bgcolor="#ffffff",
        plot_bgcolor="#ffffff",
        hoverlabel=dict(bgcolor="#0f172a", font_size=13, font_family="Inter", font_color="#ffffff"),
        xaxis=dict(
            tickfont=dict(color="#0f172a", size=12, family="Inter"),
            title=dict(font=dict(color="#0f172a", size=13, family="Inter")),
            gridcolor="#e2e8f0",
            zerolinecolor="#cbd5e1"
        ),
        yaxis=dict(
            tickfont=dict(color="#0f172a", size=12, family="Inter"),
            title=dict(font=dict(color="#0f172a", size=13, family="Inter")),
            gridcolor="#e2e8f0",
            zerolinecolor="#cbd5e1"
        ),
        legend=dict(
            bordercolor="#cbd5e1",
            borderwidth=1,
            bgcolor="#ffffff",
            font=dict(color="#0f172a", size=12, family="Inter"),
            title=dict(font=dict(color="#0f172a", size=12, family="Inter"))
        )
    )
