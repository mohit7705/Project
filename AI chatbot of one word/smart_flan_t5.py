"""
smart_flan_t5.py
A short-answer Flan-T5 chatbot.

Model: google/flan-t5-base  (change to flan-t5-small if you need smaller)
Run: python smart_flan_t5.py
"""

from transformers import T5Tokenizer, T5ForConditionalGeneration
import torch
import sys

MODEL_NAME = "google/flan-t5-base"   # change to "google/flan-t5-small" if disk/RAM are limited

def load_model(name):
    print(f"Loading model {name} (this may take a minute)...")
    tokenizer = T5Tokenizer.from_pretrained(name)
    model = T5ForConditionalGeneration.from_pretrained(name)
    return tokenizer, model

def generate_short_reply(model, tokenizer, user_text, max_length=40, device="cpu"):
    # Build a short-answer prompt
    prompt = f"Answer briefly in one short sentence: {user_text}"
    inputs = tokenizer(prompt, return_tensors="pt")
    # Send tensors to device
    input_ids = inputs.input_ids.to(device)
    attention_mask = inputs.attention_mask.to(device)

    # Generate — use conservative settings for short answers
    gen = model.generate(
        input_ids=input_ids,
        attention_mask=attention_mask,
        max_length=max_length,
        num_beams=4,
        do_sample=False,        # deterministic (use True for variety)
        early_stopping=True,
        pad_token_id=tokenizer.eos_token_id
    )
    out = tokenizer.decode(gen[0], skip_special_tokens=True)
    return out.strip()

def main():
    # pick device
    device = "cuda" if torch.cuda.is_available() else "cpu"
    tokenizer, model = load_model(MODEL_NAME)
    model.to(device)
    print("Flan-T5 chatbot ready. Type 'bye' to exit.\n")

    try:
        while True:
            user = input("You: ").strip()
            if not user:
                continue
            if user.lower() in ("bye", "exit", "quit"):
                print("Bot: Goodbye!")
                break

            reply = generate_short_reply(model, tokenizer, user, device=device)
            # Keep reply short; if empty or too long, provide fallback
            if not reply:
                reply = "Sorry, I couldn't form an answer. Can you rephrase?"
            print("Bot:", reply)

    except KeyboardInterrupt:
        print("\nExiting.")
        sys.exit(0)

if __name__ == "__main__":
    main()
