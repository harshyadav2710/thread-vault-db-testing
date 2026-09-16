import sys
import os
import json
import urllib.request
import urllib.error
import re
import subprocess
import tempfile
from pathlib import Path

def worker(payload_path):
    # This runs in the detached background process
    try:
        with open(payload_path, 'r', encoding='utf-8') as f:
            payload = json.load(f)
    except Exception:
        return

    # Delete the temp payload file now that we have it in memory
    try:
        os.remove(payload_path)
    except Exception:
        pass

    transcript_path_str = payload.get("transcriptPath")
    if not transcript_path_str:
        return
        
    transcript_path = Path(transcript_path_str)
    full_path = transcript_path.with_name("transcript_full.jsonl")
    if full_path.exists():
        transcript_path = full_path
        
    conversation_id = payload.get("conversationId", "unknown")
    
    messages = []
    first_user_message = ""
    try:
        with open(transcript_path, "r", encoding="utf-8") as f:
            for line in f:
                if not line.strip():
                    continue
                step = json.loads(line)
                step_type = step.get("type")
                if step_type == "USER_INPUT":
                    content = step.get("content", "")
                    if not first_user_message:
                        first_user_message = content
                    messages.append(f"## User\n\n{content}")
                elif step_type == "PLANNER_RESPONSE":
                    content = step.get("content", "")
                    if content:
                        messages.append(f"## Claude\n\n{content}")
    except Exception:
        return

    if not messages:
        return

    words = re.sub(r"[^a-zA-Z0-9\s]", "", first_user_message).split()
    thread_name = "-".join(words[:5]).lower()
    if not thread_name:
        thread_name = conversation_id[:8]
        
    content = "\n\n".join(messages)
    
    workspace_paths = payload.get("workspacePaths", [])
    secret = "test-secret-123"
    base_url = "http://localhost:8000"
    
    if workspace_paths:
        env_path = Path(workspace_paths[0]) / ".env"
        if env_path.exists():
            try:
                env_content = env_path.read_text(encoding="utf-8")
                match_secret = re.search(r'CLAUDE_OV_USERS.*?({.*?})', env_content)
                if match_secret:
                    users_dict = json.loads(match_secret.group(1))
                    if users_dict:
                        secret = list(users_dict.keys())[0]
                
                match_url = re.search(r'MCP_SERVER_URL\s*=\s*"?([^"\n]+)"?', env_content)
                if match_url:
                    base_url = match_url.group(1).rstrip('/')
                else:
                    match_port = re.search(r'PORT\s*=\s*"?(\d+)"?', env_content)
                    if match_port:
                        base_url = f"http://localhost:{match_port.group(1)}"
            except Exception:
                pass

    req_data = json.dumps({
        "thread_name": thread_name,
        "content": content
    }).encode("utf-8")

    api_url = f"{base_url}/{secret}/api/save"
    req = urllib.request.Request(
        api_url,
        data=req_data,
        headers={"Content-Type": "application/json"},
        method="POST"
    )
    
    try:
        # Give it up to 15 seconds in the background
        resp = urllib.request.urlopen(req, timeout=15)
        # We can write a log if we want to trace successes
        with open("hook_log.txt", "a") as log:
            log.write(f"Success saving {thread_name} to {api_url}\n")
    except Exception as e:
        # Write to a log file for debugging
        with open("hook_log.txt", "a") as log:
            log.write(f"Error calling {api_url}: {str(e)}\n")

def main():
    # If launched as worker, run the background task
    if len(sys.argv) > 2 and sys.argv[1] == "--worker":
        worker(sys.argv[2])
        return

    # MAIN PROCESS: Fast execution
    input_data = sys.stdin.read()
    if not input_data:
        print(json.dumps({"decision": "allow"}))
        return

    try:
        payload = json.loads(input_data)
    except Exception:
        print(json.dumps({"decision": "allow"}))
        return
    
    if payload.get("terminationReason") not in ["model_stop", "max_steps_exceeded", "NO_TOOL_CALL"]:
        print(json.dumps({"decision": "allow"}))
        return

    # Write payload to a temporary file
    fd, temp_path = tempfile.mkstemp(suffix=".json", prefix="chat_payload_")
    with os.fdopen(fd, 'w', encoding='utf-8') as f:
        f.write(input_data)

    # Spawn the worker in a detached process
    kwargs = {}
    if os.name == 'nt':
        kwargs['creationflags'] = 0x08000000  
    else:
        kwargs['start_new_session'] = True

    try:
        subprocess.Popen(
            [sys.executable, __file__, "--worker", temp_path],
            stdin=subprocess.DEVNULL,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            **kwargs
        )
    except Exception:
        try:
            os.remove(temp_path)
        except:
            pass

    # Immediately release the agent loop!
    print(json.dumps({"decision": "allow"}))

if __name__ == "__main__":
    main()
