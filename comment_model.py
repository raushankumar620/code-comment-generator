from transformers import pipeline

# Load the pre-trained T5 model for comment generation
comment_generator = pipeline('text2text-generation', model="t5-base")

def generate_manual_comments(code):
    """
    A basic function to insert manual comments for simple code blocks like assignments, prints, etc.
    """
    lines = code.split("\n")
    commented_code = []
    
    for line in lines:
        line = line.strip()
        
        # Adding manual comments for simple operations
        if "=" in line and "==" not in line:
            commented_code.append(f"# Assigning a value to a variable\n{line}")
        elif "print" in line:
            commented_code.append(f"# Printing the value of a variable\n{line}")
        else:
            commented_code.append(line)

    return "\n".join(commented_code)


def generate_comment(code):
    """
    This function takes the input code as a string and generates meaningful comments
    using a pre-trained NLP model (T5), along with manually added comments for simple code blocks.
    """
    try:
        # First, use the manual comment generation for simple cases
        commented_code = generate_manual_comments(code)
        
        # Now, we use the NLP model to refine complex code parts
        prompt = f"Generate meaningful comments for this code:\n{code}"
        result = comment_generator(prompt)
        
        # Extract the generated comment from the result
        generated_comment = result[0]['generated_text'].strip()
        
        # Return the commented code (combining manual and NLP-based comments)
        final_commented_code = f"# {generated_comment}\n\n{commented_code}"
        
        return final_commented_code
    except Exception as e:
        print(f"Error in generating comment: {e}")
        return "Error in generating comment!"
