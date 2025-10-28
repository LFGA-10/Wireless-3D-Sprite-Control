import utils.session
import serial, time
from vpython import box, vector, rate, color, label, sphere, curve

bt = serial.Serial('COM8', 9600, timeout=1)  
time.sleep(2)

sprite = box(pos=vector(0, 0, 0), size=vector(1, 1, 1), color=color.cyan, shininess=0.8)
trail = curve(color=color.white, radius=0.03)
tag = label(pos=vector(0, 2, 0), text="Sandra's 3D Sprite", height=16, box=False, color=color.yellow)

idle_timer = 0
rotation_speed = 0.05

while True:
    rate(30)
    line = bt.readline().decode(errors='ignore').strip()

    if line.startswith("SANDRA:"):
        try:
            data = line.replace("SANDRA:", "").split(',')
            x = int(data[0])
            y = int(data[1])
            btn = int(data[2])

            move_x = (x - 512) / 120
            move_y = (y - 512) / 120

            sprite.pos.x += move_x * 0.2
            sprite.pos.y += move_y * 0.2
            trail.append(pos=sprite.pos)
            sprite.rotate(angle=rotation_speed * (move_x + move_y), axis=vector(0, 0, 1))
            if btn == 0:
                sprite.color = color.red
            else:

                sprite.color = vector(abs(move_x), abs(move_y), 0.8)

            idle_timer = 0

        except Exception as e:
            pass

    else:
        idle_timer += 1
        if idle_timer > 20:
            sprite.pos *= 0.95

