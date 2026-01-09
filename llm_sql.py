from openai import OpenAI

client = OpenAI()

SYSTEM_PROMPT = """
You are an expert PostgreSQL assistant.

Rules:
- Generate ONLY SELECT queries
- No DELETE, UPDATE, INSERT, DROP
- Use correct joins
- Return SQL only
"""

def nl_to_sql(user_query):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_query}
        ]
    )
    return response.choices[0].message.content.strip()

def is_safe_sql(sql):
    forbidden = ["DELETE", "UPDATE", "INSERT", "DROP", ";"]
    return not any(word in sql.upper() for word in forbidden)
