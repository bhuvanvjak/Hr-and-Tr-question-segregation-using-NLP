import pandas as pd

# Paths to your text files
hr_file = 'hr questions.txt'
tr_file = 'TR questions.txt'

# Function to read questions from a text file
def read_questions(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file if line.strip()]

# Read the questions from both files
hr_questions = read_questions(hr_file)
tr_questions = read_questions(tr_file)

# Create labeled DataFrames
hr_df = pd.DataFrame({'Question': hr_questions, 'Label': 'HR'})
tr_df = pd.DataFrame({'Question': tr_questions, 'Label': 'Technical'})

# Combine both DataFrames
combined_df = pd.concat([hr_df, tr_df], ignore_index=True)

# Save as a CSV file
combined_df.to_csv('interview_questions.csv', index=False)
print("Labeled dataset saved as 'interview_questions.csv'")
