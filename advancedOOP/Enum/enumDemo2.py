from enum import Enum, unique;

@unique
class Weekday(Enum):
	Sun = 0
	Mon = 1
	Tue = 2
	Wed = 3
	Thu = 4
	Fri = 5
	Sat = 6

day1 = Weekday.Mon
print('day1', day1)												# Weekday.Mon
print('Weekday.Tue', Weekday.Tue)								# Weekday.Tue
print('Weekday["Tue"]', Weekday['Tue'])							# Weekday.Tue
print('Weekday.Tue.value', Weekday.Tue.value)					# 2
print('day1 == Weekday.Mon', day1 == Weekday.Mon)				# True
print('Weekday(1)', Weekday(1))									# Weekday.Mon
print('Weekday.Mon == Weekday(1)', Weekday.Mon == Weekday(1))	# True
print('Weekday(6)', Weekday(6))									# Weekday.Sat

print(Weekday.__members__.items())
for key, value in Weekday.__members__.items():
	print(key, value)

