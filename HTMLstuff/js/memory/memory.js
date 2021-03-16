var animals = ["turtle", "snail", "parrot", "rabbit", "bear", "panda", "fish", "shark", "crab", "pig", "rhinoceros", "corgi"]

var animalPairs = animals.concat(animals)

var randomAnimalPairs = shuffle(animalPairs)
var activeCards = []

displayCards(randomAnimalPairs)

function displayCards(pairs) {
    pairs.forEach(displayCard)
}

function displayCard(animal) {
    let card = document.createElement("div")
    card.classList.add("card")
    let img = document.createElement("img")
    img.src = `https://raw.githubusercontent.com/miezuit/html-css-python/main/js/memory/img/icons8-${animal}.png`
    card.addEventListener("click", onClick)
    card.appendChild(img)
    document.querySelector("#grid").appendChild(card)
}

function onClick(event) {
    let card = event.target

    if (activeCards.lenght == 0) {
        card.querySelector("img").style.visibility = "visible"
        activeCards.push(card)
    } else if (activeCards.lenght == 1) {
        card.querySelector("img").style.visibility = "visible"
        activeCards.push(card)
        if (areCardsTheSame(activeCards[0], activeCards[1])) {
            activeCards[0].removeEventListener("click", onClick)
            activeCards[1].removeEventListener("click", onClick)
            activeCards == []
        } else {
            setTimeout(hideActiveCards, 2000)
        }
    }
   
}

function hideActiveCards() {
    activeCards[0].querySelector("img").style.visibility = "hidden"
    activeCards[1].querySelector("img").style.visibility = "hidden"
    activeCards = []
}

function areCardsTheSame(card1, card2) {
    card1.querySelector("img").src == card2.querySelector("img").src
}

function shuffle(list) {
    return list.sort(() => .5 - Math.random())
}

