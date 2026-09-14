# Data Cleaning Agent using Gemini AI

A simple AI-assisted data cleaning project that uses **Google Gemini AI** and **Python Pandas** to identify and clean common data quality problems in a student dataset.

## Project Overview

The Data Cleaning Agent analyzes a messy CSV dataset and identifies common data quality issues such as:

* Missing values
* Duplicate records
* Invalid email addresses
* Invalid ages
* Invalid marks
* Inconsistent city names
* Extra spaces

Gemini AI is used to analyze the dataset and identify potential problems, while **Pandas** performs the actual data cleaning operations.

## Project Workflow

```text
messydata.csv
      ↓
Python / Pandas
      ↓
Data Profiling
      ↓
Gemini AI Analysis
      ↓
Identify Data Quality Problems
      ↓
Pandas Data Cleaning
      ↓
cleaneddata.csv
```

## Technologies Used

* Python
* Pandas
* Google Gemini AI
* Google GenAI Python SDK
* CSV

## Project Structure

```text
DataCleaningAgent/
│
├── messydata.csv
├── cleaning_agent.py
├── cleaneddata.csv
└── README.md
```

## Features

* Detects missing values
* Detects duplicate records
* Removes duplicate rows
* Removes unnecessary spaces
* Standardizes city names
* Validates age values
* Validates marks values
* Validates email addresses
* Handles missing age values
* Generates a cleaned CSV file

## Requirements

* Python 3.x
* Pandas
* Google GenAI Python SDK
* Gemini API key

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/DataCleaningAgent.git
```

Move into the project directory:

```bash
cd DataCleaningAgent
```

Install the required packages:

```bash
pip install pandas google-genai
```

## Gemini API Key

Open `cleaning_agent.py` and replace:

```python
API_KEY = "YOUR_GEMINI_API_KEY"
```

with your Gemini API key.

**Do not upload or share your actual API key on GitHub.**

## Running the Project

Run the following command:

```bash
python cleaning_agent.py
```

The program will:

1. Read `messydata.csv`
2. Analyze the dataset using Gemini AI
3. Identify data quality problems
4. Clean the dataset using Pandas
5. Save the cleaned dataset as `cleaneddata.csv`

## Input Dataset

The input file is:

```text
messydata.csv
```

It contains student information such as:

* Name
* Age
* Email
* Marks
* City

The dataset intentionally contains several data quality problems to demonstrate the cleaning process.

## Output

After running the program, the cleaned dataset is saved as:

```text
cleaneddata.csv
```

## Purpose

The main purpose of this project is to demonstrate how **Generative AI can assist in data preprocessing and data cleaning** by analyzing a dataset and identifying potential quality problems.

## Author

**Nithin Denkada**
