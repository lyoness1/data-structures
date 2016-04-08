def unique_houses(filename):
    """TODO: Create a set of student houses.

    Iterates over the cohort_data.txt file to look for all of the included house names
    and creates a set called 'houses' that holds those names.

        ex. houses = set([ "Hufflepuff",
                    "Slytherin",
                    "Ravenclaw",
                    "Gryffindor",
                    "Dumbledore's Army",
                    "Order of the Phoenix"
            ])

    """
    data = open("cohort_data.txt")
    #create an empty set
    houses = set()

    #read each line in from the file
    for line in data:
        #split the line based on | and put it into person
        person = line.split('|')
        #error checking for empty spaces
        if len(person[2]) > 1:

            houses.add(person[2])

    data.close()
    return houses


def sort_by_cohort(filename):
    """TODO: Sort students by cohort.

    Iterates over the data to create a list for each cohort, ordering students
    alphabetically by first name and ta's separately. Returns list of lists.

        ex. winter_15 = ["alice tsao", "amanda gilmore", "anne vetto", "..." ]
        ex. all_students = [winter_15, spring_15, summer_15, tas]

    """
    data = open("cohort_data.txt")
    
    
    all_students = []
    winter_15 = []
    spring_15 = []
    summer_15 = []
    tas = []

    for line in data:    
        fileline = line.rstrip()
        person = fileline.split('|')    
        if person[4] == 'Winter 2015':
            winter_15.append(person[0] + ' ' + person[1])
        elif person[4] == 'Spring 2015':
            spring_15.append(person[0] + ' ' + person[1])
        elif person[4] == 'Summer 2015':
            summer_15.append(person[0] + ' ' + person[1])
        elif person[4] == 'TA':
            tas.append(person[0] + ' ' + person[1])

    winter_15.sort()
    spring_15.sort()
    summer_15.sort()
    tas.sort()
    
    all_students.append(winter_15)
    all_students.append(spring_15)
    all_students.append(summer_15)
    all_students.append(tas)

    return all_students


def students_by_house(filename):
    """TODO: Sort students by house.

    Iterate over the data to create a list for each house, and sort students
    into their appropriate houses by last name. Sort TAs into a list called "tas"
    and instructors in to a list called "instructors".
    Return all lists in one list of lists.
        ex. hufflepuff = ["Gaikwad", "Le", "..." ]
        ex. tas = ["Bryant", "Lefevre", "..."]
        ex. all_students = [ hufflepuff,
                        gryffindor,
                        ravenclaw,
                        slytherin,
                        dumbledores_army,
                        order_of_the_phoenix,
                        tas,
                        instructors
            ]
    """
    data = open("cohort_data.txt")
    
    all_students = []
    gryffindor = []
    hufflepuff = []
    slytherin = []
    dumbledores_army = []
    order_of_the_phoenix = []
    ravenclaw = []
    tas = []
    instructors = []

    for line in data:    
        fileline = line.rstrip()
        person = fileline.split('|')    
        if person[2] == 'Gryffindor':
            gryffindor.append(person[1] + ', ' + person[0])
        elif person[2] == 'Hufflepuff':
            hufflepuff.append(person[1] + ', ' + person[0])
        elif person[2] == 'Slytherin':
            slytherin.append(person[1] + ', ' + person[0])
        elif person[2] == 'Dumbledore\'s Army':
            dumbledores_army.append(person[1] + ', ' + person[0])
        elif person[2] == 'Order of the Phoenix':
            order_of_the_phoenix.append(person[1] + ', ' + person[0])
        elif person[2] == 'Ravenclaw':
            ravenclaw.append(person[1] + ', ' + person[0])
        elif person[4] == 'TA':
            tas.append(person[1] + ', ' + person[0])
        elif person[4] == 'I':
            instructors.append(person[1] + ', ' + person[0])

    gryffindor.sort()
    hufflepuff.sort()
    slytherin.sort()
    dumbledores_army.sort()
    order_of_the_phoenix.sort()
    ravenclaw.sort()
    tas.sort()
    instructors.sort()

    all_students.append(gryffindor)
    all_students.append(hufflepuff)
    all_students.append(slytherin)
    all_students.append(dumbledores_army)
    all_students.append(order_of_the_phoenix)
    all_students.append(ravenclaw)
    all_students.append(tas)
    all_students.append(instructors)

    data.close()
    
    return all_students


def all_students_tuple_list(filename):
    """TODO: Create a list of tuples of student data.

    Iterates over the data to create a big list of tuples that individually
    hold all the data for each person. (full_name, house, advisor, cohort)
        ex. all_people = [
                ("Alice Tsao", "Slytherin", "Kristen", "Winter 2015"),
                ("Amanda Gilmore", "Hufflepuff", "Meggie", "Winter 2015"),
                # ...
            ]
    """
    data = open("cohort_data.txt")

    student_list = []

    for line in data:
        fileline = line.rstrip()
        person = fileline.split('|') 
        student_list.append( (person[0]+" " + person[1], person[2], person[3], person[4]))

    data.close()
    return student_list


def find_cohort_by_student_name(student_list):
    """TODO: Given full name, return student's cohort.

    Use the above list of tuples generated by the preceding function to make a small
    function that, given a first and last name, returns that student's cohort, or returns
    'Student not found.' when appropriate. """

    full_name = raw_input("For which student would you like to find the cohort (full name): ")
    
    for person in student_list:
        if full_name == person[0]:
            return person[1]
        else: 
            print 'Student no found'

    return "Student not found."


##########################################################################################
# Further Study Questions


def find_name_duplicates(filename):
    """TODO: Using set operations, make a set of student first names that have duplicates.

    Iterates over the data to find any first names that exist across multiple cohorts.
    Uses set operations (set math) to create a set of these names.
    NOTE: Do not include staff -- or do, if you want a greater challenge.

       ex. duplicate_names = set(["Sarah"])

    """

    duplicate_names = set()

    # Code goes here

    return duplicate_names


def find_house_members_by_student_name(student_list):
    """TODO: Create a function that prompts the user for a name via the command line
    and when given a name, print a statement of everyone in their house in their cohort.

    Use the list of tuples generated by all_students_tuple_list to make a small function
    that, when given a student's first and last name, print students that are in both
    that student's cohort and that student's house."""

    # Code goes here

    return


#########################################################################################

# Here is some useful code to run these functions!


#print unique_houses("cohort_data.txt")
#print sort_by_cohort("cohort_data.txt")
# print students_by_house("cohort_data.txt")
all_students_data = all_students_tuple_list("cohort_data.txt")
find_cohort_by_student_name(all_students_data)
# print find_name_duplicates("cohort_data.txt")
# find_house_members_by_student_name(all_students_data)
