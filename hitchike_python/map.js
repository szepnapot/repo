
//var btn = document.getElementById('show-map');
//btn.addEventListener("click", changeMap);


function changeMap(){

	//place IDs to put into url
	var start = document.getElementById('startLocation').value;

	var dest = document.getElementById('destination').value;


	//pieces of the url
	var mapSource1 = "https://www.google.com/maps/embed/v1/directions?origin=place_id:";

	var mapSource2 = "&destination=place_id:";

	var mapSource3 = "&key=AIzaSyDMtNzjQdNk-FX1hz7IWVcNiby1B8xiZeg";

	var mapSource = mapSource1+start+mapSource2+dest+mapSource3;

	//iframe
	var iframe = document.getElementById('map');

	//changing the src of the iframe
	iframe.src = mapSource;


}
