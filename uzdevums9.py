from transformers import pipeline, set_seed
import torch

def generate_story(sakuma_fraze, max_garums=100):
    generator = pipeline('text-generation', 
                        model='gpt2',
                        device=0 if torch.cuda.is_available() else -1)
    
    set_seed(42)
    
    rezultats = generator(sakuma_fraze, 
                         max_length=max_garums,
                         min_length=30,
                         truncation=True,
                         num_return_sequences=1,
                         temperature=0.3,
                         do_sample=True,
                         top_k=10,
                         top_p=0.7,
                         repetition_penalty=1.5)
    
    return rezultats[0]['generated_text']

sakuma_fraze = "Reiz kādā tālā zemē..."
stasts = generate_story(sakuma_fraze)
print(stasts)