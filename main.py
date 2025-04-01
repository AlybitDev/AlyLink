from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import FileResponse
import json

app = FastAPI()

templates = Jinja2Templates(directory="templates")

with open('config/config.json') as f:
    config = json.load(f)
    favicon = config['favicon']
    favicon_path = config['favicon_path']
    page_title = config['page_title']
    pfp = config['pfp']
    pfp_path = config['pfp_path']
    username = config['username']
    github = config['github']
    bio_text = config['bio_text']
    gravatar = config['gravatar']
    email = config['email']

@app.get("/")
async def portfolio_page(request: Request):
    if pfp == "False" or pfp == "false":
        return templates.TemplateResponse(request=request, name="indexwoimage.html", context={"page_title": page_title, "username": username, "github": github, "bio_text": bio_text, "gravatar": gravatar, "email": email})
    else:
        return templates.TemplateResponse(request=request, name="indexwimage.html", context={"page_title": page_title, "username": username, "pfp": "image", "github": github, "bio_text": bio_text, "gravatar": gravatar, "email": email})

@app.get("/image")
async def portfolio_image():
    if pfp == "False" or pfp == "false":
        return {"error": "You can't access this."}
    else:
        return FileResponse(pfp_path)

@app.get("/icons/{name}")
async def get_icon(name: str):
    return FileResponse("icons/" + name)

@app.get("/favicon.ico")
async def get_favicon():
    if favicon == "False" or favicon == "false":
        return {"error": "You can't access this."}
    else:
        return FileResponse(favicon_path)
