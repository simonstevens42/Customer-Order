from enum import Enum


class Staff:
    __global_id: int = 0

    # constructor
    def __init__(self, last_name: str):
        Staff.__global_id += 1
        self.__staff_id = Staff.__global_id
        self.__last_name = last_name
        self.__tasks = []

    # setter / getter
    def set_staff_id(self, new_id: int) -> None:
        if new_id > Staff.__global_id:
            self.__staff_id = new_id
            Staff.__global_id = new_id
        else:
            print(F"Id {new_id} is not available.")

    def get_staff_id(self) -> int:
        return self.__staff_id

    def set_last_name(self, last_name) -> None:
        self.__last_name = last_name

    def get_last_name(self) -> str:
        return self.__last_name

    def set_tasks(self, tasks: list) -> None:
        self.__tasks = tasks

    def get_tasks(self) -> list:
        return self.__tasks

    # methods
    def add_task(self, task_id: int) -> None:
        self.__tasks.append(task_id)

    def remove_task(self, task_id: int) -> None:
        self.__tasks.remove(task_id)

    def show_task(self) -> None:
        if len(self.__tasks) > 0:
            task_dic = Task.get_global_list()
            for task in self.__tasks:
                for key, value in task_dic.items():
                    if value == task:
                        print(F"Name: {key.get_name()}")
                        print(F"Id: {key.get_task_id()}")
                        print(F"Time: {key.get_time_estimation()}")
                        print(F"Status: {Status.staus_name(key.get_status())}")
        else:
            print(F"No tasks assigned to {self.__last_name}.")

    @staticmethod
    def get_global_id() -> int:
        return Staff.__global_id


class Status(Enum):
    ASSIGNED = 0
    OPEN = 1
    DONE = 2

    @staticmethod
    def staus_name(number: int) -> str:
        for status in Status:
            if status.value == number:
                return status.name
        return "Status not found."


class Task:
    __global_id: int = 0
    __global_list: dict = {}

    # constructor
    def __init__(self, name: str, time_estimation: float, status: int, staff: list):
        Task.__global_id += 1
        self.__task_id = Task.__global_id
        self.__name = name
        self.__time_estimation = time_estimation
        self.__staff = staff
        Task.__global_list[self] = Task.__global_id

        if status == 0 or status == 1 or status == 2:
            self.__status = status
        else:
            self.__status = 0

        if len(staff) > 0:
            self.__staff = staff
            for human in staff:
                human.add_task(self.__task_id)
        else:
            del self
            print("Object was not initialized because it was not assigned to a staff member.")

    # destructor
    def __del__(self):
        for human in self.__staff:
            human.remove_task(self.__task_id)
        del Task.__global_list[self]
        print(F"Task {self.__task_id} has been deleted.")

    # setter / getter
    def set_task_id(self, new_id) -> None:
        if new_id > Task.__global_id:
            for human in self.__staff:
                human.remove_task(self.__task_id)
                human.add_task(new_id)
            self.__task_id = new_id
            Task.__global_list[self] = self.__task_id
            Task.__global_id = new_id

        else:
            print(F"Id {new_id} is not available.")

    def get_task_id(self) -> int:
        return self.__task_id

    def set_name(self, name: str) -> None:
        self.__name = name

    def get_name(self) -> str:
        return self.__name

    def set_time_estimation(self, time_estimation: float) -> None:
        self.__time_estimation = time_estimation

    def get_time_estimation(self) -> float:
        return self.__time_estimation

    def set_status(self, status: int) -> None:
        if status == 0 or status == 1 or status == 2:
            self.__status = status
        else:
            print("No status found.")

    def get_status(self) -> int:
        return self.__status

    def set_staff(self, staff: list) -> None:
        if len(staff) > 0:
            for human in self.__staff:
                human.remove_task(self.__task_id)
            self.__staff = staff
            for human in staff:
                human.add_task(self.__task_id)
        else:
            print("No valid staff list.")

    def get_staff(self) -> list:
        return self.__staff

    # methods
    def delete_task(self) -> None:
        del self

    def update_status(self, status: int) -> None:
        if status == 0 or status == 1 or status == 2:
            self.__status = status
        else:
            print(F"Status with the number {status} not found.")

    @staticmethod
    def get_global_id() -> int:
        return Task.__global_id

    @staticmethod
    def get_global_list() -> dict:
        return Task.__global_list
