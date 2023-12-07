def checkRace(race_time_ms, record_mm):
  wins = 0

  for speed in range(0,race_time_ms+1):
    distance = speed * (race_time_ms - speed)
    #print("speed:", speed, "\tdistance:", distance)
    if distance > record_mm:
      wins += 1
      
  return wins

win1 = checkRace(48876981, 255128811171623)
# win2 = checkRace(87, 1288)
# win3 = checkRace(69, 1117)
# win4 = checkRace(81, 1623)

print("1:", win1)
#solution = win1 * win2 * win3 * win4
#print("1:", win1, "2:",win2, "3:", win3, "4:",win4, "=",solution)

#Time:        48     87     69     81
#Distance:   255   1288   1117   1623