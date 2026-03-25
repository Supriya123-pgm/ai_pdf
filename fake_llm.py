import random

def answer_question(context, query):
    return f"Answer based on document: {context[:200]}..."

def generate_notes(chunks):
    return "\n".join([f"- {chunk[:80]}..." for chunk in chunks[:5]])

def evaluate(answer):
    score = random.randint(5, 9)
    feedback = "Add more details." if score < 8 else "Good answer."
    return score, feedback

def improve(answer, feedback):
    return answer + f"\n\n[Improved: {feedback}]"