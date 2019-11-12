$(document).ready(function() {

    // jQuery for materialize components
    $('.collapsible').collapsible();
    $(".button-collapse").sideNav();
    $('.sidenav').sidenav();
    $(".dropdown-trigger").dropdown();
    $(".parallax").parallax();
    $(".carousel").carousel();
    $(".carousel").carousel({ fullWidth: true });
    $('select').formSelect();

    // Dynamically add ingredients for add_recipe
    $("#add-ingredients").click(function() {
        var lastField = $("#ingredientsform div:last");
        var intId = (lastField && lastField.length && lastField.data("idx") + 1) || 1;
        var fieldWrapper = $("<div class=\"fieldwrapper\" id=\"field" + intId + "\"/>");
        fieldWrapper.data("idx", intId);
        var fName = $("<textarea id=\"ingredients\" name=\"ingredients\" autocomplete=\"off\" minlength=\"5\" maxlength=\"500\" class=\"validate materialize-textarea col s11\" placeholder=\"List your preparation steps\" required></textarea>");
        var removeButton = $("<button class=\"btn remove col s1\" value=\"-\"><i class=\"fa fa-minus\" aria-hidden=\"true\"></i></button>");
        removeButton.click(function() {
            $(this).parent().remove();
        });
        fieldWrapper.append(fName);
        fieldWrapper.append(removeButton);
        $("#ingredientsform").append(fieldWrapper);
    });

    // Dynamically add preparations steps for add_recipe
    $("#add-instructions").click(function() {
        var lastField = $("#instructionsform div:last");
        var intId = (lastField && lastField.length && lastField.data("idx") + 1) || 1;
        var fieldWrapper = $("<div class=\"fieldwrapper\" id=\"field" + intId + "\"/>");
        fieldWrapper.data("idx", intId);
        var fName = $("<textarea id=\"instructions\" name=\"instructions\" autocomplete=\"off\" minlength=\"5\" maxlength=\"500\" class=\"validate materialize-textarea col s11\" placeholder=\"List your preparation steps\" required></textarea>");
        var removeButton = $("<button class=\"btn remove col s1\" value=\"-\"><i class=\"fa fa-minus\" aria-hidden=\"true\"></i></button>");
        removeButton.click(function() {
            $(this).parent().remove();
        });
        fieldWrapper.append(fName);
        fieldWrapper.append(removeButton);
        $("#instructionsform").append(fieldWrapper);
    });
    
});