!function(global) {
  'use strict';

  function ResponsiveSlider(elem, params) {
    this.$element = jQuery(elem);
    this.params = params || {};

    this.cssActiveItem = this.params.cssActiveItem || 'JS-ResponsiveSlider-Item-active';
    this.cssDisabledElement = this.params.cssDisabledElement || 'JS-ResponsiveSlider-disabled';
    this.cssEnabledElement = this.params.cssEnabledElement || 'JS-ResponsiveSlider-enabled';
    this.cssReadyElement = this.params.cssReadyElement || 'JS-ResponsiveSlider-ready';

    this.__construct();
  };

  ResponsiveSlider.prototype.__construct = function __construct() {
    this.$window = jQuery(window);
    this.$viewport = this.$element.find('.JS-ResponsiveSlider-Viewport');
    this.$items = this.$viewport.find('.JS-ResponsiveSlider-Item');
    this.$controls = this.$element.find('.JS-ResponsiveSlider-Control');
    this.$controlPrev = this.$controls.filter('[data-responsiveslider-control="prev"]');
    this.$controlNext = this.$controls.filter('[data-responsiveslider-control="next"]');

    this.itemsLength = this.$items.length;
    this.displayedItemsLength = null;

    this._init();
  };

  ResponsiveSlider.prototype._init = function _init() {
    var _this = this;

    this.$controlPrev.on('click.JS-ResponsiveSlider', function() { _this._showPrevItem.apply(_this, []); });
    this.$controlNext.on('click.JS-ResponsiveSlider', function() { _this._showNextItem.apply(_this, []); });
    this.$items.on('click.JS-ResponsiveSlider', function(e, data) { _this._showCurrentItem.apply(_this, [jQuery(this), data]); });
    this.$window.on('resize.JS-ResponsiveSlider', function() { _this._updateState.apply(_this, []); });

    this._start();
  };

  ResponsiveSlider.prototype._start = function _start() {
    this._updateState();

    this._ready();
  };

  ResponsiveSlider.prototype._ready = function _ready() {
    this.$element
      .addClass('JS-ResponsiveSlider-ready')
      .addClass(this.cssReadyElement);
  };

  ResponsiveSlider.prototype._showCurrentItem = function _showCurrentItem($item, data) {
    if (!arguments.length) {
      return false;
    }

    if (!data || data.source !== 'JS-ResponsiveSlider') {
      this._showItem($item, false);
    }
  };

  ResponsiveSlider.prototype._showPrevItem = function _showPrevItem() {
    var $activeItem = this.$items.filter('.JS-ResponsiveSlider-Item-active'),
        activeItemIndex = this.$items.index($activeItem),
        prevItemIndex = activeItemIndex - 1,
        $prevItem = this.$items.eq(prevItemIndex);

    this._showItem($prevItem, true);
  };

  ResponsiveSlider.prototype._showNextItem = function _showNextItem() {
    var $activeItem = this.$items.filter('.JS-ResponsiveSlider-Item-active'),
        activeItemIndex = this.$items.index($activeItem),
        nextItemIndex = activeItemIndex + 1,
        $nextItem = this.$items.eq(nextItemIndex);

    this._showItem($nextItem, true);
  };

  ResponsiveSlider.prototype._showPrev = function _showPrev() {
    var $item = this.$items.eq(this.itemsLength - 1);

    $item.prependTo(this.$viewport);
    this.$items = this.$viewport.find('.JS-ResponsiveSlider-Item');
  };

  ResponsiveSlider.prototype._showNext = function _showNext() {
    var $item = this.$items.eq(0);

    $item.appendTo(this.$viewport);
    this.$items = this.$viewport.find('.JS-ResponsiveSlider-Item');
  };

  ResponsiveSlider.prototype._updateState = function _updateState() {
    var viewportWidth = this.$viewport.innerWidth(),
        itemWidth = this.$items.eq(0).outerWidth();

    this.displayedItemsLength = Math.round(viewportWidth / itemWidth);

    if (this.displayedItemsLength < this.itemsLength) {
      if (!this.$element.hasClass('JS-ResponsiveSlider-enabled')) {
        this._setEnabledState();
      }
    } else {
      if (!this.$element.hasClass('JS-ResponsiveSlider-disabled')) {
        this._setDisabledState();
      }
    }
  };

  ResponsiveSlider.prototype._setEnabledState = function _setEnabledState() {
    this._removeStateClass('disabled');
    this._addStateClass('enabled');

    this._showActiveItem();
  };

  ResponsiveSlider.prototype._setDisabledState = function _setDisabledState() {
    this._removeStateClass('enabled');
    this._addStateClass('disabled');
  };

  ResponsiveSlider.prototype._removeStateClass = function _removeStateClass(state) {
    if (!arguments.length) {
      return false;
    }

    if (state === 'enabled') {
      this.$element
        .removeClass(this.cssEnabledElement)
        .removeClass('JS-ResponsiveSlider-enabled');
    }

    if (state === 'disabled') {
      this.$element
        .removeClass(this.cssDisabledElement)
        .removeClass('JS-ResponsiveSlider-disabled');
    }
  };

  ResponsiveSlider.prototype._addStateClass = function _addStateClass(state) {
    if (!arguments.length) {
      return false;
    }

    if (state == 'enabled') {
      this.$element
        .addClass(this.cssEnabledElement)
        .addClass('JS-ResponsiveSlider-enabled');
    }

    if (state == 'disabled') {
      this.$element
        .addClass(this.cssDisabledElement)
        .addClass('JS-ResponsiveSlider-disabled');
    }
  };

  ResponsiveSlider.prototype._showItem = function _showItem($item, doClick) {
    if (!arguments.length) {
      return false;
    }

    var itemIndex = this.$items.index($item),
        centerIndex = Math.floor(this.displayedItemsLength/2),
        offset = itemIndex - centerIndex;

    if (this.$element.hasClass('JS-ResponsiveSlider-enabled')) {
      if (offset === 0) {
        return false;
      }

      if (offset > 0) {
        this._moveToLeft(offset);
      } else {
        this._moveToRight(Math.abs(offset));
      }
    }

    this._setUnactiveItems();
    this._setActiveItem($item);

    if (doClick) {
      $item.trigger('click', {source: 'JS-ResponsiveSlider'});
    }
  };

  ResponsiveSlider.prototype._moveToLeft = function _moveToLeft(step) {
    if (!arguments.length) {
      return false;
    }

    var i;
    for (i = 0; i < step; i++) {
      this._showNext();
    }
  };

  ResponsiveSlider.prototype._moveToRight = function _moveToRight(step) {
    if (!arguments.length) {
      return false;
    }

    var i;
    for (i = 0; i < step; i++) {
      this._showPrev();
    }
  };

  ResponsiveSlider.prototype._setUnactiveItems = function _setUnactiveItems() {
    this.$items
      .removeClass(this.cssActiveItem)
      .removeClass('JS-ResponsiveSlider-Item-active');
  };

  ResponsiveSlider.prototype._setActiveItem = function _setActiveItem($item) {
    if (!arguments.length) {
      return false;
    }

    $item
      .addClass(this.cssActiveItem)
      .addClass('JS-ResponsiveSlider-Item-active');
  };

  ResponsiveSlider.prototype._showActiveItem = function _showActiveItem() {
    var $item = this.$items.filter('.JS-ResponsiveSlider-Item-active');
    this._showItem($item);
  };


  global.ResponsiveSlider = ResponsiveSlider;
}(this);
