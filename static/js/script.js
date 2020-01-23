var tags = [
    'The writings of a Software Engineer and Chief Executive.',
    'The writings of a Software Engineer.',
    'The writings of a Chief Executive.',
    'The writings of a Programmer.',
    'The blog of a guy that writes code.',
    'Do you think pigeons have feelings?',
    'This site is open source!',
    'Built in Django!',
    'Built with Love!',
    'Built in the USA!',
];

$(document).ready(function() {
    var notice = "Copyright &copy; 2014-" + new Date().getFullYear() + " Russ 'trdwll' Treadwell. All rights reserved.";
    $('.copy').append(notice);

    var tag = tags[Math.floor(Math.random() * tags.length)];
    $('#home_tagline').html(tag);
});