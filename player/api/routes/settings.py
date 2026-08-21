from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from api.services.settings import SettingsService

router = APIRouter()

templates = Jinja2Templates(directory="api/templates")


@router.get("/settings", response_class=HTMLResponse)
async def settings_page(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="settings.html",
        context={
            "title": "Settings",
            "display_mode": SettingsService.get_display_mode(),
        },
    )


@router.post("/settings/display-mode")
async def update_display_mode(mode: str = Form(...)):

    SettingsService.set_display_mode(mode)

    return RedirectResponse("/settings", status_code=303)
