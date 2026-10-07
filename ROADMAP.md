# Data Engineering Mentorship Program: Muhammad Sayed

**Start:** Tue 6 Oct 2026 | **Courses:** DeepLearning.AI Data Engineering Certificate (Coursera) + DataCamp Associate Data Engineer in SQL, then Data Engineer in Python | **Target:** Junior / Associate Data Engineer interviews by early December

---

## 0. The bar: what "hireable" means

When we finish, you should be able to do these five things. Everything below exists to get you there.

1. **SQL under time pressure:** joins, CTEs, window functions, aggregations. Solve a medium problem in 15–20 minutes.
2. **Python ETL:** clean, tested code that pulls data from files and APIs and loads it into a database.
3. **Architecture reasoning:** draw a pipeline and defend your choices (batch vs streaming, warehouse vs lake, why this tool).
4. **One flagship project on GitHub:** runs with one command, has tests, orchestration, and a clear README.
5. **Your story:** "I built a Digital Twin on MIMIC-IV, then I learned to build the data platform underneath it."

> [!NOTE]
> Nobody can promise a job. But a candidate who clears this bar is competitive for junior DE roles. Certificates alone don't clear it. Skills and proof do.

---

## 1. The independence ladder (when I help, when I step back)

| Phase | Weeks | Your mode | My role |
|---|---|---|---|
| **A: Guided** | 1–2 | Follow the courses exactly. Take notes. | I tell you exactly what to do each day. |
| **B: Rebuild** | 3–5 | After every lab or exercise, rebuild the core part from a blank file. | I review what you rebuilt and point out gaps. |
| **C: Independent** | 6–8 | Build project features with docs only, no tutorial. | I review designs and code, but I don't write it. |
| **D: Interview mode** | 9+ | Timed practice, mock interviews, applications. | I act as interviewer. |

**Rules that make independence real:**

- **20-minute rule:** stuck on a problem? Spend 20 minutes on it yourself first (read the error, check the docs, print values). Only then look at a hint.
- **Write down what you tried** before asking me. Writing it often solves it.
- **Type, never paste,** the solutions you look up. Then delete the solution and redo it from memory the next day.
- **AI tools:** use them to explain an error or a concept after you've tried. Don't use them to write the whole solution. In interviews you won't have them, and the course quizzes will expose the gap.
- **Explain it out loud** at the end of each day, as if teaching someone. If you can't, you didn't learn it yet.

---

## 2. Setup: installed only when needed

Each tool is installed in the week it's first used. Nothing is installed early.

| When | Tool | Why |
|---|---|---|
| **Week 1** | Git + GitHub (Git already installed ✅) | Version control and public proof of work. |
| **Week 1** | VS Code, Python 3.12 + venv | Pipeline code. |
| **Week 1** | DuckDB (`pip install duckdb pyarrow`) | The lakehouse query engine. It reads CSV and Parquet directly, with no server. |
| **Week 2** | DBeaver (free) | GUI for exploring DuckDB files. |
| **Week 6** | WSL2 + Docker Desktop | Needed to run Airflow in Week 7. |
| **Later, optional** | AWS account | Only for v4. Set a **billing alarm at \$1–5** first. |

**Repo layout** (already created at `scratch\mimic-iv-lakehouse`):

```
mimic-iv-lakehouse/
├── data/            # raw MIMIC-IV CSVs. NEVER committed
├── lake/            # bronze / silver / gold Parquet. NEVER committed
├── ingestion/       # Python: CSV → Parquet
├── sql/             # raw → staging → marts
├── dags/            # Airflow (Week 7)
├── tests/
├── notes/           # engineering notebook
├── tracker/         # TRACKER.md + weekly check-ins
├── ROADMAP.md       # this file
└── README.md
```

> [!CAUTION]
> **MIMIC-IV rules (PhysioNet DUA):** code goes to GitHub, data never does. Don't paste raw patient rows into any AI tool, including this one. Share schemas, column names and error messages instead. Screenshots and dashboards show aggregates only.

---

## 3. Daily rhythm (Sat–Thu, ~8 hours; Friday is review + rest)

| Time | Block | Why |
|---|---|---|
| 09:00–11:30 | **Coursera** (deep work) | Concepts need your freshest mind. |
| 11:30–12:00 | Write notes in physical notebook | Notes written the same day stick. |
| 12:00–14:00 | Break, lunch, walk | Don't skip this. |
| 14:00–17:00 | **DataCamp** | Hands-on coding. |
| 17:30–18:30 | **SQL / Python practice** (outside the courses) | This is what interviews test. |
| 20:00–21:00 | **Project** + daily commit | This is your portfolio. |

**Friday:** 1 hour weekly review (check-in template in §7), a 200-word teach-back post (§5), then rest.

---

## 4. Week-by-week plan

> [!IMPORTANT]
> **DataCamp expires 1 Dec 2026.** All DataCamp work must be finished by **Sun 29 Nov**. Week 9 has no DataCamp.

DataCamp order matters: the Python track lists the SQL track as a prerequisite, so SQL first.

| Week | Coursera | DataCamp | Practice (daily) | Project | Friday deliverable |
|---|---|---|---|---|---|
| **1** Oct 6–11 | C1: W1–2 | Understanding DE, Intro SQL, Intermediate SQL, Joining Data | LeetCode SQL 50: 15 easy | Git/GitHub + Python/DuckDB setup. Hello pipeline: `hosp/patients` CSV → Parquet → count with DuckDB | Notes: "DE lifecycle in my own words" + first push |
| **2** Oct 12–18 | C1: W3–4 | Mental Health project, Relational DBs, Database Design | 20 joins/aggregation problems | **Download** `hosp` + `icu` from PhysioNet. **Data inventory:** every table, with row counts, sizes and keys. ER diagram of core tables | **Requirements doc** (stakeholders: hospital ops + researchers; mirrors C1 W4) |
| **3** Oct 19–25 | C2: W1–2 (ingestion) | Data Warehousing, Snowflake, London project, Data Manipulation in SQL | 25 CTE + window problems | **Bronze:** all `hosp` + `icu` tables → Parquet. Large tables partitioned. Benchmark CSV vs Parquet | Bronze layer + benchmark table in README |
| **4** Oct 26–Nov 1 | C2: W3–4 (DataOps, Airflow) | PostgreSQL window functions course, then the Associate DE certification* | 20 timed window problems | **Silver:** typed, deduplicated, validated tables in SQL | Cert attempt + silver layer |
| **5** Nov 2–8 | C3 (storage, lakehouse, queries) | Start Python track: skim Python/pandas (skip videos you know) | 15 Python problems + SQL review | **Gold:** star schema (facts: admissions, ICU stays, labs; dims: patient, care unit, lab item, diagnosis, date) | Schema diagram + gold layer |
| **6** Nov 9–15 | C4: W1–2 (modeling) | Importing data, ETL & ELT in Python, **Airflow** | Timed SQL, 3/day | Turn ingestion into a package (config, logging). Data-quality tests in pytest. Install WSL2 + Airflow (standalone, no Docker) | All tests pass |
| **7** Nov 16–22 | C4: W3–4 + **Capstone** | Git, software engineering, remaining Python-track courses | Mixed SQL + Python | Airflow DAG: bronze → silver → gold → tests | **Coursera certificate done** + DAG runs end to end |
| **8** Nov 23–29 | Buffer / review | **Finish Python track (hard deadline)** | Mock-interview drills | Aggregate dashboard + README + architecture diagram | **Project v1 published** + DataCamp done |
| **9** Nov 30–Dec 6 | — | *(expired)* | Timed practice | Polish, then start v2 (dbt) | Mock interview #1 with me, CV updated |

*Check that the certification is included in your subscription. I haven't verified that.

**Where each course is strongest:**

- **Coursera:** architecture, requirements, tool choices, AWS. The *thinking*.
- **DataCamp:** SQL and Python muscle memory. The *typing*.
- **Neither** teaches window functions in depth in the SQL track. That's why Week 3–4 adds two extra DataCamp courses and daily practice.

**Book use:** only open *Fundamentals of Data Engineering* when a Coursera topic feels thin. Use the chapter that matches the module.

---

## 5. Side tasks (outside the courses)

1. **Daily SQL practice:** LeetCode SQL 50 (free), DataLemur (free tier), StrataScratch (free tier). Target **120+ problems** by Dec 6 (about 3 a day). Re-do any you needed hints for, two days later.
2. **Python practice:** 1–2 small problems or scripts a day. Focus on dicts, lists, file I/O, JSON, error handling.
3. **Engineering notebook** (`notes/` or physical): for each topic, a short note on *when I'd use X vs Y* (e.g., Kinesis vs batch, Redshift vs Athena, warehouse vs lakehouse). These are your interview answers.
4. **Git habit:** commit daily with meaningful messages ("add staging model for icustays", not "update").
5. **Linux command line:** 15 min a day in WSL (navigation, grep, pipes, permissions). OverTheWire "Bandit" is free and good practice.
6. **Friday teach-back:** a 200-word LinkedIn post or README section explaining one thing you learned. It builds visibility and forces understanding.
7. **One engineering blog a week** (Netflix, Uber, Airbnb tech blogs). Read for how they structured pipelines, not the buzzwords.

---

## 6. Flagship project: `mimic-iv-lakehouse`

**What it is:** a local lakehouse over the **full credentialed MIMIC-IV** database, modelling the whole hospital (admissions, ICU stays, transfers, labs, medications, diagnoses). It isn't about one disease.

**Why it gets interviews:** most people use toy data or the 100-patient demo. You'll handle tables with hundreds of millions of rows. That forces real engineering decisions about file formats, partitioning, memory, incremental loads and query speed, and those decisions are what interviewers ask about.

**Questions the gold layer must answer** (proof the model works):
1. Bed occupancy and ICU length of stay by care unit and month.
2. 30-day readmission rate by admission type.
3. Patient flow: transfers between units (ED → ward → ICU).
4. Lab volume and turnaround per lab item.

**Architecture:**

```
MIMIC-IV CSV.gz (hosp, icu)
      │  Python + DuckDB ingestion (idempotent, logged)
      ▼
lake/bronze  (Parquet, partitioned)
      ▼  SQL
lake/silver  (typed, deduplicated, validated)
      ▼  SQL
lake/gold    (star schema) ──► aggregate dashboard
      ▲
Airflow DAG + data-quality tests (Docker)
```

**Engineering skills it proves:** columnar formats, partitioning, out-of-core processing, dimensional modeling, idempotent pipelines, data-quality testing, orchestration, benchmarking.

**Milestones:**

| Version | Adds |
|---|---|
| **v1** (end of Week 8) | Bronze/silver/gold, tests, Airflow DAG, dashboard, README with benchmarks. |
| **v2** (December) | dbt models, incremental loads. |
| **v3** (Dec–Jan) | Real-time replay of `chartevents` through Redpanda/Kafka with streaming alerts. |
| **v4** (optional) | Spark and/or AWS (S3 + Athena). Billing alarm first. |

**Definition of done for v1:**
- One command runs the full pipeline.
- README with architecture diagram, data model, benchmarks, and key decisions and trade-offs.
- Tests pass.
- No data, secrets or individual-level outputs in the repo.

> [!NOTE]
> **Your machine: 8 GB RAM, ~400 GB free disk.** Disk is plenty. RAM is the constraint, and it's workable:
> - DuckDB settings for big tables: `SET memory_limit='4GB'; SET temp_directory='lake/tmp'; SET preserve_insertion_order=false;`
> - Convert small tables first and `chartevents` last. Close Chrome while converting.
> - Airflow runs standalone in WSL2, not in Docker, because Docker plus Airflow would eat most of 8 GB.
> - The GPU isn't used in this project.
>
> **Getting the data:** download the CSVs from the PhysioNet website with your credentialed login, which is free. Avoid copying from the GCP requester-pays buckets, because egress is billed to you. BigQuery access (`physionet-data`) is useful later for a v4 "local lakehouse vs cloud warehouse" comparison, but keep your queries small and watch the free tier.

---

## 7. Weekly check-in (send me this every Friday)

```
Week #:
Hours worked:
Coursera progress:
DataCamp progress:
SQL problems solved (total):
Commits this week:
Stuck on (and what I already tried):
One thing I now understand that I didn't last week:
Plan for next week:
```

I'll review it, point out weak spots, and adjust the plan.

---

## 8. After the courses: job-hunt phase (Dec to Feb)

- **Start applying in Week 8**, don't wait until you "finish". Aim for 5–10 tailored applications a day.
- **Target roles:** Junior Data Engineer, Associate DE, Analytics Engineer, Data Analyst moving into DE. Look at Egypt, Gulf, and remote EU/UK roles.
- **Add next:** dbt, PySpark basics. The **AWS Certified Data Engineer – Associate** is optional and costs money, so only do it after the project and applications are moving.
- **CV:** one page, project at the top, bullets with outcomes ("built star schema over X tables, Airflow-orchestrated ELT, N data-quality tests").
- **Interview prep pillars:** SQL, Python, DE system design (use the Coursera lifecycle as your framework), behavioral (STAR format built on your graduation project).

---

## 9. What goes wrong (and the rules for it)

- **Tutorial hell:** finishing videos without building anything. The project and rebuild rule are the cure.
- **Missed a day:** don't double up to catch up. Drop the lowest priority instead.
- **Priority when behind:** (1) DataCamp SQL track + SQL practice, (2) project, (3) Coursera, (4) DataCamp Python extras.
- **Perfectionism:** v1 shipped and imperfect beats v3 never finished.
- **The lost month:** it's gone. This plan was built around what's left, so don't spend energy on it.
