var tags = [
    'The writings of a Software Engineer and Chief Executive.',
    'The writings of a Software Engineer.',
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
];

$(document).ready(function() {
    $('.year').append(new Date().getFullYear());

    var tag = tags[Math.floor(Math.random() * tags.length)];
    $('#home_tagline').html(tag);

    const menuBtn = document.getElementById('menu-btn');
    const menuNav = document.getElementById('menu-nav');

    menuBtn.addEventListener('click', (e) => {
        e.preventDefault();

        menuNav.classList.toggle('hidden');
    });
});
