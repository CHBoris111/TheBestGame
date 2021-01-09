class Camera:
    # Положение камеры в виде числа с плавающей запятой
    viewx = 0
    viewy = 0
    # Pygame rect, определяющий область сцены для рендеринга
    viewpos = None
    # Минимальное и максимальное расстояние, за пределами которого камера мгновенно фиксирует положение объекта
    minSnapDistance = 5
    maxSnapDistance = 200

    def __init__(this, size):
        this.viewpos = pygame.Rect((0, 0), size)

    def update_pos(this, obj):
        # Позиция наблюдения
        (xp, yp) = obj.pos
        yp -= 80
        (dx, dy) = (xp - this.viewpos.center[0],
                    yp - this.viewpos.center[1])
        # Мы мгновенно привязываемся к позиции, если находимся либо слишком близко
        if (abs(dx) < this.minSnapDistance or abs(dx) > this.maxSnapDistance):
            this.viewx = xp
        else:
            this.viewx += dx * 0.5
        # Do the same for the vertical displacement
        if (abs(dy) < this.minSnapDistance or abs(dy) > this.maxSnapDistance):
            this.viewy = yp
        else:
            this.viewy += dy * 0.5
        # Обновление Pygame rect
        this.viewpos.center = (int(this.viewx), int(this.viewy))