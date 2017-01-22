window.onload = function(){
 function startRecording() {
		$.ajax({
			url: "http://localhost:5000/upload",
			type: "GET",
			data: form,
			
		})
  }

	function upload()
	{
			$.ajax({
				url: "http://localhost:5000/book",
				type: "POST"
	}

}
