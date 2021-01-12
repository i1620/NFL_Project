// All Credit goes to Jacob Oakley
// https://codepen.io/jacoboakley/pen/WRpdXb

const ball = document.querySelector(`.ball`);
const text = document.querySelector(`.text`);
const restart = document.querySelector(`.restart`);

let count = 0;

function playBall(e) {
    e.keyCode === 68 ? count = count + 20 : e.keyCode === 76 ? count = count - 20 : count; // Has D or L been pushed

    ball.style.setProperty(`--position`, `${count}%`); // Set margin-left to = count value

    count === 80 ? text.innerHTML = 'D Wins!' : count === -80 ? text.innerHTML = 'L Wins!' : text.innerHTML = 'GO! GO! GO!'; // Declares winner if count reachs -125 or 125;

    count === 80 || count === -80 ? (document.removeEventListener('keyup', playBall), restart.style.setProperty(`--visibility`, `visible`)) : ''; // Stop event listener and show Play Again button once someone wins  
};

function playAgain() {
    window.location.reload(true)  // Starts game over by reloading window
};


document.addEventListener('keyup', playBall);
restart.addEventListener('click', playAgain);

