$(function () {
    var _wrap_message = $(".wrap-message");
    var _inst_form_txt = $("form[name=form_txt]");
    var input_txt = _inst_form_txt.find("input[name=txt]");

    // send txt
    _inst_form_txt.submit(function (e) {
        e.preventDefault();
        _wrap_message.html("");

        var val_txt = input_txt.val().trim();
        if (val_txt === ""){
            _wrap_message.html(tmpl_error("Txt is empty or contains spaces!"));
            input_txt.val("");
            return false;
        }else if(val_txt.length>50){
            _wrap_message.html(tmpl_error("Txt field contains more than 50 characters!"));
        }

        $.ajax({
            type: "POST",
            url: "/api-v0/content/upload-text/",
            data: {"txt": val_txt},
            success: function (resp) {
                _wrap_message.html(tmpl_success);
                input_txt.val("");
            },
            error: function (request, status, error) {
                _wrap_message.html(tmpl_error(request.responseText));
            },
            dataType: "json"
        });
    });
});

// template message
var tmpl_success = "<span style='color: green'>Success!</span>";
var tmpl_error = function (text) {
    return "<span style='color: red'>" + text + "</span>";
};