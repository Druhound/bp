/*--GLOBAL--*/
  var GLOBAL = {};

  GLOBAL.parseData = function parseData(data) {
    try {
      data = JSON.parse(data.replace(/'/gim, '"'));
    } catch(e) {
      data = {};
    }

    return data;
  };
/*--/global--*/

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
/*--/init--*/


/*--RAW--*/
  function onDropdownUpdate(e, value) {
    jQuery(window).trigger('jsregionset', value);
  }

  function onRegionUpdate(e, value) {
    jQuery(window).trigger('jsdropdownset', value);
  }
/*--/raw--*/

jQuery(function(){
  initDropdown();
  initRegion();
});
