import pytest
from source.school import Classroom, Teacher, Student, TooManyStudents


# ==========================
# Fixtures
# ==========================

@pytest.fixture
def harry_potter():
    return Teacher("Harry Potter")


@pytest.fixture
def hermione_granger():
    return Student("Hermione Granger")


@pytest.fixture
def ron_weasley():
    return Student("Ron Weasley")


@pytest.fixture
def hogwarts_classroom(harry_potter):
    return Classroom(
        teacher=harry_potter,
        students=[],
        course_title="Defense Against the Dark Arts"
    )


# ==========================
# Classroom Creation
# ==========================

@pytest.mark.hogwarts
def test_classroom_creation(hogwarts_classroom):
    assert hogwarts_classroom.teacher.name == "Harry Potter"
    assert hogwarts_classroom.course_title == "Defense Against the Dark Arts"
    assert len(hogwarts_classroom.students) == 0


# ==========================
# Add Student
# ==========================

@pytest.mark.hogwarts
def test_add_student(hogwarts_classroom, hermione_granger, ron_weasley):
    hogwarts_classroom.add_student(hermione_granger)
    hogwarts_classroom.add_student(ron_weasley)

    assert len(hogwarts_classroom.students) == 2
    assert hogwarts_classroom.students[0].name == "Hermione Granger"
    assert hogwarts_classroom.students[1].name == "Ron Weasley"


# ==========================
# Too Many Students
# ==========================

@pytest.mark.hogwarts
def test_add_too_many_students(hogwarts_classroom):
    for i in range(10):
        hogwarts_classroom.add_student(Student(f"Student {i}"))

    with pytest.raises(TooManyStudents):
        hogwarts_classroom.add_student(Student("Draco Malfoy"))


# ==========================
# Remove Student
# (Expected to fail because of bug in remove_student)
# ==========================

@pytest.mark.hogwarts
@pytest.mark.xfail(reason="Bug in remove_student(): uses self.student instead of student")
def test_remove_student(hogwarts_classroom, hermione_granger, ron_weasley):
    hogwarts_classroom.add_student(hermione_granger)
    hogwarts_classroom.add_student(ron_weasley)

    hogwarts_classroom.remove_student("Hermione Granger")

    assert len(hogwarts_classroom.students) == 1
    assert hogwarts_classroom.students[0].name == "Ron Weasley"


# ==========================
# Change Teacher
# ==========================

@pytest.mark.hogwarts
def test_change_teacher(hogwarts_classroom):
    new_teacher = Teacher("Severus Snape")

    hogwarts_classroom.change_teacher(new_teacher)

    assert hogwarts_classroom.teacher.name == "Severus Snape"


# ==========================
# Parameterized Test
# ==========================

@pytest.mark.hogwarts
@pytest.mark.parametrize(
    "student_name",
    [
        "Luna Lovegood",
        "Neville Longbottom",
        "Ginny Weasley"
    ]
)
def test_parameterized_students(student_name):
    student = Student(student_name)
    assert student.name == student_name