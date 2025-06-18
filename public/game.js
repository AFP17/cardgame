const socket = io();

// Game state
let gameId = null;
let playerName = null;
let playerHand = [];

// DOM Elements
const player1Health = document.getElementById('player1-health');
const player1Mana = document.getElementById('player1-mana');
const player1Plastic = document.getElementById('player1-plastic');
const player1Paper = document.getElementById('player1-paper');
const player1Glass = document.getElementById('player1-glass');
const player1Organic = document.getElementById('player1-organic');

const player2Health = document.getElementById('player2-health');
const player2Mana = document.getElementById('player2-mana');
const player2Plastic = document.getElementById('player2-plastic');
const player2Paper = document.getElementById('player2-paper');
const player2Glass = document.getElementById('player2-glass');
const player2Organic = document.getElementById('player2-organic');

const playerHandContainer = document.getElementById('player-hand');

// Initialize game
function initGame() {
    // Get player name from prompt
    playerName = prompt('Enter your player name:');
    if (!playerName) {
        playerName = 'Player';
    }

    // Generate random game ID
    gameId = Math.random().toString(36).substring(2, 15);

    // Join game
    socket.emit('join_game', { playerName, gameId });
}

// Update game state
function updateGameState(state) {
    // Update player 1 info
    player1Health.textContent = state.player1.health;
    player1Mana.textContent = state.player1.mana;
    player1Plastic.textContent = state.player1.resources.plastic;
    player1Paper.textContent = state.player1.resources.paper;
    player1Glass.textContent = state.player1.resources.glass;
    player1Organic.textContent = state.player1.resources.organic;

    // Update player 2 info
    player2Health.textContent = state.player2.health;
    player2Mana.textContent = state.player2.mana;
    player2Plastic.textContent = state.player2.resources.plastic;
    player2Paper.textContent = state.player2.resources.paper;
    player2Glass.textContent = state.player2.resources.glass;
    player2Organic.textContent = state.player2.resources.organic;

    // Update player hand
    updatePlayerHand(state.player1.hand);
}

// Update player hand display
function updatePlayerHand(hand) {
    playerHand = hand;
    playerHandContainer.innerHTML = '';

    hand.forEach((card, index) => {
        const cardElement = createCardElement(card, index);
        playerHandContainer.appendChild(cardElement);
    });
}

// Create card element
function createCardElement(card, index) {
    const cardElement = document.createElement('div');
    cardElement.className = 'card';
    cardElement.innerHTML = `
        <div class="card-name">${card.name}</div>
        <div class="card-stats">${card.attack}/${card.defense}</div>
        <div class="card-cost">${card.cost}</div>
        <div class="card-type">${card.trash_type}</div>
    `;

    cardElement.addEventListener('click', () => {
        socket.emit('play_card', { gameId, cardIndex: index });
    });

    return cardElement;
}

// Socket event listeners
socket.on('game_state', (state) => {
    updateGameState(state);
});

// Initialize game when page loads
window.addEventListener('load', initGame);
