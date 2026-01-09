from embeddings import get_embedding
from db_config import get_connection

def semantic_product_search(query):
    conn = get_connection()
    cur = conn.cursor()

    embedding = get_embedding(query)

    cur.execute("""
        SELECT name, price
        FROM products
        ORDER BY embedding <-> %s
        LIMIT 5
    """, (embedding,))

    results = cur.fetchall()
    cur.close()
    conn.close()

    return results
