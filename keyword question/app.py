import json

# Load data
with open("data.txt", "r", encoding="utf-8") as f:
    data = json.load(f)

# Count keyword frequencies
keyword_frequency = {}
for item in data:
    for kw in item["keywords"]:
        word = kw.lower()
        keyword_frequency[word] = keyword_frequency.get(word, 0) + 1

def ask_question():
    question = input('\nType your question (or "exit" to quit): ').lower()

    if question == "exit":
        print("\nGoodbye!")
        return

    matched_answers = set()

    for item in data:
        # Use only keywords that appear once globally
        unique_keywords = [kw for kw in item["keywords"] if keyword_frequency[kw.lower()] == 1]

        # Count how many unique keywords appear in the question
        matched = [kw for kw in unique_keywords if kw.lower() in question]

        # Require at least 2 matches to accept the answer
        if len(matched) >= 2:
            matched_answers.add(item["answer"])

    if matched_answers:
        print("\nMatched Answers:")
        for ans in matched_answers:
            print(ans)
    else:
        print("No valid answer found.")

    # Ask next question
    ask_question()

print("Smart Lookup System")
ask_question()
