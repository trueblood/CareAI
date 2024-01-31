import torch
import transformers
from transformers import LlamaForCausalLM, LlamaTokenizer
from helpers.devicehelper import DeviceHelper

class LamaModel:
    def __init__(self):
        self.model_dir = "meta-llama/Llama-2-7b-chat-hf"
        self.model = LlamaForCausalLM.from_pretrained(self.model_dir)
        device = DeviceHelper.get_device()
        self.model.to(device)  # Move the model to the specified device
        self.tokenizer = LlamaTokenizer.from_pretrained(self.model_dir)
        self.pipeline = transformers.pipeline(
            "text-generation",
            model=self.model,
            tokenizer=self.tokenizer,
            torch_dtype=torch.float16,
            device_map=device,
        )

    def generate_text(self, input_text, response_length=400):
        sequences = self.pipeline(
            input_text,
            do_sample=True,
            top_k=10,
            num_return_sequences=1,
            eos_token_id=self.tokenizer.eos_token_id,
            max_length=response_length,
        )
        return sequences[0]['generated_text']

