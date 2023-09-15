//Choose any no. for the two cards between 2-11

let cards=[]
let sum=0
let hasBlackJack=false
let isStillAlive=false
let checkStart=true
let message=""
let messageEl=document.getElementById("message-el")
// let sumEl=document.getElementById("sum-el")
                      //OR
let sumEl=document.querySelector("#sum-el")  // '#' represents id
let cardsEl=document.getElementById("cards-el")

let player=    //Object Declaration
{
    name:"Player",
    chips:55,
}

let playerEl=document.getElementById("player-el")
playerEl.textContent=player.name+": $"+player.chips

function getRandomCard()
{
    // Ace is 11 and Jack,Queen,King all are 10
    //ie. total 13 cards in total, 2->11
    randNum=Math.floor(Math.random()*13)+1
    if(randNum===1)
    {
        return 11
    }
    else if(randNum>10)
    {
        return 10
    }
    else
    {
        return randNum
    }
}

function resetGame()
{
    location.reload()
}

function startGame()
{
    if(checkStart===true)
    {
        checkStart=false
        let firstCard=getRandomCard()
        let secondCard=getRandomCard()
        cards.push(firstCard)
        cards.push(secondCard)
        sum=firstCard+secondCard
        renderGame()
    }
}

function renderGame()
{
    cardsEl.textContent="Cards: "
    for(let i=0;i<cards.length;i++)
    {
        cardsEl.textContent+=cards[i]+" "
    }
    
    sumEl.textContent="Sum: "+sum
    if(sum===21)
    {
        message="Wohoo! You've got Blackjack!"
        hasBlackJack=true
        isStillAlive=false
    }
    else if(sum<21)
    {
        message="Do you want to draw a new card?"
        isStillAlive=true
    }
    else
    {
        message="You're out of the game!"
        isStillAlive=false
    }
    messageEl.textContent=message
}

function newCard()
{
    if(isStillAlive===true)
    {
        console.log("Drawing a new card from the deck!")
        let card=getRandomCard()
        sum+=card
        cards.push(card)
        renderGame()
    }
}



