// Game.jsx
import React, { useState, useEffect } from 'react';
import GameBoard from '../GameBoard';
import { getOrCreateGuestID } from '../../../utils/cookie';
import { getGameByUserId, createGame, getWordOfTheDay, localURL } from '../../../utils/api';
import '../GameBoard/GameBoard.css';

function Game() {
  const [gameData, setGameData] = useState(null);

  useEffect(() => {
    const initializeGame = async () => {
      // Get or create guest ID
      const id = getOrCreateGuestID();

      // Try to get existing game
      let game = await getGameByUserId(localURL, id);
      
      // If no game exists, create a new one
      if (!game) {
        const wordOfDay = await getWordOfTheDay(localURL);

        try {
          await createGame(localURL, {
            user_id: id,
            word: wordOfDay.word,
            guessed_words: [],
            guessed_letters: []
          });
          game = await getGameByUserId(localURL, id);
        } catch (error) {
          console.error('Error creating game:', error);
        }
      }

      setGameData(game);
    };

    initializeGame();
  }, []);

  if (!gameData) {
    return <div>Loading...</div>;
  }

  return (
    <div className="game">
      <GameBoard gameData={gameData} />
    </div>
  );
}

export default Game;