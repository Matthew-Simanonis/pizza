$(document).ready(function(){
    $('#hamburger').click(()=>{
        if($('#nav-links').css('opacity') == 0){
            $('#nav-links').toggleClass('show');
            $('#nav-links').animate({ opacity: 1}, 300);
        }
        else if($('#nav-links').css('opacity') == 1){
            $('#nav-links').animate({ opacity: 0}, 300);
            setTimeout(() => {
                $('#nav-links').toggleClass('show');
            }, 301);

        }
    })
})