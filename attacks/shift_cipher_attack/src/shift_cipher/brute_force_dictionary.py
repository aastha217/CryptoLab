# brute_force_dictionary.py
import os
from shift_cipher import decrypt

def load_dictionary(filename):
    """Load dictionary from file, create if doesn't exist"""
    words = set()
    
    # Check if file exists
    if not os.path.exists(filename):
        print(f"Dictionary file not found at: {filename}")
        print("Creating a new dictionary file...")
        
        # Create the directory if it doesn't exist
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        
        # Create sample dictionary
        sample_words = [
            'hello', 'world', 'the', 'be', 'to', 'of', 'and', 'a', 'in', 'that',
            'have', 'i', 'it', 'for', 'not', 'on', 'with', 'he', 'as', 'you',
            'do', 'at', 'this', 'but', 'his', 'by', 'from', 'they', 'we', 'say',
            'her', 'she', 'or', 'an', 'will', 'my', 'one', 'all', 'would', 'there',
            'their', 'what', 'so', 'up', 'out', 'if', 'about', 'who', 'get', 'which',
            'go', 'me', 'when', 'make', 'can', 'like', 'time', 'no', 'just', 'him',
            'know', 'take', 'people', 'into', 'year', 'your', 'good', 'some', 'could',
            'them', 'see', 'other', 'than', 'then', 'now', 'look', 'only', 'come',
            'its', 'over', 'think', 'also', 'back', 'after', 'use', 'two', 'how',
            'our', 'work', 'first', 'well', 'way', 'even', 'new', 'want', 'because',
            'any', 'these', 'give', 'day', 'most', 'us', 'test', 'secret', 'location',
            'attack', 'dawn', 'quick', 'brown', 'fox', 'jumps', 'over', 'lazy', 'dog',
            'meet', 'longer', 'message', 'from'
        ]
        
        with open(filename, 'w') as f:
            for word in sample_words:
                f.write(word + '\n')
        
        print(f"✓ Created dictionary with {len(sample_words)} words")
    
    # Load the dictionary
    with open(filename, "r") as file:
        for line in file:
            words.add(line.strip().lower())
    
    return words

def score_text(text, dictionary):
    """Score text based on how many dictionary words it contains"""
    words = text.lower().split()
    score = 0
    
    for word in words:
        # Remove punctuation
        word = word.strip(".,!?;:")
        if word in dictionary:
            score += 1
    
    return score

def brute_force(ciphertext, dictionary):
    """Try all 26 keys and score each result"""
    results = []
    
    for key in range(26):
        plaintext = decrypt(ciphertext, key)
        score = score_text(plaintext, dictionary)
        results.append((score, key, plaintext))
    
    results.sort(reverse=True)
    return results

if __name__ == "__main__":
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Build the path to the dictionary
    dict_path = os.path.join(script_dir, "dictionary", "english_words.txt")
    
    print(f"Loading dictionary from: {dict_path}")
    dictionary = load_dictionary(dict_path)
    print(f"Loaded {len(dictionary)} words from dictionary\n")
    
    ciphertext = input("Enter ciphertext: ")
    
    results = brute_force(ciphertext, dictionary)
    
    print("\nAll results (sorted by score):")
    print("-" * 50)
    
    for score, key, plaintext in results[:5]:  # Show top 5 results
        print(f"Key: {key:2} | Score: {score:3} | Text: {plaintext}")
    
    print("-" * 50)
    print("\nBest result:")
    print(f"Key: {results[0][1]}")
    print(f"Text: {results[0][2]}")