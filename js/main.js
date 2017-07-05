console.log("Reading JSON");

var test = "Want to listen to a song? How about <strong><i>{0} by {1}</i> </strong>(<a href='{2}' target='_blank'>Spotify, </a><a href='{3}' target='_blank'>{4}</a>)"
$.getJSON("website.json", function(json) {
    console.log(json); // this will show the info it in firebug console
    var tracks = json.playlists.website.tracks;
    console.log(tracks); 
    var song = tracks[Math.floor(Math.random()*tracks.length)];
    link = "https://open.spotify.com/track/"+  song.uri.split(":")[2];
    if(song.video){
        $(".song").html(test.f(song.name,song.artists[0],link,song.video,"Youtube"))
    }
    else{
        $(".song").html(test.f(song.name,song.artists[0],link,song.music,"mp3"))
    }

    

});





String.prototype.format = String.prototype.f = function() {
    var s = this,
        i = arguments.length;

    while (i--) {
        s = s.replace(new RegExp('\\{' + i + '\\}', 'gm'), arguments[i]);
    }
    return s;
};
