# import random

# def fetch_questions_from_text(filepath):
#     question_entries = []
#     try:
#         with open(filepath, 'r') as f:
#             content = f.read().strip()
#             question_blocks = content.split('\n\n')
            
#             for block in question_blocks:
#                 lines = block.splitlines()
#                 if len(lines) == 3:
#                     q_label, q_text = lines[0].split(':', 1)
#                     h_label, h_text = lines[1].split(':', 1)
#                     a_label, a_text = lines[2].split(':', 1)

#                     question_entries.append({
#                         'question': q_text.strip(),
#                         'human': h_text.strip(),
#                         'ai': a_text.strip()
#                     })
#     except FileNotFoundError:
#         print(f"Error: Could not locate the file at {filepath}")
#     except Exception as e:
#         print(f"An error occurred: {e}")
    
#     return question_entries

# def quiz(question_bank):
#     print("\n Guess Who Answered ")
#     print("You will show a answer, tell me HUMAN or AI given\n")

#     total_correct = 0
#     selected = random.sample(question_bank, k=min(5, len(question_bank)))

#     for idx, item in enumerate(selected, start=1):
#         correct_source = random.choice(['human', 'ai'])
#         answer_text = item[correct_source]

#         print(f"Q{idx}: {item['question']}")
#         print(f"Answer: {answer_text}")
        
#         user_input = input("Your answer (h=Human, a=AI): ").strip().lower()

#         if user_input == 'h':
#             guess = 'human'
#         elif user_input == 'a':
#             guess = 'ai'
#         else:
#             guess = None

#         if guess is None:
#             print("Wrong input, Skip this qustion\n")
#             continue

#         if guess == correct_source:
#             print("Correct answer\n")
#             total_correct += 1
#         else:
#             print(f"wrong! Correct answer : {correct_source.upper()}\n")

#     print(f"Score: {total_correct} / {len(selected)}")

# if __name__ == "__main__":
#     file_path = "quiz_simple.txt" 
#     questions = fetch_questions_from_text(file_path)

#     if questions:
#         quiz(questions)
#     else:
#         print("The question no find। Check your file")


import random

def load_questions(file):
    qlist = []
    with open(file, 'r', encoding='utf-8') as f:
        blocks = f.read().strip().split('\n\n')
        for b in blocks:
            q,h,a = '','',''
            for line in b.splitlines():
                line=line.strip()
                if line.lower().startswith('q.') or line.lower().startswith('question'):
                    q=line.split('.',1)[-1].strip()
                elif line.lower().startswith('human:'):
                    h=line.split(':',1)[-1].strip()
                elif line.lower().startswith('ai:'):
                    a=line.split(':',1)[-1].strip()
            if q and h and a: qlist.append({'q':q,'h':h,'a':a})
    return qlist

def quiz(qlist):
    score=0
    for i,item in enumerate(random.sample(qlist,min(5,len(qlist))),1):
        ans_type=random.choice(['h','a'])
        ans_text=item['h'] if ans_type=='h' else item['a']
        print(f"\nQ{i}: {item['q']}\nAnswer: {ans_text}")
        user=input("Your guess (h=Human, a=AI, exit=quit): ").lower()
        if user=='exit':
            print("Exiting quiz.")
            break
        if user==ans_type:
            print("Correct!")
            score+=1
        else:
            print(f"Wrong! Correct: {'Human' if ans_type=='h' else 'AI'}")
    print(f"\nScore: {score}/{i}")

if __name__=="__main__":
    qfile="quiz_simple.txt"
    questions=load_questions(qfile)
    if questions: quiz(questions)
    else: print("No questions found in file.")
