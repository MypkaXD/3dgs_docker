#!/bin/sh
cd /app/gaussian-splatting/

pip install --no-cache-dir submodules/diff-gaussian-rasterization submodules/simple-knn submodules/fused-ssim

xvfb-run -a python3 convert.py -s /app/chair
python3 train.py -s /app/chair --iterations 1000 --eval -m /app/output/
python3 render.py -m /app/output
python3 metrics.py -m /app/output/

cd /app/
python3 compare_outputs.py