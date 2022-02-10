/*
  this was made thanks to Wes Bos's video:
  https://www.youtube.com/watch?v=C9EWifQ5xqA
*/

const list = document.querySelector(".movie-list");
let isDown = false;
let StartX, scrollLeft;

list.addEventListener("mousedown", (e) => {
  isDown = true;
  StartX = e.pageX - list.offsetLeft;
  scrollLeft = list.scrollLeft;
});
list.addEventListener("mouseleave", () => {
  isDown = false;
});
list.addEventListener("mouseup", () => {
  isDown = false;
});
list.addEventListener("mousemove", (e) => {
  if (!isDown) return;
  e.preventDefault();
  const x = e.pageX - list.offsetLeft;
  const walk = x - StartX;
  list.scrollLeft = scrollLeft - walk;
});
