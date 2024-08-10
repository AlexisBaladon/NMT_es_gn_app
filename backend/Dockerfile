FROM lefterav/marian-nmt:1.11.0_sentencepiece_cuda-11.3.0

# Load models
RUN curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | bash
RUN apt-get install git-lfs
RUN git lfs install
# COPY models /app/models

# Environment variables
ENV HOME="/app"
ENV ES_GN_MODEL_SUBDIR="grammar_finetuning_es_gn"
ENV GN_ES_MODEL_SUBDIR="grammar_finetuning_gn_es"

# Install dependencies
COPY requirements.txt "${HOME}/requirements.txt"
WORKDIR $HOME
RUN pip install -r requirements.txt

# GN->ES Model
ARG MODELS_DIR="${HOME}/models"
RUN mkdir $MODELS_DIR
ARG ES_GN_MODEL_DIR="${HOME}/models/${ES_GN_MODEL_SUBDIR}"
RUN mkdir $ES_GN_MODEL_DIR
RUN git clone https://huggingface.co/alexisbaladon/grammar_finetuning_es_gn $ES_GN_MODEL_DIR

# ES->GN Model
ARG GN_ES_MODEL_DIR="${HOME}/models/${GN_ES_MODEL_SUBDIR}"
RUN mkdir $GN_ES_MODEL_DIR
RUN git clone https://huggingface.co/alexisbaladon/grammar_finetuning_gn_es $GN_ES_MODEL_DIR

# Copy app files
COPY main.py /app/main.py
COPY translation.py /app/translation.py
COPY test /app/

# Run server
CMD ["python3", "/app/main.py"]