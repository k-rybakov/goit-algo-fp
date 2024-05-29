import matplotlib.pyplot as plt
import numpy as np

def draw_pythagoras_tree(ax, x, y, angle, length, level):
    if level == 0:
        return
    
    # Обчислення координат кінця поточної гілки
    x_end = x + length * np.cos(angle)
    y_end = y + length * np.sin(angle)
    
    # Малювання поточної гілки
    ax.plot([x, x_end], [y, y_end], color='green', lw=1)
    
    # Наступні гілки (ліворуч та праворуч)
    draw_pythagoras_tree(ax, x_end, y_end, angle - np.pi / 4, length * np.sqrt(2) / 2, level - 1)
    draw_pythagoras_tree(ax, x_end, y_end, angle + np.pi / 4, length * np.sqrt(2) / 2, level - 1)

def main():
    level = int(input("Введіть рівень рекурсії: "))
    
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Початкові параметри для дерева
    x_start = 0
    y_start = 0
    length = 1
    angle = np.pi / 2  # Початковий кут (вертикальна гілка)
    
    draw_pythagoras_tree(ax, x_start, y_start, angle, length, level)
    
    plt.show()

if __name__ == "__main__":
    main()
