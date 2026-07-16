import gradio as gr


def create_home_page():

    gr.HTML("""
    <div style="
        background:white;
        padding:18px;
        border-radius:15px;
        box-shadow:0px 2px 10px rgba(0,0,0,.15);
        display:flex;
        justify-content:space-between;
        align-items:center;
        margin-bottom:20px;
    ">

        <h2 style="color:#1565C0;">
        ✈ Smart AI Travel Planner
        </h2>

        <div style="font-size:18px;">
        Home &nbsp;&nbsp;
        Trips &nbsp;&nbsp;
        About &nbsp;&nbsp;
        Contact
        </div>

    </div>
    """)

    gr.HTML("""
    <div style="
        background:linear-gradient(135deg,#1565C0,#42A5F5);
        color:white;
        text-align:center;
        padding:60px;
        border-radius:20px;
        margin-bottom:30px;
    ">

        <h1 style="font-size:45px;">
        🌍 Explore the World with AI
        </h1>

        <h3>
        Your Intelligent Travel Companion
        </h3>

        <p style="font-size:18px;">
        Hotels • Food • Weather • Budget • Itinerary
        </p>

    </div>
    """)

    gr.Markdown("## ✈ Quick Trip Planner")

    with gr.Row():

        from_city = gr.Dropdown(
            label="From",
            choices=[
                "Hyderabad",
                "Bangalore",
                "Chennai",
                "Mumbai",
                "Delhi"
            ],
            value="Hyderabad"
        )

        destination = gr.Textbox(
            label="Destination",
            placeholder="Where do you want to go?"
        )

    with gr.Row():

        departure = gr.DateTime(
            label="Departure",
            include_time=False
        )

        return_date = gr.DateTime(
            label="Return",
            include_time=False
        )

    with gr.Row():

        budget = gr.Number(
            label="Budget (₹)",
            value=30000
        )

        adults = gr.Number(
            label="Adults",
            value=2
        )

        children = gr.Number(
            label="Children",
            value=0
        )

    start_btn = gr.Button(
        "🚀 Start Planning",
        variant="primary",
        size="lg"
    )

    gr.Markdown("---")

    gr.Markdown("## ⭐ Why Choose Us")

    with gr.Row():

        gr.HTML("""
        <div style="
        background:#E3F2FD;
        padding:20px;
        border-radius:15px;
        text-align:center;
        ">
        🤖
        <h3>AI Planning</h3>
        Complete itinerary in seconds.
        </div>
        """)

        gr.HTML("""
        <div style="
        background:#E8F5E9;
        padding:20px;
        border-radius:15px;
        text-align:center;
        ">
        🏨
        <h3>Hotels</h3>
        Best hotel recommendations.
        </div>
        """)

        gr.HTML("""
        <div style="
        background:#FFF3E0;
        padding:20px;
        border-radius:15px;
        text-align:center;
        ">
        🌦
        <h3>Weather</h3>
        Live weather information.
        </div>
        """)

        gr.HTML("""
        <div style="
        background:#F3E5F5;
        padding:20px;
        border-radius:15px;
        text-align:center;
        ">
        💰
        <h3>Budget</h3>
        Smart budget optimization.
        </div>
        """)

    gr.Markdown("---")

    gr.Markdown("## 🔥 Popular Destinations")

    with gr.Row():

        gr.Button("🏖 Goa")

        gr.Button("🏔 Ooty")

        gr.Button("🕌 Tirupati")

        gr.Button("🌊 Pondicherry")

    gr.Markdown("---")

    about_btn = gr.Button("📖 About Project")

    generate_btn = gr.Button(
        "✨ AI Demo",
        visible=False
    )

    gr.HTML("""
    <div style="
    text-align:center;
    color:gray;
    padding:20px;
    ">

    Powered by Python • Gradio • Cohere AI

    <br><br>

    Created by <b>Sarika Reddy</b>

    </div>
    """)

    return (
        start_btn,
        about_btn,
        generate_btn,
        from_city,
        destination,
        departure,
        return_date,
        budget,
        adults,
        children
    )