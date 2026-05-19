1. git clone https://github.com/MypkaXD/3dgs_docker.git
2. cd 3dgs_docker
3. docker build -t 3dgs .
4. docker run -it --gpus all 3dgs

Время этапа build порядка 30-40 минут. Время выполнения скрипта внутри docker container'a порядка 10-15 минут.
<img width="974" height="505" alt="image" src="https://github.com/user-attachments/assets/78c852d0-4ae5-410d-abd7-9e6e06422b67" />
