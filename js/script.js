function httpGet(){
    console.log("de")

    var theUrl = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=-33.8670522,151.1957362&radius=5&type=restaurant&keyword=Mexican&key=AIzaSyDGnMTSopj_ZzyiNWEEM_pdb6tBCHYxEc8"
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.withCredentials = false;
    xmlHttp.open( "GET", theUrl, false ); // false for synchronous request
    xmlHttp.send( null );

    console.log(xmlHttp.responseText)
    return xmlHttp.responseText;
}

httpGet()
