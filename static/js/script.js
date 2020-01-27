$(document).ready(function () {

    // jQUERY SCRIPT

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
    $("select#difficulty").change(function () {
        var selectedOption = $(this).children("option:selected").val();
        if (selectedOption == "") {
            $(this).parent(".select-wrapper").children("input").css({ "border-bottom": "1px solid #f44336", "box-shadow": "0 1px 0 0 #f44336" });
        } else {
            $(this).parent(".select-wrapper").children("input").css({ "border-bottom": "1px solid #4CAF50", "box-shadow": "0 1px 0 0 #4CAF50" });
        };
    });

    // Remove 'required' attribute for minutes if hours
    $("#hours").change(function () {
        var inputtedHour = $(this).val();
        console.log(inputtedHour);
        if (inputtedHour == "" || inputtedHour == 0) {
            $("#minutes").prop("required", true);
        } else {
            $("#minutes").prop("required", false);
        };
    });

    // Hide all elements with this class on page load
    $(".add-item-error").hide();

    // Hide feedback when user is typing in the field
    $(document).on('keyup', '.manual-feedback', function () {
        $(this).parent("div").parent("div").siblings(".add-item-error").hide();
        $(this).siblings(".alert-div").removeClass("data-error-manual").removeClass("data-success-manual").text("");
    });

    // Function to provide manual feedback when field is changed
    function feedbackChangeFunction() {
        $(".manual-feedback").change(function () {
            var field = $(this).val();
            if (field == "") {
                $(this).siblings(".alert-div").removeClass("data-success-manual").addClass("data-error-manual").text("*required");
            } else {
                $(this).siblings(".alert-div").removeClass("data-error-manual").addClass("data-success-manual").text("validated");
            };
        });
    };

    // Function to provide manual feedback when user focuses out of field
    function feedbackFocusFunction() {
        $(".manual-feedback").focusout(function () {
            var field = $(this).val();
            if (field == "") {
                $(this).siblings(".alert-div").removeClass("data-success-manual").addClass("data-error-manual").text("*required");
            } else {
                $(this).siblings(".alert-div").removeClass("data-error-manual").addClass("data-success-manual").text("validated");
            };
        });
    };

    feedbackFocusFunction();
    feedbackChangeFunction();

    // Function to check if last ingredient field is empty before adding a new one
    $("#add-ingredients").click(function () {
        var lastIngredientField = $("#ingredientsform").children("div:last-child").children("textarea").val();
        if (lastIngredientField == "") {
            $("#data-error-ingredients").show();
        } else {
            $("#data-error-ingredients").hide();
            addIngredientsFunction();
        };
    });

    // Function to add a new ingredient to the list
    function addIngredientsFunction() {
        var fieldWrapper = $("<div class=\"fieldwrapper\"/>");
        var fName = $("<textarea id=\"ingredients\" name=\"ingredients\" minlength=\"1\" maxlength=\"100\" class=\"validate materialize-textarea manual-feedback col s11\" placeholder=\"Example: Milk, Eggs, Chocolate, Flour\" required></textarea>");
        var removeButton = $("<button class=\"btn remove-btn col s1\" value=\"-\"><i class=\"fa fa-minus\" aria-hidden=\"true\"></i></button>");
        var alertDiv = $("<div class=\"col s12 left-align alert-div\"></div>");
        removeButton.click(function () {
            $(this).parent().remove();
        });
        fieldWrapper.append(fName);
        fieldWrapper.append(removeButton);
        fieldWrapper.append(alertDiv);
        $("#ingredientsform").append(fieldWrapper);
        // Add event listeners when new item is created
        feedbackFocusFunction();
        feedbackChangeFunction();
    };

    // Function to check if last instruction field is empty before adding a new one
    $("#add-instructions").click(function () {
        var lastInstructionField = $("#instructionsform").children("div:last-child").children("textarea").val();
        if (lastInstructionField == "") {
            $("#data-error-instructions").show();
        } else {
            $("#data-error-instructions").hide();
            addInstructionsFunction();
        };
    });

    // Function to add new instructions
    function addInstructionsFunction() {
        var fieldWrapper = $("<div class=\"fieldwrapper\"/>");
        var fName = $("<textarea id=\"instructions\" name=\"instructions\" minlength=\"1\" maxlength=\"500\" class=\"validate materialize-textarea manual-feedback col s11\" placeholder=\"Example: In a large bowl, mix all the wet ingregients\" required></textarea>");
        var removeButton = $("<button class=\"btn remove col s1\" value=\"-\"><i class=\"fa fa-minus\" aria-hidden=\"true\"></i></button>");
        removeButton.click(function () {
            $(this).parent().remove();
        });
        var alertDiv = $("<div class=\"col s12 left-align alert-div\"></div>");
        fieldWrapper.append(fName);
        fieldWrapper.append(removeButton);
        fieldWrapper.append(alertDiv);
        $("#instructionsform").append(fieldWrapper);
        // Add event listener when new item is created
        feedbackFocusFunction();
        feedbackChangeFunction();
    };

    // Remove existing ingredients/instructions when user edits a recipe
    $(".remove-btn").click(function () {
        $(this).parent().remove();
    });

});

// CORE JS SCRIPT

// Function to print recipes
function myPrintFunction() {
    window.print();
}

// Use Sweet Alert to create a two-tier confirmation before deleting the recipe
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

// Use Sweet Alert to create two-tier confirmation before deleting an account
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
