#!/bin/sh
cd /app/gaussian-splatting/

pip install --no-cache-dir submodules/diff-gaussian-rasterization submodules/simple-knn submodules/fused-ssim

mkdir output

xvfb-run -a python3 convert.py -s /app/chair
python3 train.py -s /app/chair --iterations 1000 --eval -m output/
python3 render.py -m /app/gaussian-splatting/output
python3 metrics.py -m output/