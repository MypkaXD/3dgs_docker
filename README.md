Docker container для сборки и тестирования проекта 3D Gaussian Splatting (https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/).
После выполнения пользователь получит готовую модель (формат .ply), набор новых изображений, результаты сравнения изображения с исходными данными

(CMD Instruction)
1. git clone https://github.com/MypkaXD/3dgs_docker.git
2. cd 3dgs_docker
3. docker build -t 3dgs .
4. docker run -it --gpus all -v .\output:/app/output -v .\result:/app/result 3dgs 
5. ./script.sh (необходимо выполнить внутри контейнера)

(Опционально)
Если пользователь желает подробнее озканомиться с результатами работы, то необходимо выполнить
1. Запустить online viewer (https://superspl.at/editor)
2. На хосте перейти в скопированную папку -> output/point_cloud/iteration_{i}
3. Перенесети файл point_cloud.ply в online viewer

Время этапа build порядка 30-40 минут. Время выполнения скрипта внутри docker container'a порядка 10-15 минут.
<img width="974" height="505" alt="image" src="https://github.com/user-attachments/assets/78c852d0-4ae5-410d-abd7-9e6e06422b67" />
