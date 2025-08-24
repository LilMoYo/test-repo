// Paddle properties

// set paddleWidth here 💖
// set paddleHeight here 💖
let paddleWidth = 10;
let paddleHeight = 10;

let paddleX;
let paddleY;
let paddleSpeed = 10;

// Ball properties
let ballX;
let ballY;
let ballDiameter = 20;
let ballSpeedX = 4;
let ballSpeedY = 4;

function setup() {
  createCanvas(600, 400);

  // Paddle position
  paddleX = width / 2 - paddleWidth / 2;
  paddleY = height - paddleHeight - 10;

  // Ball position
  ballX = 0;
  ballY = 0;
}

function draw() {
  // background color
  background(0);

  // Draw paddle here 💖
  rect(paddleX, paddleY, 100, 20);

  // Ball
  ellipse(ballX, ballY, ballDiameter);

  // Ball movement
  ballX += ballSpeedX;
  ballY += ballSpeedY;

  // Ball bounces off left and right walls
  if (ballX < 0 || ballX > width) {
    ballSpeedX *= -1;
  }

  // Ball bounces off the top
  if (ballY < 0) {
    ballSpeedY *= -1;
  }

  // Ball bounces off the paddle
  if (
    ballY + ballDiameter / 2 > paddleY &&
    ballX > paddleX &&
    ballX < paddleX + paddleWidth
  ) {
    ballSpeedY *= -1;
  }

  // Check if the ball goes off the bottom (game over)
  if (ballY > height) {
    textSize(32);
    fill(255);
    textAlign(CENTER);
    text("Game Over", width / 2, height / 2);
    noLoop(); // Stop the game
  }

  // Add paddle movement conditionals here 💖
  if (keyIsDown(65) === true) {
    paddleX -= paddleSpeed;
  }

  if (keyIsDown(68) === true) {
    paddleX += paddleSpeed;
  }

  // Keep paddle within the canvas boundaries
  paddleX = constrain(paddleX, 0, width - paddleWidth);
}
