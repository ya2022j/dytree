"use strict";

$(document).ready(function () {
  if ($('.c-shopListOne').length > 0) {
    //initialize shopDetail when document ready
    shopDetailInit();
  }

  if ($('.js-narrowButton').length > 0) {
    //initialize narrowShopInit
    narrowShopInit();
  }

  if ($('.js-sendShopInfoModalButton').length > 0) {
    // initialize sendShopInfoModalInit
    sendShopInfoModalInit();
  }

  if ($('.js-reserveModalButton').length > 0) {
    // initialize reserveModalInit
    reserveModalInit();
  } //initialize TopPage scrollEvent


  if ($('.l-headerTop').length > 0) {
    scrollTopPageEvent();
  } //initialize swiper


  if ($('.swiper-container').length > 0) {
    swiperInit();
  }

  if ($('.js-subNav').length > 0) {
    //initialize scrollFitNav
    scrollFitNavInit();
  } //initialize Nav


  globalNavInit(); //initialize pageInScroll

  pageInScroll(); //initialize pageTopScroll

  pageTopScroll(); //initialize heroScrollMotion

  heroScrollMotion();
}); // shopDetail

var shopDetailInit = function shopDetailInit() {
  $('.c-shopListOne').on('click', function () {
    // var SelectShop = $(this).data('shop');
    var SelectLine = $(this).attr('data-line');
    var thisClose = false;
    var copyDetail = $(this).children('.c-shopListOneInner').children('.c-shopListDetailBox--outer').children('.c-shopListDetailBoxWrap').children('.c-shopListDetailBox').clone(true);

    if (!$(this).hasClass('c-shopListOne--opened')) {
      //SD
      $('.c-shopListOne--opened').children('.c-shopListOneInner').children('.c-shopListDetailBox--outer').slideUp(0, 'swing'); //Button

      $('.c-shopListOne--opened').children('.c-shopListOneInner').children('.c-shopListOneThumb').removeClass('c-shopListOneThumb--on');
      $('.c-shopListOne--opened').removeClass('c-shopListOne--opened');
    } else {
      thisClose = true;
      copyDetail = '';
    }

    $(this).toggleClass('c-shopListOne--opened');
    var TargetAfter = Math.ceil(SelectLine / 3) * 3;

    if (TargetAfter > $('.js-Filtered').length) {
      TargetAfter = $('.js-Filtered').length;
    }

    var ArrowNumber = SelectLine % 3; //PC Detail

    if (!thisClose) {
      var Speed = 350;

      if ($('.js-shopListDetail').length > 0) {
        $('.js-shopListDetail').slideUp(350, 'swing', function () {
          $('.js-shopListDetail').remove();
          $('[data-line="' + TargetAfter + '"]').after(function () {
            return '<div class="grid12__col-12 js-shopListDetail no-desktop c-shopListDetailBoxWrapOuter">' + '<div class="c-shopListDetailBoxWrap c-shopListDetailBoxWrap' + ArrowNumber + ' no-mobile js-shopListDetailWrap"></div>' + '</div>';
          });
          $('.js-shopListDetailWrap').append(copyDetail);
          $('.js-shopListDetail').slideDown(Speed, 'swing');
        });
      } else {
        $('.js-shopListDetail').remove();
        $('[data-line="' + TargetAfter + '"]').after(function () {
          return '<div class="grid12__col-12 js-shopListDetail no-desktop c-shopListDetailBoxWrapOuter">' + '<div class="c-shopListDetailBoxWrap c-shopListDetailBoxWrap' + ArrowNumber + ' no-mobile js-shopListDetailWrap"></div>' + '</div>';
        });
        $('.js-shopListDetailWrap').append(copyDetail);
        $('.js-shopListDetail').slideDown(Speed, 'swing');
      }
    } else {
      $('.js-shopListDetail').slideUp(350, 'swing', function () {
        $('.js-shopListDetail').remove();
      });
    } //SD Detail


    $(this).children('.c-shopListOneInner').children('.c-shopListDetailBox--outer').slideToggle(350, 'swing'); //Arrow

    $(this).children('.c-shopListOneInner').children('.c-shopListOneThumb').toggleClass('c-shopListOneThumb--on');
  });
  $('.c-shopListDetailBoxData__map a').on('click', function (e) {
    e.stopPropagation();
  });
  $('.c-shopListDetailBoxReserve__number a').on('click', function (e) {
    e.stopPropagation();
  });
  $('.c-shopListDetailBoxData__button').on('click', function (e) {
    e.stopPropagation();
  });
  $('.c-shopListDetailBoxReserve').on('click', function (e) {
    e.stopPropagation();
  });
}; // Narrow Shop


var narrowShopInit = function narrowShopInit() {
  $('.js-narrowDown').on('click', function () {
    $('.c-shopListNarrowDown').toggleClass('c-shopListNarrowDown--on');
    $('.c-shopListAreaList--outer').slideToggle(350, 'swing');
  });
  $('.js-narrowButton').on('click', function () {
    $(this).toggleClass('c-shopListAreaList__item--on');
    $(this).toggleClass('c-shopListAreaList__item--off');

    if ($(this).hasClass('js-narrowButtonArea')) {
      narrowArea($(this).attr('data-narrow-key'));
    }

    if ($(this).hasClass('js-narrowButtonKey')) {
      narrowKey($(this).attr('data-narrow-key'));
    } //Reset PullDown


    $('.js-shopListDetail').remove();
    $('.c-shopListDetailBox--outer').slideUp(0, 'swing');
    $('.c-shopListOneThumb--on').removeClass('c-shopListOneThumb--on');
    $('.c-shopListOne--opened').removeClass('c-shopListOne--opened');
  });
  var NarrowKeyArr = [// 'storefilter1',
    // 'storefilter2',
    // 'storefilter3',
    // 'storefilter4',
    // 'storefilter5',
  ];
  var NarrowAreaArr = [// 'kanto', 'tokai', 'kansai', 'hokkaido'
  ];

  function narrowArea(key) {
    if (NarrowAreaArr.indexOf(key) >= 0) {
      NarrowAreaArr.splice(NarrowAreaArr.indexOf(key), 1);
    } else if (NarrowAreaArr.indexOf(key) == -1) {
      NarrowAreaArr.push(key);
    }

    LoopFilter();
  }

  function narrowKey(key) {
    if (NarrowKeyArr.indexOf(key) >= 0) {
      NarrowKeyArr.splice(NarrowKeyArr.indexOf(key), 1);
    } else if (NarrowKeyArr.indexOf(key) == -1) {
      NarrowKeyArr.push(key);
    }

    LoopFilter();
  }

  function LoopFilter() {
    $('.js-Filtered').removeClass('js-Filtered');
    $('.js-shopOne').hide();
    $('.js-shopOne').addClass('js-yetFilter');
    $('.js-filterNone').addClass('no-display'); // Nothing Narrow

    if (NarrowAreaArr.length == 0 && NarrowKeyArr.length == 0) {
      $('.js-shopOne').show().addClass('js-Filtered');
      setLineGroup();
      return false;
    } // Double Area


    if (NarrowAreaArr.length > 1) {
      $('.js-filterNone').removeClass('no-display');
      setLineGroup();
      return false;
    }

    var ArrData = '';

    if (NarrowAreaArr.length > 0) {
      ArrData += '[data-area="' + NarrowAreaArr[0] + '"]';
    }

    for (var i = 0; i < NarrowKeyArr.length; i++) {
      ArrData += '[data-' + NarrowKeyArr[i] + '="true"]';
    }

    if ($(ArrData).length == 0) {
      $('.js-filterNone').removeClass('no-display');
      return false;
    }

    $(ArrData).show().addClass('js-Filtered');
    setLineGroup();
  }

  function setLineGroup() {
    var LineGroup = 0;
    $('[data-line]').attr('data-line', '');
    $('.js-Filtered').each(function (index, element) {
      LineGroup++;
      $(element).attr('data-line', LineGroup);
    });
  } // initLineGroup


  setLineGroup();
}; // Send Modal


var sendShopInfoModalInit = function sendShopInfoModalInit() {
  $('.js-sendShopInfoModalButton').on('click', function (e) {
    e.preventDefault();
    $('.js-sendShopInfoModal').removeClass('l-modalWrap--none');
  });
  $('.js-sendShopInfoModalClose').on('click', function () {
    $('.js-sendShopInfoModal').addClass('l-modalWrap--none');
  });
  $('.js-sendShopInfoModalBg').on('click', function () {
    $('.js-sendShopInfoModal').addClass('l-modalWrap--none');
  });
  $('.js-sendShopInfoCopy').on('click', function (e) {
    var input = document.createElement('textarea');
    input.setAttribute('id', 'copyinput');
    document.body.appendChild(input);
    input.value = $('.js-sendShopInfoCopyData').text();
    input.select();
    document.execCommand('copy');
    document.body.removeChild(input);
    alert('繧ｳ繝斐�縺励∪縺励◆縲�');
  });
}; // Reserve Modal


var reserveModalInit = function reserveModalInit() {
  $('.js-reserveModalButton').on('click', function (e) {
    e.preventDefault();
    e.stopPropagation();
    $('.js-reserveModal').removeClass('l-modalWrap--none');
    var Link1 = $(this).children('.js-reservation-1').text();
    var Link2 = $(this).children('.js-reservation-2').text();

    if (Link1 != '') {
      $('.js-reserveModalLink1').attr('href', $(this).children('.js-reservation-1').text());
      $('.js-reserveModalLink1').attr('onclick', "gtag('event', 'click', {'event_category': 'SeatWebBooking' , 'event_label': '" + $(this).children('.js-reservation-shop').text() + "'});");
      $('.js-reserveModalLink1').parent().parent().css({
        opacity: '1'
      });
    } else {
      $('.js-reserveModalLink1').attr('href', '');
      $('.js-reserveModalLink1').attr('onclick', 'return false;');
      $('.js-reserveModalLink1').parent().parent().css({
        opacity: '0.3'
      });
    }

    if (Link2 != '') {
      $('.js-reserveModalLink2').attr('href', $(this).children('.js-reservation-2').text());
      $('.js-reserveModalLink2').attr('onclick', "gtag('event', 'click', {'event_category': 'CourseWebBooking' , 'event_label': '" + $(this).children('.js-reservation-shop').text() + "'});");
      $('.js-reserveModalLink2').parent().parent().css({
        opacity: '1'
      });
    } else {
      $('.js-reserveModalLink2').attr('href', '');
      $('.js-reserveModalLink2').attr('onclick', 'return false;');
      $('.js-reserveModalLink2').parent().parent().css({
        opacity: '0.3'
      });
    }
  });
  $('.js-reserveModalClose').on('click', function () {
    $('.js-reserveModal').addClass('l-modalWrap--none');
  });
  $('.js-reserveModalBg').on('click', function () {
    $('.js-reserveModal').addClass('l-modalWrap--none');
  });
}; //TopPage scrollEvent


var scrollTopPageEvent = function scrollTopPageEvent() {
  $(window).on('scroll', function () {
    var scrollTop = window.pageYOffset || document.documentElement.scrollTop;

    if (scrollTop > 200) {
      $('.l-headerTop').addClass('l-headerRollDown');
    } else {
      $('.l-headerTop').removeClass('l-headerRollDown');
    }
  });
}; //swiper


var swiperInit = function swiperInit() {
  var swiper = new Swiper('.swiper-container', {
    slidesPerView: 1,
    spaceBetween: 10,
    loop: true,
    pagination: {
      el: '.swiper-pagination'
    }
  });
}; //scrollFitNav;


var scrollFitNavInit = function scrollFitNavInit() {
  var Pos = $('.js-subNav').offset().top;
  $(window).on('resize', function () {
    var Position = $('.js-subNav').css('position');

    if (Position == 'fixed') {
      if ($('.js-subNav').hasClass('js-subNavDouble')) {
        $('.js-subNav').removeClass('c-barNavWrapFixDouble');
        $('.l-container').removeClass('c-barNavWrapFixDoubleContainer');
      } else {
        $('.js-subNav').removeClass('c-barNavWrapFix');
        $('.l-container').removeClass('c-barNavWrapFixContainer');
      }

      Pos = $('.js-subNav').offset().top;

      if ($('.js-subNav').hasClass('js-subNavDouble')) {
        $('.js-subNav').addClass('c-barNavWrapFixDouble');
        $('.l-container').addClass('c-barNavWrapFixDoubleContainer');
      } else {
        $('.js-subNav').addClass('c-barNavWrapFix');
        $('.l-container').addClass('c-barNavWrapFixContainer');
      }
    } else {
      Pos = $('.js-subNav').offset().top;
    }
  });
  $(window).on('scroll', function () {
    var scrollTop = window.pageYOffset || document.documentElement.scrollTop;

    if (scrollTop > Pos) {
      if ($('.js-subNav').hasClass('js-subNavDouble')) {
        $('.js-subNav').addClass('c-barNavWrapFixDouble');
        $('.l-container').addClass('c-barNavWrapFixDoubleContainer');
      } else {
        $('.js-subNav').addClass('c-barNavWrapFix');
        $('.l-container').addClass('c-barNavWrapFixContainer');
      }
    } else {
      if ($('.js-subNav').hasClass('js-subNavDouble')) {
        $('.js-subNav').removeClass('c-barNavWrapFixDouble');
        $('.l-container').removeClass('c-barNavWrapFixDoubleContainer');
      } else {
        $('.js-subNav').removeClass('c-barNavWrapFix');
        $('.l-container').removeClass('c-barNavWrapFixContainer');
      }
    }
  });
}; //Nav


var globalNavInit = function globalNavInit() {
  $('.l-headerNavToggle').on('click', function () {
    $('.l-header').toggleClass('l-headerNavViewed');
    $('.l-headerNav').toggleClass('l-headerNav--open');
    $('.l-headerNavToggle').toggleClass('l-headerNavToggle--close');
  });
}; //pageInScroll


var pageInScroll = function pageInScroll() {
  var urlHash = location.hash;

  if (urlHash) {
    var speed = 0;
    var target = $(urlHash);
    var position = target.offset().top - 100;
    $('html, body').animate({
      scrollTop: position
    }, speed, 'swing');
    return false;
  }

  $('a[href^="#"]').on('click', function (e) {
    e.preventDefault();
    var speed = 400;
    var href = $(this).attr('href');
    var target = $(href == '#' || href == '' ? 'html' : href);
    var position = target.offset().top - 246;
    $('html, body').animate({
      scrollTop: position
    }, speed, 'swing');
    return false;
  });
}; //PageTopScroll


var pageTopScroll = function pageTopScroll() {
  $('.l-footerScrollTop').on('click', function () {
    $('html, body').animate({
      scrollTop: 0
    }, 500);
  });
  $(window).on('scroll', function () {
    var scrollTop = window.pageYOffset || document.documentElement.scrollTop;

    if (scrollTop > 100) {
      if ($('.p-footerInfoBar').length > 0) {
        $('.l-footerScrollTop').addClass('l-footerScrollTopFixDouble');
      } else {
        $('.l-footerScrollTop').addClass('l-footerScrollTopFix');
      }
    } else {
      if ($('.p-footerInfoBar').length > 0) {
        $('.l-footerScrollTop').removeClass('l-footerScrollTopFixDouble');
      } else {
        $('.l-footerScrollTop').removeClass('l-footerScrollTopFix');
      }
    }
  });
};

var heroScrollMotion = function heroScrollMotion() {
  $(window).on('scroll', function () {
    var scrollTop = window.pageYOffset || document.documentElement.scrollTop;
    $('.js-headHero').css({
      transform: 'scale(' + Number(1 + scrollTop * 0.0003) + ')',
      opacity: 1 - scrollTop / $(window).height()
    });
  });
  $(window).on('scroll', function () {
    var scrollTop = window.pageYOffset || document.documentElement.scrollTop;
    $('.p-topHeroBgImageOP').removeClass('p-topHeroBgImageOP');
    $('.p-topHeroBgImage').css({
      transform: 'scale(' + Number(1 + scrollTop * 0.0003) + ')',
      opacity: 1 - scrollTop / $(window).height()
    });
  });
};