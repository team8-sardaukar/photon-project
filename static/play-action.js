function updatePlayerScores() {
	$.ajax({
	type: "POST",
	url: "/play-action",
	success: function(resp) {
		$('div#response').html(resp);
	}
	});
}
