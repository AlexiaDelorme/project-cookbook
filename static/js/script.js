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

    // Display difficulty selected by user
    $("select#difficulty").change(function(){
        var selectedOption = $(this).children("option:selected").val();
        console.log(selectedOption);
        if (selectedOption == "") {
            $(this).parent(".select-wrapper").children("input").css({"border-bottom": "1px solid #f44336", "box-shadow": "0 1px 0 0 #f44336"});
        } else {
            $(this).parent(".select-wrapper").children("input").css({"border-bottom": "1px solid #4CAF50", "box-shadow": "0 1px 0 0 #4CAF50"});
        };
    });

    // Display difficulty selected by user
    $("#hours").change(function(){
        var inputtedHour = $(this).val();
        console.log(inputtedHour);
        if (inputtedHour == "" || inputtedHour == 0) {
            console.log("Minutes should remain required"); 
            $("#minutes").prop("required", true);
        } else {
            console.log("Minutes should not necessarily be required"); 
            $("#minutes").prop("required", false);
        };
    });

    // Check if last ingredient field is empty before adding a new one
    $("#add-ingredients").click(function() {
        var lastIngredientField = $("#ingredientsform").children("div:last-child").children("textarea").val();
        console.log(lastIngredientField); 
        if (lastIngredientField == "") {
            console.log("Last ingredient field is empty");
            $("#ingredientsform").children("#field0").children("label").prop("data-error", "*Fill in this field before adding a new ingredient");
        } else {
            console.log("You can invoke the addIngredientFunction");
            addIngredientFunction();
        };
    });

    // Function to add new ingredients for recipes forms
    function addIngredientFunction() {
        var lastField = $("#ingredientsform div:last");
        var intId = (lastField && lastField.length && lastField.data("idx") + 1) || 1;
        var fieldWrapper = $("<div class=\"fieldwrapper\" id=\"field" + intId + "\"/>");
        fieldWrapper.data("idx", intId);
        var fName = $("<textarea id=\"ingredients\" name=\"ingredients\" autocomplete=\"off\" minlength=\"1\" maxlength=\"100\"  data-length=\"100\" class=\"validate materialize-textarea col s11\" placeholder=\"Example: Milk, Eggs, Chocolate, Flour\" required></textarea>");
        var removeButton = $("<button class=\"btn remove col s1\" value=\"-\"><i class=\"fa fa-minus\" aria-hidden=\"true\"></i></button>");
        removeButton.click(function() {
            $(this).parent().remove();
        });
        fieldWrapper.append(fName);
        fieldWrapper.append(removeButton);
        $("#ingredientsform").append(fieldWrapper);
    }

    // Function to add new instructions for recipes forms
    $("#add-instructions").click(function() {
        var lastField = $("#instructionsform div:last");
        var intId = (lastField && lastField.length && lastField.data("idx") + 1) || 1;
        var fieldWrapper = $("<div class=\"fieldwrapper\" id=\"field" + intId + "\"/>");
        fieldWrapper.data("idx", intId);
        var fName = $("<textarea id=\"instructions\" name=\"instructions\" autocomplete=\"off\" minlength=\"1\" maxlength=\"500\" data-length=\"500\" class=\"validate materialize-textarea col s11\" placeholder=\"Example: In a large bowl, mix all the wet ingregients\" required></textarea>");
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

// Use Sweet Alert to create 2-tier confirmation before deleting an account
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
