import numpy as np
import matplotlib.pyplot as plt
import cv2
import os
import json
from skimage.metrics import structural_similarity as ssim
from skimage.metrics import peak_signal_noise_ratio as psnr

def resize_to_match(img1, img2):
    if img1.shape != img2.shape:
        print(f"Resizing from {img2.shape} to {img1.shape}")
        img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]), interpolation=cv2.INTER_LANCZOS4)
    return img2

def main():

    print("Starting compare results")

    path_to_my_output_folder = os.path.join(os.getcwd(), "my_output")
    path_to_user_output_folder = os.path.join(os.getcwd(), "output")

    save_result_folder = os.path.join(os.getcwd(), "result")

    plt_size = [10, 10]

    my_output_images_paths = np.array([os.path.join(os.getcwd(), path_to_my_output_folder, "test", "ours_1000", "renders", f"{file}") for file in os.listdir(os.path.join(path_to_my_output_folder, "test", "ours_1000", "renders"))])
    user_output_images_paths = np.array([os.path.join(os.getcwd(), path_to_user_output_folder, "test", "ours_1000", "renders", f"{file}") for file in os.listdir(os.path.join(path_to_user_output_folder, "test", "ours_1000", "renders"))])
    gt_images_paths = np.array([os.path.join(os.getcwd(), path_to_my_output_folder, "test", "ours_1000", "gt", f"{file}") for file in os.listdir(os.path.join(path_to_my_output_folder, "test", "ours_1000", "gt"))])
    
    my_output_images_paths = np.sort(my_output_images_paths)
    user_output_images_paths = np.sort(user_output_images_paths)
    gt_images_paths = np.sort(gt_images_paths)

    print(f"Found {len(my_output_images_paths)} renders from my_outputs")
    print(f"Found {len(user_output_images_paths)} renders from user_outputs")

    ssim_my_output_compare_with_gt = []
    psnr_my_output_compare_with_gt = []
    lpips_my_output_compare_with_gt = []
    
    ssim_user_output_compare_with_gt = []
    psnr_user_output_compare_with_gt = []
    lpips_user_output_compare_with_gt = []

    with open(os.path.join(path_to_my_output_folder, "per_view.json"), "r", encoding="utf-8") as file:
        loaded_data = json.load(file)
        for data in loaded_data["ours_1000"]["SSIM"]:
            ssim_my_output_compare_with_gt.append(loaded_data["ours_1000"]["SSIM"][data])
        for data in loaded_data["ours_1000"]["PSNR"]:
            psnr_my_output_compare_with_gt.append(loaded_data["ours_1000"]["PSNR"][data])
        for data in loaded_data["ours_1000"]["LPIPS"]:
            lpips_my_output_compare_with_gt.append(loaded_data["ours_1000"]["LPIPS"][data])

    # print(f"SSIM my_output: {ssim_my_output_compare_with_gt}")
    # print(f"PSNR my_output: {psnr_my_output_compare_with_gt}")
    # print(f"LPIPS my_output: {lpips_my_output_compare_with_gt}")

    with open(os.path.join(path_to_user_output_folder, "per_view.json"), "r", encoding="utf-8") as file:
        loaded_data = json.load(file)
        for data in loaded_data["ours_1000"]["SSIM"]:
            ssim_user_output_compare_with_gt.append(loaded_data["ours_1000"]["SSIM"][data])
        for data in loaded_data["ours_1000"]["PSNR"]:
            psnr_user_output_compare_with_gt.append(loaded_data["ours_1000"]["PSNR"][data])
        for data in loaded_data["ours_1000"]["LPIPS"]:
            lpips_user_output_compare_with_gt.append(loaded_data["ours_1000"]["LPIPS"][data])

    # print(f"SSIM user_output: {ssim_user_output_compare_with_gt}")
    # print(f"PSNR user_output: {psnr_user_output_compare_with_gt}")
    # print(f"LPIPS user_output: {lpips_user_output_compare_with_gt}")

    fig, axis = plt.subplots(nrows=3, ncols=3, figsize=(plt_size[1] * 3, plt_size[0] * 3))

    # SSIM
    axis[0][0].plot(ssim_my_output_compare_with_gt)
    axis[0][0].set_title("SSIM metric (my_output/gt)")
    axis[0][0].set_xlabel("Index of image")
    axis[0][0].set_ylabel("SSIM value")

    axis[0][1].plot(ssim_user_output_compare_with_gt)
    axis[0][1].set_title("SSIM metric (user_output/gt)")
    axis[0][1].set_xlabel("Index of image")
    axis[0][1].set_ylabel("SSIM value")

    axis[0][2].plot(np.abs(np.array(ssim_my_output_compare_with_gt) - np.array(ssim_user_output_compare_with_gt)))
    axis[0][2].set_title("SSIM metric difference abs((user_output - my_output)/gt)")
    axis[0][2].set_xlabel("Index of image")
    axis[0][2].set_ylabel("SSIM value")

    # PSNR
    axis[1][0].plot(psnr_my_output_compare_with_gt)
    axis[1][0].set_title("PSNR metric (my_output/gt)")
    axis[1][0].set_xlabel("Index of image")
    axis[1][0].set_ylabel("PSNR value")

    axis[1][1].plot(psnr_user_output_compare_with_gt)
    axis[1][1].set_title("PSNR metric (user_output/gt)")
    axis[1][1].set_xlabel("Index of image")
    axis[1][1].set_ylabel("PSNR value")

    axis[1][2].plot(np.abs(np.array(psnr_my_output_compare_with_gt) - np.array(psnr_user_output_compare_with_gt)))
    axis[1][2].set_title("PSNR metric difference abs((user_output - my_output)/gt)")
    axis[1][2].set_xlabel("Index of image")
    axis[1][2].set_ylabel("PSNR value")

    # LPIPS
    axis[2][0].plot(lpips_my_output_compare_with_gt)
    axis[2][0].set_title("LPIPS metric (my_output/gt)")
    axis[2][0].set_xlabel("Index of image")
    axis[2][0].set_ylabel("LPIPS value")

    axis[2][1].plot(lpips_user_output_compare_with_gt)
    axis[2][1].set_title("LPIPS metric (user_output/gt)")
    axis[2][1].set_xlabel("Index of image")
    axis[2][1].set_ylabel("LPIPS value")

    axis[2][2].plot(np.abs(np.array(lpips_my_output_compare_with_gt) - np.array(lpips_user_output_compare_with_gt)))
    axis[2][2].set_title("LPIPS metric difference abs((user_output - my_output)/gt)")
    axis[2][2].set_xlabel("Index of image")
    axis[2][2].set_ylabel("LPIPS value")

    plt.savefig(os.path.join(save_result_folder, "metric_compare_my_result_and_user_result_with_gt.png"), dpi=300)

    count_of_img = min(len(my_output_images_paths), len(user_output_images_paths)) 

    print(f"Count of imgs: {count_of_img}")

    ssim_values = []
    psnr_values = []

    os.makedirs(os.path.join(os.getcwd(), "result", "renders"), exist_ok=True)

    for i in range(0, count_of_img):
        
        fig, axis = plt.subplots(nrows=1, ncols=6, figsize=(plt_size[0] * 6, plt_size[1] * 1))
        
        my_output_img_path = str(my_output_images_paths[i])
        user_output_img_path = str(user_output_images_paths[i])
        gt_img_path = str(gt_images_paths[i])

        print(f"Img #{i}")

        print(f"Path to my_output img: {my_output_img_path}")
        print(f"Path to user_output img: {user_output_img_path}")
        print(f"Path to gt img: {gt_img_path}")

        gt_img = cv2.imread(gt_img_path)
        gt_img_rgb = cv2.cvtColor(gt_img, cv2.COLOR_BGR2RGB)

        my_output_img = cv2.imread(my_output_img_path)
        user_output_img = cv2.imread(user_output_img_path)
        
        my_output_img = resize_to_match(gt_img, my_output_img)
        user_output_img = resize_to_match(gt_img, user_output_img)
        
        my_output_img_rgb = cv2.cvtColor(my_output_img, cv2.COLOR_BGR2RGB)
        user_output_img_rgb = cv2.cvtColor(user_output_img, cv2.COLOR_BGR2RGB)

        print(gt_img.shape)
        print(my_output_img.shape)
        print(user_output_img.shape)

        axis[0].imshow(my_output_img_rgb)
        axis[0].set_title(f"My Output img {i}")
        axis[0].axis('off')
        
        axis[1].imshow(user_output_img_rgb)
        axis[1].set_title(f"User Output img {i}")
        axis[1].axis('off')
        
        axis[2].imshow(gt_img_rgb)
        axis[2].set_title(f"Ground Truth img {i}")
        axis[2].axis('off')

        axis[3].imshow(cv2.absdiff(my_output_img, gt_img))
        axis[3].set_title(f"My Output/Ground Truth img {i}")
        axis[3].axis('off')

        axis[4].imshow(cv2.absdiff(user_output_img, gt_img))
        axis[4].set_title(f"User Output/Ground Truth img {i}")
        axis[4].axis('off')

        axis[5].imshow(cv2.absdiff(my_output_img, user_output_img))
        axis[5].set_title(f"My Output/User Ouput img {i}")
        axis[5].axis('off')
        
        plt.savefig(os.path.join(save_result_folder, "renders", f"renders_{i}.png"), dpi=300)

        score_ssim = ssim(my_output_img_rgb, user_output_img_rgb, multichannel=True, channel_axis=2, data_range=255)
        score_psnr = psnr(my_output_img_rgb, user_output_img_rgb, data_range=255)

        print(f"PSNR my_output/user_output: {score_psnr}")
        print(f"SSIM my_output/user_output: {score_ssim}")

        ssim_values.append(score_ssim)
        psnr_values.append(score_psnr)
    
    fig, axis = plt.subplots(nrows=1, ncols=2, figsize=(plt_size[0] * 2, plt_size[1] * 1))

    axis[0].plot(ssim_values)
    axis[0].set_xlabel("Index of img")
    axis[0].set_ylabel("SSIM")
    axis[0].set_title("SSIM between MyOutput/UserOutput imgs")

    axis[1].plot(psnr_values)
    axis[1].set_xlabel("Index of img")
    axis[1].set_ylabel("PSNR")
    axis[1].set_title("PSNR between MyOutput/UserOutput imgs")

    plt.savefig(os.path.join(save_result_folder, "metric_my_result_and_user_result.png"), dpi=300)


if __name__ == "__main__":
    main()