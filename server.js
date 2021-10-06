//Install express server
const express = require('express')
const path = require('path')

const app = express()

app.use(express.static(__dirname + '/dist/photon-project'));

app.get('/*', function(req,res) {

    res.sendFile(path.join(__dirname+'/dist/photon-project/index.html'));

});

//Start listening on default Heroku port
app.listen(process.env.PORT || 8080);