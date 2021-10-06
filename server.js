//Install express server
const express = require('express')
const path = require('path')

const app = express()

app.use(express.static('./dist'));

app.get('/*', function(req,res) {

    res.sendFile('index.html', {root: 'dist/'});

});

//Start listening on default Heroku port
app.listen(process.env.PORT || 8080);