students = [{
 'first_name' = 'Batin',
'last_name' = 'Adiguzel',
'index_number' = '35134',
'nationality' = 'Turkey',
'starting_date' = '2025-01-01',
'courses' = ['Computer security', 'Logistics','Ethics']
},
{
 'first_name' = 'Yusuf',
'last_name' = 'Hayaloglu',
'index_number' = '22768',
'nationality' = 'Turkey',
'starting_date' = '2023-11-05',
'courses' = ['Computer Science', 'Match','Ethics']
},
{
 'first_name' = 'Ahmet',
'last_name' = 'Lale',
'index_number' = '45123',
'nationality' = 'Turkey',
'starting_date' = '2022-03-12',
'courses' = ['English', 'Match','Marketing']
}
]
def add_student():
    """Adds a new student to the list by prompting for input."""
    first_name = input("Enter student's first name: ")
    last_name = input("Enter student's last name: ")
    index_number = input("Enter student's index number: ")
    nationality = input("Enter student's nationality: ")
    starting_date = input("Enter starting date (YYYY-MM-DD): ")
    courses = input("Enter courses (comma-separated): ").split(',')
    courses = [course.strip() for course in courses]

    students.append({
        'first_name': first_name,
        'last_name': last_name,
        'index_number': index_number,
        'nationality': nationality,
        'starting_date': starting_date,
        'courses': courses
    })
    print(f"Student {first_name} {last_name} added successfully.")

def display_students():
    """Displays all students in the list."""
    print("\nCurrent Students:")
    for student in students:
        print(f"Name: {student['first_name']} {student['last_name']}, Index: {student['index_number']}")
