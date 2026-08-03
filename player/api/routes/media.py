from fastapi import APIRouter, File, Request, UploadFile, Form
from fastapi.responses import HTMLResponse, RedirectResponse
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

@router.get("/gallery", response_class=HTMLResponse)
async def gallery(request: Request):

    media = MediaService.list()

    return templates.TemplateResponse(
        request=request,
        name="gallery.html",
        context={
            "title": "Memories",
            "media": media,
        },
    )


@router.post("/upload")
async def upload(files: list[UploadFile] = File(...)):
    count = MediaService.save_files(files)

    return {
        "success": True,
        "uploaded": count,
        "message": f"{count} file(s) uploaded successfully."
    }

@router.post("/gallery/delete")
async def delete(filename: str = Form(...)):

    MediaService.delete(filename)

    return RedirectResponse(
        "/gallery",
        status_code=303,
    )