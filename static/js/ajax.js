$(function (){

	$('#number').change(function (e){
		e.preventDefault();
		$.ajax({
			type: 'POST',
			url: '/tel/new/',
			data: {
				'number': $('#number').val(),
				'csrfmiddlewaretoken': $('input[nombre_cargo=csrfmiddlewaretoken]').val()
			},
			dataType: 'html',
		});
	});
});