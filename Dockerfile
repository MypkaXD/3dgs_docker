# FROM ubuntu:24.04
# FROM nvidia/cuda:12.4.1-cudnn-devel-ubuntu22.04
FROM nvidia/cuda:12.8.0-cudnn-devel-ubuntu22.04

WORKDIR /app

RUN apt-get update && \
    apt-get install -y \
        git \
        wget \
        python3 \
        pip \
        libxml2 \
        unzip \
        cmake \
        build-essential \
        libgl1-mesa-dev \
        libglx-dev \
        libxrandr-dev \
        libxinerama-dev \
        libxcursor-dev \
        libxi-dev \
        libtbb-dev \
        libglu1-mesa-dev \
        libglib2.0-0 \
        libgl1-mesa-glx \
        colmap \
        dos2unix \
        xvfb
RUN git clone https://github.com/graphdeco-inria/gaussian-splatting.git --recursive
pip install --no-cache-dir torch==2.11.0 torchvision==0.26.0 torchaudio==2.11.0 --index-url https://download.pytorch.org/whl/cu128
RUN pip install --no-cache-dir plyfile==1.1.3 tqdm opencv-python joblib matplotlib numpy scikit-image

COPY script.sh dataset .

RUN dos2unix script.sh

COPY compare_outputs.py .
COPY my_output/ ./my_output/
