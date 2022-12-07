"use strict";
(function() {
        'use strict';
        window.addEventListener('load', function() {
            var forms = document.getElementsByClassName('needs-validation');
            var validation = Array.prototype.filter.call(forms, function(form) {
                form.addEventListener('submit', function(event) {
                    if (form.checkValidity() === false) {
                        event.preventDefault();
                        event.stopPropagation();
                        $('.front-error').text("Something is Missing please check all pages.");
                        // console.log("lkdsfj")
                        
                      
                    }
                    form.classList.add('was-validated');
                    
                  
                }, false);
            });
        }, false);
})();




$(document).ready(function() {
    $("select").on("select2:close", function (e) {  
        $(this).valid(); 
    });

    $("select").on("change", function (e) { 
        if (this.validity.valid) {
            $(this).closest(".form-group").removeClass("has-error")
            $(this).closest(".form-group").addClass("valid-select")
        } else{
            $(this).closest(".form-group").addClass("has-error")
            $(this).closest(".form-group").removeClass("valid-select")
        }
    });



    $("#participation_form").validate({
        ignore: '*:not([name])',

        debug: false,
        
        onfocusout: function(element) {$(element).valid()},
        onchange:function(element) {$(element).valid()},
        onkeyup:function(element) {$(element).valid()},

        onsubmit: true,
        submitHandler: function(form) {  
        if ($(form).valid())
        {
            form.submit(); 
        }
        return false; // prevent normal form posting
        }
        

     

    }
    );

    });













$('#participation_form').on('submit', function(e) {

    var $select2 = $('.js-select2', $(this));




})