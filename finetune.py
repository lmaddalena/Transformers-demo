# 1. prepare dataset
# 2. load pretrained tokenizer. call it with dataset -> encodings
# 3. build PyTorch (or Tensorflow) Dataset with encodings
# 4. load pretrained Model
# 5. a) Load Trainer and train it
#    b) native PyTorch training loop



# from transformers import Trainer, TrainingArguments
# 
# training_args = TrainingArguments("test-trainer")
# 
# trainer = Trainer (
#     model,
#     training_args,
#     train_dataset = tokenized_datasets["train"],
#     eval_dataset = tokenized_datasets["validation"],
#     data_collator = data_collator,
#     tokenizer = tokenizer
# )
# 
# trainer.Train()




