from backend.services.cohere_service import co


def hotel_agent(destination, budget):

    prompt = f"""
You are a Hotel Recommendation Agent.

Suggest 5 hotels for {destination}.

Budget: ₹{budget}

For each hotel provide:

1. Hotel Name
2. Price Per Night
3. Rating
4. Family Friendly or Not
5. Short Description

Return only hotel recommendations.
"""

    response = co.chat(
        model="command-a-03-2025",
        message=prompt
    )

    return response.text