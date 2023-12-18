from enum import Enum
from typing import  Dict
from pydantic import BaseModel

class Roles(str, Enum):
    STUDENT = "student"
    TEACHING_STAFF = "teaching_staff"
    RESEARCH_STAFF = "research_staff"
    ADMINISTRATION_STAFF = "administration_staff"

class PersonBase(BaseModel):
    id: int
    first_name: str
    last_name: str
    role: Roles

class PersonCreate(PersonBase):
    pass

class Person(PersonBase):
    class Config:
        orm_mode = True

class StudentCreate(PersonCreate):
    research_score: Dict[str, int] = {}
    academic_score: int = 0
    visited_lectures: int = 0

class Student(Person):
    research_score: Dict[str, int] = {}
    academic_score: int = 0
    visited_lectures: int = 0

class ProfessorCreate(PersonCreate):
    research_score: Dict[str, int] = {}
    academic_score: int = 0
    unique_attribute: str = ""

class Professor(Person):
    research_score: Dict[str, int] = {}
    academic_score: int = 0
    unique_attribute: str = ""

class GrantRequest(BaseModel):
    student_id: int
    professor_id: int

class Processor:
    def visit_student(self, student: Student):
        student.academic_score += 10

    def visit_professor(self, professor: Professor):
        professor.academic_score += 5

    def make_compliant(self, person: Person):
        if isinstance(person, Student):
            person.academic_score -= 5
        elif isinstance(person, Professor):
            person.academic_score -= 2
