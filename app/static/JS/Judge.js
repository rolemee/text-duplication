function judge_rule(str,check,hint){
    if(check.test(str)){
        return true;
    }else {
        var wrong="<div class='wrong'>"+hint+"</div>";
        create_hint(wrong,".wrong");
        setTimeout(function (){
            $(".wrong").remove();
        },3000)
        return false;
    }
}
function judge(str,hint){
    if(str==''){
        var waring="<div class='waring'>"+hint+"</div>";
        create_hint(waring,".waring");
        setTimeout(function (){
            $(".waring").remove();
        },3000)
        return false;
    }else {
        return true;
    }
}