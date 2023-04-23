'use strict';

// navbar variables
const nav = document.querySelector('.mobile-nav');
const navMenuBtn = document.querySelector('.nav-menu-btn');
const navCloseBtn = document.querySelector('.nav-close-btn');

// theme toggle variables
const themeBtn = document.querySelectorAll('.theme-btn');
let currentTheme = localStorage.getItem('theme') || 'light-theme';

// set initial theme
document.body.classList.add(currentTheme);
for (let i = 0; i < themeBtn.length; i++) {
  themeBtn[i].classList.add(currentTheme === 'light-theme' ? 'light' : 'dark');
}

// navToggle function
const navToggleFunc = function () { nav.classList.toggle('active'); }

navMenuBtn.addEventListener('click', navToggleFunc);
navCloseBtn.addEventListener('click', navToggleFunc);

// add event listener to theme buttons
for (let i = 0; i < themeBtn.length; i++) {
  themeBtn[i].addEventListener('click', function () {
    currentTheme = currentTheme === 'light-theme' ? 'dark-theme' : 'light-theme';
    document.body.classList.remove('light-theme', 'dark-theme');
    document.body.classList.add(currentTheme);
    for (let j = 0; j < themeBtn.length; j++) {
      themeBtn[j].classList.toggle('light', currentTheme === 'light-theme');
      themeBtn[j].classList.toggle('dark', currentTheme === 'dark-theme');
    }
    localStorage.setItem('theme', currentTheme);
  });
}
