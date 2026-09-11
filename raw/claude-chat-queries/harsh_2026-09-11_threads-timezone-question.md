---
thread_name: "threads-timezone-question"
user: "harsh"
type: claude-chat
created: 2026-09-11
updated: 2026-09-11
---

User: Hey need to get info on some thing which is in claude we are prompting and it gets saving  the threads into the back end i want to know that on which time format it is saving the threads is it in IST or UCT or EST because we are prompting from the IST time zone but the claude account is on EST time zone based so my general question is this if the time zone is IST or EST or is it UCT in the threads ov  in the backend where the chat threads are getting saved?

Assistant: Straight answer: **UTC**.

The `threads` database session reports `current_setting('TIMEZONE')` as `Etc/UTC`, and `created_at` is stored as `timestamp with time zone`, with values consistently in `+00:00` offset (e.g. `2026-09-11 00:00:00+00:00`). It's not IST and not EST — regardless of whether you're prompting from IST or the account is set up under an EST-based workspace, the backend timestamp for when a thread/message was saved is captured and stored in UTC.

So if you need IST-local times for reporting, you'd convert by adding +5:30 to the stored `created_at`; for EST/EDT it'd be -5/-4 hours depending on daylight saving.
