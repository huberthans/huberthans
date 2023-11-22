start_hug_time = time.time()
# Do the hug mechanic
# hug ends
end_hug_time = time.time()
hug_duration = end_hug_time - start_hug_time
if hug_duration < 10:
    affection += 0.75
elif 10 <= hug_duration < 30:
    affection += 1.25
elif 30 <= hug_duration < 90:
    affection += 2
else:
    # At this point we know hug_duration >= 90
    if monika.is_asleep():
        if monika.sleep_duration() < (60 * 30): # number of seconds in 30 minutes.
            affection += 5
        else:
            # this high of an affection gain might warrant this event being an occasional bypass.
            # Make bypass-capable have a 3-5 day cool down maybe?
            affection += 10 
    else:
        affection += 3
