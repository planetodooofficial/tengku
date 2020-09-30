
function copy_address(check) {

    var checkbox = $("#address_check");

    checkbox.change(function() {

    if (checkbox.is(':checked')) {

        $("#shipping_address_line1").val($("#register_address_line1").val());
        $("#shipping_address_line2").val($("#register_address_line2").val());
        $("#shipping_addr_state").val($("#register_address_state").val());
        $("#shipping_address_city").val($("#register_address_city").val());
        $("#shipping_address_gps").val($("#register_address_gps").val());
        $("#shipping_address_pin_code").val($("#register_address_pin_code").val());

    }
    else {

        $('#shipping_address_line1').val(' ');
        $('#shipping_address_line2').val(' ');
        $('#shipping_addr_state').val(' ');
        $('#shipping_address_city').val(' ');
        $('#shipping_address_gps').val(' ');
        $('#shipping_address_pin_code').val(' ');

    }

    });

};


function submit_validation(submit) {

    var org_name = $('#org_nick_name').val();

    if ( !org_name ){

        $('.username-or-password-is-incorrect-2139').show();

    }
    else{

        $('.username-or-password-is-incorrect-2139').hide();

    }

};