from fastapi import APIRouter, File, Request, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from api.services.media import MediaService

router = APIRouter()

templates = Jinja2Templates(directory="api/templates")


@router.get("/upload", response_class=HTMLResponse)
async def upload_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="upload.html",
        context={"title": "Upload Media"},
    )


@router.post("/upload")
async def upload(files: list[UploadFile] = File(...)):
    count = MediaService.save_files(files)

    return {
        "success": True,
        "uploaded": count,
        "message": f"{count} file(s) uploaded successfully."
    }