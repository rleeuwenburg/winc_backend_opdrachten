# Factors:
is_raining = True
is_sunshine = True
is_daytime = False
cows_are_in_pasture = True
is_windy = True
manurepit_is_full = True
cows_need_milking = True
is_fall = True

# Actions:
"""
print("take the cows inside")
print("milk the cows")
print("fertilize the land")
print("mow the grass to make hay")
print("cows go outside")
"""

# Combo's:
# 1. Als de koeien gemolken moeten worden dan moeten ze naar binnen gehaald worden en vervolgens gemolken.
if cows_need_milking: 
    print("take the cows inside")
    print("milk the cows")
    
# 2. Als de koeien 's nachts op het weiland staan en het regent dan moeten ze naar binnen gehaald worden.
if cows_are_in_pasture and is_raining and is_daytime != True:
    print("take the cows inside")
    
# 3. Als de koeien op het weiland staan en er staat veel wind dan moeten ze binnen gehaald worden, als ze ook nog gemolken moeten worden, doe dat dan vervolgens.
if cows_are_in_pasture and is_windy:
    print("take the cows inside")
    if cows_need_milking: 
        print("milk the cows")
        
# 4. Als de gierput vol is en het regent moet het land bemest worden. Denk aan de koeien.
if manurepit_is_full and is_raining:
    if cows_are_in_pasture:
        print("take the cows inside")
    print("fertilize the land")
    
# 5. Als het herfst is en de zon schijnt moet het gras gemaaid worden. Denk aan de koeien.
if is_fall and is_sunshine:
    if cows_are_in_pasture:
        print("take the cows inside")
    print("mow the grass to make hay")
    
# 6. Als het herfst is en de zon schijnt moeten de koeien naar buiten, tenzij ze al buiten zijn.
cows_are_in_pasture = False
if not cows_are_in_pasture and is_fall and is_sunshine:
    print("cows go outside")
   
    
    
    

