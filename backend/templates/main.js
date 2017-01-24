	function upload()
	{	
		 var formData = new FormData($(this)[0]);
			$.ajax({
				//url: "http://localhost:5000/book",
				url: "https://requestb.in/1n05iyw1"
        type: "POST",
        data: formData,
        dataType: 'txt',
        contentType: false,
    		processData: false,	
				success: function(response){
        	console.log('success')
          console.log(response)
         }
}); 

}

$('.send').click(function() { 
		 var formData = new FormData($(this)[0]);

        $.ajax({
				    url: "http://localhost:5000/book",
            type: 'POST',
            data: {'submit':true}, // An object with the key 'submit' and value 'true;
            success: function (result) {
              alert("Your bookmark has been saved");
            }
        });  

});
