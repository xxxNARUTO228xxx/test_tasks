

from omegaconf import DictConfig, OmegaConf
from pocketsphinx import AudioFile, get_model_path




def speech2text(audio_file: str, lang: str, cfg: DictConfig):
    """
    Распознавание речи с помощью pocketsphinx.
    Input:
        audio_file: path to file - str,
        lang: [rus, eng] - str
        cfg: DictConfig - hydra config
    Output:
        text - str
    """
    if lang=='rus':
        model_cfg = cfg.speech2text.rus
    elif lang=='eng':
        model_cfg = cfg.speech2text.eng

    speech = AudioFile(
        audio_file=audio_file,
        **model_cfg
    )

    text = []
    for phrase in speech:
        text.append(str(phrase))

    return " ".join(text)
