# Task 1 Compare the flight tourte of a competing airloine. Find out
    #1. Which Destinations both airelines fly  (items present in both sets) <intersection>
    #2. Unique Desginations to my airline (items present only in the first set) <difference>
    #3. If there is a destination neither airline shares (items that are in only one set) <sym diff - intersection >
    #   I'm not sure if theres a method that lets me do this, so I'll take the difference of both sets and then union them together to print 


our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

def routecomp(ourset,theirset):
    dest_both = ourset.intersection(theirset)
    dest_diff = ourset.difference(theirset)
    dest_diff_flip = theirset.difference(ourset)
    dest_unique = dest_diff.union(dest_diff_flip)    
    print (f"Desinations you can travel to via either Airline:\n{dest_both}")
    print (f"Desinations you can travel to via Our Airline:\n{dest_diff}")
    print (f"Desinations you can travel to only via a Specific Airline:\n{dest_unique}")

routecomp(our_routes,competitor_routes)