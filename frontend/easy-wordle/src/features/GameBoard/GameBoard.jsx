// GameBoard.jsx
import React, { useState, useEffect } from 'react';
import Row from './Row';

function GameBoard() {
  const [grid, setGrid] = useState(Array(6).fill(Array(5).fill(''))); // 6 rows, 5 columns
  const [currentRow, setCurrentRow] = useState(0);
  const [currentCol, setCurrentCol] = useState(0);

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
          if(handleGuess(newGrid[currentRow])) {
            setCurrentRow(currentRow + 1);
            setCurrentCol(0);
          }
        }
      }

      return newGrid;
    });
  };


  function handleGuess(row) {
    const guess = row.join('');
    console.log('guess', guess);
    // api call to check if guess is a valid word
    // if valid return true and update the grid
    // if not valid return false and do not update the grid
    // if the valid guess is correct, update the grid with the correct letters
    // if the valid guess is incorrect, update the grid with the incorrect letters

  
    //placeholder
    return true;
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