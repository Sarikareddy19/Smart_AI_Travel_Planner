from backend.services.cohere_service import co


def food_agent(destination):

    prompt = f"""
You are a Food Expert.

Destination:
{destination}

Suggest:

1. Famous Local Foods
2. Best Restaurants
3. Vegetarian Restaurants
4. Non-Vegetarian Restaurants
5. Street Food
6. Approximate Food Cost Per Day

Return the response in a clean format.
"""

    response = co.chat(
        model="command-a-03-2025",
        message=prompt
    )

    return response.text