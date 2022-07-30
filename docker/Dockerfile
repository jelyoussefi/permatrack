# Copyright 2020 Toyota Research Institute.  All rights reserved.

FROM nvidia/cuda:11.3.0-cudnn8-devel-ubuntu20.04

ENV PROJECT=permatrack
ENV PYTORCH_VERSION=1.11.0
ENV TORCHVISION_VERSION=0.12.0
ENV NCCL_VERSION=2.9.6-1+cuda11.3
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

ARG python=3.9
ENV PYTHON_VERSION=${python}
ENV DEBIAN_FRONTEND=noninteractive

# Set default shell to /bin/bash
SHELL ["/bin/bash", "-cu"]

RUN apt-get update && apt-get install -y --allow-downgrades --allow-change-held-packages --no-install-recommends \
    build-essential \
    cmake \
    g++ \
    git \
    curl \
    docker.io \
    vim \
    wget \
    ca-certificates \
    libnccl2=${NCCL_VERSION} \
    libnccl-dev=${NCCL_VERSION} \
    libjpeg-dev \
    libpng-dev \
    python${PYTHON_VERSION} \
    python${PYTHON_VERSION}-dev \
    python3-tk \
    librdmacm1 \
    libibverbs1 \
    libgtk2.0-dev \
    unzip \
    bzip2 \
    htop \
    gnuplot \
    ffmpeg

# Install OpenSSH for MPI to communicate between containers
RUN apt-get install -y --no-install-recommends openssh-client openssh-server && \
    mkdir -p /var/run/sshd

RUN ln -sf /usr/bin/python${PYTHON_VERSION} /usr/bin/python

RUN curl -O https://bootstrap.pypa.io/get-pip.py && \
    python get-pip.py && \
    rm get-pip.py

# Install Pydata and other deps
RUN pip install easydict scipy numpy pyquaternion matplotlib jupyter h5py \
    awscli nuscenes-devkit tqdm progress path.py pyyaml opencv-python \
    pycuda numba cython motmetrics scikit-learn moviepy imageio yacs

# Install PyTorch
RUN pip install torch==${PYTORCH_VERSION} \
    torchvision==${TORCHVISION_VERSION} && ldconfig


RUN pip install -U 'git+https://github.com/cocodataset/cocoapi.git#subdirectory=PythonAPI'

RUN pip3 install git+https://github.com/achalddave/python-script-utils.git@v0.0.2#egg=script_utils

# create project workspace dir
RUN mkdir -p /workspace/experiments
RUN mkdir -p /workspace/${PROJECT}
WORKDIR /workspace/${PROJECT}

# Copy project source last (to avoid cache busting)
WORKDIR /workspace/${PROJECT}
COPY . /workspace/${PROJECT}
ENV PYTHONPATH="/workspace/${PROJECT}:$PYTHONPATH"
