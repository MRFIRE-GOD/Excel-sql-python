import mysql.connector as conn

#connect to server
db=conn.connect(host="localhost",user="root",password="password")
cursor=db.cursor()
#create database
cursor.execute("""CREATE DATABASE IF NOT EXISTS Testdb""")
db.commit()
#use database
cursor.execute("""USE Testdb""")
db.commit()
#create Teacher table
cursor.execute("""CREATE TABLE IF NOT EXISTS Teacher(
    TeacherUsername VARCHAR(255) PRIMARY KEY,
    TeacherPassword TEXT)""")
db.commit()
#create student table
cursor.execute("""CREATE TABLE IF NOT EXISTS Student(
    StudentNo INT PRIMARY KEY,
    StudentSurname TEXT,
    StudentForename TEXT,
    StudentTeacher VARCHAR(255),
    StudentPassword TEXT,
    FOREIGN KEY(StudentTeacher) REFERENCES Teacher(TeacherUsername))""")
db.commit()
#create exam table
cursor.execute("""CREATE TABLE IF NOT EXISTS Exam(
    TestName VARCHAR(255) PRIMARY KEY,
    TestTotalMarks TEXT,
    Teacher VARCHAR(255),
    FOREIGN KEY(Teacher) REFERENCES Teacher(TeacherUsername))""")
db.commit()
#create StudentExam table
cursor.execute("""CREATE TABLE IF NOT EXISTS StudentExam(
    TestName VARCHAR(255),
    StudentID INT,
    StudentTotalMarks INT,
    PRIMARY KEY(TestName,StudentID),
    FOREIGN KEY(TestName) REFERENCES Exam(TestName),
    FOREIGN KEY(StudentID) REFERENCES Student(StudentID))""")
db.commit()
#create ExamSection table
cursor.execute("""CREATE TABLE IF NOT EXISTS ExamSection(
    TestName VARCHAR(255),
    SectionID INT,
    PRIMARY KEY(TestName,SectionID),
    FOREIGN KEY(TestName) REFERENCES Exam(TestName),
    FOREIGN KEY(SectionID) REFERENCES Section(SectionID))""")
db.commit()
#create Section table
cursor.execute("""CREATE TABLE IF NOT EXISTS Section(
    SectionID INT PRIMARY KEY,
    SectionName TEXT,
    SectionTotalMarks INT)""")
db.commit()
#create Question table
cursor.execute("""CREATE TABLE IF NOT EXISTS Question(
    QuestionID INT PRIMARY KEY,
    SectionID VARCHAR(255),
    Image TEXT,
    Question TEXT,
    PossibleAnswer TEXT,
    CorrectAnswer TEXT,
    QuestionType TEXT,
    FOREIGN KEY(SectionID) REFERENCES Section(SectionID))""")
db.commit()
#create QuestionResults Table
cursor.execute("""CREATE TABLE IF NOT EXISTS QuestionResults(
    QuestionID INT,
    StudentID INT,
    SectionID VARCHAR(255),
    StudentAnswer TEXT,
    PRIMARY KEY(QuestionID,StudentID),
    FOREIGN KEY(QuestionID) REFERENCES Question(QuestionID)
    FOREIGN KEY(StudentID) REFERENCES Student(StudentID))""")
db.commit()
#create Revision table
cursor.execute("""CREATE TABLE IF NOT EXISTS Revision(
    RevisionID INT PRIMARY KEY,
    RevisionSheet TEXT,
    TeacherUsername VARCHAR(255),
    FOREIGN KEY(TeacherUsername) REFERENCES Teacher(TeacherUsername))""")
db.commit()
#create StudentRevition table
cursor.execute("""CREATE TABLE IF NOT EXISTS StudentRevision(
    RevisionID INT,
    StudentID INT,
    PRIMARY KEY(RevisionID,StudentID),
    FOREIGN KEY(RevisionID) REFERENCES Revision(RevisionID),
    FOREIGN KEY(StudentID) REFERENCES Student(StudentID))""")
db.commit()
#create StudentResults table
cursor.execute("""CREATE TABLE IF NOT EXISTS StudentResults(
    SectionID VARCHAR(255),
    StudentID INT,
    StudentSectionMarks INT,
    PRIMARY KEY(SectionID,StudentID),
    FOREIGN KEY(SectionID) REFERENCES Section(SectionID),
    FOREIGN KEY(StudentID) REFERENCES Student(StudentID))""")
db.commit()
cursor.close()         