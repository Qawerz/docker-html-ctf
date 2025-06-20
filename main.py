# main.py
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import docker
import random
import string
import asyncio
from datetime import datetime, timedelta

app = FastAPI()

client = docker.from_env()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")



def generate_random_name(length=8):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/start-container")
async def start_container():
    username = "user"
    container_name = f"ctf_ssh_{generate_random_name()}"
    port = random.randint(2200, 2299)
    expiration_time = datetime.now() + timedelta(minutes=5)
    
    try:
        container = client.containers.run(
            "alpine-ssh-cgpt",
            name=container_name,
            detach=True,
            ports={'22/tcp': port},
            auto_remove=True
        )
        
        asyncio.create_task(stop_container_after_delay(container, 300))
        
        return JSONResponse({
            "status": "success",
            "host": "localhost",
            "port": port,
            "username": username,
            "password": "ctfpassword",
            "container_id": container.short_id,
            "ssh_command": f"ssh {username}@localhost -p {port}",
            "expires_at": expiration_time.isoformat()
        })
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)

@app.post("/start-web-container")
async def start_web_container():
    container_name = f"ctf_web_{generate_random_name()}"
    port = random.randint(2300, 2399)
    expiration_time = datetime.now() + timedelta(minutes=5)
    
    try:
        container = client.containers.run(
            "nginx-ctf",
            name=container_name,
            detach=True,
            ports={'80/tcp': port},
            auto_remove=True
        )
        
        asyncio.create_task(stop_container_after_delay(container, 300))
        
        return JSONResponse({
            "status": "success",
            "host": "localhost",
            "port": port,
            "container_id": container.short_id,
            "url": f"http://localhost:{port}",
            "expires_at": expiration_time.isoformat()
        })
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)

async def stop_container_after_delay(container, delay_seconds):
    await asyncio.sleep(delay_seconds)
    try:
        container.stop()
    except:
        pass


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)