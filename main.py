from openai import OpenAI
from os import path, getenv
import sys, subprocess


client = OpenAI()
IMAGE_NAME = getenv("IMAGE_NAME")


def main():
    prompt = check_input(sys.argv)
    image  = create_image(prompt).data[0].url
    subprocess.run(f"curl \"{image}\" -o {IMAGE_NAME}.png", shell="True")


def create_image(prompt):
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1
    )
    return response


def check_input(arguments):
    arguments_length = len(arguments)
    prompt = ""
    if(arguments_length == 1 or arguments_length > 2):
        print("Recuerde ingresar solo un argumento")
        exit()
    if(path.isfile(arguments[1])):
        prompt = subprocess.run(f"cat {arguments[1]}").read().replace("\n", "\\n", shell=True)
    else:
        prompt = arguments[1]
    return prompt


main()
