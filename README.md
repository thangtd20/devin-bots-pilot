# Deployment Progress Reporting Pilot

This personal pilot will evaluate whether Devin Bots can build and maintain a small reporting tool for recurring deployment reviews. The proposed stack is FastAPI, SQLite, and pytest. All sample records will be synthetic.

## Planned workflow

1. Import a CSV with a project ID, team, due date, status, and last update date.
2. Validate required fields and flag overdue items, missing updates, and duplicate IDs.
3. Produce a summary by team and compare it with an expected report built from the sample CSV.
4. Add a field in a second iteration, migrate the existing SQLite records, and rerun the tests.

The pilot succeeds if the report matches the expected output, importing the same CSV twice creates no duplicate records, and the migration preserves existing IDs and statuses.

This repository describes the pilot plan. Implementation has not started.
