from pathlib import Path


DOCUMENT_PATH = Path("documents/ai_guide.txt")


# Topics that this assistant is allowed to discuss
ALLOWED_TOPICS = [
    "artificial intelligence",
    "ai",
    "machine learning",
    "generative ai",
    "large language models",
    "llm",
    "rag",
    "retrieval",
    "embeddings",
    "chunking",
    "prompt engineering",
    "structured output",
    "json",
    "ai safety",
]


# Simple detection for clearly unsafe requests
UNSAFE_WORDS = [
    "make a bomb",
    "build a bomb",
    "make a weapon",
    "hack someone's account",
    "steal a password",
    "create malware",
]


def load_document():
    return DOCUMENT_PATH.read_text(encoding="utf-8")


def is_unsafe(question):
    question_lower = question.lower()

    return any(
        phrase in question_lower
        for phrase in UNSAFE_WORDS
    )


def is_on_topic(question):
    question_lower = question.lower()

    return any(
        topic in question_lower
        for topic in ALLOWED_TOPICS
    )


def check_guardrails(question):

    if is_unsafe(question):
        return "unsafe"

    if not is_on_topic(question):
        return "off_topic"

    return "allowed"


def main():

    question = input("Ask the AI Learning Assistant: ")

    result = check_guardrails(question)

    if result == "unsafe":
        print("\nGuardrail:")
        print("I can't help with unsafe or harmful requests.")
        return

    if result == "off_topic":
        print("\nGuardrail:")
        print(
            "This assistant only answers questions "
            "about the AI Learning Guide."
        )
        return

    print("\nRequest accepted.")
    print("The question is within the assistant's allowed topic.")

    document = load_document()

    print("\nKnowledge base loaded successfully.")
    print(f"Knowledge base size: {len(document)} characters.")


if __name__ == "__main__":
    main()