import itertools
import requests
import random

def check_video(url):
    try:
        response = requests.head(url)
        if response.status_code == 200 and 'video' in response.headers.get('Content-Type', ''):
            return True
    except requests.RequestException as e:
        print(f'Error checking URL {url}: {e}')
    return False

def generate_combinations(start, end, num_random=100):
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    combinations = itertools.product(chars, repeat=4)
    
    all_combinations = [''.join(combination) for i, combination in enumerate(combinations) if start <= i < end]

    random_combinations = random.sample(all_combinations, num_random)
    
    for code in random_combinations:
        url = f"https://qu.ax/{code}.mp4"
        if check_video(url):
            print(f'Video ditemukan: {url}')

if __name__ == '__main__':
    start_index = 0 
    end_index = 1679616
    num_random = 100
    generate_combinations(start_index, end_index, num_random)
