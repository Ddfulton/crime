#!/usr/bin/env nodejs
var express = require('express');
var path = require('path');
var app = express();
let pug = require('pug');

// Define the port to run on
app.set('port', 8080);

// Define static directories
app.use(express.static(path.join(__dirname, 'public')));

// Serve the pdf
app.use('/pdf', express.static(__dirname + '/public/rush.pdf'));

app.get('/mosaics', function (req, res) {
  res.sendFile(__dirname + '/public/mosaics.html');
})

app.get('/', function (req, res) {
  res.sendFile(__dirname + '/public/rush.pdf');
})

// Listen for requests on '/'
var server = app.listen(app.get('port'), function() {
  var port = server.address().port;
  console.log('Magic happens on port ' + port);
});