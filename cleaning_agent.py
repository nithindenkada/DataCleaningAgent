import pandas as pd
from google import genai

API_KEY = "YOUR_GEMINI_API_KEY"

client = genai.Client(api_key=API_KEY)
data = pd.read_csv("messydata.csv")
print("\nOriginal Dataset:")
print(data)

summary = f"""
You are a data cleaning agent.

Analyze the following student dataset and identify
data quality problems.

Columns:
{list(data.columns)}

Number of rows:
{len(data)}

Missing values:
{data.isnull().sum().to_dict()}

Duplicate rows:
{data.duplicated().sum()}

Sample data:
{data.to_string(index=False)}

Identify problems such as:
- Missing values
- Duplicate records
- Invalid emails
- Invalid ages
- Invalid marks
- Inconsistent city names
- Extra spaces
- Other obvious data quality problems

Give a clear list of the problems you find.
"""
response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=summary
)

print("\nGemini's Analysis:")
print(response.text)
print("\nCleaning the dataset...")

data = data.drop_duplicates()

data["Name"] = data["Name"].str.strip()
data["Email"] = data["Email"].str.strip()
data["City"] = data["City"].str.strip()
data["City"] = data["City"].str.title()
data["Age"] = pd.to_numeric(data["Age"], errors="coerce")
data["Marks"] = pd.to_numeric(data["Marks"], errors="coerce")

data.loc[(data["Age"] < 15) | (data["Age"] > 100), "Age"] = None
data.loc[(data["Marks"] < 0) | (data["Marks"] > 100), "Marks"] = None
email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

invalid_email = (
    data["Email"].notna()
    & ~data["Email"].str.match(email_pattern)
)
data.loc[invalid_email, "Email"] = None
data["Age"] = data["Age"].fillna(data["Age"].median())

data.to_csv("cleaneddata.csv", index=False)
print("\nCleaned Dataset:")
print(data)
print("\nCleaning completed successfully!")
print("Cleaned data saved to: cleaneddata.csv")