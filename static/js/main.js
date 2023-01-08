/*-----------Utilities-----------*/
/*-----------Searching-----------*/
const sanitizeInput = function(value){
    restrictedChars = ["{", "}", "%", "<", ">", "?", "&", "'", ",", ";",
     "+", "#", "$", "^", "*", "=", "(", ")", "[", "]", "!", "\"", "  "]
     for(var i = 0; i < restrictedChars.length; i++){
         while(value.indexOf(restrictedChars[i])!=-1){
             if(restrictedChars[i]=="  "){
                 value = value.replace(restrictedChars[i], " ")
             }
             value = value.replace(restrictedChars[i],"");
             if(value.indexOf(restrictedChars[i])==-1)
                i++
         }
     }
     console.log(value);

     return (
         value.trim()
         );
}

$("document").ready(function(){
    $(".search-bar").on("keyup", function(){
        let value = sanitizeInput($(this).val().toLowerCase())
        console.log(value)
        $(".article-container").each(function(){
            if(!$(this).children("div").children("div").children("h4").text().toLowerCase().includes(value)){
                $(this).hide()
            }else{
                $(this).show()
            }
        })
    })
})

/*--------- Hover Effects--------*/
var $navbarItems = $("ul.nav").children("li").children(".nav-link");
$navbarItems.each(function(){
    if(!$(this).attr("class").split(/\s+/).includes("text-primary")){
        $(this).on("mouseover", function(){
            $(this).removeClass("text-secondary");
            $(this).addClass("text-primary");
        })
        $(this).on("mouseout", function(){
            $(this).removeClass("text-primary");
            $(this).addClass("text-secondary");
        })
    }   
})

var $primaryButtons = $(".btn-primary")
$primaryButtons.each(function(){
    $(this).hover(function(){
        $(this).addClass("text-primary bg-white");
    }, function(){
        $(this).removeClass("text-primary bg-white");

    })
})

var $dangerButtons = $(".btn-danger")
$dangerButtons.each(function(){
    $(this).hover(function(){
        $(this).addClass("text-danger bg-white");
    }, function(){
        $(this).removeClass("text-danger bg-white");

    })
})

var $categories = $(".category")
$categories.each(function(){
    $(this).hover(function(){
        if($(this).attr("class").split(/\s+/).includes("text-primary")){
            $(this).css({
                "border-bottom-color":"rgba(0, 0, 0, 0.0)"
            })
        }
    })
})
/*---------Adding Styles---------*/
var $subjects = $(".subject");
$subjects.each(function(){
    if(!$(this).is(":last-child")){
        $(this).append(" / ");
    }
})

/*---------Utilities End---------*/


