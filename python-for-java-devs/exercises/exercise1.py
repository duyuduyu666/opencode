#!/usr/bin/env python3
"""
练习1: 学生成绩管理系统
对比Java实现思路，用Python实现
"""

class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.scores = {}
    
    def add_score(self, subject, score):
        if 0 <= score <= 100:
            self.scores[subject] = score
            return True
        return False
    
    def get_average(self):
        if not self.scores:
            return 0
        return sum(self.scores.values()) / len(self.scores)
    
    def __str__(self):
        return f"{self.student_id} - {self.name}"


class StudentManager:
    def __init__(self):
        self.students = {}
    
    def add_student(self, student_id, name):
        if student_id in self.students:
            return False
        self.students[student_id] = Student(student_id, name)
        return True
    
    def find_student(self, student_id):
        return self.students.get(student_id)
    
    def add_score(self, student_id, subject, score):
        student = self.find_student(student_id)
        if student:
            return student.add_score(subject, score)
        return False
    
    def get_class_average(self, subject=None):
        if not self.students:
            return 0
        
        total = 0
        count = 0
        for student in self.students.values():
            if subject:
                if subject in student.scores:
                    total += student.scores[subject]
                    count += 1
            else:
                total += student.get_average() * len(student.scores)
                count += len(student.scores) if subject else 1
        
        return total / count if count > 0 else 0


def main():
    manager = StudentManager()
    
    manager.add_student("S001", "Alice")
    manager.add_student("S002", "Bob")
    manager.add_student("S003", "Charlie")
    
    manager.add_score("S001", "Math", 90)
    manager.add_score("S001", "English", 85)
    manager.add_score("S002", "Math", 78)
    manager.add_score("S002", "English", 92)
    manager.add_score("S003", "Math", 88)
    manager.add_score("S003", "English", 80)
    
    for sid in ["S001", "S002", "S003"]:
        student = manager.find_student(sid)
        print(f"{student}: 平均分 = {student.get_average():.2f}")
    
    print(f"\n班级数学平均分: {manager.get_class_average('Math'):.2f}")
    print(f"班级英语平均分: {manager.get_class_average('English'):.2f}")


if __name__ == "__main__":
    main()
