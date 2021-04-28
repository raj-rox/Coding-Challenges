#https://www.hackerrank.com/challenges/30-inheritance/problem

class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)
from statistics import mean
class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self,firstName,lastName,idNum,scores):
        self.firstName=firstName
        self.lastName=lastName
        self.idNumber=idNum
        self.scores=scores
    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        a=mean(self.scores)
        if a>=90 and a<=100:
            return "O"
        if a>=80 and a<90:
            return "E"
        if a>=70 and a<80:
            return "A"
        if a>=55 and a<70:
            return "P"
        if a>=40 and a<55:
            return "D"
        if a<40:
            return "T"
line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())