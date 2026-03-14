#!/usr/bin/env python3
"""
项目实战: 简单的任务管理器 (Todo List)
综合练习: 类、字典、列表、文件操作
"""

import json
import os
from datetime import datetime

class Task:
    def __init__(self, title, description="", priority="medium"):
        self.id = datetime.now().timestamp()
        self.title = title
        self.description = description
        self.priority = priority
        self.completed = False
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def mark_completed(self):
        self.completed = True
    
    def mark_pending(self):
        self.completed = False
    
    def __str__(self):
        status = "✓" if self.completed else "✗"
        priority_symbol = {"high": "🔴", "medium": "🟡", "low": "🟢"}
        return f"{status} [{priority_symbol.get(self.priority, '')}] {self.title}"
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "priority": self.priority,
            "completed": self.completed,
            "created_at": self.created_at
        }
    
    @classmethod
    def from_dict(cls, data):
        task = cls(data["title"], data["description"], data["priority"])
        task.id = data["id"]
        task.completed = data["completed"]
        task.created_at = data["created_at"]
        return task


class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = []
        self.load()
    
    def add_task(self, title, description="", priority="medium"):
        task = Task(title, description, priority)
        self.tasks.append(task)
        self.save()
        return task
    
    def delete_task(self, task_id):
        for i, task in enumerate(self.tasks):
            if task.id == task_id:
                self.tasks.pop(i)
                self.save()
                return True
        return False
    
    def complete_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                task.mark_completed()
                self.save()
                return True
        return False
    
    def get_pending_tasks(self):
        return [t for t in self.tasks if not t.completed]
    
    def get_completed_tasks(self):
        return [t for t in self.tasks if t.completed]
    
    def get_tasks_by_priority(self, priority):
        return [t for t in self.tasks if t.priority == priority]
    
    def list_tasks(self, filter_type="all"):
        if filter_type == "pending":
            tasks = self.get_pending_tasks()
        elif filter_type == "completed":
            tasks = self.get_completed_tasks()
        else:
            tasks = self.tasks
        
        for task in tasks:
            print(task)
    
    def save(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            data = [task.to_dict() for task in self.tasks]
            json.dump(data, f, ensure_ascii=False, indent=2)
    
    def load(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    self.tasks = [Task.from_dict(d) for d in data]
            except:
                self.tasks = []


def main():
    manager = TaskManager()
    
    print("=== 任务管理器 ===")
    print("命令: add, list, complete, delete, filter, quit")
    
    while True:
        cmd = input("\n请输入命令: ").strip().lower()
        
        if cmd == "add":
            title = input("任务标题: ").strip()
            if not title:
                print("标题不能为空")
                continue
            desc = input("任务描述: ").strip()
            priority = input("优先级 (high/medium/low): ").strip() or "medium"
            task = manager.add_task(title, desc, priority)
            print(f"✓ 已添加任务: {task.title}")
        
        elif cmd == "list":
            print("\n所有任务:")
            manager.list_tasks()
        
        elif cmd == "complete":
            task_id = input("输入任务ID完成: ").strip()
            try:
                task_id = float(task_id)
                if manager.complete_task(task_id):
                    print("✓ 任务已完成")
                else:
                    print("未找到任务")
            except ValueError:
                print("无效的ID")
        
        elif cmd == "delete":
            task_id = input("输入任务ID删除: ").strip()
            try:
                task_id = float(task_id)
                if manager.delete_task(task_id):
                    print("✓ 任务已删除")
                else:
                    print("未找到任务")
            except ValueError:
                print("无效的ID")
        
        elif cmd == "filter":
            print("筛选: pending, completed, high, medium, low")
            ftype = input("输入筛选类型: ").strip().lower()
            if ftype == "pending":
                manager.list_tasks("pending")
            elif ftype == "completed":
                manager.list_tasks("completed")
            elif ftype in ["high", "medium", "low"]:
                tasks = manager.get_tasks_by_priority(ftype)
                for t in tasks:
                    print(t)
            else:
                print("未知筛选类型")
        
        elif cmd == "quit":
            print("再见!")
            break
        
        else:
            print("未知命令")


if __name__ == "__main__":
    main()
