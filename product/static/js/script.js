     var price;
     var tax_per;
     var perc;
    $(document).ready(function() {
       $(".input").on("keyup", function(){
        price = Number($("#id_price").val())  
        tax_per = Number($("#id_tax_per").val());
    });
       $('#id_tax_type').on('change', function() {
        // var tax_type = (this.value)
        if ((this.value) == 2){
            // Tax amount = Value inclusive of tax X tax rate ÷ (100+ tax rate)
            // Tax-exclusive price = Tax-inclusive price / (1 + Tax rate)
            perc = (price * tax_per) / (100 + tax_per);
            $("#id_tax_amount").val(perc);
    }else{  

            // Tax amount + Amount before tax
            perc = (tax_per + price) - price ;
            $("#id_tax_amount").val(perc);
    }
    });
});
