$(function (){
    var hint_register='';
    $(".code").focus(function (){
        $(".code").removeAttr("placeholder");
    });
    $(".code").blur(function (){
        $(".code").attr("placeholder","验证码");
    })
    $(".Login-box .username").focus(function (){
        $(".Login-box .username").removeAttr("placeholder");
    });
    $(".Login-box .username").blur(function (){
        $(".Login-box .username").attr("placeholder","Username/Phone");
    })
    $(".Login-box .password").focus(function (){
        $(".Login-box .password").removeAttr("placeholder");
    })
    $(".Login-box .password").blur(function (){
        $(".Login-box .password").attr("placeholder","Password");
    })

    $(".register-box .username").focus(function (){
        hint_register='<div class="hint">只能由数字、字母和下划线组成,且必须有字母且不能超过13位</div>'
        create_hint(hint_register,".hint");
        $(".register-box .username").removeAttr("placeholder");
    })
    $(".register-box .username").blur(function (){
        $(".hint").remove();
        $(".register-box .username").attr("placeholder","Username");
    })
    $(".register-box .password").focus(function (){
        hint_register='<div class="hint">只能由数字、字母和下划线组成且不能超过13位</div>'
        create_hint(hint_register,".hint");
        $(".register-box .password").removeAttr("placeholder");
    })
    $(".register-box .password").blur(function (){
        $(".hint").remove();
        $(".register-box .password").attr("placeholder","Password");
    })
    $(".phone").focus(function (){
        $(".phone").removeAttr("placeholder");
    })
    $(".phone").blur(function (){
        $(".phone").attr("placeholder","Phone");
    })

    //登录注册页面转换
    $(".register_or_logo_round").click(function (){
        $(".register_or_logo_round").css({
            'animation': '',
            'transform': 'scale(0.8)',
            'visibility':'visible'
        })
        $(".register_or_logo_round").animate({},1,function (){
            $(".register_or_logo_round").css({
                'transform': 'scaleX(0)',
            })
        })
        if($(".register_or_logo_round").text()=="注册") {
            $(".register-box .phone,.register-box .username,.register-box .password").val('');
            reset(".Login-box",".register-box");
            toggle(".Login-box",".register-box")
            $(".register_or_logo_round").text("登录");
        }else {
            $(".Login-box .password,.Login-box .username,.code").val('');
            reset(".register-box",".Login-box")
            toggle(".register-box",".Login-box")
            $(".register_or_logo_round").text("注册");
        }
    })
})
function create_hint(str,a){
    $('body').append(str);
    create_hint_css(a);
}
function create_hint_css(a){
    $(a).css({
        'position': 'relative',
        'left': '35%',
        'right': '50%',
        'margin-top': '20px',
        'width': '25%',
        'height': '20px',
        'border-radius': '12px',
        'background':'whitesmoke',
        'text-align': 'center',
        'font-size': '13.8px',
        'font-weight':'2px',
        'border': '1px solid rgba(169,220,251,0.8)',
        'transition': 'all 0.4s ease-in-out 0.6s',
        'z-index':'5',
        'animation':'move 0.6s ease-in-out',
        'animation-fill-mode': 'forwards'
    });
}
function reset(a,b){
    $(a).css({
        'animation': '',
        'visibility':'visible'
    });
    $(".back-view-1,.back-view-2").css({
        "animation": "",
        'visibility':'hidden',
        'transform': 'rotateX(0deg) rotateY(0deg)'
    })
    $(b).css({
        "animation": "",
        'visibility':'hidden',
        'transform': 'rotateX(0deg) rotateY(0deg)'
    })
}
function toggle(a,b){
    $(a).animate({}, 800, function () {
        $(a).css({'transform': 'rotateX(-10deg) rotateY(50deg)'});
        $(".back-view-1").animate({}, 1000, function () {
            $(".back-view-1").css({
                'height': '228px',
                'transform': 'rotateX(-10deg) rotateY(50deg) translate3d(45%,26%,-250px) scaleX(1.1)',
                'visibility': 'visible'
            })
        })
        $(".back-view-2").animate({}, 1200, function () {
            $(".back-view-2").css({
                'height': '215px',
                'transform': 'rotateX(-10deg) rotateY(50deg) translate3d(50%,38%,-330px) scaleX(1.2)',
                'visibility': 'visible'
            })
            $(b).animate({}, 1400, function () {
                $(b).css({
                    'animation': 'jump 1.6s ease-in-out 1.5s',
                    'animation-fill-mode': 'forwards'
                })
                $(a).css({
                    'animation': 'show 1s ease-in-out 2.2s',
                    'animation-fill-mode': 'forwards'
                })
                $(".back-view-2").css({
                    'animation': 'jump-show 0.7s ease-in-out 1.7s',
                    'animation-fill-mode': 'forwards'
                })
                $(".back-view-1").css({
                    'animation': 'jump-show 0.7s ease-in-out 1.7s',
                    'animation-fill-mode': 'forwards'
                })
                $(".register_or_logo_round").css({
                    'animation': 'reshow 0.7s ease-in-out 2.7s',
                    'animation-fill-mode': 'forwards',
                })
            })
        })
    })
}