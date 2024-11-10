# CGPA Calculator

A simple Python program that calculates the Cumulative Grade Point Average (CGPA) based on course marks and credit units.

## Description

This CGPA Calculator is a command-line application that:
- Takes student information (name and student number)
- Accepts marks and credit units for 4 courses
- Converts marks to letter grades
- Calculates the CGPA using a 5-point grading scale

## Features

- Input validation for marks and credit units
- Grade conversion based on the following scale:
  - 90-100: A (5 points)
  - 80-89: B (4 points)
  - 70-79: C (3 points)
  - 60-69: D (2 points)
  - 50-59: E (1 point)
  - Below 50: F (0 points)
- Precise CGPA calculation weighted by credit units
- Formatted output display

## Usage

1. Run the program:
   ```bash
   python cgpa_calculator.py
   ```

2. Follow the prompts to enter:
   - Your name
   - Student number
   - Marks for each course (1-4)
   - Credit units for each course (1-4)

3. The program will display your calculated CGPA

## Example
