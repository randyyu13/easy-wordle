// Row.jsx
import React from 'react';
import Cell from './Cell';

function Row({ letters }) {
  return (
    <div className="row">
      {letters.map((letter, index) => (
        <Cell key={index} letter={letter} />
      ))}
    </div>
  );
}

export default Row;