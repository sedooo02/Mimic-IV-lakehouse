# MIMIC-IV Hospital Lakehouse

A local lakehouse over the full MIMIC-IV clinical database (hundreds of millions of rows):
raw CSVs → Bronze (Parquet) → Silver (cleaned, typed) → Gold (star schema), orchestrated with Airflow
and covered by data-quality tests.

> Status: in progress (started 2026-10-06)

## Why this project
- **Scale:** `chartevents` and `labevents` together are hundreds of millions of rows. That makes
  partitioning, file formats, incremental loads and query performance real problems, not toy ones.
- **Whole-hospital model:** admissions, ICU stays, transfers, labs, medications and diagnoses, not a single disease.

## Architecture
_TODO: diagram (Week 8)_

| Layer | Contents | Tech |
|---|---|---|
| Bronze | Raw tables converted to Parquet, partitioned where useful | Python, DuckDB, PyArrow |
| Silver | Typed, deduplicated, validated tables | SQL (DuckDB) |
| Gold | Star schema for analytics | SQL (DuckDB), dbt later |
| Orchestration | Daily DAG: bronze → silver → gold → tests | Airflow (Docker) |
| Serving | Aggregate dashboard | Streamlit or Metabase |

## Roadmap
- **v1:** batch lakehouse + tests + Airflow + dashboard
- **v2:** dbt models, incremental loads
- **v3:** real-time replay of `chartevents` through Redpanda/Kafka with streaming alerts
- **v4 (optional):** Spark and/or AWS (S3 + Athena)

## How to run
_TODO (Week 7)_

## Benchmarks
_TODO: CSV vs Parquet, partitioned vs not (Week 3)_

## Data use
MIMIC-IV is credentialed data under the PhysioNet Data Use Agreement.
**No data is stored in this repository.** Credentialed users download it from PhysioNet into `data/raw/`.
Outputs shown here are aggregates only.
