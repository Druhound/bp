!function(global) {
  'use strict';

  function Dropdown(elem, params) {
    this.$element = jQuery(elem);
    this.params = params || {};

    this.dataName = this.params.dataName || 'value';
    this.classActive = this.params.classActive || 'JS-Dropdown-active';
    this.classHidden = this.params.classHidden || '';
    this.classReady = this.params.classReady || 'JS-Dropdown-ready';

    this.__construct();
  };

  Dropdown.prototype.__construct = function __construct() {
    this.$window = jQuery(window);
    this.$switcher = this.$element.find('.JS-Dropdown-Switcher');
    this.$list = this.$element.find('.JS-Dropdown-List');
    this.$item = this.$list.find('.JS-Dropdown-Item');
    this.$label = this.$item.find('.JS-Dropdown-Label');
    this.$overlay = this.$element.find('.JS-Dropdown-Overlay');

    this._init();
  };

  Dropdown.prototype._init = function _init() {
    var _this = this;

    this.$element.trigger('jsdropdowninit', this);

    this.$window.on('jsdropdownset.JS-Dropdown', function(e, data) {
      _this._update.apply(_this, [data]);
    });

    this.$switcher
      .add(this.$overlay)
        .on('click.JS-Dropdown', function() {
          _this.toggle.apply(_this, []);
        });

    this.$label.on('click.JS-Dropdown', function() {
      _this._select.apply(_this, [this]);
    });

    this._ready();
  };

  Dropdown.prototype._ready = function _ready() {
    this.$element
      .addClass('JS-Dropdown-ready')
      .addClass(this.classReady)
      .trigger('jsdropdownready', this);
  };

  Dropdown.prototype.open = function open() {
    this.$element
      .addClass('JS-Dropdown-active')
      .addClass(this.classActive);
  };

  Dropdown.prototype.close = function close() {
    this.$element
      .removeClass('JS-Dropdown-active')
      .removeClass(this.classActive);
  }

  Dropdown.prototype.toggle = function toggle() {
    if (this.$element.hasClass('JS-Dropdown-active')){
      this.close();
    } else {
      this.open();
    }
  };

  Dropdown.prototype._update = function _update(value) {
    if (!arguments.length) {
      return;
    }

    var $label = this.$label.filter('[data-'+this.dataName+'="'+value+'"]');

    this.$switcher.html($label.html());

    this.$item
      .removeClass('JS-Dropdown-hidden')
      .removeClass(this.classHidden)
      .has($label)
        .addClass('JS-Dropdown-hidden')
        .addClass(this.classHidden);
  };

  Dropdown.prototype.update = function update(value) {
    this._update(value);
    this.$element.trigger('jsdropdownupdate', value);
  };

  Dropdown.prototype._select = function _select(elem) {
    this.update(jQuery(elem).data(this.dataName));
    this.close();
  };
  /*--/Dropdown--*/

  global.Dropdown = Dropdown;
}(this);
