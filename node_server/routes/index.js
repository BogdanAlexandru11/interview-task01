var express = require('express');
var router = express.Router();
router.get('/', function (req, res, next) {
  //the landing page of the user
    res.render('index', {
  });
});

module.exports = router;