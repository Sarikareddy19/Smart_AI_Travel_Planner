import gradio as gr


def create_trip_details_page():

    with gr.Column(visible=False) as trip_page:

        gr.HTML("""
        <div style="
            background:linear-gradient(135deg,#1565C0,#42A5F5);
            color:white;
            padding:25px;
            border-radius:20px;
            text-align:center;
            margin-bottom:20px;
        ">

        <h1>✈ Trip Details</h1>

        <p>Enter your travel information</p>

        </div>
        """)

        with gr.Row():

            from_city = gr.Textbox(
    label="📍 From",
    placeholder="Enter your departure city"
)

            

            destination = gr.Textbox(
    label="📍 Destination",
    placeholder="Enter your destination"
)

        with gr.Row():

            departure = gr.DateTime(

                label="Departure Date",

                include_time=False

            )

            return_date = gr.DateTime(

                label="Return Date",

                include_time=False

            )

        with gr.Row():

            budget = gr.Number(

                label="Budget (₹)",

                value=30000

            )

            adults = gr.Number(

                label="Adults",

                value=None,

                minimum=1,
                precision=0

            )

            children = gr.Number(

                label="Children",

                value=0

            )

        with gr.Row():

            travel_type = gr.Dropdown(

                choices=[
                    "Solo",
                    "Family",
                    "Friends",
                    "Couple"
                ],

                value="Family",

                label="Travel Type"

            )

            transport = gr.Dropdown(

                choices=[
                    "Flight",
                    "Train",
                    "Bus",
                    "Car"
                ],

                value="Flight",

                label="Transport"

            )

        accommodation = gr.Dropdown(

            choices=[
                "Budget Hotel",
                "Standard Hotel",
                "Luxury Hotel",
                "Resort"
            ],

            value="Standard Hotel",

            label="Accommodation"

        )

        gr.Markdown("---")

        with gr.Row():

            back_btn = gr.Button(
                "⬅ Back"
            )

            next_btn = gr.Button(
                "Next ➜",
                variant="primary"
            )

    return (

        trip_page,

        from_city,
        destination,
        departure,
        return_date,
        budget,
        adults,
        children,
        travel_type,
        transport,
        accommodation,

        back_btn,
        next_btn

    )