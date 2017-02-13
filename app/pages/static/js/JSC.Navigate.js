!function(namespace) {
  'use strict';

  function Navigate(elem, params) {
    this.$element = jQuery(elem);
    this.params = params || {};

    this.classContentActive = this.params.classContentActive || 'JS-Navigate-active';
    this.classSwitcherActive = this.params.classSwitcherActive || 'JS-Navigate-active';
    this.classReady = this.params.classReady || 'JS-Navigate-ready';
    this.menu = this.params.menu || '.JS-Navigate-Menu';
    this.menuSwitcher = this.params.menuSwitcher || '.JS-Navigate-MenuSwitcher';
    this.content = this.params.content || '.JS-Navigate-Content';
    this.contentItems = this.params.contentItems || '.JS-Navigate-ContentItem';

	if( this.menu.charAt(0) != '.' ) {
		this.menu = '.' + this.menu;
	}
	if( this.menuSwitcher.charAt(0) != '.' ) {
		this.menuSwitcher = '.' + this.menuSwitcher;
	}
	if( this.content.charAt(0) != '.' ) {
		this.content = '.' + this.content;
	}
	if( this.contentItems.charAt(0) != '.' ) {
		this.contentItems = '.' + this.contentItems;
	}
    this.__construct();
  }

    Navigate.prototype.__construct = function __construct() {
      this.$document = jQuery(document);

      this.$menu = this.$element.find(this.menu);
      this.$menuSwitchers = this.$menu.find(this.menuSwitcher);
      this.$content = this.$element.find(this.content);
      this.$contentItems = this.$content.find(this.contentItems);

      this._init();
    };

    Navigate.prototype._init = function _init() {
      var _this = this;

      this.$element.trigger('jsnavigateinit', this);

      this.$menuSwitchers.on('click.JS-Navigate', function(e) {
        GLOBAL.stopEvent(e);
        _this.navigate.apply(_this, [this]);
      });

      this._setActiveContent();

      this._ready();
    };

    Navigate.prototype._ready = function _ready() {
      this.$element
        //.addClass('JS-Navigate-ready')
        .addClass(this.classReady)
        .trigger('jsnavigateready', this);
    };

    Navigate.prototype._setActiveContent = function _setActiveContent() {
      var target = this.$menuSwitchers
        .filter(this.classSwitcherActive)
          .data('source-id');

      if (target) {
        this.$contentItems
          //.removeClass('JS-Navigate-active')
          .removeClass(this.classContentActive)
          .filter('[data-content-id="'+target+'"]')
           // .addClass('JS-Navigate-active')
            .addClass(this.classContentActive);
      }
    };

    Navigate.prototype.navigate = function navigate(elem) {
      var $elem = jQuery(elem),
          target = $elem.data('source-id'),
          $activeContent;

      if ($elem.hasClass(this.classSwitcherActive)) {
        return;
      }

      $activeContent = this.$contentItems.filter('[data-content-id="'+target+'"]');

      if (!$activeContent.length) {
        return;
      }

      this.$menuSwitchers
        //.removeClass('JS-Navigate-active')
        .removeClass(this.classSwitcherActive);

      $elem
        //.addClass('JS-Navigate-active')
        .addClass(this.classSwitcherActive);

      this.$contentItems
        //.removeClass('JS-Navigate-active')
        .removeClass(this.classContentActive);

      $activeContent
        //.addClass('JS-Navigate-active')
        .addClass(this.classContentActive);
    };

    Navigate.prototype.show = function show() {
      this.$menu.show();
    };

    Navigate.prototype.hide = function hide() {
      this.$menu.hide();
    };

  namespace.Navigate = Navigate;
}(this);
