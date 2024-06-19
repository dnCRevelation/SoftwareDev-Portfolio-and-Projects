import torch
import matplotlib.pyplot as plt
import textwrap
from pandas import DataFrame
from trl import SFTTrainer
from datasets import load_dataset
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments 

# Load the dataset
train_dataset = load_dataset("tatsu-lab/alpaca", split="train")
print(train_dataset)

# Converting the Dict Into a DataFrame and Displaying the First 5 Rows
pandas_format = train_dataset.to_pandas()
print(pandas_format.head())

# Better Visualization of Data
for index in range(3):
    print("---"*15)
    print("Instruction: {}".format(textwrap.fill(pandas_format.iloc[index]["instruction"], width=50)))
    print("Text: {}".format(textwrap.fill(pandas_format.iloc[index]["text"], width=50)))

# Load the model and tokenizer
pretrained_model_name = "Salesforce/xgen-7b-8k-base"
model = AutoModelForCausalLM.from_pretrained(pretrained_model_name, torch_dtype=torch.bfloat16)
tokenizer = AutoTokenizer.from_pretrained(pretrained_model_name, trust_remote_code=True)

# Training Arguments
model_training_args = TrainingArguments(
    output_dir="xgen-7b-8k-base-fine-tuned",
    per_device_train_batch_size=4,
    optim="adamw_torch",
    logging_steps=80,
    learning_rate=2e-4,
    warmup_ratio=0.1,
    lr_scheduler_type="linear",
    num_train_epochs=1,
    save_strategy="epoch"
)

# SFT Trainer
pandas_format['text_length'] = pandas_format['text'].apply(len)

plt.figure(figsize=(10,6))
plt.hist(pandas_format['text_length'], bins=50, alpha=0.5, color='g')
plt.annotate('Max Length: {}', xy=(pandas_format['text_length'].max(), 1000), xytext=(pandas_format['text_length'].max() + 100, 1000))
plt.title('Distribution of Text Length')
plt.xlabel('Length of Text')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# Distribution Length of Text
mask = pandas_format['text_length'] > 1024
percentage = (mask.sum() / pandas_format['text_length'].count()) * 100

print(f"The Percentage of Texts with Length greater than 1024 is: {percentage}%")

# Training the Model

SFT_trainer = SFTTrainer(
    model=model,
    train_dataset=train_dataset,
    dataset_text_field="text",
    max_seq_length=1024,
    tokenizer=tokenizer,
    args=model_training_args,
    packing=True,
    peft_config=lora_peft_config,
)

# Training Execution
tokenizer.pad_token = tokenizer.eos_token
model.resize_token_embeddings(len(tokenizer))
model = prepare_model_for_kbit_training(model)
model = get_peft_model(model, lora_peft_config)
training_args = model_training_args
trainer = SFT_trainer 
trainer.train()
      