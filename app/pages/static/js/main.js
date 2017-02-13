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


/*--INIT--*/
  function initDropdown(context) {
    if (typeof(Dropdown) === 'undefined' || !jQuery.isFunction(Dropdown)) {
      return false;
    }

    var common = {};

    jQuery('.JS-Dropdown', context || document).not('.JS-Dropdown-ready').each(function() {
      var $elem = jQuery(this),
          local = GLOBAL.parseData($elem.data('dropdown')),
          handlers = GLOBAL.parseData($elem.data('dropdown-handlers')),
          e,
          i,
          l;

      for (e in handlers) {
        if (!jQuery.isArray(handlers[e])) {
          handlers[e] = [handlers[e]];
        }

        for (i = 0, l = handlers[e].length; i < l; i++) {
          $elem.on(e, window[handlers[e][i]]);
        }
      }

      new Dropdown(this, jQuery.extend({}, common, local));
    });
  }

  function initRegion(context) {
    if (typeof(Region) === 'undefined' || !jQuery.isFunction(Region)) {
      return false;
    }

    var common = {};

    jQuery('.JS-Region', context || document).not('.JS-Region-ready').each(function() {
      var $elem = jQuery(this),
          local = GLOBAL.parseData($elem.data('region')),
          handlers = GLOBAL.parseData($elem.data('region-handlers')),
          e,
          i,
          l;

      for (e in handlers) {
        if (!jQuery.isArray(handlers[e])) {
          handlers[e] = [handlers[e]];
        }

        for (i = 0, l = handlers[e].length; i < l; i++) {
          $elem.on(e, window[handlers[e][i]]);
        }
      }

      new Region(this, jQuery.extend({}, common, local));
    });
  }

  function initFix(context) {
    if (typeof(Fix) === 'undefined' || !jQuery.isFunction(Fix)) {
      return false;
    }

    var common = {};

    jQuery('.JS-Fix', context || document).not('.JS-Fix-ready').each(function() {
      var local = GLOBAL.parseData(jQuery(this).data('fix'));
      new Fix(this, jQuery.extend({}, common, local));
    });
  }

  function initRotator(context) {
    if (typeof Rotator === 'undefined' || !jQuery.isFunction(Rotator)) {
      return false;
    }

    var common = {};

    jQuery('.JS-Rotator', context || document).not('.JS-Rotator-ready').each(function() {
      var local = GLOBAL.parseData(jQuery(this).data('rotator-params'));
      new Rotator(this, jQuery.extend({}, common, local));
    });
  }

  function initToUp(context){
    if(typeof ToUp === 'undefined' || !jQuery.isFunction(ToUp)){
      return false;
    }

    var common = {};

    jQuery('.JS-ToUp', context || document).not('.JS-ToUp-ready').each(function(){
      var local = GLOBAL.parseData(jQuery(this).data('toup'));
      new ToUp(this, jQuery.extend({}, common, local));
    });
  }

  function initNavigate(context) {
    if (typeof Navigate === 'undefined' || !jQuery.isFunction(Navigate)) {
      return false;
    }

    jQuery('.JS-Navigate', context || document).not('.JS-Navigate-ready').each(function() {
      new Navigate(this, GLOBAL.parseData(jQuery(this).data('navigate-params')));
    });
  }

  function initCut(context) {
    if (typeof Cut === 'undefined' || !jQuery.isFunction(Cut)) {
      return false;
    }

    var common = {
      duration: 250,
      classSwitcher: 'cut-title',
      classBar: 'cut-text',
      classControls: 'cut-controls',
      classControlOpen: 'cut-controls__switcher cut-controls__switcher_open',
      classControlClose: 'cut-controls__switcher cut-controls__switcher_close',
      classActive: 'cut_active'
    };

    jQuery('.cut', context || document).not('.JS-Cut-ready').each(function() {
      var local = GLOBAL.parseData(jQuery(this).data('cut-params'));
      new Cut(this, jQuery.extend({}, common, local));
    });
  }

  function initFocus() {
    jQuery('.JS-Focus').each(function(){
      var $field = jQuery(this),
          $fieldValue = $field.find('.JS-Focus-Field'),
          classFocus = $field.data('focus') || 'JS-Focus-active';

      $fieldValue
        .on('focus', function(){
          $field.addClass(classFocus);
        })
        .on('blur', function(){
          $field.removeClass(classFocus);
        });
    });
  }

  function initGrid(context) {
    if (typeof Grid === 'undefined' || !jQuery.isFunction(Grid)) {
      return false;
    }

    var common = {};

    jQuery('.JS-Grid', context || document).not('.JS-Grid-ready').each(function() {
      var local = GLOBAL.parseData(jQuery(this).data('grid'));
      new Grid(this, jQuery.extend({}, common, local));
    });
  }

  function initAjaxForm(context) {
    if (typeof AjaxForm === 'undefined' || !jQuery.isFunction(AjaxForm)) {
      return false;
    }

    jQuery('.JS-AjaxForm', context || document).not('.JS-AjaxForm-ready').each(function() {
      new AjaxForm(this, GLOBAL.parseData(jQuery(this).data('ajaxform-params')));
    });
  }

  function initResponsiveSlider(context) {
    if (typeof ResponsiveSlider === 'undefined' || !jQuery.isFunction(ResponsiveSlider)) {
      return false;
    }

    var common = {};

    jQuery('.JS-ResponsiveSlider', context || document).not('.JS-ResponsiveSlider-ready').each(function() {
      var local = GLOBAL.parseData(jQuery(this).data('responsiveslider-params'));
      new ResponsiveSlider(this, jQuery.extend({}, common, local));
    });
  }

  function initSearchToggler(context) {
    if (typeof SearchToggler === 'undefined' || !jQuery.isFunction(SearchToggler)) {
      return false;
    }

    var common = {};

    jQuery('.JS-SearchToggler', context || document).not('.JS-SearchToggler-ready').each(function() {
      var local = GLOBAL.parseData(jQuery(this).data('searchtoggler'));
      new SearchToggler(this, jQuery.extend({}, common, local));
    });
  }
/*--/init--*/


/*--RAW--*/
  function onDropdownUpdate(e, value) {
    jQuery(window).trigger('jsregionset', value);
  }

  function onRegionUpdate(e, value) {
    jQuery(window).trigger('jsdropdownset', value);
    jQuery('.JS-Navigate-MenuSwitcher[data-value="'+value+'"]').trigger('click');
  }
/*--/raw--*/

function addLink() {
    //Get the selected text and append the extra info
    var selection = window.getSelection(),
        pagelink = '<br /><br />У меня есть совесть, но я все равно скопировал этот текст со страницы ' + document.location.href + ', которая была написана профессиональным журналистом, для того, чтобы куда-то вставить. Конечно же, я не забуду вставить ссылку на первоисточник http://www.centrattek.ru/ . Я благодарю за предоставленную информацию администратора, редактора сайта и весь IT-отдел attek group!',
        copytext = selection + pagelink,
        newdiv = document.createElement('div');

    //hide the newly created container
    newdiv.style.position = 'absolute';
    newdiv.style.left = '-99999px';

    //insert the container, fill it with the extended text, and define the new selection
    document.body.appendChild(newdiv);
    newdiv.innerHTML = copytext;
    selection.selectAllChildren(newdiv);

    window.setTimeout(function () {
        document.body.removeChild(newdiv);
    }, 100);
}

jQuery(function(){
  initResponsiveSlider();
  initDropdown();
  initNavigate();
  initRegion();
  initFix();
  initRotator();
  initPopup();
  initToUp();
  initCut();
  initFocus();
  initGrid();
  initAjaxForm();
  initSearchToggler();
});
