const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();
const timeoutDur = 3000;
const fadeFX = () => {
  $('#message').fadeOut('slow');
};
setTimeout(fadeFX, timeoutDur);
