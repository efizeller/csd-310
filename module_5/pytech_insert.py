from pymongo import MongoClient


url = "mongodb+srv://efraim:admin@cluster0.8qnuc.mongodb.net/pytech?retryWrites=true&w=majority"


client = MongoClient(url)


db = client.pytech

""" three student documents"""

Hank = {
    "student_id": "1007",
    "first_name": "Hank",
    "last_name": "Ronald",
    "enrollments": [
        {
            "term": "Winter",
            "gpa": "3.2",
            "start_date": "Janurary 5, 2019",
            "end_date": "June 20, 2019",
            "courses": [
                {
                    "course_id": "Cybr360",
                    "description": "Technology",
                    "instructor": "Professor Kim",
                    "grade": "A"
                },
                {
                    "course_id": "Cybr350",
                    "description": "Databases",
                    "instructor": "Professor Moore",
                    "grade": "B"
                }
            ]
        }
    ]

}


Max = {
    "student_id": "1008",
    "first_name": "Max",
    "last_name": "Shawn",
    "enrollments": [
        {
            "term": "Summer",
            "gpa": "3.4",
            "start_date": "June 25, 2019",
            "end_date": "September 15, 2019",
            "courses": [
                {
                    "course_id": "Cis310",
                    "description": "Python",
                    "instructor": "Professor Lincoln",
                    "grade": "A"
                },
                {
                    "course_id": "Cis300",
                    "description": "JavaScript",
                    "instructor": "Professor Lincoln",
                    "grade": "B"
                }
            ]
        }
    ]
}


John = {
    "student_id": "1009",
    "first_name": "John",
    "last_name": "Renolds",
    "enrollments": [
        {
            "term": "winter",
            "gpa": "2.6",
            "start_date": "Janurary 15, 2020",
            "end_date": "June 18, 2020",
            "courses": [
                {
                    "course_id": "Cybr 420",
                    "description": "forensics",
                    "instructor": "Professor red",
                    "grade": "D"
                },
                {
                    "course_id": "Cis 411",
                    "description": "Access control",
                    "instructor": "Professor red",
                    "grade": "A"
                }
            ]
        }
    ]
}

 
students = db.students


print("\n  -- INSERT STATEMENTS --")
Hank_student_id = students.insert_one(Hank).inserted_id
print("  Inserted student record Hank Ronald into the students collection with document_id " + str(Hank_student_id))

Max_student_id = students.insert_one(Max).inserted_id
print("  Inserted student record John Renolds into the students collection with document_id " + str(Max_student_id))

John_student_id = students.insert_one(John).inserted_id
print("  Inserted student record Frodo Baggins into the students collection with document_id " + str(John_student_id))

input("\n\n  End of program, press any key to exit... ")
