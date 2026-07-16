import os
import cohere
from dotenv import load_dotenv

load_dotenv()

co = cohere.Client(os.getenv("COHERE_API_KEY"))


def generate_travel_plan(destination, budget, travel_type, interests):

    prompt = f"""
You are an Expert AI Travel Planner.

Generate a professional travel plan.

Destination: {destination}
Budget: ₹{budget}
Travel Type: {travel_type}
Interests: {interests}

IMPORTANT RULES

1. Use clear headings.
2. Do NOT repeat information.
3. Keep hotel names realistic.
4. Keep budget realistic according to destination.
5. Create a beautiful day-wise itinerary.
6. Mention restaurants near attractions whenever possible.
7. Return ONLY the format below.
8. Keep the total response below 900 words.

==================================================

# HOTEL RECOMMENDATIONS

Recommend ONLY 3 hotels.

For each hotel include:

Hotel Name

⭐ Rating

💰 Price Per Night

📍 Location

📝 Short Description

==================================================

# WEATHER INFORMATION

Include

🌡 Temperature

☀ Climate

📅 Best Time to Visit

👕 Recommended Clothes

🌄 Sunrise

🌇 Sunset

==================================================

# ESTIMATED BUDGET

Return ONLY this table.

| Category | Cost |
|----------|------|
| Hotel | |
| Food | |
| Transport | |
| Activities | |
| Shopping | |
| Total | |

==================================================

# FOOD & RESTAURANTS

Include

🍲 Famous Foods

🍽 Top Restaurants

💰 Average Meal Cost

🍨 Famous Desserts

==================================================

# COMPLETE DAY-WISE ITINERARY

Create a proper itinerary.

For EACH DAY include:

## Day 1

🌅 Morning

🌞 Afternoon

🌆 Evening

🌙 Night

Repeat the same format until the trip ends.

Mention attractions, nearby restaurants and activities.

==================================================

# TOP ATTRACTIONS

Return ONLY attraction names.

Example

Eiffel Tower

Louvre Museum

Notre-Dame Cathedral

Seine River Cruise

Montmartre

==================================================

# PACKING CHECKLIST

Return ONLY bullet points.

==================================================

# SAFETY TIPS

Return ONLY bullet points.

"""

    response = co.chat(
        model="command-a-03-2025",
        message=prompt
    )
    

    return response.text