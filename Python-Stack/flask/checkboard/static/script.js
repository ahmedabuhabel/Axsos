// get the first board element
let board = document.getElementsByClassName("board")[0];
// Here is a board loop to create the checkboard
for (let i = 0; i < rows; i++) {
  // create cell container for each row
  const cellContainer = document.createElement("div");
  // add style for each row
  cellContainer.classList.add("cellContainer");

  for (let j = 0; j < columns; j++) {
    // create a cell for each column
    const cell = document.createElement("div");
    // add style for each cell
    cell.classList.add("cell");
    // check if cell is odd or even to determine color
    if ((i + j) % 2 === 0) {
      cell.style.backgroundColor = color1;
    } else {
      cell.style.backgroundColor = color2;
    }
    // add cell to cell container
    cellContainer.appendChild(cell);
  }
  // add cell container to board
  board.appendChild(cellContainer);
}
