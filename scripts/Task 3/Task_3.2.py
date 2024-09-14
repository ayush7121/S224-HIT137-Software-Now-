from transformers import AutoTokenizer
from collections import Counter
from concurrent.futures import ProcessPoolExecutor

def tokenize_and_count(chunk, model_name):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    tokens = tokenizer.tokenize(tokenizer.decode(tokenizer.encode(chunk)))
    return Counter(tokens)

def read_file_in_chunks(file_path, chunk_size=10 * 1024 * 1024):
    with open(file_path, 'r', encoding='utf-8') as file:
        while True:
            data_chunk = file.read(chunk_size)
            if not data_chunk:
                break
            yield data_chunk

def process_and_display_top_tokens(file_path, model_name, top_n=30, num_processes=2):
    if __name__ == '__main__':
        with ProcessPoolExecutor(max_workers=num_processes) as executor:
            counters = list(executor.map(tokenize_and_count, read_file_in_chunks(file_path), [model_name] * num_processes))

        total_counter = sum(counters, Counter())

        top_tokens = total_counter.most_common(top_n)
        print(f"Top {top_n} tokens:")
        for token, count in top_tokens:
            print(f"{token}: {count}")

# Example usage:
file_path = 'aggregated_texts.txt'
model_name = 'bert-base-uncased'  # Replace with any model from the transformers library
process_and_display_top_tokens(file_path, model_name)
