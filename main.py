function evaluateGuess (text: string) {
    match = 0
    info.setScore(0)
    for (let index = 0; index <= 4; index++) {
        if (guess == text_list) {
            music.baDing.play()
            info.changeScoreBy(1)
        } else {
            music.wawawawaa.play()
            info.changeScoreBy(-1)
        }
    }
}
let match = 0
let guess: string[] = []
let text_list: string[] = []
scene.setBackgroundImage()
let picnicFood = sprites.create(, SpriteKind.Player)
picnicFood.setImage()
let picnicfoodList = [
sprites.food.smallHam,
sprites.food.smallStrawberry,
sprites.food.smallBurger,
sprites.food.smallDrumstick,
sprites.food.smallTaco
]
text_list = [
"ham",
"strawberry",
"burger",
"drumstick",
"taco"
]
for (let index = 0; index <= 4; index++) {
    picnicFood.setImage(picnicfoodList[index])
    pause(500)
}
picnicFood.destroy()
guess = game.askForString("What food was in Yogi's basket?")
evaluateGuess(guess)
