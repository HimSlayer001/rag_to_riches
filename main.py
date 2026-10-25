from vector_db import add_chunk_to_db
from load_dataset import dataset


def main():
    print(f"Loaded {len(dataset)} Entries ")

    for fact in dataset:
        fact=fact.strip()
        
        if fact:
            add_chunk_to_db(fact)


    print("Finished the Embedding")




if __name__ == "__main__":
    main()
