# Given an unordered list of flights taken by 
# someone, each represented as (origin, destination) 
# pairs, and a starting airport, compute the person's 
# itinerary. If no such itinerary exists, return null. 
# If there are multiple possible itineraries, return the 
# lexicographically smallest one. All flights must be used in the itinerary.

def get_itinerary(flight, str):

    itinerary = []
    src = str

    while flight:

        itinerary.append(src)
        destinations = [dest for (src, dest) in flight if src == src]

        if not destinations:
            break

        min_dest = min(destinations)
        flight.remove((src, min_dest))
        src = min_dest

    itinerary.append(src)

    if not flight:
        return itinerary

    return None

if __name__ == "__main__":
    get_itinerary([('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')], 'YUL') == ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD']