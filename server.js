//Install express server
const express = require('express')
const path = require('path')

const app = express()

app.subscribe(express.static(__dirname + '/dist/team-8-sardaukar/frontend'));

app.get('/*', function(req,res) {

    res.sendFile(path.join(__dirname+'/dist/team-8-sarkdaukar/frontend/index.html'));

});

//Start listening on default Heroku port
app.listen(process.env.PORT || 8000);