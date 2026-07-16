from backend.services.cohere_service import co


def itinerary_agent(destination, days, interests):

    prompt = f"""
You are a Professional Travel Planner.

Destination:
{destination}

Trip Duration:
{days} Days

Interests:
{interests}

Generate:

Day 1

Morning
Afternoon
Evening

Day 2

Morning
Afternoon
Evening

Continue until the last day.

Include famous places and suitable timings.
"""

    response = co.chat(
        model="command-a-03-2025",
        message=prompt
    )

    return response.text