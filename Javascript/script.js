// canvas creator
var canvas = document.getElementById('myCanvas');
var ctx = canvas.getContext('2d');

// variables for position of circle
var x = 0;
var y = 0;

// variable for location of paddle
var paddleX = 202.5;

// variable to track the score
var score = 0;

// variables for button presses
var rightPressed = false;
var leftPressed = false;

document.addEventListener("keydown", keyDownHandler, false);
document.addEventListener("keyup", keyUpHandler, false);

function keyDownHandler(e) {
    if(e.keyCode == 39) {
        rightPressed = true;
    }
    else if(e.keyCode == 37) {
        leftPressed = true;
    }
}

function keyUpHandler(e) {
    if(e.keyCode == 39) {
        rightPressed = false;
    }
    else if(e.keyCode == 37) {
        leftPressed = false;
    }
}

// function to draw parts
function draw(){
  // clear canvas
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  // draw circle
  ctx.beginPath();
  ctx.arc(x, y, 10, 0, Math.PI*2);
  ctx.fillStyle = "#0095DD";
  ctx.fill();
  ctx.closePath();

  // draw the paddle
  ctx.beginPath();
  ctx.rect(paddleX, 310, 75, 10);
  ctx.fillStyle = "#0095DD";
  ctx.fill();
  ctx.closePath();

  // draw the score
  ctx.font = "16px Arial";
  ctx.fillStyle = "#0095DD";
  ctx.fillText("Score: "+score, 8, 20);

  // move the circle 2 units down
  y += 2;

  // move the paddle according to key
  if(rightPressed) {
    paddleX += 7;
  }
  else if(leftPressed) {
    paddleX -= 7;
  }

  // check if ball hits paddle
  if ( (x < paddleX + 40) && ( x > paddleX - 40) && (y > 300 )){
    x = Math.random() * (canvas.height);
    y = 0;
    score++;
  }

  // move circle back to top if circle reaches bottom
  if (y == canvas.height+30){
    x = Math.random() * (canvas.height);
    y = 0;
  }
}

// calls draw function every 10 milliseconds
setInterval(draw, 10);
