def on_up_pressed():
    simplified.gravity_jump(mySprite)
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_overlap_tile(sprite, location):
    tiles.set_tile_at(location, assets.tile("""
        transparency16
    """))
    info.change_score_by(1)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        orange bauble
    """),
    on_overlap_tile)

def on_overlap_tile2(sprite2, location2):
    game.over(True)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        chest1
    """),
    on_overlap_tile2)

def on_overlap_tile3(sprite3, location3):
    game.over(False)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        poison pit
    """),
    on_overlap_tile3)

mySprite: Sprite = None
scene.set_background_image(assets.image("""
    background
"""))
tiles.set_tilemap(tilemap("""
    level1
"""))
mySprite = sprites.create(assets.image("""
    stand
"""), SpriteKind.player)
controller.move_sprite(mySprite, 100, 0)
mySprite.ay = 500
scene.camera_follow_sprite(mySprite)