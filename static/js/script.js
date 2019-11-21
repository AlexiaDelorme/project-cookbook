$(document).ready(function() {

    // jQuery for materialize components
    $('.collapsible').collapsible();
    $(".button-collapse").sideNav();
    $(".parallax").parallax();
    $(".carousel").carousel();
    $('select').material_select();

    // Dynamically add new ingredients for add_recipe and edit_recipe
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

    // Dynamically add preparations steps for add_recipe and edit_recipe
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
    
    // Use Sweet Alert to create 2-tier confirmation before deleting the recipe
    $("#{{recipe._id}}-button-delete").click(function() {
        swal({
              title: "Are you sure?",
              text: "Once deleted, you will not be able to recover this recipe",
              icon: "warning",
              buttons:  {
                        cancel: "Cancel!",
                        catch: {
                        text: "Delete!",
                        value: "delete"
                                },
                        },
        })
        .then((value) => { switch (value) {
                case "delete":
                        swal("Your recipe was deleted!", 
                            { icon: "success"
                            })
                        .then((value) => { document.getElementById("{{recipe._id}}-form").submit(); });
                        break;
                 default:
                        swal("Your recipe is safe!");
            }
        });
    });
    
});