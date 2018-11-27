  var typed2 = new Typed('.h1-home-header', {
    strings: ['WORK HARD','WORK SMART'],
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

  $(".typed-cursor").addClass("display-2");