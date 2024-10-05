import turtle

# Функція для малювання сніжинки Коха
def draw_koch_segment(t, length, depth):
    if depth == 0:
        t.forward(length)
    else:
        length /= 3
        draw_koch_segment(t, length, depth-1)
        t.left(60)
        draw_koch_segment(t, length, depth-1)
        t.right(120)
        draw_koch_segment(t, length, depth-1)
        t.left(60)
        draw_koch_segment(t, length, depth-1)

def draw_koch_snowflake(t, length, depth):
    for _ in range(3):
        draw_koch_segment(t, length, depth)
        t.right(120)

# Основна функція для малювання сніжинки Коха
def main():
    depth = int(input("Введіть рівень рекурсії для сніжинки Коха: "))
    screen = turtle.Screen()
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-200, 100)
    t.pendown()

    draw_koch_snowflake(t, 400, depth)

    screen.mainloop()

if __name__ == "__main__":
    main()
