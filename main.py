import random
import pygame
import time
import os
import copy

pygame.mixer.init()

AUDIO_FOLDER = "audio"

def play_number_audio(number):
    audio_path = os.path.join(AUDIO_FOLDER, f"{number}.mp3")

    if not os.path.exists(audio_path):
        print(f"Audio file missing: {audio_path}")
        return

    # Load and play audio
    pygame.mixer.music.load(audio_path)
    pygame.mixer.music.play()

    # Wait until playback finishes
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

def highest_to_low(num_arr2):
    num_arr = copy.deepcopy(num_arr2)
    biggest = num_arr[0]
    temp_arr = []
    repeat = len(num_arr)
    for j in range(repeat):
        for i in range(len(num_arr)):
            if num_arr[i] > biggest:
                biggest = num_arr[i]
        temp_arr.append(biggest)
        num_arr.remove(biggest)
        biggest = -1
    return temp_arr

def low_to_high(num_arr2):
    num_arr = copy.deepcopy(num_arr2)
    smallest = num_arr[0]
    temp_arr = []
    repeat = len(num_arr)
    for j in range(repeat):
        for i in range(len(num_arr)):
            if num_arr[i] < smallest:
                smallest = num_arr[i]
        temp_arr.append(smallest)
        num_arr.remove(smallest)
        smallest = 123
    return temp_arr

def main():
    amount_digits = 7 #If this number is bigger than 10 digits will repeat
    number_all = []
    while len(number_all) < amount_digits:
        # Generate random number
        number = random.randint(0, 9)
        if number in number_all and amount_digits < 11:
            continue
        number_all.append(number)

    for i in range(len(number_all)):

        play_number_audio(number_all[i])

        # Wait before next number
        time.sleep(0.8)

    print("Target numbers:",number_all)
    print("Biggest to smallest",highest_to_low(number_all))
    print("Smallest to biggest",low_to_high(number_all))
    print("Reversed numbers:", number_all[::-1])

if __name__ == "__main__":
    main()