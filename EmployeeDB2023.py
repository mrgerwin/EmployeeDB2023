from guizero import *

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
nextButton = PushButton(buttonBox, text="Next", grid=[0,0])
saveButton = PushButton(buttonBox, text="Save", grid=[1,0])
newButton = PushButton(buttonBox, text="New", grid=[2,0])


#["Brewster.jpeg", "Danko.jpeg", "Dzierwa.jpeg", "Ferdig.jpeg", "Krabill.jpeg", "Lambert.jpeg", "Oshea.jpeg", "Roberts.png", "Ruckstuhl.jpeg"]
#["Mike", "Julie", "Matt", "Tom", "Nick", "Natalie", "Kevin", "Betsy", "Brian"]
#["Brewster", "Danko", "Dzierwa", "Ferdig", "Krabill", "Lambert", "Oshea", "Roberts", "Ruckstuhl"]
#["3562", "1324", "2049", "3420", "9463", "5603", "3420", "2304", "6707"]
#[80000,82475, 74300, 126000, 52600, 65230, 267000, 62000, 54320]
#["Science Teacher", "Social Studies Teacher", "Math Teacher", "Assistant Principal", "Math Teacher", "Spanish Teacher", "Superintendent", "Secretary", "Deputy"]
#[23, 33, 26, 18, 2, 9, 15, 16, 6]

app.display()