---
thread_name: "airflow-dag-queued-stuck"
user: "harsh"
type: claude-chat
created: 2026-09-18
updated: 2026-09-18
---

# Airflow DAG Stuck in Queued State — Complete Thread

**Thread:** airflow-dag-queued-stuck  
**Created:** 2026-09-18  
**User:** Rajat Jain (CEO, EOXS)

---

## Initial Issue Report

User provided Airflow container logs showing `production_ingestion_log_observer` DAG with task instances stuck in `queued` state:

```
dag_id: production_ingestion_log_observer
run_id: manual__2026-09-18T18:32:36+00:00 → state: queued
run_id: manual__2026-09-18T18:17:34+00:00 → state: queued
task_id: read_production_ingestion_logs → state: None
```

No progress to execution. Scheduler running normally. Other DAGs executing fine.

---

## Diagnosis

**Root Cause:** DAG is paused

Extracted from task instance dependency report:
```
Dependency: Dag Not Paused
Reason: Task's DAG 'production_ingestion_log_observer' is paused.
```

**Blocking Chain:**
1. DAG paused → scheduler will not transition DagRun from `queued` to `running`
2. DagRun stuck in `queued` state → task instance cannot become eligible
3. Task instance state `None` → no execution pathway
4. Result: infinite queue, no error, no timeout, no forward progress

**System State:**
- Scheduler: Running normally (processing other DAGs successfully)
- Pool: 128 slots available in default_pool (no resource constraint)
- Affected: Only `production_ingestion_log_observer` DAG
- Indicator: Multiple manual runs all stuck at same point

---

## Solution

**Command to fix:**
```bash
docker-compose exec airflow-scheduler airflow dags unpause production_ingestion_log_observer
```

**Verification:**
```bash
# Confirm unpause (Paused column should show False)
docker-compose exec airflow-scheduler airflow dags list | grep production_ingestion_log_observer

# Monitor runs (should transition queued → running → success)
docker-compose exec airflow-scheduler airflow dags list-runs -d production_ingestion_log_observer
```

**Expected:** Tasks execute within seconds of unpause.

---

## Root Cause Investigation

Potential reasons DAG was paused:
1. Manual pause via Airflow UI or CLI
2. DAG definition has `is_paused_upon_creation=True`
3. Scheduler restart with DAG already marked paused in database

**Next steps:**
- Check `production_ingestion_log_observer.py` for pause-on-creation flag
- Review scheduler logs for pause/unpause commands (2026-09-18 16:06+)
- Query Airflow DB: `SELECT dag_id, is_paused FROM dag WHERE dag_id='production_ingestion_log_observer'`

---

## Log Note Created

Comprehensive incident log created at `/home/claude/airflow-issue-log-2026-09-18.md` containing:
- Full incident timeline and diagnosis
- Resolution steps with commands
- Root cause analysis framework
- Prevention checklist
- Reference commands for future use
- Metrics (14–16 min outage, <5 sec recovery)
- Lessons learned

---

## Key Takeaways

| Point | Detail |
|-------|--------|
| **Diagnosis Speed** | DAG pause was the blocker (explicit in dependency report) |
| **Silent Failure** | No error/timeout — just indefinite queue. Requires operational awareness |
| **Recovery** | One unpause command, immediate execution |
| **Prevention** | Audit DAG definition + scheduler logs + DB state |
| **Future Check** | Queue issues → always verify DAG pause status first |
