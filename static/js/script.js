$(document).ready(function() {

    // jQuery for materialize components
    $(".collapsible").collapsible();
    $(".button-collapse").sideNav();
    $(".parallax").parallax();
    $(".carousel").carousel();
    $("select").material_select();
    $(".modal").modal();

    // Add center-align class for pagination after DOM is loaded
    $(".pagination-page-info").addClass("center-align");
    $(".pagination").addClass("center-align");

    // Dynamically add new ingredients for add_recipe and edit_recipe
    $("#add-ingredients").click(function() {
        var lastField = $("#ingredientsform div:last");
        var intId = (lastField && lastField.length && lastField.data("idx") + 1) || 1;
        var fieldWrapper = $("<div class=\"fieldwrapper\" id=\"field" + intId + "\"/>");
        fieldWrapper.data("idx", intId);
        var fName = $("<textarea id=\"ingredients\" name=\"ingredients\" autocomplete=\"off\" minlength=\"1\" maxlength=\"100\"  data-length=\"100\" class=\"validate materialize-textarea col s11\" placeholder=\"Example: Milk, Eggs, Chocolate, Flour\"></textarea>");
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
        var fName = $("<textarea id=\"instructions\" name=\"instructions\" autocomplete=\"off\" minlength=\"1\" maxlength=\"500\" data-length=\"500\" class=\"validate materialize-textarea col s11\" placeholder=\"Example: In a large bowl, mix all the wet ingregients\"></textarea>");
        var removeButton = $("<button class=\"btn remove col s1\" value=\"-\"><i class=\"fa fa-minus\" aria-hidden=\"true\"></i></button>");
        removeButton.click(function() {
            $(this).parent().remove();
        });
        fieldWrapper.append(fName);
        fieldWrapper.append(removeButton);
        $("#instructionsform").append(fieldWrapper);
    });

    // Remove existing ingredients/instructions when user edits a recipe
    $(".remove-btn").click(function() {
            $(this).parent().remove();
    });
    
});

// Print function to print recipes
function myPrintFunction() {
  window.print();
}

// Use Sweet Alert to create 2-tier confirmation before deleting the recipe
function deleteRecipeFunction(recipeId) {
    swal({
            title: "Are you sure?",
            text: "Once deleted, you will not be able to recover this recipe",
            icon: "warning",
            buttons: {
                cancel: "Cancel",
                catch: {
                    text: "Delete",
                    value: "delete"
                },
            },
        })
        .then((value) => {
            switch (value) {
                case "delete":
                    swal("Request to delete recipe sent!", {
                            icon: "success"
                        })
                        .then((value) => { document.getElementById(recipeId + "Form").submit(); });
                    break;
                default:
                    swal("Your recipe is safe!");
            }
        });
}

function deleteAccountFunction() {
    swal({
            title: "Are you sure?",
            text: "Your account will be permanently deleted.",
            icon: "warning",
            buttons: {
                cancel: "Cancel",
                catch: {
                    text: "Delete",
                    value: "delete"
                },
            },
        })
        .then((value) => {
            switch (value) {
                case "delete":
                    swal("Request to delete your account sent!", {
                            icon: "success"
                        })
                        .then((value) => { document.getElementById("deleteAccountForm").submit(); });
                    break;
                default:
                    swal("Your account is still live!");
            }
        });
}