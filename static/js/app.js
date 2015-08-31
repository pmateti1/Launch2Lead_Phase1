$(document).ready(function(){

    new WOW().init();

    $('.home_page').height($(window).height());

    if($('.contact_page').length != 0){
        $('.contact_page').crossfade();
    }

    if($('.company_page').length != 0){
        $('.company_page').crossfade();
    }

    if($('.work_page').length != 0){
        $('.work_page').crossfade();
    }


    $("#owl-example").owlCarousel({
        items : 1,
        itemsCustom : false ,
        itemsDesktop : [1199,1],
        itemsDesktopSmall : [980,1],
        itemsTablet: [768,1],
        itemsTabletSmall: false,
        itemsMobile : [479,1],
        singleItem : false,
        itemsScaleUp : false,
        autoPlay : true,
        stopOnHover : true,
        navigation : true,
        autoHeight:false

    });

    var animationNotDone = true;

    if($(window).width() > 640){
        $('.earlystage').waypoint(function(direction){
            if(direction == 'down' && animationNotDone){
                $(this).find('.left').slideDown('slow', function(){
                    $('.brainstorm img, .brainstorm h1, .brainstorm p').css({opacity: 0.0, visibility: "visible"}).animate({opacity: 1.0});
                });
            }
        });

        $('.brainstorm').waypoint(function(direction){
            if(direction == 'down' && animationNotDone){
                $(this).find('.right').slideDown('slow', function(){
                    $('.making img, .making h1, .making p').css({opacity: 0.0, visibility: "visible"}).animate({opacity: 1.0});
                });
            }
        });

        $('.making').waypoint(function(direction){
            if(direction == 'down' && animationNotDone){
                $(this).find('.left').slideDown('slow', function(){
                    $('.decoration img, .decoration h1, .decoration p').css({opacity: 0.0, visibility: "visible"}).animate({opacity: 1.0});
                });
            }
        });

        $('.decoration').waypoint(function(direction){
            if(direction == 'down' && animationNotDone){
                $(this).find('.right').slideDown('slow', function(){
                    $('.selfsustain img, .selfsustain h1, .selfsustain p').css({opacity: 0.0, visibility: "visible"}).animate({opacity: 1.0});
                });
            }
        });

        $('.selfsustain').waypoint(function(direction){
            if(direction == 'down' && animationNotDone){
                $(this).find('.left').slideDown('slow', function(){
                    $('.client-heart img, .client-heart h1').css({opacity: 0.0, visibility: "visible"}).animate({opacity: 1.0});
                });

                animationNotDone = false;
            }
        });

    }else{

        $('.earlystage').waypoint(function(direction){
            if(direction == 'down' && animationNotDone){
                $('.brainstorm img, .brainstorm h1, .brainstorm p').css({opacity: 0.0, visibility: "visible"}).animate({opacity: 1.0});
            }
        });

        $('.brainstorm').waypoint(function(direction){
            if(direction == 'down' && animationNotDone){
                $('.making img, .making h1, .making p').css({opacity: 0.0, visibility: "visible"}).animate({opacity: 1.0});
            }
        });

        $('.making').waypoint(function(direction){
            if(direction == 'down' && animationNotDone){
                $('.decoration img, .decoration h1, .decoration p').css({opacity: 0.0, visibility: "visible"}).animate({opacity: 1.0});
            }
        });

        $('.decoration').waypoint(function(direction){
            if(direction == 'down' && animationNotDone){
                $('.selfsustain img, .selfsustain h1, .selfsustain p').css({opacity: 0.0, visibility: "visible"}).animate({opacity: 1.0});
            }else{
                $('.selfsustain img, .selfsustain h1, .selfsustain p').css({opacity: 0.0, visibility: "hidden"});
            }
        });

        $('.selfsustain').waypoint(function(direction){
            if(direction == 'down' && animationNotDone){
                $('.client-heart img, .client-heart h1').css({opacity: 0.0, visibility: "visible"}).animate({opacity: 1.0});
            }

            animationNotDone = false;
        });
    }

});

