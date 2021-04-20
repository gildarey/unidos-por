(function($) {
  
    "use strict";
    
/*
|===================
| SLIDER Preloader
|===================
*/
    $(window).on('load', function() {
      $('.slider_preloader_status').fadeOut();
      $('.slider_preloader').delay(350).fadeOut('slow');
      $('.header-slider').removeClass("header-slider-preloader");
    })

/*
|===================
| SLIDER JS
|===================
*/
    
    $(window).load(function(){
       $('#header-slider #animation-slide').owlCarousel({
              autoHeight: true,
              items: 1,
              loop: true,
              autoplay: true,
              dots: true,
              nav: true,
              autoplayTimeout: 7000,
              navText: ["<i class='fa fa-angle-left'></i>", "<i class='fa fa-angle-right'></i>"],
              animateIn: "zoomIn",
              animateOut: "fadeOutDown",
              autoplayHoverPause: false,
              touchDrag: true,
              mouseDrag: true
          });
        $("#animation-slide").on("translate.owl.carousel", function () {
            $(this).find(".owl-item .slide-text > *").removeClass("fadeInUp animated").css("opacity","0");
            $(this).find(".owl-item .slide-img").removeClass("fadeInRight animated").css("opacity","0");
        });          
        $("#animation-slide").on("translated.owl.carousel", function () {
            $(this).find(".owl-item.active .slide-text > *").addClass("fadeInUp animated").css("opacity","1");
            $(this).find(".owl-item.active .slide-img").addClass("fadeInRight animated").css("opacity","1");
        });
    });
    
/*
|=====================
| NAV FIXED ON SCROLL
|=====================
*/
    
    $(window).on('scroll', function() {
        var scroll = $(window).scrollTop();
        if (scroll >= 50) {
            $(".nav-scroll").addClass("strict");
        } else {
            $(".nav-scroll").removeClass("strict");
        }
    });
    

/*
|===========
| FANCYBOX
|===========
*/
        
    $(".single_image").fancybox({
    
    });
    
    $( document ).ready(function() {

/*
|====================
| Mobile NAv trigger
|====================
*/
  
      $('#mobile-menu-active').meanmenu();
          var win = $(window);
          var headerArea = $('.menu-spacing ');
          var header3 = $('.menu-spacing ');
          var stick = 'stick';
          var stick2 = 'stick2';
  	
          win.on('scroll',function() {    
             var scroll = win.scrollTop();
             if (scroll < 245) {
              headerArea.removeClass(stick);
             }else{
              headerArea.addClass(stick);
             }
          });
          win.on('scroll',function() {    
             var scroll = win.scrollTop();
             if (scroll < 100) {
              header3.removeClass(stick2);
             }else{
              header3.addClass(stick2);
             }
      });
      
      $('ul.nav li.dropdown').hover(function() {
        $(this).find('.dropdown-menu').stop(true, true).delay(200).fadeIn(500);
      }, function() {
        $(this).find('.dropdown-menu').stop(true, true).delay(200).fadeOut(500);
      });
    
/*
|===================
| PROGRESS BAR
|===================
*/
    
      
     $(".progress-bar").each(function(){
      var width = $(this).text();
      $(this).css("width", width)
        .empty()
        .append('<span class="progress-circle"></span>');                
    });
      
/*
|================
| WOW ANIMATION
|================
*/

    	var wow = new WOW({
          mobile: false  // trigger animations on mobile devices (default is true)
      });
      wow.init();
      
/*
|===================
| EVENT SLIDE 
|===================
*/
      
    $('#my-carousel').owlCarousel({
          loop: false,
          responsiveClass: true,
          nav: true,
          navText: ["<i class='fa fa-angle-left'></i>", "<i class='fa fa-angle-right'></i>"],
          responsive:{
              0:{
                  items: 1,
                  nav: true,
                  loop:true
              },
              768:{
                  items: 2,
                  nav:true,
                  loop:true
              },
              992:{
                  items: 3,
                  nav:true,
                  loop:true
              }
          }
      })
      
    /*
    |=====================
    | SMOTHSCROLL
    |=====================
    */
      
      $('a[href*="#"]:not([href="#"])').click(function() {
        if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
          var target = $(this.hash);
          target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
          if (target.length) {
            $('html, body').animate({
              scrollTop: target.offset().top
            }, 1000);
            return false;
          }
        }
      });

    /*
    |================
    | CONTACT FORM
    |================
    */
        
      $("#contactForm").validator().on("submit", function (event) {
          if (event.isDefaultPrevented()) {
            // handle the invalid form...
            formError();
            submitMSG(false, "Did you fill in the form properly?");
          } else {
            // everything looks good!
            event.preventDefault();
            submitForm();
          }
       });
  
      function submitForm(){
        var name = $("#name").val();
        var email = $("#email").val();
        var message = $("#message").val();
        $.ajax({
            type: "POST",
            url: "process.php",
            data: "name=" + name + "&email=" + email + "&message=" + message,
            success : function(text){
                if (text == "success"){
                    formSuccess();
                  } else {
                    formError();
                    submitMSG(false,text);
                  }
              }
          });
      }
      function formSuccess(){
          $("#contactForm")[0].reset();
          submitMSG(true, "Message Sent!")
      }
  	  function formError(){   
  	    $("#contactForm").removeClass().addClass('shake animated').one('webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend', function(){
  	        $(this).removeClass();
  	    });
  	  }
      function submitMSG(valid, msg){
        if(valid){
          var msgClasses = "h3 text-center fadeInUp animated text-success";
        } else {
          var msgClasses = "h3 text-center shake animated text-danger";
        }
        $("#msgSubmit").removeClass().addClass(msgClasses).text(msg);
      }
      
      
/*
|===================
| MAP
|===================
*/
      if( $('#ch-map').length ) {
          google.maps.event.addDomListener(window, 'load', init);
        
          function init() {
              var mapOptions = {
                  zoom: 14,
                  scrollwheel: false, 
                  navigationControl: false,
                  center: new google.maps.LatLng(40.6700, -73.9400), // New York
                  styles: [{"featureType":"landscape","elementType":"geometry","stylers":[{"hue":"#f3f4f4"},{"saturation":-84},{"lightness":59},{"visibility":"on"}]},
                  {"featureType":"landscape","elementType":"labels","stylers":[{"hue":"#ffffff"},{"saturation":-100},{"lightness":100},{"visibility":"off"}]},
                  {"featureType":"poi.park","elementType":"geometry","stylers":[{"hue":"#83cead"},{"saturation":1},{"lightness":-15},{"visibility":"on"}]},
                  {"featureType":"poi.school","elementType":"all","stylers":[{"hue":"#d7e4e4"},{"saturation":-60},{"lightness":23},{"visibility":"on"}]},
                  {"featureType":"road","elementType":"geometry","stylers":[{"hue":"#ffffff"},{"saturation":-100},{"lightness":100},{"visibility":"on"}]},
                  {"featureType":"road","elementType":"labels","stylers":[{"hue":"#bbbbbb"},{"saturation":-100},{"lightness":26},{"visibility":"on"}]},
                  {"featureType":"road.highway","elementType":"geometry","stylers":[{"hue":"#ffcc00"},{"saturation":100},{"lightness":-22},{"visibility":"on"}]},
                  {"featureType":"road.arterial","elementType":"geometry","stylers":[{"hue":"#ffcc00"},{"saturation":100},{"lightness":-35},{"visibility":"simplified"}]},
                  {"featureType":"water","elementType":"all","stylers":[{"hue":"#7fc8ed"},{"saturation":55},{"lightness":-6},{"visibility":"on"}]},
                  {"featureType":"water","elementType":"labels","stylers":[{"hue":"#7fc8ed"},{"saturation":55},{"lightness":-6},{"visibility":"off"}]}]
              };

              // Get the HTML DOM element that will contain your map 
              // We are using a div with id="map" seen below in the <body>
              var mapElement = document.getElementById('ch-map');

              // Create the Google Map using our element and options defined above
              var map = new google.maps.Map(mapElement, mapOptions);

              // Let's also add a marker while we're at it
              var marker = new google.maps.Marker({
                  position: new google.maps.LatLng(40.6700, -73.9400),
                  map: map,
                  title: 'Charity!'
              });
          }
      }

  });
}(jQuery));