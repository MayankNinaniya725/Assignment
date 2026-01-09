# Natural Language Search Interface

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
5. Start Streamlit app

```bash
streamlit run app.py
