from agents.planner_agent import planner_agent



def generate_complete_trip(
    destination,
    budget,
    travel_type,
    interests
):

    # Generate AI Travel Plan
    result = planner_agent(
        destination,
        budget,
        travel_type,
        interests
    )

    # Import parser
    from backend.utils.parser import get_section

    hotels = get_section(result, "HOTELS")
    weather = get_section(result, "WEATHER")
    budget_data = get_section(result, "BUDGET")
    food = get_section(result, "FOOD")
    itinerary = get_section(result, "ITINERARY")
    attractions = get_section(result, "TOP_ATTRACTIONS")
    packing = get_section(result, "PACKING")

    

    return result
