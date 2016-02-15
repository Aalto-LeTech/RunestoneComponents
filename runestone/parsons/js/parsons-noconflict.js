// revert the version of underscore and jquery to whatever it was
// before parson's code included header files


// Modified so, that jQuery won't be removed from the scope but the components
// relying on the $pjQ and _p variables still work.


var $pjQ = $    // jQuery.noConflict(true);
var _p = _      // .noConflict();
