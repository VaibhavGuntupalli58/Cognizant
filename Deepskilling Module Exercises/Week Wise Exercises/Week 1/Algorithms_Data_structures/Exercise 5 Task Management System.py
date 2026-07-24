class Task:
    def __init__(self, task_id, task_name, status):
        self.task_id = task_id
        self.task_name = task_name
        self.status = status
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def add_task(self, task):
        if self.head is None:
            self.head = task
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = task
    def traverse(self):
        temp = self.head
        while temp:
            print(temp.task_id, temp.task_name, temp.status)
            temp = temp.next
    def search(self, task_id):
        temp = self.head
        while temp:
            if temp.task_id == task_id:
                return temp
            temp = temp.next
        return None
    def delete(self, task_id):
        temp = self.head
        if temp and temp.task_id == task_id:
            self.head = temp.next
            return
        prev = None
        while temp:
            if temp.task_id == task_id:
                prev.next = temp.next
                return
            prev = temp
            temp = temp.next
ll = LinkedList()
ll.add_task(Task(1, "Coding", "Pending"))
ll.add_task(Task(2, "Testing", "Completed"))
ll.traverse()
