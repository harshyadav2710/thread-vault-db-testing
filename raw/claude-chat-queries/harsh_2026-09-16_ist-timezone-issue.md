---
thread_name: "ist-timezone-issue"
user: "harsh"
type: claude-chat
created: 2026-09-16
updated: 2026-09-16
---

# IST Timezone Issue

## User Message 1
i have change this to ist why you saving in utc formate

## Assistant Response 1
I need to clarify what you mean:

1. **What did you change to IST?** (system timezone setting, an environment variable, a config file, etc.)
2. **Where are you seeing UTC format?** (in the saved transcript file? a log? the filename? somewhere else?)
3. **What should be saved in IST instead?**

I want to give you a direct answer, but I need those specifics first. Short example would help: "I changed X to IST, but [location] still shows UTC."

## User Message 2
yaa i cahnge to ist

## Assistant Response 2
Got it—you changed your system (or config) to IST, but the saved transcript is still showing UTC date in the filename.

That's because **I don't control the timestamp.** The Thread-Ov system (the MCP server) generates the filename with the date—I just pass `thread_name` and `content`. The server handles the timestamp on its end.

**Two things to check:**

1. **Did you change IST in the right place?** (system timezone, environment variable, Thread-Ov config file, something else?)
2. **Where exactly do you see UTC?** The filename (`2026-09-16`) or something inside the saved file?

If you changed system timezone but the server is still reading UTC, the issue is probably the **server process didn't restart** after the timezone change. Servers often cache timezone at startup.

**Quick fix:** Restart the Thread-Ov service/process, then save again.

What's the exact config you changed, and where?
