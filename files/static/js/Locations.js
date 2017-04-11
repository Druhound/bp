!function(global) {
  'use strict';

  function Region(elem, params) {
    this.$element = jQuery(elem);
    this.params = params || {};

    this.dataName = this.params.dataName || 'city';
    this.cookieName = this.params.cookieName || 'city_id';
    this.cookieExpires = this.params.cookieExpires || 60*60*24*365;
    this.classHidden = this.params.classHidden || '';
    this.classReady = this.params.classReady || 'JS-Region-ready';

    this.__construct();
  };

    Region.prototype.__construct = function __construct() {
      this.$window = jQuery(window);
      this.$switcher = this.$element.find('.JS-Region-Switcher');
      this.$data = this.$element.find('.JS-Region-Data');

      this._init();
    };

    Region.prototype._init = function _init() {
      var _this = this;

      this.$element.trigger('jsregioninit', this);

      this.$window.on('jsregionset.JS-Region', function(e, data) {
          _this.update.call(_this, data);
      });

      this.update(jQuery.cookie(this.cookieName));

      this._ready();
    };

    Region.prototype._ready = function _ready() {
      this.$element
        .addClass('JS-Region-ready')
        .addClass(this.classReady)
        .trigger('jsregionready', this);
    };

    Region.prototype.update = function update(value) {
      if (!arguments.length) {
        return;
      }

      var $active = this.$data.filter('[data-'+this.dataName+'="'+value+'"]');

      this.$data
        .addClass('JS-Region-hidden')
        .addClass(this.classHidden);

      $active
        .removeClass('JS-Region-hidden')
        .removeClass(this.classHidden);

      if (this.dataName == 'code' && value > 3){
        this.$data
          .addClass('JS-Region-hidden')
          .addClass(this.classHidden);
        this.$data.filter('[data-'+this.dataName+'="1"]')
            .removeClass('JS-Region-hidden')
            .removeClass(this.classHidden);
      }

      jQuery.cookie(this.cookieName, value, {path : '/'}, this.cookieExpires);

      this.$element.trigger('jsregionupdate', value);
    };
  /*--/Region--*/

  global.Region = Region;
}(this);
