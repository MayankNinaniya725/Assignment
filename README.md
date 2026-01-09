# Natural Language Search Interface

For demonstration purposes, embeddings are locally generated. In production, OpenAI embeddings can be used

This project implements a Natural Language Search system using:
- PostgreSQL
- pgvector
- OpenAI LLM
- Streamlit

## Features
- Convert English queries to SQL
- Secure SQL validation
- Hybrid semantic + SQL search
- Simple Streamlit UI

## Example Queries
- Show employees in Engineering department
- Top 5 expensive products
- Orders handled by Sales employees
- Products similar to laptop

## Setup
1. Create PostgreSQL database
2. Run schema.sql and sample_data.sql
3. Install dependencies
4. Run embeddings.py
5. psql -U postgres nl_search_db -f db\schema.sql
6. psql -U postgres nl_search_db -f db\sample_data.sql
7. psql -U postgres nl_search_db (verify tables exist \dt \q)
5. Start Streamlit app

```bash
python -m streamlit run app.py

