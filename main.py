from classes import *
import gc

gc.enable()

staff1 = Staff("Stevens")
staff2 = Staff("Johner")
staff3 = Staff("Urban")

staff1.show_task()

task1 = Task("LF08 homework", 5, 0, [staff1])

task2 = Task("LF08 exam", 5, 0, [staff1])

staff1.show_task()

staff2.add_task(task2.get_task_id())

staff2.show_task()


staff2.show_task()
