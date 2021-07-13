

// -------homepage--------


let mouseCursor = document.querySelector('.cursor');
let navLinks = document.querySelectorAll('.nav-links li');
let explore =document.querySelector('.explore h1');
let lists =document.querySelector('.home-posts');
console.log(lists)
let run =document.querySelector('.run');



console.log(navLinks)

window.addEventListener("mousemove",cursor);

function cursor(e){
  mouseCursor.style.top = e.pageY+'px';
  mouseCursor.style.left = e.pageX+'px';
}

explore.addEventListener("mouseover",()=>{
  mouseCursor.classList.add("link-grow");
  explore.classList.add("text-grow");
})
explore.addEventListener("mouseleave",()=>{
  mouseCursor.classList.remove("link-grow");
  explore.classList.remove("text-grow");
})


navLinks.forEach(link => {
  link.addEventListener("mouseover",()=>{
    mouseCursor.classList.add("link-grow");
    link.classList.add("text-grow");
  })

  link.addEventListener("mouseleave",()=>{
    mouseCursor.classList.remove("link-grow");
    link.classList.remove("text-grow");
    explore.classList.remove("text-grow");

  })
})


// ------ratings---------


// Profile page
