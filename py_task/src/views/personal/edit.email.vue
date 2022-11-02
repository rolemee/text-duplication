<route>
{
    meta: {
        title: "修改邮箱"
    }
}
</route>
<script setup name="personalEditEmail">
const route = useRoute(), router = useRouter()

import useUserStore from '@/store/modules/user'
const userStore = useUserStore()

const TIP_TEXT = '{{time}}s重新获取'
const DELAY_TIME = 20
const text = ref('发送验证码')
const disableButton = ref(false)

const formRef = ref()
const form = ref({
    name: '',
    email: '',
    captcha: ''
})

const rules = ref({
    name: [
        { required: true,message: '请输入你的姓名', trigger: 'blur' }
    ],
    email: [
        { required: true,message: '请输入邮箱', trigger: 'blur' },
        { type: 'email',message: '请输入正确的邮箱格式', trigger: 'blur'}
    ],
    captcha: [
        { required: true,message: '请输入验证码', trigger: 'blur' }
    ]
})

function sendCaptcha() {
    formRef.value.validateField('email', valid => {
        console.log(valid)
        if (valid) {
            disableButton.value = true
            //向邮箱发送验证码

            let nowTime = DELAY_TIME
            let checkFlag = setInterval(() => {
                --nowTime
                if (nowTime <= 0) {
                    text.value = '发送验证码'
                    clearInterval(checkFlag)
                    disableButton.value = false
                }else {
                    text.value = TIP_TEXT.replace('{{time}}', String(nowTime))
                }
            }, 1000)
        }
    })
}

function onSubmit() {
    formRef.value.validate(valid => {
        if (valid) {
            //提交修改操作
            //成功提示
            ElMessage({
                type: 'success',
                message: '修改邮箱成功'
            })
            //失败提示
            ElMessage({
                type: 'error',
                message: '失败'//提示
            })
        }
    })
}
function onCancel() {
    router.push({ name: 'personalSetting' })
}
</script>


<template>
    <div>
        <page-header title="修改邮箱" content="绑定邮箱可以提高帐号安全性噢~" >
            <el-button size="default" round @click="onCancel">
                <template #icon>
                    <el-icon>
                        <svg-icon name="ep:arrow-left" />
                    </el-icon>
                </template>
                返回
            </el-button>
        </page-header>
        <page-main>
            <el-row>
                <el-col :md="24" :lg="12">
                    <el-form ref="formRef" :model="form" :rules="rules" label-width="120px">
                        <el-form-item label="姓 名" prop="name">
                            <el-input v-model="form.name"  placeholder="请输入你的姓名" tabindex="1"/>
                        </el-form-item>
                        <el-form-item label="邮箱" prop="email">
                            <el-input v-model="form.email"  placeholder="请输入要绑定的邮箱" tabindex="1"/>
                        </el-form-item>
                        <el-form-item label="验证码" prop="captcha">
                            <el-input  v-model="form.captcha" placeholder="请输入验证码" tabindex="2" >
                                <template #append>
                                    <el-button :disabled="disableButton" @click="sendCaptcha">{{text}}</el-button>
                                </template>
                            </el-input>
                        </el-form-item>
                    </el-form>
                </el-col>
            </el-row>
        </page-main>
        <fixed-action-bar>
            <el-button type="default" size="large" @click="onCancel">取消</el-button>
            <el-button type="primary" size="large" @click="onSubmit">提交</el-button>
        </fixed-action-bar>
    </div>
</template>



<style scoped>

</style>
