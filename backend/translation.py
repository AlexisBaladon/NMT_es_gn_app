import subprocess
import os
import re

from dotenv import load_dotenv
load_dotenv()

HOME = os.getenv("HOME")
ES_GN_MODEL_SUBDIR = os.getenv("ES_GN_MODEL_SUBDIR", "model_s2s_adjusted_es_gn_s2s")
GN_ES_MODEL_SUBDIR = os.getenv("GN_ES_MODEL_SUBDIR", "model_s2s_adjusted_gn_es_s2s")
MODEL_PATH = "models"
INPUT_PATH = f"{HOME}/input.txt"

ES_GN_MODEL_PATH = f"{HOME}/{MODEL_PATH}/{ES_GN_MODEL_SUBDIR}/s2s_adjusted_es_gn_s2s.npz"
ES_GN_VOCAB_PATH = f"{HOME}/{MODEL_PATH}/{ES_GN_MODEL_SUBDIR}/pretrain_test_vocab.esV6000_6000.spm {HOME}/{MODEL_PATH}/{ES_GN_MODEL_SUBDIR}/pretrain_test_vocab.gnV6000_6000.spm"
print(f"ES_GN_MODEL_PATH: {ES_GN_MODEL_PATH}")

GN_ES_MODEL_PATH = f"{HOME}/{MODEL_PATH}/{GN_ES_MODEL_SUBDIR}/s2s_adjusted_gn_es_s2s.npz"
GN_ES_VOCAB_PATH = f"{HOME}/{MODEL_PATH}/{GN_ES_MODEL_SUBDIR}/pretrain_test_vocab.gnV6000_6000.spm {HOME}/{MODEL_PATH}/{GN_ES_MODEL_SUBDIR}/pretrain_test_vocab.esV6000_6000.spm"
print(f"GN_ES_MODEL_PATH: {GN_ES_MODEL_PATH}")

TRANSLATION_COMMAND_TEMPLATE = f'/marian/build/marian-decoder -m {{MODEL_PATH}} -v {{VOCAB_PATH}} -i {INPUT_PATH} --cpu-threads 1 > /mnt/test_output.gn'
# print(str(TRANSLATION_COMMAND_TEMPLATE).format(MODEL_PATH=GN_ES_MODEL_PATH, VOCAB_PATH=GN_ES_VOCAB_PATH).replace(HOME, "/app"))


def translate(source: str, target: str, text: str):
    if source == "es":
        model_path = ES_GN_MODEL_PATH
        vocab_path = ES_GN_VOCAB_PATH
    else:
        model_path = GN_ES_MODEL_PATH
        vocab_path = GN_ES_VOCAB_PATH
    print(f"Translating {text} from {source} to {target}")

    translation_command = TRANSLATION_COMMAND_TEMPLATE.format(MODEL_PATH=model_path, VOCAB_PATH=vocab_path)
    print(f"Translation command: {translation_command}")

    with open(INPUT_PATH, "w") as f:
        f.write(text + "\n")
        f.write(text)

    p = subprocess.Popen(translation_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    result = p.communicate()

    translated_text = result[1].decode()

    print(f"Translated text: {translated_text}")

    translation_regex = r'Best translation 0 : ([^\n]+)\n'
    translated_text = re.search(translation_regex, translated_text)

    if translated_text:
        translated_text = translated_text.group(1)
    else:
        translated_text = "..."
    
    print(f"Translated text: {translated_text}")
    return translated_text