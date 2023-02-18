def _getNextDay(weekday='', stepsNextDay=0):
	_Weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
	if stepsNextDay>7:
		stepsNextDay %= 7
	if 0<stepsNextDay<_Weekdays.index(weekday.lower().capitalize()):
		return(_Weekdays[_Weekdays.index(weekday.lower().capitalize())+stepsNextDay])
	elif _Weekdays.index(weekday.lower().capitalize()) <= stepsNextDay < 6:
		return(_Weekdays[_Weekdays.index(weekday.lower().capitalize())+stepsNextDay])
	elif stepsNextDay == 6:
		return(_Weekdays[0])

def _getCountDay(arrTime=[0,2]):
	arrTime[0] = [(int(arrTime[0][0]/24)), 
				arrTime[0][0]%24, arrTime[0][1]]
	return arrTime
def _strToArrTime(strTime=""):
	strTime = strTime.split(' ')
	strTime[0] = strTime[0].split(':')
	for index, value in enumerate(strTime[0]):
		strTime[0][index] = int(strTime[0][index])
	return strTime

def add_time(start, duration, weekdays='', deBug=True):
	if deBug: print('\n\n', f"{'debug':*^30}")
	start = _getCountDay(_strToArrTime(start))
	duration = _getCountDay(_strToArrTime(duration))

	for step in range(0, 3):
		rStep = len(start[0])-(step+1)
		match rStep:
			case 2:
				if start[0][rStep]+duration[0][rStep]<60:
					start[0][rStep]+=duration[0][rStep]
				else:
					start[0][rStep-1]+=int((start[0][rStep]+duration[0][rStep])/60)
					start[0][rStep]=(start[0][rStep]+duration[0][rStep])%60
				duration[0][rStep]=0
			case 1:
				match start[1]:
					case "AM":
						timeRemaining = 24-start[0][rStep]
						if duration[0][rStep]>timeRemaining:
							start[0][rStep-1] += 1
							start[0][rStep] = duration[0][step]-timeRemaining
							if start[0][rStep]>=12 and start[0][rStep+1]>0:
								start[1]='PM'
								if start[0][rStep]>12: start[0][rStep]-=12
						else:
							start[0][rStep] += duration[0][step]
							if start[0][rStep]>=12 and start[0][rStep+1]>0:
								start[1]='PM'
								if start[0][rStep]>12: start[0][rStep]-=12
					case "PM":
						timeRemaining = 12-start[0][rStep]
						if duration[0][rStep]>=timeRemaining:
							start[0][rStep-1] += 1
							start[0][rStep] = duration[0][step]-timeRemaining
							if start[0][rStep]==0: start[0][rStep]=12
							if start[0][rStep]>=12 and start[0][rStep+1]>0:
								start[1]='AM'
								if start[0][rStep]>12: start[0][rStep]-=12
							else: start[1] = 'AM'
						else:
							start[0][rStep] += duration[0][step]
				duration[0][step]=0
			case 0:
				start[0][rStep]+=duration[0][rStep]
				duration[0][step]=0
		if deBug: print(f"{start} | {duration}")
	if deBug: print('\n')

	new_time = str(start[0][1])
	new_time += ':'
	if start[0][2]<10: new_time += '0'
	new_time += str(start[0][2])
	new_time += f' {start[1]}'
	if weekdays!='': new_time += f', {_getNextDay(weekdays, start[0][0])}' 
	if start[0][0]>1:
		new_time += f' ({start[0][0]} days later)'
	elif start[0][0]==1:
		new_time += f' (next day)'

	if deBug: print ('\n',new_time,'\n')

	return new_time