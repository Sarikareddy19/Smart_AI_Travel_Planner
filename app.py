import os
import gradio as gr
from backend.controller import generate_complete_trip
from frontend.pages.dashboard_page import create_dashboard_page

from frontend.pages.home_page import create_home_page
from frontend.pages.user_details import create_user_details_page
from frontend.pages.trip_details import create_trip_details_page
from frontend.pages.preferences_page import create_preferences_page
from frontend.pages.review_page import create_review_page
from backend.utils.parser import get_section


# --------------------------------------
# Navigation Functions
# --------------------------------------

def open_user_page():
    return (
        gr.update(visible=False),
        gr.update(visible=True)
    )


def back_home():
    return (
        gr.update(visible=True),
        gr.update(visible=False)
    )


def open_trip_page():
    return (
        gr.update(visible=False),
        gr.update(visible=True)
    )


def back_user_page():
    return (
        gr.update(visible=True),
        gr.update(visible=False)
    )


def open_preferences_page():
    return (
        gr.update(visible=False),
        gr.update(visible=True)
    )


def back_trip_page():
    return (
        gr.update(visible=True),
        gr.update(visible=False)
    )


def open_review_page(

    name,
    email,

    destination,
    budget,

    transport,
    accommodation,

    interests

):

    return (

        gr.update(visible=False),

        gr.update(visible=True),

        name,

        email,

        destination,

        f"₹ {budget}",

        transport,

        accommodation,

        ", ".join(interests)

    )


def back_preferences_page():
    return (
        gr.update(visible=True),
        gr.update(visible=False)
    )


# --------------------------------------
# Application
# --------------------------------------
def generate_ai_plan(

        destination,
        budget,
        travel_type,
        interests

):

    # Generate AI plan + PDF
    result = generate_complete_trip(
        destination,
        budget,
        travel_type,
        interests
    )

    hotels = get_section(result, "HOTELS")
    weather = get_section(result, "WEATHER")
    budget_data = get_section(result, "BUDGET")
    food = get_section(result, "FOOD")
    itinerary = get_section(result, "ITINERARY")
    attractions = get_section(result, "TOP_ATTRACTIONS")
    gallery = attractions
    packing = get_section(result, "PACKING")

    return (
        gr.update(visible=False),
        gr.update(visible=True),
        destination,
        hotels,
        weather,
        budget_data,
        food,
        itinerary,
        gallery,
        packing
    )

   

with gr.Blocks(
    title="Smart AI Travel Planner",
    theme=gr.themes.Soft(
        primary_hue="blue",
        secondary_hue="orange"
    )
) as app:

    # ---------------- HOME ----------------

    with gr.Column(visible=True) as home_page:

        (
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
        ) = create_home_page()

    # ---------------- USER DETAILS ----------------

    (
        user_page,
        full_name,
        age,
        gender,
        email,
        phone,
        country,
        state,
        user_back_btn,
        user_next_btn
    ) = create_user_details_page()

    # ---------------- TRIP DETAILS ----------------

    (
        trip_page,
        trip_from,
        trip_destination,
        trip_departure,
        trip_return,
        trip_budget,
        trip_adults,
        trip_children,
        travel_type,
        transport,
        accommodation,
        trip_back_btn,
        trip_next_btn
    ) = create_trip_details_page()

    # ---------------- PREFERENCES ----------------

    (
        preferences_page,
        interests,
        preferences_back_btn,
        preferences_next_btn
    ) = create_preferences_page()

    # ---------------- REVIEW ----------------

    (
        review_page,
        review_name,
        review_email,
        review_destination,
        review_budget,
        review_transport,
        review_accommodation,
        review_preferences,
        review_back_btn,
        review_generate_btn
    ) = create_review_page()

    # ---------------- Dashboard ----------------

    (
        dashboard_page,
        dashboard_destination,
        dashboard_hotels,
        dashboard_weather,
        dashboard_budget,
        dashboard_food,
        dashboard_itinerary,
        dashboard_attractions,
        dashboard_packing
    ) = create_dashboard_page()

    # --------------------------------------
    # BUTTON EVENTS
    # --------------------------------------

    # Home -> User Details
    start_btn.click(
        fn=open_user_page,
        outputs=[home_page, user_page]
    )

    # User -> Home
    user_back_btn.click(
        fn=back_home,
        outputs=[home_page, user_page]
    )

    # User -> Trip
    user_next_btn.click(
        fn=open_trip_page,
        outputs=[user_page, trip_page]
    )

    # Trip -> User
    trip_back_btn.click(
        fn=back_user_page,
        outputs=[user_page, trip_page]
    )

    # Trip -> Preferences
    trip_next_btn.click(
        fn=open_preferences_page,
        outputs=[trip_page, preferences_page]
    )

    # Preferences -> Trip
    preferences_back_btn.click(
        fn=back_trip_page,
        outputs=[trip_page, preferences_page]
    )

    # Preferences -> Review
    preferences_next_btn.click(
        fn=open_review_page,
        inputs=[
            full_name,
            email,
            trip_destination,
            trip_budget,
            transport,
            accommodation,
            interests
        ],
        outputs=[
            preferences_page,
            review_page,
            review_name,
            review_email,
            review_destination,
            review_budget,
            review_transport,
            review_accommodation,
            review_preferences
        ]
    )

    # Review -> Preferences
    review_back_btn.click(
        fn=back_preferences_page,
        outputs=[preferences_page, review_page]
    )

    # --------------------------------------
    # AI Button (Temporary)
    # --------------------------------------

    review_generate_btn.click(
        fn=generate_ai_plan,
        inputs=[
            trip_destination,
            trip_budget,
            travel_type,
            interests
            
        ],
        outputs=[
    review_page,
    dashboard_page,
    dashboard_destination,
    dashboard_hotels,
    dashboard_weather,
    dashboard_budget,
    dashboard_food,
    dashboard_itinerary,
    dashboard_attractions,
    dashboard_packing
]
    )

app.launch(
    server_name="0.0.0.0",
    server_port=int(os.environ.get("PORT", 7860))
)