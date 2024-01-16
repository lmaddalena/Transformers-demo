from transformers import pipeline

classifier = pipeline("zero-shot-classification")

res = classifier(
    "This is a course about Python list comprehnsion",
    candidate_labels = ["education", "politics", "business"]
)

print(res)