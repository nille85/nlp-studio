from diffusers import AutoPipelineForText2Image
import torch
import os
import time
import random


def generate_image(prompt : str):
    folder_name = "images"
    create_images_dir(folder_name)
    pipe = load_model()
    image = pipe(prompt=prompt, num_inference_steps=2, guidance_scale=1.0).images[0]
    file_name = generate_file_name(folder_name)
    image.save(file_name) 

def create_images_dir(folder_name : str):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

def load_model():
    device = get_device()
    pipe = AutoPipelineForText2Image.from_pretrained("stabilityai/sdxl-turbo", torch_dtype=torch.float16, variant="fp16").to(device)
    return pipe

def get_device():
    if torch.cuda.is_available():
        return "cuda"
    elif torch.backends.mps.is_available():
        return "mps"
    else:
        return "cpu"


def generate_file_name(folder_name : str):
    timestamp = int(time.time())
    random_number = random.randint(0, 99999)
    filename = f"{folder_name}/image_{timestamp}_{random_number}.png"
    return filename



