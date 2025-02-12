#extra for my name hehe
#i used char kasi ginamit ko na yung str sa baba idk di sha gumana nong ginamit ko str pero nung ginamit ko char gumana

print("Technical Midterm Exam")
char = input("Enter your name: ")
if char == "Justin Fernando":
    print("Student Number: 202420033")
    print("")
    print("Activity 1: Palindrom or Not Palindrome")

#main class for the activity - use def when defining a statement ALWAYS REMEMBER THAT
#if matanga ka at di mo alam ang palindrome - basta pag binaliktad mo yung number ganon pa rin yun na yun
def is_palindrome(number):
    "Check if a given number is a palindrome."
    str_num = str(number)
    return str_num == str_num[::-1]

def process_file(file_path):
    "Process the file and check if the sum of each line's numbers is a palindrome."
    with open(file_path, 'r') as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        numbers = list(map(int, line.strip().split(',')))
        total_sum = sum(numbers)
        result = "Palindrome" if is_palindrome(total_sum) else "Not a palindrome"
        print(f"Line {i+1}: {line.strip()} (sum {total_sum}) - {result}")

#enter where naka locate yung file na gusto i-run (tip: desktop lang para madali hanapin)
#i used r kasi read lang naman ang need
#REMEMEBER: 
#1. r+: Opens the file for both reading and writing.
#2. w+: Opens the file for reading and writing, but it overwrites the file 
#3. rb+: Opens the file in binary mode for reading and writing.
#4. w: Opens the file for writing only
file_path = r"C:\Users\itzyo\OneDrive\Desktop\numbers.txt"
#call mo yung file
process_file(file_path)