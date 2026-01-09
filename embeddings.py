import random
from db_config import get_connection

def get_embedding(text):
    random.seed(hash(text))
    return [random.random() for _ in range(1536)]

def store_embeddings():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT id, name FROM products")
    products = cur.fetchall()

    for pid, name in products:
        emb = get_embedding(name)
        cur.execute(
            "UPDATE products SET embedding = %s WHERE id = %s",
            (emb, pid)
        )

    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    store_embeddings()
