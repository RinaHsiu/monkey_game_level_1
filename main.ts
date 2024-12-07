controller.up.onEvent(ControllerButtonEvent.Pressed, function on_up_pressed() {
    simplified.gravity_jump(mySprite)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`
        orange bauble
    `, function on_overlap_tile(sprite: Sprite, location: tiles.Location) {
    tiles.setTileAt(location, assets.tile`
        transparency16
    `)
    info.changeScoreBy(1)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`
        chest1
    `, function on_overlap_tile2(sprite2: Sprite, location2: tiles.Location) {
    game.over(true)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`
        poison pit
    `, function on_overlap_tile3(sprite3: Sprite, location3: tiles.Location) {
    game.over(false)
})
let mySprite : Sprite = null
scene.setBackgroundImage(assets.image`
    background
`)
tiles.setTilemap(tilemap`
    level1
`)
mySprite = sprites.create(assets.image`
    stand
`, SpriteKind.Player)
controller.moveSprite(mySprite, 100, 0)
mySprite.ay = 500
scene.cameraFollowSprite(mySprite)
