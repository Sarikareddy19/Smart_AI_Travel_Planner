from backend.services.cohere_service import co


def packing_agent(destination):

    prompt = f"""
You are a Travel Packing Expert.

Destination:
{destination}

Suggest:

1. Clothes
2. Footwear
3. Medicines
4. Electronics
5. Documents
6. Accessories

Return a checklist.
"""

    response = co.chat(
        model="command-a-03-2025",
        message=prompt
    )

    return response.text