import torch
import transformers
from transformers import LlamaForCausalLM, LlamaTokenizer


def main():
    model_dir = "./llama-2-7b-chat-hf"
    model = LlamaForCausalLM.from_pretrained(model_dir)
    tokenizer = LlamaTokenizer.from_pretrained(model_dir)
    max_length_of_response = 400

    pipeline = transformers.pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        torch_dtype=torch.float16,
        device_map="auto",
    )

    sequences = pipeline(
        'I have tomatoes, basil and cheese at home. What can I cook for dinner?\n',
        do_sample=True,
        top_k=10,
        num_return_sequences=1,
        eos_token_id=tokenizer.eos_token_id,
        max_length=max_length_of_response,
    )

    for seq in sequences:
        print(f"{seq['generated_text']}")







'''import torch
from llama.models import LlamaForCausalLM
from llama.tokenizers import LlamaTokenizer
from llama.pipelines import Pipeline

model = LlamaForCausalLM.from_pretrained("meta-ai/llama-2-7b-chat")

tokenizer = LlamaTokenizer.from_pretrained("meta-ai/llama-2-7b-chat")
prompt = "Write a story about a cat and a dog."
inputs = tokenizer(prompt, return_tensors="pt")

pipeline = Pipeline(model=model, tokenizer=tokenizer)
outputs = pipeline(inputs)
generated_text = outputs["generated_text"]

print(generated_text)'''
