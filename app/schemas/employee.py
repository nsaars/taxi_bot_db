from typing import Optional, List

from schemas.base import Base


class Employee(Base):
    id: int
    user_id: int
    office_id: int


class EmployeeCreate(Base):
    user_id: int
    office_id: int


class EmployeeUpdate(Base):
    user_id: Optional[int] = None
    office_id: Optional[int] = None


class Employees(Base):
    employees: List[Employee]
