function toggleButton(el) {
  el.classList.toggle("active");
  var state = el.classList.contains("active");
  console.log("Toggle state:", state);
  // send event or command here
}
