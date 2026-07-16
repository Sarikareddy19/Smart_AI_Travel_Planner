from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from xml.sax.saxutils import escape
styles = getSampleStyleSheet()  

title_style = styles["Heading1"]
title_style.alignment = TA_CENTER
title_style.textColor = HexColor("#1565C0")
title_style.spaceAfter = 20

heading_style = styles["Heading2"]
heading_style.textColor = HexColor("#0D47A1")
heading_style.spaceBefore = 15
heading_style.spaceAfter = 8

normal_style = styles["BodyText"]
normal_style.leading = 18
normal_style.spaceAfter = 6
def generate_pdf(
    destination,
    hotels,
    weather,
    budget,
    food,
    itinerary,
    attractions,
    packing
):
    pdf_file = "travel_report.pdf"

    doc = SimpleDocTemplate(
        pdf_file,
        pagesize=A4
    )

    story = []
    story.append(
        Paragraph(
            "🌍 Smart AI Travel Planner",
            title_style
        )
    )

    story.append(
        Paragraph(
            "Professional Travel Report",
            heading_style
        )
    )

    story.append(
        Spacer(1,0.3*inch)
    )
    story.append(
        Paragraph(
            f"<b>Destination:</b> {destination}",
            normal_style
        )
    )

    story.append(
        Spacer(1,0.2*inch)
    )
        # ==========================================================
    # HOTEL RECOMMENDATIONS
    # ==========================================================

    story.append(
        Paragraph(
            "🏨 Hotel Recommendations",
            heading_style
        )
    )

    story.append(
        Paragraph(
    escape(hotels).replace("\n", "<br/>"),
    normal_style
)
    )

    story.append(
        Spacer(1,0.2*inch)
    )
        # ==========================================================
    # WEATHER
    # ==========================================================

    story.append(
        Paragraph(
            "🌦 Weather Information",
            heading_style
        )
    )

    story.append(
        Paragraph(
            escape(weather).replace("\n", "<br/>"),
            normal_style
        )
    )

    story.append(
        Spacer(1,0.2*inch)
    )
    # ==========================================================
    # BUDGET
    # ==========================================================

    story.append(
        Paragraph(
            "💰 Estimated Budget",
            heading_style
        )
    )

    budget_table = Table(
        [
            ["Budget Details"],
            [budget]
        ],
        colWidths=[450]
    )

    budget_table.setStyle(
        TableStyle(
            [
                ("BACKGROUND",(0,0),(-1,0),HexColor("#1565C0")),
                ("TEXTCOLOR",(0,0),(-1,0),colors.white),
                ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),
                ("FONTSIZE",(0,0),(-1,0),14),
                ("BOTTOMPADDING",(0,0),(-1,0),10),
                ("GRID",(0,0),(-1,-1),1,colors.grey),
                ("BACKGROUND",(0,1),(-1,-1),colors.whitesmoke),
                ("LEFTPADDING",(0,0),(-1,-1),12),
                ("RIGHTPADDING",(0,0),(-1,-1),12),
            ]
        )
    )

    story.append(budget_table)

    story.append(
        Spacer(1,0.3*inch)
    )

    story.append(
        Spacer(1,0.3*inch)
    )
        # ==========================================================
    # FOOD & RESTAURANTS
    # ==========================================================

    story.append(
        Paragraph(
            "🍴 Food & Restaurants",
            heading_style
        )
    )

    story.append(
        Paragraph(
            escape(food).replace("\n", "<br/>"),
            normal_style
        )
    )

    story.append(
        Spacer(1, 0.2 * inch)
    )
        # ==========================================================
    # DAY-WISE ITINERARY
    # ==========================================================

    story.append(
        Paragraph(
            "📅 Complete Day-wise Itinerary",
            heading_style
        )
    )

    story.append(
        Paragraph(
            escape(itinerary).replace("\n", "<br/>"),
            normal_style
        )
    )

    story.append(
        Spacer(1, 0.2 * inch)
    )
    # ==========================================================
    # TOP ATTRACTIONS
    # ==========================================================

    story.append(
        Paragraph(
            "🏖 Top Attractions",
            heading_style
        )
    )

    story.append(
        Paragraph(
            escape(attractions).replace("\n", "<br/>"),
            normal_style
        )
    )

    story.append(
        Spacer(1, 0.2 * inch)
    )
    # ==========================================================
    # PACKING CHECKLIST
    # ==========================================================

    story.append(
        Paragraph(
            "🎒 Packing Checklist",
            heading_style
        )
    )

    story.append(
        Paragraph(
            escape(packing).replace("\n", "<br/>"),
            normal_style
        )
    )

    story.append(
        Spacer(1, 0.3 * inch)
    )
    story.append(
        Paragraph(
            "<br/><br/><b>Generated by Smart AI Travel Planner</b>",
            title_style
        )
    )

    story.append(
        Paragraph(
            "Powered by Cohere AI | Python | Gradio",
            normal_style
        )
    )
    doc.build(story)

    return pdf_file

