import re

SECTIONS = {
    "HOTELS": (
        "HOTEL RECOMMENDATIONS",
        "WEATHER INFORMATION"
    ),

    "WEATHER": (
        "WEATHER INFORMATION",
        "ESTIMATED BUDGET"
    ),

    "BUDGET": (
        "ESTIMATED BUDGET",
        "FOOD & RESTAURANTS"
    ),

    "FOOD": (
        "FOOD & RESTAURANTS",
        "COMPLETE DAY-WISE ITINERARY"
    ),

    "ITINERARY": (
        "COMPLETE DAY-WISE ITINERARY",
        "TOP ATTRACTIONS"
    ),

    "TOP_ATTRACTIONS": (
        "TOP ATTRACTIONS",
        "PACKING CHECKLIST"
    ),

    "PACKING": (
        "PACKING CHECKLIST",
        "SAFETY TIPS"
    ),

    "SAFETY": (
        "SAFETY TIPS",
        None
    )
}


def get_section(text, section):

    if section not in SECTIONS:
        return "No Data Found"

    start_title, end_title = SECTIONS[section]

    # Find start heading
    start_match = re.search(
        re.escape(start_title),
        text,
        re.IGNORECASE
    )

    if not start_match:
        return "No Data Found"

    start = start_match.end()

    # Find end heading
    if end_title:

        end_match = re.search(
            re.escape(end_title),
            text[start:],
            re.IGNORECASE
        )

        if end_match:
            end = start + end_match.start()
            return text[start:end].strip()

    return text[start:].strip()