from transformers import pipeline

# for Initializing the text generation model
# using GPT-2 (device=0 -> CUDA; remove if no GPU)
generator = pipeline("text-generation", model="gpt2", device=0)

# Prompt to get from the user for input
prompt = input("Enter a topic or starting sentence: ").strip()

# If user didn't give input
if prompt == "":
    print("No input provided, using default.")
    prompt = "Artificial intelligence is revolutionizing the world because"

# Debugging print
print(f"Prompt received: {prompt}")

# Generating the text - set various parameters
print("\nGenerating text...\n")
generated_text = generator(
    prompt,
    max_length=150,  # Limit the text length
    num_return_sequences=1,  # Only one result
    truncation=True,  # Prevent going over the limit
    pad_token_id=50256  # GPT-2 requires this
)

# Printing the already generated result
print("Text generation complete! Here's the output:")
print(generated_text[0]["generated_text"])

# Saving e the generated text to a file
output_file = "generated_text.txt"  # File path
try:
    with open(output_file, "w") as f:
        # Writing prompt and generated text to the file
        f.write("Prompt:\n")
        f.write(prompt + "\n\n")
        f.write("Generated Text:\n")
        f.write(generated_text[0]["generated_text"])
    print(f"Generated text saved to '{output_file}'")
except Exception as e:
    # Handle file saving errors
    print(f"Error saving file: {e}")

# TO debug
print("\n[DEBUG]: Process completed.")
