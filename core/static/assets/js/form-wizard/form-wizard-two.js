(function ($) {
  "use strict";
  var fomr_wizard_two = {
    init: function () {
      var navListItems = $("div.setup-panel div a"),
        allWells = $(".setup-content"),
        allNextBtn = $(".nextBtn");
      allWells.hide();
      navListItems.click(function (e) {
        e.preventDefault();
        var $target = $($(this).attr("href")),
          $item = $(this);
        if (!$item.hasClass("disabled")) {
          navListItems.removeClass("btn btn-light").addClass("btn btn-primary");
          $item.addClass("btn btn-light");
          allWells.hide();
          $target.show();
          $target.find("input:eq(0)").focus();
        }
      }),
        allNextBtn.click(function () {
          var curStep = $(this).closest(".setup-content"),
            curStepBtn = curStep.attr("id"),
            nextStepWizard = $(
              'div.setup-panel div a[href="#' + curStepBtn + '"]'
            )
              .parent()
              .next()
              .children("a"),
            curInputs = curStep.find(
              "input[type='text'],input[type='url'],input[required=required], select"
            ),
            isValid = true;
            // console.log(curInputs);
          $(".form-group").removeClass("has-error");
          for (var i = 0; i < curInputs.length; i++) {
            if (!curInputs[i].validity.valid) {
              isValid = false;
              $(curInputs[i]).closest(".form-group").addClass("has-error");

              if (curInputs[i].tagName=='SELECT') {
                console.log(curInputs[i])
                if ($(curInputs[i]).val() ==='') {
                  
                  $(curInputs[i]).parents('.form-group').addClass('is-invalid');
                }
              }

              $("form.needs-validation").find(":submit").click();
            }
          }
          if (isValid) nextStepWizard.removeAttr("disabled").trigger("click");
        }),
        $("div.setup-panel div a.btn-primary").trigger("click");
    },
  };
  (function ($) {
    "use strict";
    fomr_wizard_two.init();
  })(jQuery);
})(jQuery);
