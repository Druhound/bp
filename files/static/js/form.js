
$(function() {
	$('.requestForm').submit(function(e) {
		e.preventDefault();
		var $form = $(this);
		$form.find(':button[type="submit"]').prop('disabled', true);
		var url = 'http://' + window.location.hostname + window.location.pathname;
		console.log($(this).serialize());
		$.ajax({
			type: 'POST',
			url: '/feedback/ajax1/',
			data: $(this).serialize()
        })
		.done(function(){
			$form.find('.error').hide();
			$form.find('.thx').show();
			$form.find(':button[type="submit"]').prop('disabled', false);
			$form[0].reset();
		})
		.fail(function(){
			$form.find('.error').show();
		})
		.always(function(){
			$form.find(':button[type="submit"]').prop('disabled', false);
		});
	});
});

// WITH ATTACH
$(function() {
	$('.attachForm').submit(function(e) {
		e.preventDefault();
		var $form = $(this),
			url = 'http://' + window.location.hostname + window.location.pathname,
			formData = new FormData( this );
			formData.append('title', document.title);
			formData.append('url', url);
		$form.find(':button[type="submit"]').prop('disabled', true);
		$.ajax({
			type: 'POST',
			url: '/feedback/ajax2/',
			data: formData,
			processData: false,
			contentType: false
        })
		.done(function(){
			$form.find('.error').hide();
			$form.find('.thx').show();
			$form.find(':button[type="submit"]').prop('disabled', false);
			$form[0].reset();
		})
		.fail(function(){
			$form.find('.error').show();
		})
		.always(function(){
			$form.find(':button[type="submit"]').prop('disabled', false);
		});
	});
});