#KCPE Assignment

i = 1
marks = []

while i <= 5:
	mark = int(input("Mark: "))
	if mark <= 100 and mark >= 0:
		marks.append(mark)
		i += 1
	else:
		print("Invalid marks! Try again.")

total = sum(marks)

ave = total / 5

if ave >= 70:
	grade = "A"
elif ave >= 60:
	grade = "B"
elif ave >= 50:
	grade = "C"
elif ave >= 40:
	grade = "D"
else:
	grade = "E"

print("Total Marks: {0}, Grade: {1}".format(total,grade))