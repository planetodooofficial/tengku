
function copy_address(check) {

    var checkbox = $("#address_check");

    checkbox.change(function() {

    if (checkbox.is(':checked')) {

        $("#shipping_address_line1").val($("#register_address_line1").val());
        $("#shipping_address_line2").val($("#register_address_line2").val());
        $("#shipping_address_state").val($("#register_address_state option:selected").val());
        $("#shipping_address_city").val($("#register_address_city option:selected").val());
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

function submit_validation1(submit) {

    var org_name = $('#nick_name').val();

    if ( !org_name ){

        $('.username-or-password-is-incorrect-2139').show();

    }
    else{

        $('.username-or-password-is-incorrect-2139').hide();

    }

};


//    // Material Select Initialization
//    $(document).ready(function() {
//    $('.mdb-select').materialSelect();
//    });



$(document).ready(function(){

    $.ajax({
    type: 'POST',
    url: '/get_state',
    dataType: 'json',
    data : {},
    }).done(function(data){

        state_select= $('.state_select').empty();
        state_select_data= '<option value="" selected="selected">State</option>';


        for(i=0;i<data.states.length; i++){
            state_select_data+='<option value="'+data.states[i].id+'">'+data.states[i].value+'</option>'
        }

        state_select.append(state_select_data)

    })

});




function onchange_register_state(state){

    $.ajax({
    type: 'POST',
    url: '/get_city',
    dataType: 'json',
    data : {'state': state.value},
    }).done(function(data){

        city_select=$('.register_city_select').empty();
        city_data='<option value="" selected="selected">City</option>';
        if (data.length != null){
            for(i=0;i<data.length; i++){
                city_data+='<option value="'+data[i].id+'">'+data[i].value+'</option>'
            }

        }
        city_select.append(city_data);
    });
;}


function onchange_shipping_state(state){

    $.ajax({
    type: 'POST',
    url: '/get_city',
    dataType: 'json',
    data : {'state': state.value},
    }).done(function(data){

        city_select=$('.shipping_city_select').empty();
        city_data='<option value="" selected="selected">City</option>';
        if (data.length != null){
            for(i=0;i<data.length; i++){
                city_data+='<option value="'+data[i].id+'">'+data[i].value+'</option>'
            }

        }
        city_select.append(city_data);
    });
;}