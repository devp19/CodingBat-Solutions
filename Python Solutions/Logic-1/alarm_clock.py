def alarm_clock(day, vacation):
  
  weekday = [1, 2, 3, 4, 5]
  
  if vacation:
    if day in weekday:
      return "10:00"
    else:
      return "off"
  
  else:
    if day in weekday:
      return "7:00"
    else:
      return "10:00"
