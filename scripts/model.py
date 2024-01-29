from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-chat-hf")
model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-7b-chat-hf")

# Example of how to use the model to generate text
inputs = tokenizer("Hello, how are you?", return_tensors="pt")
with torch.no_grad():
    outputs = model.generate(**inputs)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
