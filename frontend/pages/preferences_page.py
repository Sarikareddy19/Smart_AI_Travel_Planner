import gradio as gr


def create_preferences_page():

    with gr.Column(visible=False) as preferences_page:

        gr.HTML("""
        <div style="
            background:linear-gradient(135deg,#1565C0,#42A5F5);
            color:white;
            padding:25px;
            border-radius:20px;
            text-align:center;
            margin-bottom:20px;
        ">
            <h1>❤️ Travel Preferences</h1>
            <p>Select your interests</p>
        </div>
        """)

        interests = gr.CheckboxGroup(

            label="Choose Your Interests",

            choices=[
                "🏖 Beaches",
                "🏔 Adventure",
                "🌳 Nature",
                "🛕 Temples",
                "🍔 Food",
                "🛍 Shopping",
                "📸 Photography",
                "🦁 Wildlife",
                "🌃 Nightlife",
                "🏰 Historical Places"
            ]
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

        preferences_page,

        interests,

        back_btn,

        next_btn

    )