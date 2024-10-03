from datasets import load_dataset
from random import randrange

wiki = load_dataset("graelo/wikipedia", "20230901.ja", cache_dir="./data")

for _ in range(10):
  article = wiki["train"][randrange(0, len(wiki["train"]))]
  print(f"id: {article['id']}, title: {article['title']}, text: {article['text'][0:30]}")
