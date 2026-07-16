import gradio as gr


def create_dashboard_page():

    with gr.Column(
        visible=False,
        elem_id="dashboard-page"
    ) as dashboard_page:

        gr.HTML("""

<style>

/* ===========================
   PAGE
=========================== */

body{
    background:#eef3fb;
    font-family:Segoe UI,Arial,sans-serif;
}

#dashboard-page{

    background:#eef3fb;

    padding:25px;

}


/* ===========================
   HEADER
=========================== */

.main-header{

background:linear-gradient(135deg,#1565C0,#0D47A1);

padding:35px;

border-radius:22px;

box-shadow:0 12px 30px rgba(0,0,0,.25);

color:white;

text-align:center;

margin-bottom:25px;

}

.main-header h1{

font-size:42px;

margin:0;

font-weight:bold;

}

.main-header h3{

margin-top:12px;

font-weight:400;

}

.main-header p{

opacity:.9;

}


/* ===========================
   CARDS
=========================== */

.card{

background:white;

padding:18px;

border-radius:18px;

box-shadow:0 6px 18px rgba(0,0,0,.08);

margin-bottom:18px;

transition:.25s;

}

.card:hover{

transform:translateY(-4px);

box-shadow:0 12px 25px rgba(0,0,0,.15);

}


/* ===========================
   TITLES
=========================== */

.section-title{

font-size:24px;

font-weight:bold;

color:#1565C0;

margin-bottom:10px;

border-bottom:2px solid #E3EAF8;

padding-bottom:8px;

}


/* ===========================
   FOOTER
=========================== */

.footer{

background:white;

padding:20px;

border-radius:16px;

text-align:center;

color:#666;

margin-top:25px;

box-shadow:0 5px 15px rgba(0,0,0,.08);

}

</style>



<div class="main-header">

<h1>
🌍 Smart AI Travel Planner
</h1>

<h3>
Plan Smarter • Travel Better
</h3>

<p>
AI Powered Personalized Travel Planning using Cohere
</p>

</div>

        """)

        destination = gr.Textbox(

            label="📍 Destination",

            interactive=False,

            lines=1

        )

        gr.Markdown("---")
                # ==========================================================
        # ROW 1
        # HOTELS & WEATHER
        # ==========================================================

        with gr.Row(equal_height=True):

            # ================= HOTELS =================

            with gr.Column(scale=1):

                gr.HTML("""
                <div class="card">
                    <div class="section-title">
                        🏨 Hotel Recommendations
                    </div>

                    <p style="color:#666;margin-top:-5px;">
                        Recommended stays based on your destination.
                    </p>

                </div>
                """)

                hotels = gr.Markdown(
                    value=""
                )

            # ================= WEATHER =================

            with gr.Column(scale=1):

                gr.HTML("""
                <div class="card">
                    <div class="section-title">
                        🌦 Weather Information
                    </div>

                    <p style="color:#666;margin-top:-5px;">
                        Weather forecast and travel season.
                    </p>

                </div>
                """)

                weather = gr.Markdown(
                    value=""
                )


        # ==========================================================
        # ROW 2
        # BUDGET & FOOD
        # ==========================================================

        with gr.Row(equal_height=True):

            # ================= BUDGET =================

            with gr.Column(scale=1):

                gr.HTML("""
                <div class="card">

                    <div class="section-title">

                        💰 Estimated Budget

                    </div>

                    <p style="color:#666;margin-top:-5px;">
                        Complete trip cost estimation.
                    </p>

                </div>
                """)

                budget = gr.Markdown(
                    value=""
                )

            # ================= FOOD =================

            with gr.Column(scale=1):

                gr.HTML("""
                <div class="card">

                    <div class="section-title">

                        🍴 Food & Restaurants

                    </div>

                    <p style="color:#666;margin-top:-5px;">
                        Famous foods and recommended restaurants.
                    </p>

                </div>
                """)

                food = gr.Markdown(
                    value=""
                )
                        # ==========================================================
        # COMPLETE DAY-WISE ITINERARY
        # ==========================================================

        gr.HTML("""
        <div class="card">

            <div class="section-title">
                📅 Complete Day-wise Itinerary
            </div>

            <p style="
                color:#666;
                margin-top:-5px;
                margin-bottom:15px;
            ">
                Your personalized day-by-day travel schedule.
            </p>

        </div>
        """)

        itinerary = gr.Markdown(
            value="",
            elem_classes=["card"]
        )

        # ==========================================================
        # TOP ATTRACTIONS
        # ==========================================================

        gr.HTML("""
        <div class="card">

            <div class="section-title">
                🏖 Top Attractions
            </div>

            <p style="
                color:#666;
                margin-top:-5px;
                margin-bottom:15px;
            ">
                Must-visit places recommended for your destination.
            </p>

        </div>
        """)

        attractions = gr.Markdown(
            value="",
            elem_classes=["card"]
        )
                # ==========================================================
        # PACKING CHECKLIST
        # ==========================================================

        gr.HTML("""
        <div class="card">

            <div class="section-title">
                🎒 Packing Checklist
            </div>

            <p style="
                color:#666;
                margin-top:-5px;
                margin-bottom:15px;
            ">
                Essentials you should carry for your trip.
            </p>

        </div>
        """)

        packing = gr.Markdown(
            value="",
            elem_classes=["card"]
        )


        # ==========================================================
        # FOOTER
        # ==========================================================

        gr.HTML("""
        <div class="footer">

            <h3 style="margin:0;color:#1565C0;">
                🌍 Smart AI Travel Planner
            </h3>

            <p style="margin-top:10px;">
                AI Powered Personalized Travel Planning
            </p>

            <p style="
                font-size:14px;
                color:#888;
            ">
                Built with Python • Gradio • Cohere AI
            </p>

        </div>
        """)

    return (
        dashboard_page,
        destination,
        hotels,
        weather,
        budget,
        food,
        itinerary,
        attractions,
        packing,
    )