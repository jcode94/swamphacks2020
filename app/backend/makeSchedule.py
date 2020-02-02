import student


def makeSchedule(s=student.Student):
    choice = input("Would you like to create a schedule for you with default settings or would you like to input "
                       "manual settings? ")

    if choice == "manual":

        print(
            "Rank the following 3 options on a 1-5 scale, with 1 being 'I strongly disagree' and 5 being 'I strongly "
            "agree': 'I would like to take a rigorous courseload'; 'I would like to take courses in subjects I "
            "have had success with in the past'; 'I would like to take courses that are prerequisites for many other "
            "courses' -\n")

        coursePriorityIndex = int(input("'I would like to take a rigorous courseload': "))
        pastSuccessIndex = int(input("'I would like to take courses in subjects I have had success with in the past': "))
        bottleneckIndex = int(input("'I would like to take courses that are prerequisites for many other courses': "))

    elif choice == "default":
        totalCreditsTaken = 0
        for c in s.classes:
            totalCreditsTaken += c.credits
        if totalCreditsTaken <= 30:
            coursePriorityIndex = 2
            pastSuccessIndex = 1
            bottleneckIndex = 5
        elif totalCreditsTaken <= 60:
            coursePriorityIndex = 3
            pastSuccessIndex = 3
            bottleneckIndex = 4
        elif totalCreditsTaken <= 90:
            coursePriorityIndex = 5
            pastSuccessIndex = 4
            bottleneckIndex = 3
        else:
            coursePriorityIndex = 4
            pastSuccessIndex = 5
            bottleneckIndex = 2


    creditNumHigh = int(input("\nWhat is the maximum number of credits you would like to take your next semester? "))

    curCreditNum = 0

    courseList = []

    # CourseList is a list of courses which the student must take to graduate AND is eligible to take

    for c in courseList:
        courseRanking = coursePriorityIndex * c.difficulty + pastSuccessIndex * s.getAvg(c.category) + bottleneckIndex
        # * number of classes in CourseList this course is a prereq for
        c.curRank = courseRanking

    courseList.sort(key=lambda x: x.curRank, reverse=True)

    i = 0
    schedule = []

    while curCreditNum < creditNumHigh and i < len(courseList):
        if curCreditNum == creditNumHigh:
            break
        elif curCreditNum + courseList[i].credits > creditNumHigh:
            i += 1
            continue
        else:
            schedule.append(courseList[i])
            curCreditNum += courseList[i].credits
            course = courseList[i].pop
            updateCourseRanking(course, courseList)
    for c in schedule:
        c.curRank = 0
    for c in courseList:
        c.curRank = 0
    return schedule


def updateCourseRanking(course, courseList):
    for c in courseList:
        if course.category == c.category:
            c.curRank -= course.difficulty
        if course.difficulty > c.difficulty:
            c.curRank -= 2 * (c.difficulty - course.difficulty)
    courseList.sort(key=lambda x: x.curRank, reverse=True)

def changeSchedule(schedule, courseList):
    print("Current Schedule:")
    for c in schedule:
        print(c.name)
    choice = input("What class would you like to replace? (in format XXX ####")
    for c in schedule:
        if choice == c.name:
            courseList.append(c)
            schedule.remove(c)
            break
    choice2 = input("What class would you like to add? (in format XXX ####")
    for c in courseList:
        if choice == c.name:
            schedule.append(c)
            courseList.remove(c)
            break

