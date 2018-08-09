//for time
			$(document).ready(function(){
				$('#form_date input').on('change',function(){
					console.log($('input[name=date]:checked', '#form_date').val());
					$.ajax({
						url: "{% url 'booktime' %}",
						type: 'post',
						data: {},
						success: function(data){
							alert(data);	
						},
						failure: function(){
							alert("Contact admin server error");
						}
					});
					});
				});