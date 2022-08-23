import engine as e

# --- OBJECTS --- #

# ENGINE OBJECTS
display = e.Display(1080, 720, "LOL THIS WORK ;O")

# TRANSFORM OBJECTS
e.init()

transform = e.game_object.Transform(200, 200)

sprite = e.images.Sprite("sprite.jpg", (0.1, 0.1))

transform.sprite = sprite

transform.phycics = True
transform.collider = True

# -----------------
run = True

while run:
    display.update()

    _engine.Engine.transforms.append(transform)

    _engine.Engine.DoBeforeLoop()

    display.draw(sprite)