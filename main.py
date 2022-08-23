import engine as en

# --- OBJECTS --- #

# ENGINE OBJECTS
display = en.Display(1080, 720, "LOL THIS WORK ;O")

# TRANSFORM OBJECTS
_engine = en.Engine()

transform = en.game_object.Transform(200, 200)

sprite = en.images.Sprite("sprite.jpg", (0.1, 0.1))

transform.sprite = sprite

transform.phycics = True
transform.collider = True

# -----------------
run = True

while run:
    display.update()

    _engine.transforms.append(transform)

    #display.draw(sprite) 