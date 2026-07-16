import gradio as gr


def create_user_details_page():

    with gr.Column(visible=False) as user_page:

        gr.HTML("""
        <div style="
            background:linear-gradient(135deg,#1565C0,#42A5F5);
            color:white;
            padding:25px;
            border-radius:20px;
            text-align:center;
            margin-bottom:20px;
        ">
            <h1>👤 Traveler Information</h1>
            <p>Please enter your personal details</p>
        </div>
        """)

        with gr.Row():

            full_name = gr.Textbox(
                label="Full Name",
                placeholder="Enter your full name"
            )

            age = gr.Number(
    label="🎂 Age",
    value=None,
    minimum=1,
    precision=0
)

        with gr.Row():

            gender = gr.Dropdown(
                choices=[
                    "Male",
                    "Female",
                    "Other"
                ],
                label="Gender"
            )

            email = gr.Textbox(
                label="Email",
                placeholder="example@gmail.com"
            )

        with gr.Row():

            phone = gr.Textbox(
                label="Phone Number",
                placeholder="9876543210"
            )

            country = gr.Dropdown(
                choices=[
                    "India"
                ],
                value="India",
                label="Country"
            )

        state = gr.Dropdown(
            choices=[
                "Andhra Pradesh",
                "Telangana",
                "Tamil Nadu",
                "Karnataka",
                "Kerala",
                "Maharashtra",
                "Delhi"
            ],
            label="State"
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
        user_page,
        full_name,
        age,
        gender,
        email,
        phone,
        country,
        state,
        back_btn,
        next_btn
    )