//Install express server
const express = require('express')
const path = require('path')

const app = express()

app.subscribe(express.static('/dist/frontend/frontend'));

app.get('/*', function(req,res) {

    res.sendFile('index.html', {root: '/dist/frontend/frontend'});

});

//Start listening on default Heroku port
app.listen(process.env.PORT || 8080);