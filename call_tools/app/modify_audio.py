

import logging
from omegaconf import DictConfig, OmegaConf
from pydub import AudioSegment




def modify_audio(audio_file, volume: float, speed: float, cfg: DictConfig):
    """
    Функция обертка для модификации аудио. Изменяет скорость и громкость аудио файла.
    Сохраняет файл по пути конфига.
    Input:
        audio_file: fastapi.UploadFile,
        volume: float - dB
        speed: float
        cfg: omegaconf.DictConfig - hydra config
    Output:
        save_path - path to modified audio file
    """
    ext = audio_file.filename.split('.')[-1]
    audio = AudioSegment.from_file(audio_file.file, format=ext)
    logging.info("opened audio file")

    audio = speed_change(audio, speed)
    logging.info(f"speeded up {speed} times")

    audio = audio + volume
    logging.info(f"changed volume by {volume} dB")

    save_path = f"{cfg.common.save_dir}/{cfg.common.save_name}.{cfg.common.save_ext}"
    audio.export(save_path, format=ext)
    logging.info(f"modified file saved in {save_path}")
    
    return save_path


def speed_change(sound, speed=1.0):
    # Manually override the frame_rate. 
    # It tells samples to play per second
    sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={
        "frame_rate": int(sound.frame_rate * speed)
    })

    # convert the sound with altered frame rate to a standard frame rate
    return sound_with_altered_frame_rate.set_frame_rate(sound.frame_rate)

