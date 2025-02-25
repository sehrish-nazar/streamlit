import streamlit as st
import pandas as pd

# Load quiz data
def load_quiz_data():
    data = pd.read_csv('data/quiz_data.csv')
    return data

# Display the quiz
def display_quiz(data):
    score = 0
    total_questions = len(data)

    for index, row in data.iterrows():
        st.write(f"**Q{index + 1}: {row['question']}**")
        options = [row['option1'], row['option2'], row['option3'], row['option4']]
        answer = st.radio("Choose an option:", options, key=index)

        if st.button("Submit", key=f"submit_{index}"):
            if answer == row['answer']:
                st.success("Correct!")
                score += 1
            else:
                st.error("Incorrect!")

    st.write(f"Your score: {score}/{total_questions}")

# Main function
def main():
    st.title("Quiz Master")
    st.write("Welcome to the Quiz! Let's see how much you know.")

    quiz_data = load_quiz_data()
    display_quiz(quiz_data)

if __name__ == "__main__":
    main()
