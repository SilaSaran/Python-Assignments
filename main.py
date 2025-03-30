{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "6e178bdd-1dda-4ed7-8b43-7489a2eea3d1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Employee Name: Alice\n",
      "Employee Salary: 50000\n"
     ]
    }
   ],
   "source": [
    "# main.py\n",
    "\n",
    "from employee import Employee  # Import the Employee class from the employee module\n",
    "\n",
    "# Create an instance of the Employee class\n",
    "employee = Employee(\"Alice\", 50000)\n",
    "\n",
    "# Display the employee's name and salary using the class methods\n",
    "print(\"Employee Name:\", employee.get_name())\n",
    "print(\"Employee Salary:\", employee.get_salary())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a494668c-0d9b-4dff-a8b4-e3141454ecb4",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
