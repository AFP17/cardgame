const express = require('express');
const http = require('http');
const socketIo = require('socket.io');
const cors = require('cors');
const path = require('path');

const app = express();
const server = http.createServer(app);
const io = socketIo(server, {
  cors: {
    origin: "*",
    methods: ["GET", "POST"]
  }
});

// Middleware
app.use(cors());
app.use(express.json());
app.use(express.static('public')); // Serve static files from public directory

// Routes
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// Game state management
const games = new Map(); // Map of game rooms
const players = new Map(); // Map of connected players

// Socket.IO connection handling
io.on('connection', (socket) => {
  console.log('New client connected');

  // Handle player connection
  socket.on('join_game', (data) => {
    const { playerName, gameId } = data;
    
    // Create new game if it doesn't exist
    if (!games.has(gameId)) {
      games.set(gameId, {
        players: new Map(),
        state: {
          turn: 0,
          board: {
            player1: [],
            player2: []
          }
        }
      });
    }

    // Add player to game
    const game = games.get(gameId);
    game.players.set(socket.id, {
      name: playerName,
      health: 30,
      mana: 1,
      hand: [],
      deck: []
    });

    // Send initial game state
    socket.emit('game_state', game.state);
  });

  // Handle card play
  socket.on('play_card', (data) => {
    const { gameId, cardIndex } = data;
    const game = games.get(gameId);
    const player = game.players.get(socket.id);

    if (player && player.hand[cardIndex]) {
      // TODO: Implement card playing logic
      // For now, just remove card from hand
      player.hand.splice(cardIndex, 1);
      
      // Update game state
      io.to(gameId).emit('game_state', game.state);
    }
  });

  // Handle player disconnection
  socket.on('disconnect', () => {
    console.log('Client disconnected');
    // TODO: Handle player disconnection
  });
});

// Start server
const PORT = process.env.PORT || 3000;
server.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
