---
thread_name: "airflow-dag-queued-stuck"
user: "harsh"
type: claude-chat
created: 2026-09-18
updated: 2026-09-18
---

# Airflow DAG Stuck in Queued State

**Thread:** airflow-dag-queued-stuck  
**Issue:** `production_ingestion_log_observer` DAG has task instances stuck in `queued` state and not progressing to execution.

## Problem Analysis

User provided Airflow logs showing:
- Multiple manual runs (2026-09-18T18:32:36+00:00 and 18:17:34+00:00) both in `queued` state
- Task instance state is `None`
- DagRun state is `queued` (should be `running`)
- Task dependency report explicitly shows: "Dag Not Paused → Task's DAG 'production_ingestion_log_observer' is paused"

## Root Cause

**Primary:** DAG is paused at the Airflow scheduler level  
**Secondary:** DagRun stuck in `queued` state (dependency blocker)  
**Tertiary:** Task instance state is `None` (never became eligible)

The scheduler will not move a DagRun from `queued` → `running` if its DAG is paused.

## Solution

1. Unpause the DAG:
   ```bash
   docker-compose exec airflow-scheduler airflow dags unpause production_ingestion_log_observer
   ```

2. Verify unpause succeeded (Paused column should show False):
   ```bash
   docker-compose exec airflow-scheduler airflow dags list | grep production_ingestion_log_observer
   ```

3. Trigger fresh run or let scheduler pick up existing runs:
   ```bash
   docker-compose exec airflow-scheduler airflow dags trigger production_ingestion_log_observer
   ```

4. Monitor progression:
   ```bash
   docker-compose exec airflow-scheduler airflow dags list-runs -d production_ingestion_log_observer
   ```

## Key Findings

- Pool has 128 slots available (not a resource constraint)
- Scheduler is running normally (processing other DAGs)
- Only this DAG is affected
- Likely cause: manual pause or `is_paused_upon_creation=True` in DAG definition

## Next Steps if Still Stuck

- Check DAG Python file for `is_paused_upon_creation` setting
- Review scheduler logs for pause/unpause events
- Verify database state is consistent (check `dag.is_paused` in Airflow DB)
