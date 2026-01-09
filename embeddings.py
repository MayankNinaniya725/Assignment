from openai import OpenAI
from db_config import get_connection

client = OpenAI()

def get_embedding(text):
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return response.data[0].embedding

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
