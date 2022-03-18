# 클래스 선언
class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name,
        self.korean = korean,
        self.math = math,
        self.english = english,
        self.science = science

# 학생 리스트
students = [
    Student("윤인성", 87, 98, 88, 95),
    Student("연하진", 92, 98, 96, 98),
    Student("구지연", 76, 96, 94, 90),
    Student("나선주", 98, 92, 96, 92),
    Student("윤아린", 95, 98, 98, 98),
    Student("운명월", 64, 88, 92, 92)
]

# Student 인스턴스의 속성에 접근하는 방법
print("students[0].name : ", students[0].name)
print("students[1].korean : ", students[1].korean)
print("students[2].math : ", students[2].math)
print("students[3].english : ", students[3].english)
print("students[4].science : ", students[4].science)