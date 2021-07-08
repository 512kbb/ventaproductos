$(document).ready(function() {
    jQuery.validator.addMethod("selected",
    function (value, element)
    {
        if ($(element).find(":selected").val() == 0) {
            return false; 
        }
        else return true;
    },
   
);

    $('#formulario-registro').validate({
        
        
        rules:{
            txtCodigo:{
                required: true,
                minlength: 5,
                maxlength: 5
            },
            txtModelo:{
                required: true,
                maxlength: 50,
                minlength: 5,
            },
            cboMarca:{
                selected: true
            },

            txtPrecio:{
                required: true,
                minlength: 3,
                maxlength: 11
            },
            txtColor:{
                required: true,
                minlength: 3,
                maxlength: 30
            },
            txtImagen:{
                required: true,

            },
            txtTalla:{
                required:true
            }

        },
        
        messages:{
            txtCodigo:{
                required: "El codigo es obligatorio es obligatorio\.",
                minlength: "El largo del codigo debe ser de 5 caracteres\."
            },
            txtModelo:{
                required: "Especifique un modelo por favor\.",
                maxlength: "El largo maximo es de 50 caracteres",
                minlength: "El largo minimo es de 3 caracteres"

            },
            cboMarca: {
                selected: "Seleccione una marca\."
            },
            txtPrecio:{
                required: "Ingresa el precio",
                minlength: "El precio debe ser mayor o igual a 100\.",
                maxlength: "El precio no puede tener mas de 11 digitos\." 
            },
            txtColor:{
                required: "Especifique el color de la prenda",
                minlength: "El color debe tener al menos 3 carácteres\.",
                maxlength: "El color no puede superar los 30 carácteres\."
            },
            txtImagen:{
                required: "Añade una imagen, porfavor.\.",
               
            },
            txtTalla:{
                required: "Ingrese una talla"
            }

        },
        errorClass: "error-red",

    });
});
