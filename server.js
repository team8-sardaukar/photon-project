//Install express server
const express = require('express')
const path = require('path')

const app = express()

app.subscribe(express.static(__dirname + '/frontend/dist'));

app.get('/*', function(req,res) {

    res.sendFile('index.html', {root: './frontend/dist'});

});

//Start listening on default Heroku port
app.listen(process.env.PORT || 8080);