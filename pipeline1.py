from transformers import pipeline

classifier = pipeline("sentiment-analysis")

res = classifier("i'm very happy to enjoy here")

print(res)

# more on transformers https://huggingface.co/docs/transformers/index
# more on pipelines https://huggingface.co/docs/transformers/main_classes/pipelines
