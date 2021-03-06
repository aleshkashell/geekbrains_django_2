window.onload = function () {
    var _quantity, _price, orderitem_num, delta_quantity, orderitem_quantity, delta_cost;
    var quantity_arr = [];
    var price_arr = [];

    var TOTAL_FORMS = parseInt($('input[name="orderitems-TOTAL_FORMS"]').val());

    var order_total_quantity = parseInt($('.order_total_quantity').text()) || 0;
    var order_total_cost = parseFloat($('.order_total_cost').text().replace(',', '.')) || 0;
    updateData();
    function updateData(){
        TOTAL_FORMS = parseInt($('input[name="orderitems-TOTAL_FORMS"]').val());
        console.log("Total: ", TOTAL_FORMS);
        for (var i = 0; i < TOTAL_FORMS; i++) {
            _quantity = parseInt($('input[name="orderitems-' + i + '-quantity"]').val());
            _price = parseFloat($('.orderitems-' + i + '-price').text().replace(',', '.'));
            quantity_arr[i] = _quantity;
            if (_price) {
                price_arr[i] = _price;
            } else {
                price_arr[i] = 0;
            }
            console.log(i, _quantity, _price);
        }
        
        if (!order_total_quantity) {
            for (var i = 0; i < TOTAL_FORMS; i++) {
                order_total_quantity += quantity_arr[i];
                order_total_cost += quantity_arr[i] * price_arr[i];
            }
            $('.order_total_quantity').html(order_total_quantity.toString());
            $('.order_total_cost').html(Number(order_total_cost.toFixed(2)).toString());
        }
        console.log(quantity_arr);
        console.log(price_arr);
    };
    
    $('.order_form').on('click', 'input[type="number"]', function (event) {
        var target = event.target;
        orderitem_num = parseInt(target.name.replace('orderitems-', '').replace('-quantity', ''));
        console.log(price_arr);
        if (price_arr[orderitem_num]) {
            orderitem_quantity = parseInt(target.value);
            delta_quantity = orderitem_quantity - quantity_arr[orderitem_num];
            quantity_arr[orderitem_num] = orderitem_quantity;
            orderSummaryUpdate(price_arr[orderitem_num], delta_quantity);
        }
    });

    $('.order_form').on('click', 'input[type="checkbox"]', function (event) {
        var target = event.target;
        orderitem_num = parseInt(target.name.replace('orderitems-', '').replace('-DELETE', ''));
        if (target.checked) {
            delta_quantity = -quantity_arr[orderitem_num];
        } else {
            delta_quantity = quantity_arr[orderitem_num];
        }
        orderSummaryUpdate(price_arr[orderitem_num], delta_quantity);
    });

    function orderSummaryUpdate(orderitem_price, delta_quantity) {
        delta_cost = orderitem_price * delta_quantity;

        order_total_cost = Number((order_total_cost + delta_cost).toFixed(2));
        order_total_quantity = order_total_quantity + delta_quantity;

        $('.order_total_cost').html(order_total_cost.toString());
        $('.order_total_quantity').html(order_total_quantity.toString());
    }

    $('.formset_row').formset({
        addText: 'добавить продукт',
        deleteText: 'удалить',
        prefix: 'orderitems',
        removed: deleteOrderItem
    });

    function deleteOrderItem(row) {
        var target_name = row[0].querySelector('input[type="number"]').name;
        orderitem_num = parseInt(target_name.replace('orderitems-', '').replace('-quantity', ''));
        delta_quantity = -quantity_arr[orderitem_num];
        orderSummaryUpdate(price_arr[orderitem_num], delta_quantity);
    }

    $('.order_form').on('change', 'select', function(event){
        var target = event.target;
        orderitem_num = parseInt(target.name.replace('orderitems-', '').replace('-product', ''));
        console.log(event);
        if(target.value == ""){
            foundElement = target.parentElement.parentElement.getElementsByClassName("td3");
            foundElement[0].innerHTML = "";
        };
        $.ajax({
            url: "/order/price/" + target.value + "/",
                
            success: function (data) {
                priceField = target.parentElement.parentElement.getElementsByClassName("td3");
                priceField[0].innerHTML = '<span class="orderitems-' + orderitem_num + '-price">' + data.result + '</span> руб';
                quantityField = target.parentElement.parentElement.getElementsByClassName("td2");
                quantityField[0].innerHTML = '<input type="number" name="orderitems-' + orderitem_num + '-quantity" value="0" min="0" class="form-control" id="id_orderitems-' + orderitem_num + '-quantity">';
                updateData();
            },
        });
        updateData();
    });
}