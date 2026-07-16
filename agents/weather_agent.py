from backend.services.cohere_service import co


def weather_agent(destination):

    prompt = f"""
You are a Weather Expert.

Give weather information for {destination}.

Include:

1. Temperature
2. Climate
3. Rain Chances
4. Best Time to Visit
5. Clothes to Carry
"""

    response = co.chat(
        model="command-a-03-2025",
        message=prompt
    )

    return response.text