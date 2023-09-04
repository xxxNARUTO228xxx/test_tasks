

import uvicorn
from pathlib import Path
from omegaconf import DictConfig, OmegaConf
from hydra import compose, initialize
from fastapi import FastAPI, UploadFile, File, Query, status
from fastapi.responses import PlainTextResponse, FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydub import AudioSegment
from app.modify_audio import modify_audio
from app.speech2text import speech2text


# инициализируем конфиг
parsed = Path("configs/config.yaml")
initialize(config_path=str(parsed.parent))
cfg = compose(parsed.name)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[f"http://{cfg.common.host}:{cfg.common.port}"],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)




@app.post("/modify_audio")
async def modify_audiofile(
        volume: float=Query(1.0, description=cfg.modify.desc_volume),
        speed: float=Query(1.0, description=cfg.modify.desc_speed),
        audio_file: UploadFile=File(..., description=cfg.common.desc_audio)
    ):

    if speed <= 0:
        return JSONResponse(
                status_code=cfg.response_errors.params.status_code, 
                content=cfg.response_errors.params.message
            )

    ext = audio_file.filename.split('.')[-1]
    if not ext in cfg.common.exts:
        return JSONResponse(
                status_code=cfg.response_errors.file_format.status_code, 
                content=cfg.response_errors.file_format.message
            )
        
    audio_path = modify_audio(audio_file, volume, speed, cfg)
    headers = {'Content-Disposition': f'attachment; filename="{audio_file.filename}"'}
    return FileResponse(audio_path, headers=headers, media_type="audio/mp3")


@app.post("/speech2text")
async def speech2text_audiofile(
        lang: str=Query(..., description=cfg.speech2text.desc_lang),
        audio_file: UploadFile=File(..., description=cfg.common.desc_audio)
    ):

    if lang not in cfg.speech2text.langs:
        return JSONResponse(
                status_code=cfg.response_errors.params.status_code, 
                content=cfg.response_errors.params.message
            )

    ext = audio_file.filename.split('.')[-1]
    if not ext in cfg.common.exts:
        return JSONResponse(
                status_code=cfg.response_errors.file_format.status_code, 
                content=cfg.response_errors.file_format.message
            )

    audio = AudioSegment.from_file(audio_file.file, format=ext)
    audio_path = f"{cfg.common.save_dir}/{cfg.common.save_name}.{cfg.common.save_ext}"
    audio.export(audio_path, format=ext)
    text = speech2text(audio_path, lang, cfg)
    return PlainTextResponse(text)




if __name__ == "__main__":
    Path('./logs').mkdir(parents=True, exist_ok=True)
    Path(cfg.common.save_dir).mkdir(parents=True, exist_ok=True)
    uvicorn.run(app, host=cfg.common.host, port=cfg.common.port, log_config="./log.ini")
