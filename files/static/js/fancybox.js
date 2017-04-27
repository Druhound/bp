/*--GLOBAL--*/
  var GLOBAL = GLOBAL || {};

  GLOBAL.stopEvent = function( event, mode ){
    if( arguments.length == 0 || !event || !jQuery ){
      return;
    }else{
      if( (arguments.length == 1 || (''+mode).toLowerCase().search(/(^|\|)propagation($|\|)/) != -1 ) && jQuery.isFunction(event.stopPropagation) ){
        event.stopPropagation();
      }
      if( (arguments.length == 1 || (''+mode).toLowerCase().search(/(^|\|)default($|\|)/) != -1) && jQuery.isFunction(event.preventDefault) ){
        event.preventDefault();
      }
      if( (arguments.length == 2 && (''+mode).toLowerCase().search(/(^|\|)immediate($|\|)/) != -1) && jQuery.isFunction(event.stopImmediatePropagation) ){
        event.stopImmediatePropagation();
      }
    }
  };

  GLOBAL.parseData = function parseData(data) {
    try {
      data = JSON.parse(data.replace(/'/gim, '"'));
    } catch(e) {
      data = {};
    }

    return data;
  };
/*--/global--*/


/*--FANCYBOX--*/
  GLOBAL.fancybox = GLOBAL.fancybox || {};
    GLOBAL.fancybox.common = GLOBAL.fancybox.common || {};
      GLOBAL.fancybox.common.title = false;
      GLOBAL.fancybox.common.fitToView = false;
      GLOBAL.fancybox.common.tpl = GLOBAL.fancybox.common.tpl || {};
        GLOBAL.fancybox.common.tpl.closeBtn = '<a class="fancybox-close" href="javascript:;" title="Закрыть"></a>';

  GLOBAL.fancybox.popup = GLOBAL.fancybox.popup || {};
    GLOBAL.fancybox.popup.wrapCSS = 'fancy-popup';
    GLOBAL.fancybox.popup.padding = 0;
    GLOBAL.fancybox.popup.openSpeed = 100;
    GLOBAL.fancybox.popup.closeSpeed = 100;

  GLOBAL.fancybox.image = GLOBAL.fancybox.image || {};
    GLOBAL.fancybox.image.wrapCSS = 'fancy-image-popup';

  function initPopup() {
    if(!jQuery.fancybox) {
      return;
    }

    jQuery('.js-popup').fancybox(jQuery.extend({}, GLOBAL.fancybox.common, GLOBAL.fancybox.popup, {
    }));

    jQuery('.js-popup-image').fancybox(jQuery.extend({}, GLOBAL.fancybox.common, GLOBAL.fancybox.popup, GLOBAL.fancybox.image, {
    }));
  }

  function openPopup(popup, mode, params){
    jQuery.fancybox(jQuery(popup), jQuery.extend({}, GLOBAL.fancybox.common, GLOBAL.fancybox[mode] || GLOBAL.fancybox.popup, params || {}));
  }
/*--/fancybox--*/