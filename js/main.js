console.log("Reading JSON");

var test = "Want to listen to a song? How about <a href='{0}'>{1} by {2}</a>"
$.getJSON("website.json", function(json) {
    console.log(json); // this will show the info it in firebug console
    var tracks = json.playlists.website.tracks;
    console.log(tracks); 
    var song = tracks[Math.floor(Math.random()*tracks.length)];
    link = "https://open.spotify.com/track/"+  song.uri.split(":")[2];

    $(".song").html(test.f(link,song.name,song.artists[0]))

});





String.prototype.format = String.prototype.f = function() {
    var s = this,
        i = arguments.length;

    while (i--) {
        s = s.replace(new RegExp('\\{' + i + '\\}', 'gm'), arguments[i]);
    }
    return s;
};
