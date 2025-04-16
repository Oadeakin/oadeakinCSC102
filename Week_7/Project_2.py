cs_admitted = []
cs_not_admitted = []
mass_com_admitted = []
mass_com_not_admitted = []

cont = "yes"
while cont == "yes":
    info = {
        "Student_Name": name,
        "Department": department,
        "Jamb Score": jamb_score,
        "Interview": interview,

    }
    name = str(input("Enter your full name: "))
    jamb_score = int(input("Enter your Jamb score: "))
    department = str("Computer Science/Mass Communication: ")
    waec_score = int(input("How many credits did you get: "))
    interview = int(input("Did you pass the interview(yes/no)")).lower()

    if department == "Computer Science":
        if jamb_score >= 250 and waec_score >=5 and interview == "yes":
            print("Congratulations on your admission")
            cs_admitted.append(info)

        else:
            print("Not admitted")
            cs_not_admitted.append(info)
        cont = input("Is there anymore entry(yes/no): ")
    
        if department == "Mass Communication":
            if jamb_score >= 230 and waec_score >=5 and interview == "yes":
                print("Congratulations on your admission")
                mass_com_admitted.append(info) 
            else:
                print("Not admitted")
                mass_com_not_admitted.append(info) 
        cont = input("Is there anymore entry(yes/no): ")

    else:
        print("Invalid Entry")
        cont = input("Is there anymore entry(yes/no): ")

print("Admissions List\n Computer Science Admitted")
for applicants in cs_admitted:
    print(applicants, end="")
print()
print("Not Admitted")
for applicants in cs_not_admitted:
    print(applicants, end="")
print("Admissions List\n Mass Communication Admitted")
for applicants in mass_com_admitted:
    print(applicants, end="")
print()
print("Not admitted")
for applicants in mass_com_not_admitted:
    print(applicants, end="")