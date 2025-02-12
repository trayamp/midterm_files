def main():
    birthdate = input("Input your birthdate (mm/dd/yyyy): ")
    
    try:
        # Split the input into month, day, and year
        birthmonth, birthday, birthyear = birthdate.split("/")
        
        # Dictionary for month names
        months = {
            "01": "January", "02": "February", "03": "March",
            "04": "April", "05": "May", "06": "June",
            "07": "July", "08": "August", "09": "September",
            "10": "October", "11": "November", "12": "December"
        }

        # Print the corresponding month name
        if birthmonth in months:
            print("Month:", months[birthmonth])
        else:
            print("Invalid month")

        # Display full birthdate
        print(f"Your birthdate is: {months.get(birthmonth, 'Unknown')} {birthday}, {birthyear}")
    
    except ValueError:
        print("Invalid input format. Please use mm/dd/yyyy.")
    
if __name__ == "__main__":
    main()
