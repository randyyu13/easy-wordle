// GameBoard.jsx
import React, { useState, useEffect } from 'react';
import Row from './Row';
import { localURL, wordDataApiUrl, upsertGame, isRealWord } from '../../../utils/api';

function GameBoard({ gameData: initialGameData }) {
  const initialGrid = Array(6).fill(Array(5).fill(''));
  
  // Initialize grid with guessed words
  initialGameData.guessed_words.forEach((word, index) => {
    initialGrid[index] = word.split('');
  });

  const [grid, setGrid] = useState(initialGrid);
  const [currentRow, setCurrentRow] = useState(initialGameData.guessed_words.length);
  const [currentCol, setCurrentCol] = useState(0);
  const [isGameOver, setIsGameOver] = useState(false);
  const [gameData, setGameData] = useState(initialGameData);

  useEffect(() => {
    const handleKeyDown = (event) => {
      if (event.key.length === 1 && event.key.match(/[a-z]/i) || event.key === 'Enter' || event.key === 'Backspace') {
        updateGrid(event.key.toUpperCase());
      }
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [currentRow, currentCol]);

  const updateGrid = (keystroke) => {
    setGrid((prevGrid) => {
      const newGrid = prevGrid.map((row) => [...row]);

      if (keystroke.length === 1 && keystroke.match(/[a-z]/i)) {
        if (currentCol < 5) {
          newGrid[currentRow][currentCol] = keystroke;
          setCurrentCol(currentCol + 1);
        }
      } else if (keystroke === 'BACKSPACE') {
        if (currentCol > 0) {
          setCurrentCol(currentCol - 1);
          newGrid[currentRow][currentCol - 1] = '';
        }
      } else if (keystroke === 'ENTER') {
        if (currentCol === 5 && currentRow < 6) {
          handleGuess(newGrid[currentRow]).then(isValid => {
            if(isValid) {
              setCurrentRow(currentRow + 1);
              setCurrentCol(0);
            }
          });
        }
      }

      return newGrid;
    });
  };

  async function handleGuess(row) {
    const guess = row.join('').toLowerCase();
    console.log('guess', guess);
    // api call to check if guess is a valid word
    // if valid return true and update the grid
    // if not valid return false and do not update the grid
    // if the valid guess is correct, update the grid with the correct letters
    // if the valid guess is incorrect, update the grid with the incorrect letters

    const response = await isRealWord(wordDataApiUrl, guess);
    const isReal = response.length > 0 && response[0].word === guess;

    if(isReal) {
      // Convert existing letters to Set, add new letters, convert back to array
      const existingLetters = new Set(gameData.guessed_letters || []);
      guess.split('').forEach(letter => existingLetters.add(letter));
      
      const updatedGame = {
        word: gameData.word,
        user_id: gameData.user_id,
        guessed_letters: Array.from(existingLetters),
        guessed_words: [...(gameData.guessed_words || []), guess]
      };
      
      await upsertGame(localURL, updatedGame)
      setGameData(updatedGame);

      if(guess === gameData.word) {
        console.log('You win');
      } else {
        if(currentRow === 6) {
          console.log('You lose');
        }
      }
    } else {
      console.log('Invalid guess');
    }

    return isReal;
  }

  return (
    <div className="game-board">
      {grid.map((row, rowIndex) => (
        <Row key={rowIndex} letters={row} />
      ))}
    </div>
  );
}

export default GameBoard;