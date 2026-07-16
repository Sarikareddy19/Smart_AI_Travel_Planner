from backend.services.cohere_service import co


def budget_agent(destination, budget):

    prompt = f"""
You are a Budget Planner.

Destination:
{destination}

Total Budget:
₹{budget}

Split the budget into:

Hotel

Food

Transport

Shopping

Emergency

Return as a table.
"""

    response = co.chat(
        model="command-a-03-2025",
        message=prompt
    )

    return response.text