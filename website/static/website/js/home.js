var typed2 = new Typed('.h1-home-header', {
    strings: ['<b>WORK HARDER</b>','<b>WORK SMARTER</b>','<b>WORK SMARTER =)</b>','<b>WORK SMARTER</b>'],
    startDelay: 1000,
    typeSpeed: 100,
    backSpeed: 50,
    fadeOut: false,
    loop: false,
    onComplete: function(self) {
        setTimeout(function() {
            $('.typed-cursor').hide();
        }, 5000);
     },
});

function topFunction() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}
