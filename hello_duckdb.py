import duckdb

# 1. Run standard SQL directly in Python using DuckDB
result = duckdb.sql("""
    SELECT 
        'DuckDB is working!' AS status,
        2026 AS year,
        'MIMIC-IV Lakehouse Engine Ready' AS message
""").df()

# 2. Print the table to your screen
print(result)
