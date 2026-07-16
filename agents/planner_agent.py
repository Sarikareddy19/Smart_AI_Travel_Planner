from backend.services.cohere_service import generate_travel_plan


def planner_agent(destination, budget, travel_type, interests):

    return generate_travel_plan(
        destination=destination,
        budget=budget,
        travel_type=travel_type,
        interests=interests
    )