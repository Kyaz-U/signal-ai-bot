import csv
import random
import os

def generate_mines_data(num_rows=1000, num_cells=5, bomb_probability=0.2):
    data = []
    for _ in range(num_rows):
        row = [1 if random.random() < bomb_probability else 0 for _ in range(num_cells)]
        data.append(row)
    return data

def save_to_csv(data, filename='train.csv'):
    os.makedirs('mines_csv', exist_ok=True)
    with open(f'mines_csv/{filename}', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
    print(f"{filename} fayli muvaffaqiyatli yaratildi!")

if __name__ == "__main__":
    dataset = generate_mines_data(num_rows=1000, num_cells=5, bomb_probability=0.2)
    save_to_csv(dataset)
