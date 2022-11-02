$(function () {//验证码操作
    // var number=createNumber();
    // $(".Login-box .verificationCode .randomNumber").on('click', function () {//刷新验证码
    //     number = createNumber();
    // })
    var hint = '';
    var wrong = '';
    var check_name = /^(([A-Za-z_]+[A-Za-z0-9_]+)|[A-Za-z_]+)$/;//匹配用户名必须有字母
    var check_phone = /^[1]+\d{10}$/;//匹配开头是1 一共11位数字的电话
    var check_password = /^[A-Za-z0-9_]+$/;//匹配密码

    $("#Login").click(function (){//判断验证码输入正确与否 并进行登录验证
        var enterNumber=$(".Login-box .verificationCode input").val();
            var password=$(".Login-box .password[type=password]").val();
            var name=$(".Login-box .username").val();
            if(judge(name,"用户名不为空") && judge(password,"密码不为空")){
                if(judge_name(name,check_name)||judge_name(name,check_phone)){
                    if(judge_rule(password,check_password,"密码输入格式错误")){
                        $("#Login").attr({
                            'form':"login-form"
                        })
                        $(".back").css({
                            'z-index': '4',
                            'visibility': 'visible',
                            'animation':'lode-back  0.8s ease-in 0.3s',
                            'animation-fill-mode': 'forwards',
                            'cursor':'wait'
                        })
                        $(".load").css({
                            'animation':'reshow  0.4s ease-in 0.3s',
                            'animation-fill-mode': 'forwards',
                        })
                        $.ajax({
                            url:'/login',
                            data: $("#login-form").serialize(),
                            type: 'post',
                            success:function (res){
                                console.log(res)
                                location.href = "/"
                            },
                            error:function (){
                                wrong="<div class='wrong'>连接失败</div>";
                                create_hint(wrong,".wrong");
                                setTimeout(function (){
                                    $(".wrong").remove();
                                },5000)
                                end_load();
                            }
                        })
                    }
                }else {
                    var wrong="<div class='wrong'>用户输入格式错误</div>";
                    create_hint(wrong,".wrong");
                    setTimeout(function (){
                        $(".wrong").remove();
                    },3000)
                }
            }

        setTimeout(function (){
            $(".hint_code").remove();
        },3000);
    })
    $("#register").click(function (){//注册验证
        var name = $(".register-box .username").val();
        var password = $(".register-box .password[type=password]").val();
        var phone = $(".register-box .phone").val();
        if(judge(name,'用户名不为空') && judge(password,"密码不为空") && judge(phone,'电话不为空')){
            if (judge_rule(name, check_name, "用户名输入格式错误")) {
                if (judge_rule(password, check_password, "密码输入格式错误")) {
                    if (judge_rule(phone, check_phone, "电话输入格式错误")) {
                        $("#register").attr({
                            'form': "register-form"
                        });
                        $.ajax({
                            url: 'http://127.0.0.1:8080/register',
                            data: $('#register-form').serialize(),//表单数据
                            type: 'post',
                            async: 'true',
                            success: function (res) {
                                var json = eval("(" + res + ")");
                                if (json.code == "0") {
                                    hint = "<div class='hint'>注册成功</div>";
                                    create_hint(hint, ".hint");
                                    setTimeout(function () {
                                        $(".hint").remove();
                                    }, 5000)
                                    $(".register_or_logo_round").trigger("click");
                                } else {
                                    wrong = "<div class='wrong'>注册失败" + json.msg + "</div>";
                                    create_hint(wrong, ".wrong");
                                    setTimeout(function () {
                                        $(".wrong").remove();
                                    }, 5000)
                                    $(".register-box .phone,.register-box .username,.register-box .password").val('');
                                }
                            },
                            error: function () {
                                wrong = "<div class='wrong'>连接失败</div>";
                                create_hint(wrong, ".wrong");
                                setTimeout(function () {
                                    $(".wrong").remove();
                                }, 5000)
                            }
                        })
                    }else {
                        $(".register-box .phone").val('');
                    }
                }else {
                    $(".register-box .password").val('');
                }
            }else {
                $(".register-box .username").val('');
            }
        }
    })
})

function end_load(){
    setTimeout(function (){
        $(".load").animate({},800,function (){
            $(".load").css({
                'animation':'',
                'transform':'scale(0)',
                'cursor':'default'
            })
            $(".back").animate({},800,function (){
                $(".back").css({
                    'z-index': '-1',
                    'visibility': 'hidden',
                    'animation':''
                })
            })
        })
    },2000);
}
function judge_name(str,check){
    if(check.test(str)){
        return true;
    }else {
        return false
    }
}
function createNumber() {
    var str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890";
    var arr = str.split("")
    var canvas = document.getElementsByClassName("randomNumber")[0];
    var context = canvas.getContext("2d")
    var width = $('.Login-box .verificationCode .randomNumber').width();
    var height = $('.Login-box .verificationCode .randomNumber').height();
    canvas.width=width;
    canvas.height=height;
    var number = [];
    for (var i = 0; i < 4; i++)//生成随机数
    {
        var n = Math.floor(Math.random() * arr.length);
        var result = arr[n];
        number[i]= result;
        var deg = Math.random() * 5;//产生随即弧度
        var x = 8 + i * 20;
        var y = 17 + Math.random() * 8;//坐标
        context.font = "bold 21px 微软雅黑"
        context.translate(x, y);
        context.rotate(deg * Math.PI / 180);
        context.fillStyle = randomColor();
        context.fillText(result, 0, 0);
        context.rotate(-deg * Math.PI / 180);
        context.translate(-x, -y);
    }
    for (var i = 0; i < 5; i++)//添加横线
    {
        context.strokeStyle = randomColor();
        context.beginPath();//开始绘制路径
        context.moveTo(Math.random() * width, Math.random() * height);//开始
        context.lineTo(Math.random() * width, Math.random() * height);//结束
        context.stroke();//绘制
    }
    for (var i = 0; i < 20; i++)//添加杂点
    {
        context.strokeStyle = randomColor();
        context.beginPath();
        var x = Math.random() * width;
        var y = Math.random() * height;
        context.moveTo(x, y);
        context.lineTo(x + 1, y + 1);
        context.stroke();
    }
    var Number='';
    for (var i=0;i < 4;i++){
        Number+=number[i];
    }
    return Number;
}
function randomColor() {//生成随机颜色
    var r = Math.floor(Math.random() * (255 + 1));
    var g = Math.floor(Math.random() * (255 + 1));
    var b = Math.floor(Math.random() * (255 + 1));
    return "rgba(" + r + "," + g + "," + b + "," + "95%)";
}
