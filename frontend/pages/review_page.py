import gradio as gr


def create_review_page():

    with gr.Column(visible=False) as review_page:

        gr.HTML("""
        <div style="
            background:linear-gradient(135deg,#1565C0,#42A5F5);
            color:white;
            padding:25px;
            border-radius:20px;
            text-align:center;
            margin-bottom:20px;
        ">

        <h1>📋 Review Your Trip</h1>

        <p>Please verify all details before generating your AI travel plan.</p>

        </div>
        """)

        gr.Markdown("## 👤 Traveler Details")

        review_name = gr.Textbox(
            label="Full Name",
            interactive=False
        )

        review_email = gr.Textbox(
            label="Email",
            interactive=False
        )

        gr.Markdown("---")

        gr.Markdown("## ✈ Trip Details")

        review_destination = gr.Textbox(
            label="Destination",
            interactive=False
        )

        review_budget = gr.Textbox(
            label="Budget",
            interactive=False
        )

        review_transport = gr.Textbox(
            label="Transport",
            interactive=False
        )

        review_accommodation = gr.Textbox(
            label="Accommodation",
            interactive=False
        )

        gr.Markdown("---")

        gr.Markdown("## ❤️ Preferences")

        review_preferences = gr.Textbox(
            label="Selected Interests",
            lines=4,
            interactive=False
        )

        gr.Markdown("---")

        with gr.Row():

            back_btn = gr.Button(
                "⬅ Back"
            )

            generate_btn = gr.Button(
                "✨ Generate AI Travel Plan",
                variant="primary"
            )

    return (

        review_page,

        review_name,
        review_email,

        review_destination,
        review_budget,
        review_transport,
        review_accommodation,

        review_preferences,

        back_btn,
        generate_btn

    )