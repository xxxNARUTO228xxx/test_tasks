import os
import shutil
from pathlib import Path
from fastapi.testclient import TestClient
from main import app, cfg
import pytest


client = TestClient(app)
Path(cfg.test.response_files).mkdir(parents=True, exist_ok=True)




def test_docs():
    response = client.get("/docs")
    assert response.status_code == 200


def test_modify_audiofile():
    files = os.listdir(cfg.test.test_files)
    for filename in files:
        ext = filename.split('.')[-1]
        print(ext)
        filepath = os.path.join(cfg.test.test_files, filename)
        with open(filepath, 'rb') as f:
            upload_file = {'audio_file': f}
            params = {
                'volume': 5,
                'speed': 3
            }
            response = client.post("/modify_audio", params=params, files=upload_file)
            if not ext in cfg.common.exts:
                assert response.status_code == 415
            elif params['speed'] <= 0:
                assert response.status_code == 406
            else:
                assert response.status_code == 200






            
