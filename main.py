{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "540cce39-7813-43df-80d5-94f3606f9b36",
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
   "id": "d7c1454a-bc22-4a94-bd28-ce3b2bbbbc6f",
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
