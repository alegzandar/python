class Person:
    def __init__(self, Name, Age, Sex, Agenda, Bio):
            self.Name=Name
            self.Age=Age
            self.Sex=Sex
            self.Agenda=Agenda
            self.Bio=Bio
i=0
PersonalBook=[]
Entry=input("""
    What would you like to do?
    \'C\' - Create new record
    \'E\' - Edit existing data with ID
    \'R\' - Remove person by ID
    \'V\' - View ALL data or someone's personal data by ID
    \'W\' - Write current content to the local PersonalBook.txt file
    \"EXIT"\" - to exit the program
    NOTE: letters are not case-sensivive 'c' instead of 'C' will work as well
    >>>""").split()
while Entry[0].lower()!='exit':
    if Entry[0].lower()=='c':
        Entry=input("""
    Enter person\' data separated by \', \' as it follows:
    -Name
    -Age
    -Gender
    -Agenda
    -Bio
>>>""").split(', ')
        if len(Entry)==5:
            PersonalBook.append(Person(Entry[0],Entry[1],Entry[2],Entry[3],Entry[4]))
            i+=1
        else:
            print('insufficient or wrong Input') 
        print()
    elif Entry[0].lower()=='v':
        for person in PersonalBook:
            Entry=input('would you like to view \'ALL\' data or someone specific - by \'ID\'?').split()
            if Entry[0].lower()=='all':
                ID=1
                for Person in PersonalBook:
                    print("""
The ID of this person is: {}
    Name: {}
    Age: {}
    Gender: {}
    Agenda: {}  
    Bio: {}""".format(ID, Person.Name,Person.Age,Person.Sex,Person.Agenda,Person.Bio))
                    ID+=1
            elif Entry[0].lower()=='id':
                Entry = input("what's the ID, starting from 1 :")
                ID=int(Entry[0])
                print("""
    Name: {}
    Age: {}
    Gender: {}
    Agenda: {}
    Bio: {}""".format(PersonalBook[ID-1].Name,PersonalBook[ID-1].Age,PersonalBook[ID-1].Sex,PersonalBook[ID-1].Agenda,PersonalBook[ID-1].Bio))
    elif Entry[0].lower()=='e':
        Entry=input('Could you please enter the needed information in the specified format: \'ID:Attribute:Changed Information\' >>> ').split(':')
        ID=int(Entry[0])-1
        Attribute=Entry[1]
        Change=Entry[2]
        if Attribute.lower()=='name':
            PersonalBook[ID].Name=Change
            print('Changed succesfully!')
        elif Attribute.lower()=='age':
            PersonalBook[ID].Age=Change
            print('Changed succesfully!')
        elif Attribute.lower()=='gender':
            PersonalBook[ID].Gender=Change
            print('Changed succesfully!')
        elif Attribute.lower()=='agenda':
            PersonalBook[ID].Agenda=Change
            print('Changed succesfully!')
        elif Attribute.lower()=='bio':
            PersonalBook[ID].Bio=Change
            print('Changed succesfully!')
        else: 
            print('you\'ve entered wrong attribute')
    elif Entry[0].lower()=='r':
        ID=int(input('what\'s the ID of the person you\'d like to remove: '))
        PersonalBook.pop(ID-1)
        print('succesfully removed the person under ID: {}'.format(ID))
    elif Entry[0].lower()=='w':
        ID=0
        f = open("PersonalBook.txt","w+")
        for Person in PersonalBook:
            f.write("""
    The ID of this person is: {}
    Name: {}
    Age: {}
    Gender: {}
    Agenda: {}
    Bio: {}
    \n""".format(ID, Person.Name,Person.Age,Person.Sex,Person.Agenda,Person.Bio))
            ID+=1
        f.close()
        print('written successfully')
    Entry=input(
    """What would you like to do NEXT?
    \'C\' - Create new record
    \'E\' - Edit existing data with ID
    \'R\' - Remove person by ID
    \'V\' - View ALL data or someone's personal by ID
    \'W\' - Write current data to the local PersonalBook.txt file
    \"EXIT"\" - to exit the program
    >>>""").split()
