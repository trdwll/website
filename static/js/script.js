var tags = [
  'Am I even good enough to have imposter syndrome?',
  'The writings of a Software Engineer and Chief Executive.',
  'The writings of a Software Engineer.',
  'The writings of a Game Engineer.',
  'The writings of a Chief Executive.',
  'The writings of a Programmer.',
  'The blog of a guy that writes code.',
  'Do you think pigeons have feelings?',
  'This site is open source!',
  'Built in Django!',
  'Built in Django &amp; Powered by FreeBSD!',
  'Built with Love!',
  'Built with <span class="text-red-800"><i class="fas fa-heart"></i></span>',
  'Built in the USA!',
  '"Arguing that you don\'t care about the right to privacy because you have nothing to hide, is no different than saying you don\'t care about free speech because you have nothing to say." - Edward Snowden',
  'Trust, but verify',
  '"All our dreams can come true, if we have the courage to pursue them." - Walt Disney',
  '"Someone is sitting in the shade today because someone planted a tree a long time ago." - Warren Buffett',
  '"If you can\'t explain it simply, you don\'t understand it well enough." - Albert Einstein',
  'I love code',
  'I love you <span class="text-red-800"><i class="fas fa-heart"></i></span>',
  'Thanks for visiting my site! :)',
  '"The way to get started is to quit talking and begin doing." - Walt Disney',
  '"Life is what happens when you\'re busy making other plans." - John Lennon',
  '"Tell me and I forget. Teach me and I remember. Involve me and I learn." - Benjamin Franklin',
  '"Never let the fear of striking out keep you from playing the game." - Babe Ruth',
  '"The way to get started is to quit talking and begin doing." - Walt Disney'
];

const getInitialTheme = () => {
  const row = document.cookie.split('; ').find((row) => row.startsWith('theme='));
  if (row && row.split('=')[1]) {
    return row.split('=')[1];
  }

  const userMedia = window.matchMedia('(prefers-color-scheme: dark)');
  if (userMedia.matches) {
    return 'dark';
  }

  return 'light';
};

const setTheme = (theme) => {
  const root = document.documentElement;
  const isDark = theme === 'dark';

  root.classList.remove(isDark ? 'light' : 'dark');
  root.classList.add(theme);

  document.cookie = `theme=${theme}; path=/; SameSite=Lax;`;

  const light = document.getElementById('light-hljs');
  const dark = document.getElementById('dark-hljs');

  if (light && dark) {
    (isDark ? dark : light).removeAttribute("disabled");
    (isDark ? light : dark).setAttribute("disabled", "disabled");
  }

  const themeIcon = document.getElementById('theme-icon');

  if (themeIcon) {
    themeIcon.classList.remove(isDark ? 'fa-sun' : 'fa-moon');
    themeIcon.classList.add(isDark ? 'fa-sun' : 'fa-moon');
  }

  return theme;
};

document.addEventListener('DOMContentLoaded', function (event) {
  let theme = setTheme(getInitialTheme());
  const toggleBtn = document.getElementById('theme-toggle');

  toggleBtn.addEventListener('click', () => {
    theme = setTheme(theme === 'dark' ? 'light' : 'dark');
  });

  document.getElementById('cur-year').innerHTML = new Date().getFullYear().toString();

  if (document.getElementById('home-tagline'))
  {
    var tag = tags[Math.floor(Math.random() * tags.length)];
    document.getElementById('home-tagline').innerHTML = tag;
  }

  const menuBtn = document.getElementById('menu-btn');
  const menuNav = document.getElementById('menu-nav');

  menuBtn.addEventListener('click', (e) => {
    e.preventDefault();
    menuNav.classList.toggle('hidden');
  });
});
