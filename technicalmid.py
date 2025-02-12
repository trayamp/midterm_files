#extra for my name hehe
print("Technical Midterm Exam")
str = input("Enter your name: ")
if str == "Justin Fernando":
    print("Student Number: 202420033")
    print("")
    print("Activity 2: Translate the given date")

#main class for the activity
def date():
    try:
        today_date = input("Enter the date: (mm/dd/yyyy): ")
        month, days, year = today_date.split("/")
#months to numbers or vice versa hadhahdahha
        months = {
            "1": "January", 
            "2": "February", 
            "3": "March", 
            "4": "April",
            "5": "May", 
            "6": "June", 
            "7": "July",
            "8": "August",
            "9": "September",
            "10": "October", 
            "11": "November", 
            "12": "December"
        }
#printing obvs(duh?!?!?)
        if month in months:
            print(f"The date is: {months[month]} {days}, {year}\n")
        else:
            print("Invalid date")
    except ValueError:
        print("Invalid input format. Please use mm/dd/yyyy.")
#idk what this is for but the rules said it should be here ah basta
if __name__ == "__main__":
#for the lutang self, call ito ng function mo or like a class pag java usapan
    date()