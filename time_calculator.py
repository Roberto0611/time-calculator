def add_time(start, duration):
  #set variables
  new_hour = 0
  day = 0

  #Get moment
  pos_moment = start.find(' ')
  moment = start[pos_moment + 1:]  #Moment can be PM or AM

  #Get starting hour
  pos_hour = start.find(":")
  starting_hour = int(start[0:pos_hour])

  #Get starting minutes
  starting_minute = int(start[pos_hour + 1:pos_moment])

  #Get hour
  pos_hour = duration.find(":")
  added_hour = int(duration[0:pos_hour])

  #get minutes
  added_minutes = int(duration[pos_hour + 1:])

  #change values for PM
  if moment == 'PM':
    starting_hour = starting_hour + 12

  #Add the time

  #get new minutes
  new_minute = starting_minute + added_minutes

  #check for minutes being more than 60
  if new_minute > 60:
    new_hour = new_hour + 1
    new_minute = new_minute - 60

  #get new hour
  new_hour = starting_hour + added_hour + new_hour

  #Check if hours are more than 24
  while new_hour > 24:
    day = day + 1
    new_hour = new_hour - 24

  #check for PM or AM
  if new_hour == 12:
    new_moment = 'PM'
  elif new_hour == 24:
    new_moment = 'AM'
  elif new_hour > 12:
    new_moment = 'PM'
    new_hour = new_hour - 12
  else:
    new_moment = 'AM'

  #Make correct format for minutes :)
  if len(str(new_minute)) == 1:
    new_minute = "0" + str(new_minute)
    
  new_time = str(new_hour) + ":" + str(new_minute) + ' ' + new_moment

  if day == 0:
    return new_time
  elif day == 1:
    return new_time + ' (next day)'
  else:
    return new_time + ' ' + '(' + str(day) + ' days later)'