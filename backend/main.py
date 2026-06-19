from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException

app = FastAPI()

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

employees = []


class Employee(BaseModel):
    name: str
    email: str
    department: str


@app.get("/")
def home():
    return {"message": "Employee API Running"}


@app.post("/employees")
def create_employee(employee: Employee):
    # assign a simple incremental id and store as dict
    next_id = (employees[-1]["id"] + 1) if employees else 1
    emp_dict = {"id": next_id, "name": employee.name, "email": employee.email, "department": employee.department}
    employees.append(emp_dict)
    return {"message": "Employee added successfully", "employee": emp_dict}


@app.get("/employees")
def get_employees():
    return employees

# READ ONE
@app.get("/employees/{employee_id}")
def get_employee(employee_id: int):
    for employee in employees:
        if employee["id"] == employee_id:
            return employee

    raise HTTPException(status_code=404, detail="Employee not found")

@app.put("/employees/{employee_id}")
def update_employee(employee_id: int, updated_employee: Employee):
    for index, employee in enumerate(employees):
        if employee["id"] == employee_id:
            emp_dict = {"id": employee_id, "name": updated_employee.name, "email": updated_employee.email, "department": updated_employee.department}
            employees[index] = emp_dict
            return {"message": "Employee updated successfully", "employee": emp_dict}

    raise HTTPException(status_code=404, detail="Employee not found")