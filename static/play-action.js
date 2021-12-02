function updatePlayerScores() {
	$.ajax({
		type: "POST",
		url: "/play-action",
		success: function(resp) {
			$('div#response').html(resp);
		}
	});
	var objDiv = document.getElementById("hits-list");
     objDiv.scrollTop = objDiv.scrollHeight;
}

function stopUDPListener() {
	$.ajax({
		type: "PUT",
		url: "/play-action",
		success: function(resp) {
			$('div#response').html(resp);
		}
	});
}
