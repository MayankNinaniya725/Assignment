import streamlit as st
from llm_sql import nl_to_sql, is_safe_sql
from db_config import get_connection
from hybrid_search import semantic_product_search

st.set_page_config(page_title="NL Database Search", layout="wide")
st.title("🔍 Natural Language Database Search")

query = st.text_input("Ask your question")

if st.button("Search"):
    if "similar" in query.lower() or "related" in query.lower():
        results = semantic_product_search(query)
        st.write("### Semantic Search Results")
        st.table(results)
    else:
        sql = nl_to_sql(query)
        st.code(sql, language="sql")

        if is_safe_sql(sql):
            conn = get_connection()
            cur = conn.cursor()
            cur.execute(sql)
            rows = cur.fetchall()
            st.write("### Query Results")
            st.table(rows)
            cur.close()
            conn.close()
        else:
            st.error("❌ Unsafe SQL detected")
