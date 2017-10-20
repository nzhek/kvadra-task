$(function () {
    var _wrap_message = $(".wrap-message");
    var name_form = 'txt_list';

    var _list_txt = $(".list-txt");

    updateList();

    $(document).on("submit", "form[name="+name_form+"]", function (e) {
        e.preventDefault();
        var list = [];
        $(this).serializeArray().map(function(x){list.push(x.value)});
        if(list.length === 0) {
            _wrap_message.html(tmpl_error("Not selected"));
            return false;
        }

        var obj = list.reduce(function(o, val) { o[val] = val; return o; }, {});

        $.ajax({
            type: "POST",
            url: "/api-v0/content/remove-text/",
            data: {"list_txt": JSON.stringify(obj)},
            success: function (resp) {
                _wrap_message.html(tmpl_success);
                updateList();
            },
            error: function (request, status, error) {
                _wrap_message.html(tmpl_error(request.responseText));
            },
            dataType: "json"
        });
    });

    function updateList() {
        $.get("/api-v0/content/get-text/", function (data) {
            _list_txt.html(render_list(data.txt_list, name_form));
        }).fail(function (resp) {
            _wrap_message.html(tmpl_error(resp));
        });
    }

// template render list
    var render_list = function (list, name_form) {
        var result = "<form name=" + name_form + ">";
        $.each(list, function (key, elem) {
            result += '<div><input type="checkbox" id="elem' + key + '" name="elem' + key + '" value="' + elem.id + '">' +
                '<label for="elem' + key + '">' + elem.txt + '</label></div>';
        });
        return result + "<div><br><button type='submit'>Delete</button></div>" +
            "</form>";
    };

// template message
    var tmpl_success = "<span style='color: green'>Success!</span>";
    var tmpl_error = function (text) {
        return "<span style='color: red'>" + text + "</span>";
    };

});