from guizero import *

def openPressed():
    global picList, fnameList, lnameList, enList, salList, jobList, yearsList
    picList = []
    fnameList = []
    lnameList = []
    enList = []
    salList = []
    jobList = []
    yearsList = []
    employeeList=[]
    f = open(filename, "r")
    data = f.readlines()
    for row in data:
        employeeList.append(row.split(","))
    f.close()
    for employee in employeeList:
        picList.append(employee[0])
        fnameList.append(employee[1])
        lnameList.append(employee[2])
        enList.append(employee[3])
        salList.append(employee[4])
        jobList.append(employee[5])
        yearsList.append(employee[6])

def savePressed():
    
    f = open(filename, "a")
    
    f.write("Default.png,"+firstNameText.value+","+lastNameText.value+","+ employeeNumText.value+ "," + salaryText.value + ","+jobText.value+","+yearsText.value+"\n")
    
    f.close()
    saveButton.enabled = False
def newPressed():
    pic.value = "Default.png"
    firstNameText.value = ""
    lastNameText.value = ""
    employeeNumText.value = ""
    salaryText.value = ""
    jobText.value = ""
    yearsText.value = ""
    saveButton.enabled = True

def nextPressed():
    global index
    index += 1
    if index == len(lnameList):
        index = 0
    
    pic.value = picList[index]
    firstNameText.value = fnameList[index]
    lastNameText.value = lnameList[index]
    employeeNumText.value = enList[index]
    salaryText.value = salList[index]
    jobText.value = jobList[index]
    yearsText.value = yearsList[index]
    saveButton.enabled = False

app = App(title="Employee Database", width = 450, height = 600, layout="grid")

pic = Picture(app, image="./Default.png", grid=[0,0, 2, 1])

firstNameBox = TitleBox(app, "First Name", grid=[0,1])
firstNameText = TextBox(firstNameBox, width=20)

lastNameBox = TitleBox(app, "Last Name", grid=[1,1])
lastNameText=TextBox(lastNameBox, width=20)

employeeNumBox = TitleBox(app, "Employee Number", grid=[0,2])
employeeNumText =TextBox(employeeNumBox, width=10)

salaryBox=TitleBox(app, "Salary", grid=[1,2])
salaryText=TextBox(salaryBox, width=15)

jobBox=TitleBox(app, "Job Title", grid=[0,3])
jobText=TextBox(jobBox, width=15)

yearsBox= TitleBox(app, "Years Experience", grid=[1,3])
yearsText= TextBox(yearsBox, width=15)

buttonBox = TitleBox(app, "Buttons", layout="grid", grid=[0,4,2,1])
nextButton = PushButton(buttonBox, text="Next", grid=[0,0], command = nextPressed)
saveButton = PushButton(buttonBox, text="Save", grid=[1,0], command = savePressed)
newButton = PushButton(buttonBox, text="New", grid=[2,0], command = newPressed)
openButton = PushButton(buttonBox, text="Open", grid=[3,0], command = openPressed)

filename = "Data.txt"
index = 0
picList=["Brewster.jpeg", "Danko.jpeg", "Dzierwa.jpeg", "Ferdig.jpeg", "Krabill.jpeg", "Lambert.jpeg", "Oshea.jpeg", "Roberts.png", "Ruckstuhl.jpeg"]
fnameList=["Mike", "Julie", "Matt", "Tom", "Nick", "Natalie", "Kevin", "Betsy", "Brian"]
lnameList=["Brewster", "Danko", "Dzierwa", "Ferdig", "Krabill", "Lambert", "Oshea", "Roberts", "Ruckstuhl"]
enList=["3562", "1324", "2049", "3420", "9463", "5603", "3420", "2304", "6707"]
salList=[80000,82475, 74300, 126000, 52600, 65230, 267000, 62000, 54320]
jobList=["Science Teacher", "Social Studies Teacher", "Math Teacher", "Assistant Principal", "Math Teacher", "Spanish Teacher", "Superintendent", "Secretary", "Deputy"]
yearsList=[23, 33, 26, 18, 2, 9, 15, 16, 6]

app.display()